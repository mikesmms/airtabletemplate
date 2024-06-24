# main/views.py
from django.shortcuts import render
from .airtable_service import get_records

def index(request):
    records = get_records()
    return render(request, 'main/index.html', {'records': records})

def contact(request):
    return render(request, 'main/contact.html')