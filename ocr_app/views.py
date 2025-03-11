from django.shortcuts import render
from django.http import JsonResponse
from .utils import extract_text_from_pdf, extract_transaction_details
import os
from django.http import HttpResponse
import csv

def home(request):
    # Initialize extracted_data as None
    extracted_data = None

    if request.method == "POST" and request.FILES.get("file"):
        # Handle file upload and extraction
        uploaded_file = request.FILES["file"]
        media_path = "media/"
        os.makedirs(media_path, exist_ok=True)
        file_path = os.path.join(media_path, uploaded_file.name)

        # Save the uploaded file
        with open(file_path, "wb+") as destination:
            for chunk in uploaded_file.chunks():
                destination.write(chunk)

        # Extract text and transaction details
        extracted_text = extract_text_from_pdf(file_path)
        extracted_data = extract_transaction_details(extracted_text)

        # Store extracted_data in session for CSV download
        request.session['extracted_data'] = extracted_data

    # Render the home page with extracted_data (if available)
    return render(request, "ocr/home.html", {"extracted_data": extracted_data})

def download_csv(request):
    if request.method == "POST":
        # Create a CSV response
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="extracted_data.csv"'

        # Write CSV data
        writer = csv.writer(response)
        writer.writerow(['Field', 'Value'])

        # Retrieve extracted_data from session
        extracted_data = request.session.get('extracted_data', {})
        for key, value in extracted_data.items():
            writer.writerow([key, value])

        return response


def upload_file(request):
    if request.method == "POST" and request.FILES.get("file"):
        uploaded_file = request.FILES["file"]
        media_path = "media/"
        os.makedirs(media_path, exist_ok=True)
        file_path = os.path.join(media_path, uploaded_file.name)
        
        with open(file_path, "wb+") as destination:
            for chunk in uploaded_file.chunks():
                destination.write(chunk)
        
        extracted_text = extract_text_from_pdf(file_path)
        print("Extracted Text:", extracted_text)  # Debugging: Print the extracted text
        extracted_data = extract_transaction_details(extracted_text)
        return JsonResponse(extracted_data)
    
    return render(request, "ocr/upload.html")
