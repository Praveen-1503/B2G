import streamlit as st
from src.utils.data_loader import load_ngo_data, get_negotiation_profile
from src.agents.minister import MinisterAgent
from src.agents.cfo import CFOAgent
from src.engine.negotiation import NegotiationEngine

# Page Config
st.set_page_config(page_title="Agentic-SDG-17", layout="wide")

st.title("🤝 Agentic-SDG-17: The Strategic Friction Engine")
st.markdown("""
    **Transforming Global Partnerships from static documents into dynamic bargaining.** This sandbox simulates high-stakes negotiations to find **Debt-Neutral Swaps** before humans meet.
""")

# 1. Sidebar - Data Selection
st.sidebar.header("📁 Step 1: Select Partner Profile")
df = load_ngo_data()

if df is not None:
    target_ngo = st.sidebar.selectbox("Choose an NGO/Region to Simulate", df['NGO_Name'].unique())
    profile = get_negotiation_profile(df, target_ngo)

    st.sidebar.write("---")
    st.sidebar.subheader("Strategic Brief")
    st.sidebar.json(profile) # Quick view of constraints

    # 2. Main Area - Simulation Setup
    col1, col2 = st.columns(2)
    
    with col1:
        st.info(f"🏛️ **Minister Persona**\n\nGoal: {profile['mission']}\nConstraint: Zero Debt")
        
    with col2:
        st.warning("💼 **Corporate CFO Persona**\n\nGoal: ROI & ESG Growth\nConstraint: Business Utility")

    st.write("---")

    # 3. Execution - The Negotiation Sandbox
    if st.button("🚀 Start Multi-Agent Negotiation"):
        # Initialize Agents
        minister = MinisterAgent(profile)
        cfo = CFOAgent(profile)
        
        # Initialize Engine
        engine = NegotiationEngine(minister, cfo, max_rounds=5)
        
        st.subheader("📡 Live Bargaining Stream")
        with st.spinner("Agents are bargaining over resource swaps..."):
            history = engine.run_simulation()
            
        st.write("---")
        st.success("🏁 Simulation Complete. Review the 'Zones of Agreement' above.")
else:
    st.error("Please upload the 'ngo_details.csv' to the data/ folder to begin.")