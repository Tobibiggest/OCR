import easyocr
from pdf2image import convert_from_path
import os
import re


reader = easyocr.Reader(['en'])  

def extract_text_from_image(image_path):
    """ Extract text from an image using EasyOCR """
    result = reader.readtext(image_path, detail=0)  
    return "\n".join(result)

def extract_text_from_pdf(pdf_path):
    """ Convert PDF to images and extract text from each page using EasyOCR """
    images = convert_from_path(pdf_path)
    text_output = ""

    for i, image in enumerate(images):
        image_path = f"temp_page_{i}.png"
        image.save(image_path, "PNG")
        extracted_text = extract_text_from_image(image_path)
        text_output += extracted_text + "\n"
        os.remove(image_path)  # Clean up

    # Debug statement to print all extracted text
    print("DEBUG: Full Extracted Text from Document:\n", text_output)

    return text_output


def preprocess_text(text):
    """ Replace common OCR errors in the text """
    replacements = {
        "Stanbir": "Stanbic",  # Fix bank name
        "[L:": "Terminal ID:",  # Fix Terminal ID format
        "!": "1",  # Replace '!' with '1'
        "z": "2",  # Replace 'z' with '2'
        "Reefererec": "Reference",  # Fix "Reference"
        "Numrver": "Number",  # Fix "Number"
        " ": "",  # Remove extra spaces
        "4": "9",
        "K": "F",
    }
    for old, new in replacements.items():
        text = text.replace(old, new)
    return text

def extract_transaction_details(text):
    """ Extract Terminal ID, STAN, and RRN using regex """
    text = preprocess_text(text)  # Preprocess the text to fix OCR errors
    
    patterns = {
        #"Terminal ID": r"Terminal\s*ID[:\s-]*([\w\d]+)",  
        "STAN": r"STAN[:\s-]*([\d]+)",  
        #"RRN": r"(?:Reference\s*Number|RRN)[:\s-]*([\d]+)"
    }
    
    extracted_data = {}
    for key, pattern in patterns.items():
        match = re.search(pattern, text, re.IGNORECASE)
        extracted_data[key] = match.group(1) if match else "Not found"
    
    # Debug statement to print extracted data
    print("DEBUG: Extracted Transaction Details:", extracted_data)

    return extracted_data

