import streamlit as st
import time

# --- 1. PAGE CONFIGURATION ---
st.set_page_config(
    page_title="Gruden's Tailgate in a Box",
    page_icon="🥩",
    layout="wide",
    initial_sidebar_state="collapsed" # Hide the default sidebar completely
)

# --- 2. PREMIUM CSS INJECTION ---
st.markdown("""
    <style>
    /* Global Theme */
    .stApp { background-color: #050505; color: #ffffff; }
    header {visibility: hidden;} /* Hide default streamlit header */
    
    /* Typography & Branding */
    .gold-text { color: #D4AF37 !important; font-weight: 800; text-transform: uppercase; }
    .crimson-text { color: #cc0000 !important; font-weight: 900; text-transform: uppercase; }
    
    /* Top Navigation Button Styling */
    div[data-testid="column"] button {
        width: 100%;
        background-color: transparent !important;
        border: 1px solid #333 !important;
        color: #a3a3a3 !important;
        font-weight: bold !important;
        transition: 0.3s;
    }
    div[data-testid="column"] button:hover {
        border-color: #D4AF37 !important;
        color: #D4AF37 !important;
    }

    /* Product Cards - Fixed Heights for Alignment */
    .product-card {
        background: linear-gradient(135deg, #111111 0%, #161616 100%);
        padding: 20px;
        border-radius: 12px 12px 0 0;
        border: 1px solid #222222;
        border-bottom: none;
        text-align: center;
    }
    .price-tag { font-size: 2rem; font-weight: 900; color: #ffffff; margin: 10px 0; }
    .box-desc { 
        color: #a3a3a3; 
        font-size: 0.9rem; 
        min-height: 100px; /* THIS FIXES THE BUTTON ALIGNMENT */
    }
    
    /* Action Buttons (Add to Cooler) */
    .stButton>button[kind="primary"] {
        width: 100%;
        background-color: #1a1a1a !important;
        color: #D4AF37 !important;
        border: 1px solid #D4AF37 !important;
        border-radius: 0 0 12px 12px !important;
        padding: 15px 0 !important;
        text-transform: uppercase !important;
        font-weight: bold !important;
        margin-top: -15px !important;
    }
    .stButton>button[kind="primary"]:hover {
        background-color: #cc0000 !important;
        color: #ffffff !important;
        border-color: #cc0000 !important;
    }

    /* Floating Bottom-Right AI Assistant */
    div[data-testid="stPopover"] {
        position: fixed;
        bottom: 30px;
        right: 30px;
        z-index: 9999;
    }
    div[data-testid="stPopover"] > button {
        background-color: #cc0000 !important;
        color: white !important;
        border-radius: 50px !important;
        border: none !important;
        padding: 15px 25px !important;
        font-size: 16px !important;
        box-shadow: 0 4px 15px rgba(204,0,0,0.5) !important;
    }
    </style>
""", unsafe_allow_html=True)

# --- 3. TOP NAVIGATION LOGIC ---
if 'current_page' not in st.session_state:
    st.session_state.current_page = "Home"

# Top Navigation Bar Layout
st.markdown("<h2 style='text-align: center; color: #D4AF37; font-weight: 900; letter-spacing: 2px;'>GRUDEN'S TAILGATE IN A BOX</h2>", unsafe_allow_html=True)
nav1, nav2, nav3, nav4, nav5 = st.columns(5)

with nav1:
    if st.button("🏟️ HOME", use_container_width=True): st.session_state.current_page = "Home"
with nav2:
    if st.button("🥩 SHOP BOXES", use_container_width=True): st.session_state.current_page = "Shop"
with nav3:
    if st.button("⚖️ BULK SHARES", use_container_width=True): st.session_state.current_page = "Bulk"
with nav4:
    if st.button("🚜 OUR STORY", use_container_width=True): st.session_state.current_page = "Story"
with nav5:
    if st.button("🏈 NIL AWARD", use_container_width=True): st.session_state.current_page = "NIL"

st.markdown("---")

# --- 4. PAGE ROUTING ---

