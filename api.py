import os
import datetime
import smtplib
from email.mime.text import MIMEText
from fastapi import FastAPI, BackgroundTasks, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from openai import OpenAI

# Initialize API Gateway
app = FastAPI(title="AQP Operational Backend API")

# Allow your GitHub Pages frontend to communicate with this backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # In production, restrict this to your GitHub Pages URL (e.g., "https://alphahca.github.io")
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize OpenAI Client (Grabs OPENAI_API_KEY from environment variables automatically)
client = OpenAI()

# --- IN-MEMORY DATABASE (Replace with PostgreSQL/SQLAlchemy at scale) ---
orders_db = []

# --- DATA MODELS ---
class ChatRequest(BaseModel):
    message: str

class OrderRequest(BaseModel):
    customer_name: str
    customer_email: str
    item_name: str
    price: float

class StatusUpdate(BaseModel):
    order_id: str
    new_status: str

# --- MODULE: AUTOMATED COMMUNICATIONS ---
def send_email(to_email: str, subject: str, body: str):
    """Background task to dispatch operational emails."""
    sender_email = os.environ.get("AQP_EMAIL", "alerts@americanqualityprotein.com")
    sender_password = os.environ.get("AQP_APP_PASSWORD", "your-secure-password")
    
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = sender_email
    msg['To'] = to_email

    try:
        # Configuration for standard SMTP (e.g., Gmail/Google Workspace)
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
            server.login(sender_email, sender_password)
            server.send_message(msg)
    except Exception as e:
        print(f"Failed to send email payload to {to_email}: {e}")

# --- API ENDPOINTS ---

@app.post("/api/chat")
async def chat_engine(request: ChatRequest):
    """Handles the LLM routing for the Coach Gruden persona."""
    user_msg = request.message
    
    # THE SYSTEM PROMPT: Hidden instructions for the LLM
    system_prompt = """
    You are Coach Jon Gruden, the energetic, football-obsessed face and co-founder of American Quality Protein (AQP). 
    Your job is to assist customers in selecting their Tailgate Box or Bulk Beef Share. 
    Tone: Intense, passionate, authoritative, and welcoming. Use football analogies naturally (e.g., "draft your roster," "in the trenches," "gameplan"). Keep responses concise—never more than 3 sentences.

    Strict Factual Guidelines:
    1. Product Origin: All beef is 100% American, USDA Choice, born, raised, and processed in Iowa.
    2. Box Roster (All boxes are exactly 20 lbs and ship express on dry ice):
       - The Rookie ($259): 60 third-pound premium hamburger patties.
       - The Tailgate ($349): Brisket, chuck roasts, sirloin, tri-tip, skirt, and ground beef.
       - The Prime Time ($499): Ribeye, NY Strip, and Top Sirloin.
       - The Hall of Fame ($649): Ribeyes, Filet Mignons, NY Strips, and Top Sirloins. No fillers.
    3. Bulk Shares (For large freezers):
       - 1/4 Steer ($1,695): 140 lbs of perfectly packaged premium beef.
       - 1/2 Steer ($3,390): 280 lbs of our absolute best yields.
    4. Logistics: We bypassed the middleman. Coach Gruden oversees the fulfillment directly. Orders are hand-cut, vacuum-sealed, and shipped express out of our Iowa facility on dry ice to arrive in 1-3 days.
    5. Constraints: NEVER invent prices or cuts not listed here. If a user asks a question outside of ordering beef, politely pivot back to the tailgate boxes.
    """
    
    try:
        # Call the OpenAI API
        response = client.chat.completions.create(
            model="gpt-4o", # You can use "gpt-3.5-turbo" if you want lower costs
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_msg}
            ]
        )
        
        # Extract the AI's reply
        reply_text = response.choices[0].message.content
        return {"reply": reply_text}
        
    except Exception as e:
        print(f"OpenAI API Error: {e}")
        # Fallback message if OpenAI's servers are down or API key is missing
        return {"reply": "Hold your horses, we've got a signal issue on the headset. Try asking me that one more time."}

@app.post("/api/order")
async def create_order(order: OrderRequest, background_tasks: BackgroundTasks):
    """Ingests front-end orders, updates accounting, and triggers confirmation emails."""
    order_id = f"AQP-{len(orders_db) + 1000}"
    
    # Accounting Core Logic
    cogs_base = 189.42 if "Box" in order.item_name else (order.price * 0.70) # Baseline assumption
    gateway_fee = order.price * 0.03
    net_margin = order.price - cogs_base - gateway_fee
    
    new_order = {
        "order_id": order_id,
        "date": datetime.datetime.now().strftime("%Y-%m-%d %H:%M"),
        "customer": order.customer_name,
        "email": order.customer_email,
        "item": order.item_name,
        "revenue": order.price,
        "cogs": cogs_base,
        "net_profit": net_margin,
        "status": "Processing in Iowa"
    }
    orders_db.append(new_order)
    
    # Trigger Automated Confirmation Email
    email_body = f"""
    Welcome to the roster, {order.customer_name}!
    
    Coach Gruden and the AQP team have received your order for {order.item_name}.
    It has been routed directly to our Iowa facility for hand-cutting and dry-ice packaging.
    
    Order ID: {order_id}
    Total Paid: ${order.price:,.2f}
    
    We will update you the moment the cooler hits the delivery truck.
    """
    background_tasks.add_task(send_email, order.customer_email, f"Order Confirmed: {order_id}", email_body)
    
    return {"status": "success", "order_id": order_id}

@app.post("/api/admin/update_status")
async def update_status(update: StatusUpdate, background_tasks: BackgroundTasks):
    """Admin endpoint to update fulfillment status and trigger tracking emails."""
    for order in orders_db:
        if order["order_id"] == update.order_id:
            order["status"] = update.new_status
            
            # If marked as shipped, trigger the notification
            if update.new_status.lower() == "shipped":
                email_body = f"Get the grill hot! Your order ({update.order_id}) has officially shipped from our Iowa facility on dry ice."
                background_tasks.add_task(send_email, order["email"], f"AQP Order Shipped: {update.order_id}", email_body)
            
            return {"status": "updated", "order": order}
            
    raise HTTPException(status_code=404, detail="Order not found")

@app.get("/api/admin/dashboard")
async def get_dashboard():
    """Generates the accounting and reporting payload for the admin front-end."""
    total_rev = sum(o["revenue"] for o in orders_db)
    total_net = sum(o["net_profit"] for o in orders_db)
    return {
        "metrics": {
            "total_orders": len(orders_db),
            "gross_revenue": total_rev,
            "net_operating_profit": total_net,
            "blended_margin": (total_net / total_rev * 100) if total_rev > 0 else 0
        },
        "orders": orders_db
    }
