# main/airtable_service.py
import requests

AIRTABLE_API_KEY = 'patA8uN5MRNI0SMdF.658add4be79cfa0342f9a000e9c2321e89ce1863ed300b971e654c2777de7dd7'
BASE_ID = 'appQwaugYAZTqsajd'
TABLE_NAME = 'Templates'

def get_records():
    url = f'https://api.airtable.com/v0/{BASE_ID}/{TABLE_NAME}'
    headers = {
        'Authorization': f'Bearer {AIRTABLE_API_KEY}',
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()['records']
    else:
        return None