# PAGE: HOME
if st.session_state.current_page == "Home":
    st.markdown("<h1 style='text-align: center; font-size: 4rem; font-weight: 900; line-height: 1.1;'>THE ULTIMATE TAILGATE.<br><span class='crimson-text'>DELIVERED.</span></h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #a3a3a3; font-size: 1.2rem; margin-bottom: 2rem;'>Premium, Iowa-Raised Beef Delivered Directly From Our Farm to Your Stadium Cooler.</p>", unsafe_allow_html=True)
    
    col_img_l, col_img_m, col_img_r = st.columns([1, 4, 1])
    with col_img_m:
        try:
            st.image("PHOTO-2026-06-03-10-39-16.jpg", use_column_width=True)
        except:
            st.warning("Please upload 'PHOTO-2026-06-03-10-39-16.jpg' to view the main promotional image.")
            
    st.markdown("<div style='text-align: center; font-weight: bold; color: #666; letter-spacing: 4px; font-size:0.85rem; margin-top:20px;'>🇺🇸 100% AMERICAN BEEF • 🌽 BORN & RAISED IN IOWA • 🥩 HAND-CUT USDA CHOICE</div>", unsafe_allow_html=True)

# PAGE: SHOP BOXES
elif st.session_state.current_page == "Shop":
    st.markdown("<h2 style='text-align: center; font-weight: 900;'>DRAFT YOUR ROSTER</h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #888888; margin-bottom: 40px;'>Select your curation level. Orders route instantly to our Iowa floor for hand-cutting and dry-ice packaging.</p>", unsafe_allow_html=True)
    
    c1, c2, c3, c4 = st.columns(4)
    
    with c1:
        st.markdown("""<div class='product-card'><div class='gold-text' style='font-size:1.3rem;'>The Rookie</div><div class='price-tag'>$259</div><div class='box-desc'>60 third-pound premium hamburger patties. Built for high-volume family cookouts.</div></div>""", unsafe_allow_html=True)
        if st.button("ADD TO COOLER", key="btn1", type="primary"): st.success("Routed to Iowa fulfillment!")
    with c2:
        st.markdown("""<div class='product-card' style='border-color: #cc0000;'><div class='crimson-text' style='font-size:1.3rem;'>The Tailgate</div><div class='price-tag' style='color:#ff3333;'>$349</div><div class='box-desc'>20 lbs of brisket, chuck roasts, top sirloin, tri-tip, skirt, and ground beef.</div></div>""", unsafe_allow_html=True)
        if st.button("ADD TO COOLER (COACH'S PICK)", key="btn2", type="primary"): st.success("Routed to Iowa fulfillment!")
    with c3:
        st.markdown("""<div class='product-card'><div class='gold-text' style='font-size:1.3rem;'>The Prime Time</div><div class='price-tag'>$499</div><div class='box-desc'>20 lbs centered on classic premium cuts: Ribeye, NY Strip, and Top Sirloin.</div></div>""", unsafe_allow_html=True)
        if st.button("ADD TO COOLER", key="btn3", type="primary"): st.success("Routed to Iowa fulfillment!")
    with c4:
        st.markdown("""<div class='product-card'><div class='gold-text' style='font-size:1.3rem;'>Hall of Fame</div><div class='price-tag'>$649</div><div class='box-desc'>20 lbs pure luxury steaks. Ribeyes, Filet Mignons, and NY Strips. No fillers.</div></div>""", unsafe_allow_html=True)
        if st.button("ADD TO COOLER", key="btn4", type="primary"): st.success("Routed to Iowa fulfillment!")

