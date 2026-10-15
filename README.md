# Custom OCR Lab Report Extractor (Project-10)

An end-to-end Automated Medical Lab Report Parsing and Extraction System built using **YOLO Object Detection**, **Tesseract OCR**, **OpenCV**, and **Streamlit Community Cloud**.

---

##  Live Application
 **Streamlit Live Dashboard**: [https://project-10-hyuqxswfk9i6udukrekncc.streamlit.app/](https://project-10-hyuqxswfk9i6udukrekncc.streamlit.app/)

---

##  Project Overview
Medical laboratory reports vary widely in visual layouts, headers, and tabular formats, making manual data entry slow and error-prone. This project delivers an automated pipeline that:
1. **Detects Layout Regions**: Uses YOLO for bounding-box detection of key report sections (patient metadata, test names, numerical values, unit ranges).
2. **Preprocessing & OCR**: Applies OpenCV noise reduction and adaptive thresholding prior to passing localized crops to Tesseract OCR.
3. **Structured Data Extraction**: Converts raw OCR outputs into key metrics, actionable diagnostic indicators, and clean tabular data formats.
4. **Interactive Dashboard**: Displays parsed lab report summaries, high-level patient metadata, and raw JSON outputs in real time.

---

##  Technology Stack
* **Frontend / Web Framework**: Streamlit
* **Computer Vision & Image Processing**: OpenCV (`opencv-python-headless`), PIL (Pillow)
* **Object Detection & Segmentation**: Ultralytics YOLO
* **Optical Character Recognition (OCR)**: Tesseract OCR (`pytesseract`, `tesseract-ocr`)
* **Data Processing & Analytics**: NumPy, Pandas
* **Deployment & OS Environment**: Streamlit Community Cloud (Debian Linux container with `libgl1`)

---

##  Repository Structure
```text
Project-10/
├── app.py                                          # Main Streamlit web application & execution pipeline
├── requirements.txt                               # Python package dependencies
├── packages.txt                                   # Linux system dependencies (libgl1, tesseract-ocr)
├── Custom_Object_Character_Recognition(OCR).ipynb  # Jupyter Notebook for model training & testing
├── Project 10_ Custom OCR Lab Report Extractor.pptx # Project presentation slide deck
├── Dashboard link with some image inputs.docx      # Test dataset & documentation link
└── README.md                                      # Documentation and project overview
