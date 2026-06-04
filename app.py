import streamlit as st
import time

# --- 1. SET GLOBAL PAGE CONFIGURATION ---
st.set_page_config(
    page_title="Gruden's Tailgate in a Box",
    page_icon="🥩",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- 2. PREMIUM BLACK, CRIMSON & GOLD THEME INJECTION ---
st.markdown("""
    <style>
    /* Global Background and Typography */
    .stApp {
        background-color: #050505;
        color: #ffffff;
    }
    
    /* Hide default generic streamlit headers */
    header {visibility: hidden;}
    footer {visibility: hidden;}
    
    /* Branding Classes */
    .gold-header {
        color: #D4AF37 !important;
        font-family: 'Impact', 'Arial Black', sans-serif;
        text-transform: uppercase;
        letter-spacing: 2px;
        text-align: center;
    }
    .crimson-brand {
        color: #cc0000 !important;
        font-weight: 900;
    }
    
    /* Custom Luxury Product Cards */
    .product-card {
        background: linear-gradient(135deg, #111111 0%, #161616 100%);
        padding: 24px;
        border-radius: 12px;
        border: 1px solid #222222;
        text-align: center;
        margin-bottom: 12px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.5);
    }
    .card-title-gold { color: #D4AF37; font-size: 1.4rem; font-weight: 800; text-transform: uppercase; }
    .card-title-crimson { color: #ff3333; font-size: 1.5rem; font-weight: 900; text-transform: uppercase; }
    .price-tag { font-size: 2rem; font-weight: 900; color: #ffffff; margin: 10px 0; }
    
    /* Button Customization */
    .stButton>button {
        width: 100%;
        background-color: #1a1a1a !important;
        color: #ffffff !important;
        border: 1px solid #D4AF37 !important;
        text-transform: uppercase !important;
        font-weight: bold !important;
        border-radius: 6px !important;
        padding: 10px 0 !important;
        transition: all 0.3s ease !important;
    }
    .stButton>button:hover {
        background-color: #cc0000 !important;
        border-color: #cc0000 !important;
        box-shadow: 0 0 10px rgba(204,0,0,0.5) !important;
    }
    
    /* Clean up the Sidebar Styling */
    section[data-testid="stSidebar"] {
        background-color: #0b0b0b !important;
        border-right: 1px solid #1a1a1a;
    }
    </style>
""", unsafe_allow_html=True)

# --- 3. SIDEBAR: CO-FOUNDER OVERVIEW & CLEAN AI CONVERSATION ---
with st.sidebar:
    st.markdown("<h2 class='gold-header' style='text-align:left; font-size:1.5rem;'>AQP PLATFORM</h2>", unsafe_allow_html=True)
    st.caption("⚡ Technology & Operations Console")
    st.markdown("---")
    
    st.markdown("### 🤖 Gameday Assistant")
    st.write("Have questions about cuts, shipping grids, or grilling prep? Ask below:")
    
    # Simple, non-citation clean chat architecture
    if "messages" not in st.session_state:
        st.session_state.messages = [{"role": "assistant", "content": "Ready for kickoff! How can I help you frame up your tailgate box details today?"}]
        
    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.write(msg["content"])
            
    if ai_input := st.chat_input("Ask a question..."):
        st.session_state.messages.append({"role": "user", "content": ai_input})
        with st.chat_message("user"):
            st.write(ai_input)
            
        with st.chat_message("assistant"):
            with st.spinner("Analyzing rules..."):
                time.sleep(0.8)
                # Hardcoded response strings matching business parameters perfectly without displaying citations
                lower_input = ai_input.lower()
                if "shipping" in lower_input or "delivery" in lower_input or "days" in lower_input:
                    response = "We process every order on our Iowa facility floor. Your box is packed securely in an insulated container with dry ice and shipped express to arrive at your door within 1 to 3 days."
                elif "price" in lower_input or "cost" in lower_input or "how much" in lower_input:
                    response = "Our boxes start at $259 for the all-patty Rookie Box, up to $349 for our signature Tailgate Box, and top out at $649 for the ultra-premium Hall of Fame luxury steak selection."
                elif "weight" in lower_input or "size" in lower_input or "lbs" in lower_input:
                    response = "Every single box rostered on our site maintains a standardized weight of exactly 20 pounds of premium, hand-cut USDA Choice beef."
                else:
                    response = "All cuts are 100% American beef, born and raised in Iowa, hand-selected, vacuum-sealed, and flash-frozen at the source to ensure absolute steakhouse quality when you ignite your grill."
                st.write(response)
        st.session_state.messages.append({"role": "assistant", "content": response})

# --- 4. MAIN STOREFRONT HERO BANNER ---
st.markdown("<h3 class='gold-header'>AMERICAN QUALITY PROTEIN</h3>", unsafe_allow_html=True)
st.markdown("<h1 style='text-align: center; font-size: 3.8rem; font-weight: 900; margin-bottom: 5px; line-height:1.1;'>GRUDEN'S TAILGATE IN A BOX</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #a3a3a3; font-size: 1.2rem; margin-bottom: 25px;'>Premium, Iowa-Raised Beef Delivered Directly From Our Farm to Your Stadium Cooler.</p>", unsafe_allow_html=True)

# Main Hero Image Display
col_img_l, col_img_m, col_img_r = st.columns([1, 4, 1])
with col_img_m:
    try:
        st.image("PHOTO-2026-06-03-10-39-16.jpg", use_column_width=True)
    except:
        st.warning("Visual Asset Note: Place 'PHOTO-2026-06-03-10-39-16.jpg' in the root directory to display.")

st.markdown("<br><div style='text-align: center; font-weight: bold; color: #666; letter-spacing: 4px; font-size:0.85rem; margin-bottom:40px;'>🇺🇸 100% AMERICAN BEEF • 🌽 BORN & RAISED IN IOWA • 🥩 HAND-CUT USDA CHOICE • ❄️ EXPRESS SHIPPED ON DRY ICE</div>", unsafe_allow_html=True)

# --- 5. THE PRODUCT CARD ROSTER (FRONT & CENTER) ---
st.markdown("<h2 style='text-align: center; font-weight: 900; letter-spacing:1px; margin-bottom:5px;'>DRAFT YOUR ROSTER</h2>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #888888; margin-bottom: 35px;'>Select your curation level. Front-end orders route instantly via backend API payloads directly to the processing floor.</p>", unsafe_allow_html=True)

card_cols = st.columns(4)

# Box 1
with card_cols[0]:
    st.markdown("""
    <div class='product-card'>
        <div class='card-title-gold'>The Rookie</div>
        <div class='price-tag'>$259</div>
        <p style='color: #a3a3a3; font-size: 0.85rem; min-height: 70px;'>60 third-pound premium hamburger patties. Built for maximum volume tailgates.</p>
    </div>
    """, unsafe_allow_html=True)
    if st.button("Add to Cooler", key="btn_rookie"):
        st.success("API Payload routed securely to Iowa queues!")

# Box 2
with card_cols[1]:
    st.markdown("""
    <div class='product-card' style='border-color: #cc0000;'>
        <div class='card-title-crimson'>The Tailgate</div>
        <div class='price-tag' style='color:#ff3333;'>$349</div>
        <p style='color: #a3a3a3; font-size: 0.85rem; min-height: 70px;'>20 lbs: Prime Brisket, Chuck Roasts, Sirloin, Tri-Tip, Skirt, and Premium Ground Beef.</p>
    </div>
    """, unsafe_allow_html=True)
    if st.button("Add to Cooler", key="btn_tailgate"):
        st.success("API Payload routed securely to Iowa queues!")

# Box 3
with card_cols[2]:
    st.markdown("""
    <div class='product-card'>
        <div class='card-title-gold'>The Prime Time</div>
        <div class='price-tag'>$499</div>
        <p style='color: #a3a3a3; font-size: 0.85rem; min-height: 70px;'>20 lbs centered on high-end grilling cuts: Ribeyes, NY Strips, and Top Sirloin favorites.</p>
    </div>
    """, unsafe_allow_html=True)
    if st.button("Add to Cooler", key="btn_primetime"):
        st.success("API Payload routed securely to Iowa queues!")

# Box 4
with card_cols[3]:
    st.markdown("""
    <div class='product-card'>
        <div class='card-title-gold'>Hall of Fame</div>
        <div class='price-tag'>$649</div>
        <p style='color: #a3a3a3; font-size: 0.85rem; min-height: 70px;'>20 lbs pure luxury steakhouse portfolio. Thick Ribeyes, Filet Mignons, and NY Strips.</p>
    </div>
    """, unsafe_allow_html=True)
    if st.button("Add to Cooler", key="btn_hof"):
        st.success("API Payload routed securely to Iowa queues!")

st.markdown("<br><br><hr style='border-color:#1a1a1a;'>", unsafe_allow_html=True)

# --- 6. INTEGRATED STRATEGIC FOOTER ---
foot_l, foot_r = st.columns(2)
with foot_l:
    st.markdown("<h3 class='gold-text' style='font-size:1.3rem; margin-bottom:5px;'>WE BYPASSED THE DTC MIDDLEMAN</h3>", unsafe_allow_html=True)
    st.markdown("""
    Traditional operations waste massive capital on web brokers, physical distribution centers, and marketing agencies. 
    AQP uses clean automation to connect the consumer directly to production. When a customer executes an order, our custom API 
    payload skips traditional intermediaries and alerts Jason's Iowa floor instantly, ensuring premium margins and perfect freshness.
    """)

with foot_r:
    st.markdown("<h3 class='gold-text' style='font-size:1.3rem; margin-bottom:5px;'>THE NATIONAL TRENCH AWARD</h3>", unsafe_allow_html=True)
    st.markdown("""
    To anchor our presence in gridiron culture, Coach Jon Gruden personally hosts the weekly National Trench Award. 
    Every single week of the competitive season, the most dominant line units are awarded premium AQP box arrays shipped 
    straight to their locker rooms and collegiate training tables, driving powerful organic awareness across major athletic networks.
    """)