# PAGE: BULK SHARES (NEW)
elif st.session_state.current_page == "Bulk":
    st.markdown("<h2 style='text-align: center; font-weight: 900;'>BIG APPETITES & BULK SHARES</h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #888888; margin-bottom: 40px; max-width: 800px; margin-left: auto; margin-right: auto;'>For the serious families, deep-freezer owners, and legendary tailgaters. Skip the 20 lb boxes and buy a massive, pre-sold share of a full Iowa steer. We harvest, process, cryovac, and express ship it directly to you.</p>", unsafe_allow_html=True)
    
    b1, b2 = st.columns(2)
    with b1:
        st.markdown("""
        <div class='product-card'>
            <div class='gold-text' style='font-size:1.5rem;'>The Quarter Share (1/4 Steer)</div>
            <div class='price-tag'>$1,695</div>
            <div class='box-desc'>
                <strong>140 lbs of perfectly packaged premium beef.</strong><br><br>
                Ideal for a standard deep freezer. This share keeps an active family grilling all season long. Price includes the harvest processing fee, heavy-duty insulated boxing, and 1-3 day express shipping straight from Iowa.
            </div>
        </div>
        """, unsafe_allow_html=True)
        if st.button("SECURE 1/4 SHARE (10% DEPOSIT)", key="btn_q", type="primary"): st.success("Deposit routing initiated via API!")

    with b2:
        st.markdown("""
        <div class='product-card' style='border-color: #cc0000;'>
            <div class='crimson-text' style='font-size:1.5rem;'>The Half Share (1/2 Steer)</div>
            <div class='price-tag' style='color:#ff3333;'>$3,390</div>
            <div class='box-desc'>
                <strong>280 lbs of our absolute best yields.</strong><br><br>
                The ultimate investment in your family's protein. A massive yield of steaks, roasts, and ground beef. Price is all-inclusive for harvest, processing, and multi-box dry ice express delivery.
            </div>
        </div>
        """, unsafe_allow_html=True)
        if st.button("SECURE 1/2 SHARE (10% DEPOSIT)", key="btn_h", type="primary"): st.success("Deposit routing initiated via API!")

# PAGE: OUR STORY
elif st.session_state.current_page == "Story":
    st.markdown("<h2 style='font-weight: 900;'>WE KILLED THE MIDDLEMAN</h2>", unsafe_allow_html=True)
    st.write("""
    Traditional online meat brands acquire customers through massive advertising spending, source from processing brokers, and utilize external logistics centers. Every single step cuts their margin and delays your delivery.
    
    **The Zero-Latency Front End**
    We changed the game. When you click order, our custom API payload skips the corporate bureaucracy and transmits directly to Jason Birt's fulfillment floor in Iowa for immediate processing. 
    
    He cuts it, packs it in an insulated container with compostable foam and dry ice, and ships it express to your door. Better margins for us. Better beef for you.
    """)

# PAGE: NIL AWARD
elif st.session_state.current_page == "NIL":
    st.markdown("<h2 style='font-weight: 900;'>DOMINATING THE TRENCHES</h2>", unsafe_allow_html=True)
    st.write("""
    Football games are won and lost on the line of scrimmage. To honor the hardest workers on the field, Coach Jon Gruden personally presents the weekly **National Trench Award**.
    
    Every week during the college football season, the most dominant Offensive Line and Defensive Line units in the country are awarded premium American Quality Protein beef, shipped directly to their training tables.
    """)

# --- 5. FLOATING AI ASSISTANT (BOTTOM RIGHT) ---
with st.popover("💬 GAMEDAY AI SUPPORT", use_container_width=False):
    st.markdown("<div class='gold-text' style='font-size: 1rem; margin-bottom: 10px;'>AQP Virtual Assistant</div>", unsafe_allow_html=True)
    
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = [{"role": "assistant", "content": "Welcome to the roster! How can I help you today?"}]
        
    for msg in st.session_state.chat_history:
        with st.chat_message(msg["role"]):
            st.write(msg["content"])
            
    if prompt := st.chat_input("Ask about cuts, shipping, or bulk shares..."):
        st.session_state.chat_history.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.write(prompt)
            
        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                time.sleep(0.5)
                # AI Logic without any citations
                p_lower = prompt.lower()
                if "shipping" in p_lower or "days" in p_lower:
                    response = "We express ship all boxes from our Iowa facility on dry ice. Deliveries typically arrive in 1 to 3 days."
                elif "bulk" in p_lower or "share" in p_lower or "steer" in p_lower:
                    response = "We offer a 1/4 steer share (140 lbs) for $1,695, and a 1/2 steer share (280 lbs) for $3,390. Those prices include the harvest fee, packaging, and express shipping."
                else:
                    response = "All of our beef is 100% American, USDA Choice, raised in Iowa, and vacuum-sealed for maximum freshness. Check out 'Shop Boxes' or 'Bulk Shares' at the top to draft your roster!"
                st.write(response)
        st.session_state.chat_history.append({"role": "assistant", "content": response})
