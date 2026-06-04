import streamlit as st
import time

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="Gruden's Tailgate Box",
    page_icon="🥩",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- BRANDING & CSS ---
st.markdown("""
    <style>
    .stApp { background-color: #0a0a0a; color: #ffffff; }
    .gold-text { color: #D4AF37 !important; font-weight: 800; }
    .red-text { color: #cc0000 !important; font-weight: 900; }
    .product-card {
        background-color: #161616;
        padding: 24px;
        border-radius: 12px;
        border: 1px solid #262626;
        text-align: center;
        height: 100%;
    }
    .stButton>button {
        width: 100%;
        background-color: #1a1a1a;
        color: #ffffff;
        border: 1px solid #D4AF37;
        text-transform: uppercase;
        font-weight: bold;
        transition: all 0.3s ease;
    }
    .stButton>button:hover {
        background-color: #cc0000;
        border-color: #cc0000;
        color: #ffffff;
    }
    </style>
""", unsafe_allow_html=True)

# --- SIDEBAR NAVIGATION & AI ---
st.sidebar.markdown("<h2 class='gold-text'>NAVIGATION</h2>", unsafe_allow_html=True)
page = st.sidebar.radio("", [
    "🏟️ Home - The Ultimate Tailgate", 
    "🥩 Shop The Roster", 
    "🚜 The Iowa Farm Story", 
    "🏈 NIL Trench Award"
])

st.sidebar.markdown("---")
st.sidebar.markdown("### 🤖 Gameday AI Support")
st.sidebar.caption("Ask me about shipping, cuts, or prep!")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = [{"role": "assistant", "content": "Welcome! I'm here to help you draft your perfect tailgate box."}]

for msg in st.session_state.chat_history:
    with st.sidebar.chat_message(msg["role"]):
        st.write(msg["content"])

if ai_prompt := st.sidebar.chat_input("Ask a question..."):
    st.session_state.chat_history.append({"role": "user", "content": ai_prompt})
    with st.sidebar.chat_message("user"):
        st.write(ai_prompt)
    
    with st.sidebar.chat_message("assistant"):
        with st.spinner("Thinking..."):
            time.sleep(1)
            # AI Logic mimicking Jason's fulfillment rules
            response = "All of our boxes are a full 20 lbs of USDA Choice beef[cite: 1]. We process it in Iowa, vacuum-seal it, and ship it express on dry ice straight to your door[cite: 1, 3]!"
            st.write(response)
    st.session_state.chat_history.append({"role": "assistant", "content": response})

# --- PAGE: HOME ---
if page == "🏟️ Home - The Ultimate Tailgate":
    st.markdown("<h3 style='text-align: center; color: #D4AF37; letter-spacing: 3px;'>AMERICAN QUALITY PROTEIN PRESENTS</h3>", unsafe_allow_html=True)
    st.markdown("<h1 style='text-align: center; font-size: 4rem; font-weight: 900;'>GRUDEN'S TAILGATE IN A BOX</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #a3a3a3; font-size: 1.2rem; margin-bottom: 2rem;'>Premium, Iowa-Raised Beef Delivered Directly From Our Farm to Your Stadium Cooler.</p>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 3, 1])
    with col2:
        try:
            st.image("PHOTO-2026-06-03-10-39-16.jpg", use_column_width=True)
        except:
            st.error("Please ensure 'PHOTO-2026-06-03-10-39-16.jpg' is uploaded.")

    st.markdown("<br><div style='text-align: center; font-weight: bold; color: #888; word-spacing: 15px;'>🇺🇸 100%_AMERICAN_BEEF 🌽 BORN_&_RAISED_IN_IOWA 🥩 HAND-CUT ❄️ EXPRESS_SHIPPED_ON_DRY_ICE</div>", unsafe_allow_html=True)

# --- PAGE: SHOP THE ROSTER ---
elif page == "🥩 Shop The Roster":
    st.markdown("<h1 style='text-align: center; font-weight: 900; text-transform: uppercase;'>Draft Your Box</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #888888; margin-bottom: 3rem;'>Select your curation. Orders are routed instantly to our Iowa floor for hand-cutting and dry-ice packaging.</p>", unsafe_allow_html=True)
    
    col1, col2, col3, col4 = st.columns(4)
    
    boxes = [
        {"col": col1, "name": "The Rookie", "price": "259", "color": "gold-text", "desc": "60 third-pound premium hamburger patties. Built for high-volume cookouts[cite: 1]."},
        {"col": col2, "name": "The Tailgate (Coach's Pick)", "price": "349", "color": "red-text", "desc": "20 lbs of brisket, chuck roasts, top sirloin, tri-tip, skirt, and premium ground beef[cite: 1]."},
        {"col": col3, "name": "The Prime Time", "price": "499", "color": "gold-text", "desc": "20 lbs of classic premium grilling steaks: Ribeyes, NY Strips, and Top Sirloin[cite: 1]."},
        {"col": col4, "name": "The Hall of Fame", "price": "649", "color": "gold-text", "desc": "20 lbs of pure luxury steaks. Ribeyes, Filet Mignons, and NY Strips. No fillers[cite: 1]."}
    ]
    
    for i, box in enumerate(boxes):
        with box["col"]:
            st.markdown(f"""
            <div class='product-card'>
                <h3 class='{box["color"]}'>{box["name"]}</h3>
                <h2 style='margin: 15px 0;'>${box["price"]}</h2>
                <p style='color: #a3a3a3; font-size: 0.9rem; min-height: 80px;'>{box["desc"]}</p>
            </div>
            <br>
            """, unsafe_allow_html=True)
            if st.button("Add to Cooler", key=f"btn_{i}"):
                with st.spinner("Processing API transmission..."):
                    time.sleep(1.2)
                st.success("API Payload Sent! Order routed to Jason's Iowa facility[cite: 3].")

# --- PAGE: THE IOWA FARM STORY ---
elif page == "🚜 The Iowa Farm Story":
    st.markdown("<h1 style='font-weight: 900; text-transform: uppercase;'>We Killed The Middleman</h1>", unsafe_allow_html=True)
    st.write("""
    Traditional online meat brands acquire customers through massive advertising spending, source from processing brokers, and utilize external logistics centers. Every step cuts margin and delays delivery.
    
    **The Zero-Latency Front End**
    We changed the game. When you click order, our custom API payload skips the corporate bureaucracy and transmits directly to Jason Birt's fulfillment floor in Iowa for immediate processing[cite: 2, 3]. 
    
    He cuts it, packs it in an insulated 14x14x14 container with compostable foam and dry ice, and ships it express to your door[cite: 1, 3]. Better margins for us. Better beef for you.
    """)

# --- PAGE: NIL TRENCH AWARD ---
elif page == "🏈 NIL Trench Award":
    st.markdown("<h1 style='font-weight: 900; text-transform: uppercase;'>Dominating The Trenches</h1>", unsafe_allow_html=True)
    st.write("""
    ### The Ultimate Trophy for the Big Guys
    Football games are won and lost on the line of scrimmage. To honor the hardest workers on the field, Coach Jon Gruden personally presents the weekly **National Trench Award**[cite: 2].
    
    Every week during the college football season, the most dominant Offensive Line and Defensive Line units in the country are awarded premium American Quality Protein beef, shipped directly to their training tables[cite: 2].
    
    *Supporting the athletes who bring the heat, every single Saturday.*
    """)