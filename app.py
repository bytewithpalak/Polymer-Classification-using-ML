import streamlit as st
import pandas as pd
import joblib

# Load saved model and tools
model = joblib.load("polymer_rf_model.pkl")
scaler = joblib.load("scaler.pkl")
le = joblib.load("label_encoder.pkl")

# Set custom page config
st.set_page_config(page_title="Polymer Classifier", page_icon="🧪", layout="centered")

# Header
st.markdown("<h1 style='color:#6a0dad;text-align:center;'>🧪 Polymer Type Classifier</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center;'>Upload your polymer data & let AI tell you what it is 💡</p>", unsafe_allow_html=True)
st.write("---")

# Sidebar
st.sidebar.header("📂 Upload Your File")
uploaded_file = st.sidebar.file_uploader("Upload CSV", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    
    st.subheader("📄 Uploaded Data")
    st.dataframe(df.head())

    try:
        # Drop unwanted columns
        X_new = df.drop(columns=["Unnamed: 0", "label", "smiles"], errors="ignore")
        
        # Scale features
        X_scaled = scaler.transform(X_new)

        # Predict
       y_pred = model.predict(X_scaled)
       y_label = y_pred  

        st.subheader("🔍 Predicted Polymer Types")
        st.success("✅ Successfully predicted! Here's the result:")
        st.dataframe(pd.DataFrame(y_label, columns=["Predicted Type"]))

    except Exception as e:
        st.error(f"❌ Oops! Something went wrong: {e}")
else:
    st.warning("⬅️ Please upload a valid CSV file to begin.")

# Footer
st.markdown("---")
st.markdown("<p style='text-align:center;font-size:13px;'>Made with ❤️ using Streamlit</p>", unsafe_allow_html=True)
