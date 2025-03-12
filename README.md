# **OCR-Based Transaction Processing with EasyOCR & PDF2Image**

## **Project Overview**
This project automates the extraction of critical transaction details—**Terminal ID, STAN (System Trace Audit Number), and RRN (Reference Retrieval Number)**—from financial receipts and statements using **EasyOCR** and **PDF2Image**.

## **Features**
✅ Convert PDFs to images for OCR processing  
✅ Extract structured text using **EasyOCR**  
✅ Preprocess and clean extracted data to improve accuracy  
✅ Use **Regular Expressions (Regex)** to retrieve key transaction details  
✅ Print extracted text and transaction details for debugging  
✅ Lightweight and efficient Python-based implementation  

## **Technologies Used**
- **Python** (OS, Regex, PIL, Logging)
- **EasyOCR** (Deep-learning-based OCR for text extraction)
- **PDF2Image** (Convert PDFs into images for OCR processing)
- **Regular Expressions** (Extract structured transaction details)

## **Installation**
### **Prerequisites**
Ensure you have Python installed. Then, install the required dependencies:
```bash
pip install easyocr pdf2image pillow
```

### **Running the Project**
1. Place your **PDF receipt** in the project folder.
2. Run the script to extract transaction details:
   ```bash
   python utils.py <path_to_pdf>
   ```
3. View extracted text and transaction details in the terminal.

## **Project Screenshots**
📌 ![Screenshot (38)](https://github.com/user-attachments/assets/dba9e54b-b938-43f5-801e-62cf84f32cad)
![Screenshot (37)](https://github.com/user-attachments/assets/27e7b059-435c-4c03-a44f-7bb2265d6c2c)


## **Video Demo**
🎥 Watch full demo on [LinkendIn](https://www.linkedin.com/posts/tobiloba-oluwadamilare-a850b0223_machinelearning-ocr-python-activity-7305180359862702081-nyOQ?utm_source=share&utm_medium=member_desktop&rcm=ACoAADgTsQUB-CKN8O7D3fow2KTN2OF0AK3yd08)


## **Future Enhancements**
- ✅ NLP-based text correction for improved accuracy
- ✅ Multi-language support for receipts from various regions
- ✅ Web interface for real-time transaction processing using **Django**

## **Contributing**
Pull requests are welcome! If you’d like to contribute, please fork the repository and submit a PR.

## **License**
This project is licensed under the **MIT License**.

---
🚀 **Let’s connect!** If you find this project useful, feel free to star ⭐ the repo and connect with me on [LinkedIn](https://www.linkedin.com/in/tobiloba-oluwadamilare-a850b0223/).

