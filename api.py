from fastapi import FastAPI, BackgroundTasks, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List
import smtplib
from email.mime.text import MIMEText
import datetime
import os

# Initialize API Gateway
app = FastAPI(title="AQP Operational Backend API")

# Allow GitHub Pages frontend to communicate with this backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # In production, restrict this to "https://alphahca.github.io"
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- IN-MEMORY DATABASE (Replace with PostgreSQL/SQLAlchemy in scale) ---
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
    
    # -------------------------------------------------------------------------
    # TODO: INSERT OPENAI OR GEMINI API CALL HERE
    # client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))
    # response = client.chat.completions.create(
    #     model="gpt-4",
    #     messages=[
    #         {"role": "system", "content": "You are Coach Jon Gruden... (insert prompt here)"},
    #         {"role": "user", "content": user_msg}
    #     ]
    # )
    # reply_text = response.choices[0].message.content
    # -------------------------------------------------------------------------
    
    # Placeholder Logic
    reply_text = f"Coach Gruden here! I received your message: '{user_msg}'. We are getting the offensive line ready to ship your Iowa beef."
    
    return {"reply": reply_text}

@app.post("/api/order")
async def create_order(order: OrderRequest, background_tasks: BackgroundTasks):
    """Ingests front-end orders, updates accounting, and triggers confirmation emails."""
    order_id = f"AQP-{len(orders_db) + 1000}"
    
    # Accounting Core Logic[cite: 1]
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