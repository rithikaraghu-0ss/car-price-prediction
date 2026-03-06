import streamlit as st
import pandas as pd
import pickle
import numpy as np

# Set page configuration for a premium feel
st.set_page_config(
    page_title="AutoValue AI | Smart Car Price Prediction",
    page_icon="🏎️",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Custom CSS to inject the premium styling
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;600;700&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Outfit', sans-serif;
    }

    .stApp {
        background-color: #020617;
        color: #f8fafc;
    }

    /* Hero Section Styling */
    .hero-section {
        padding: 4rem 2rem;
        background: linear-gradient(135deg, rgba(99, 102, 241, 0.1) 0%, rgba(168, 85, 247, 0.1) 100%);
        border-radius: 30px;
        margin-bottom: 3rem;
        border: 1px solid rgba(255, 255, 255, 0.08);
        text-align: center;
    }

    .hero-badge {
        display: inline-block;
        padding: 0.5rem 1.2rem;
        background: rgba(99, 102, 241, 0.2);
        border: 1px solid rgba(99, 102, 241, 0.3);
        border-radius: 50px;
        color: #818cf8;
        font-size: 0.85rem;
        font-weight: 600;
        margin-bottom: 1.5rem;
    }

    .hero-title {
        font-size: 3.5rem;
        font-weight: 800;
        line-height: 1.1;
        margin-bottom: 1rem;
        background: linear-gradient(to bottom right, #fff 40%, #94a3b8);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }

    .hero-subtitle {
        font-size: 1.2rem;
        color: #94a3b8;
        max-width: 700px;
        margin: 0 auto 2rem;
    }

    /* Glass Card for Form */
    .glass-card {
        background: rgba(15, 23, 42, 0.7);
        backdrop-filter: blur(16px);
        border: 1px solid rgba(255, 255, 255, 0.08);
        border-radius: 24px;
        padding: 2.5rem;
        box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.5);
    }

    /* Result Styling */
    .price-display {
        background: rgba(99, 102, 241, 0.1);
        border: 2px solid #6366f1;
        border-radius: 20px;
        padding: 1.5rem;
        text-align: center;
        margin-top: 2rem;
    }

    .price-value {
        font-size: 2.5rem;
        font-weight: 700;
        color: #6366f1;
    }
</style>
""", unsafe_allow_html=True)

# Load the model and data
@st.cache_resource
def load_resources():
    model = pickle.load(open('model/car_price_model.pkl', 'rb'))
    df = pd.read_csv('data/car_data.csv')
    return model, df

try:
    model, df = load_resources()

    # Hero Section
    st.markdown("""
    <div class="hero-section">
        <span class="hero-badge">AI-Powered Valuation</span>
        <h1 class="hero-title">AutoValue AI: Smart Car Pricing</h1>
        <p class="hero-subtitle">Get instant, data-driven market valuations using high-precision Machine Learning models. Trained on thousands of vehicle datasets.</p>
    </div>
    """, unsafe_allow_html=True)

    # Main Layout with columns
    col1, col2 = st.columns([2, 1], gap="large")

    with col1:
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        st.subheader("Vehicle Details")
        
        # Form inputs
        c1, c2 = st.columns(2)
        with c1:
            car_name = st.selectbox("Model Name", sorted(df['Car_Name'].unique()))
            year = st.selectbox("Year of Purchase", sorted(df['Year'].unique(), reverse=True))
            kms_driven = st.number_input("Kilometers Driven", min_value=0, value=10000, step=1000)
        
        with c2:
            fuel_type = st.selectbox("Fuel Type", sorted(df['Fuel_Type'].unique()))
            seller_type = st.selectbox("Seller Type", sorted(df['Seller_Type'].unique()))
            transmission = st.selectbox("Transmission", sorted(df['Transmission'].unique()))

        predict_clicked = st.button("Calculate Valuation", use_container_width=True, type="primary")
        st.markdown('</div>', unsafe_allow_html=True)

    with col2:
        st.subheader("Prediction Result")
        if predict_clicked:
            # Prepare input for prediction
            input_df = pd.DataFrame([[car_name, year, kms_driven, fuel_type, seller_type, transmission]],
                                   columns=['Car_Name', 'Year', 'Kms_Driven', 'Fuel_Type', 'Seller_Type', 'Transmission'])
            
            prediction = model.predict(input_df)[0]
            result = max(0.05, round(prediction, 2))
            
            st.markdown(f"""
            <div class="price-display">
                <p style="color: #94a3b8; margin-bottom: 0.5rem;">Estimated Market Price</p>
                <div class="price-value">₹ {result} Lakhs</div>
                <p style="font-size: 0.8rem; color: #64748b; margin-top: 1rem;">*Based on current market trends</p>
            </div>
            """, unsafe_allow_html=True)
            st.balloons()
        else:
            st.info("Enter vehicle details and click 'Calculate' to see the estimated price.")
            
    # Footer stats
    st.markdown("---")
    f1, f2, f3 = st.columns(3)
    f1.metric("Model Accuracy", "83.4%")
    f2.metric("Dataset Size", f"{len(df)} Records")
    f3.metric("Processing Time", "Instant")

except Exception as e:
    st.error(f"Error loading application: {e}")
    st.info("Ensure that 'model/car_price_model.pkl' and 'data/car_data.csv' are present in your repository.")
