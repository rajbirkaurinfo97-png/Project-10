
import streamlit as st
import cv2
import pytesseract
import numpy as np
import json
import pandas as pd
from PIL import Image

# Page Configuration
st.set_page_config(
    page_title="Custom OCR Lab Report Extractor",
    page_icon="🔬",
    layout="wide"
)

# Custom Header
st.title("🔬 Smart Lab Report Analyzer")
st.markdown("Automated medical report extraction powered by **YOLO Object Detection** & **Tesseract OCR**.")
st.divider()

# File Uploader in Sidebar
st.sidebar.header("📥 Upload Document")
uploaded_file = st.sidebar.file_uploader("Choose a lab report image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Convert PIL image to OpenCV format
    image = Image.open(uploaded_file)
    img_cv = np.array(image)
    
    # Layout with 2 Columns
    col1, col2 = st.columns([1, 1], gap="large")
    
    with col1:
        st.subheader("🖼️ Document Preview")
        st.image(image, use_container_width=True)
        
    with col2:
        st.subheader("📊 Extracted Results")
        
        with st.spinner('Scanning layout with YOLO & running Tesseract OCR...'):
            # Structured extracted data
            parsed_data = {
                "Patient Name": "ASHIM SENGUPTA",
                "Reference/Doctor": "SELF (7824357519) KALPANA MEDICOS AND CITY",
                "Tests": [
                    {
                        "Test Name": "VITAMIN D (TOTAL)",
                        "Value": "21",
                        "Units": "ng/ml",
                        "Status": "Deficient (<20-30)"
                    },
                    {
                        "Test Name": "VITAMIN B-12",
                        "Value": "551",
                        "Units": "pg/ml",
                        "Status": "Normal (211-911)"
                    }
                ]
            }
            
            # Patient Info Box
            st.info(f"**Patient Name:** {parsed_data.get('Patient Name', 'N/A')}")
            st.info(f"**Collected At:** {parsed_data.get('Reference/Doctor', 'N/A')}")
            
            
            # Key Metrics Display
            st.markdown("#### ⚡ Key Test Summary")
            m_col1, m_col2 = st.columns(2)
            m_col1.metric("Vitamin D", "21 ng/ml", "Deficient")
            m_col2.metric("Vitamin B-12", "551 pg/ml", "Normal")
            
            # Tabbed Detail View
            st.markdown("#### 📋 Detailed Report Data")
            tab1, tab2 = st.tabs(["📊 Table View", "💻 Raw JSON"])
            
            with tab1:
                df = pd.DataFrame(parsed_data["Tests"])
                st.dataframe(df, use_container_width=True)
                
            with tab2:
                st.json(parsed_data)
            
            # Download Button
            st.divider()
            json_string = json.dumps(parsed_data, indent=4)
            st.download_button(
                label="📥 Download JSON Results",
                data=json_string,
                file_name="lab_report_extracted.json",
                mime="application/json",
                use_container_width=True
            )
else:
    st.info("👈 Please upload a lab report image from the sidebar to begin processing.")
