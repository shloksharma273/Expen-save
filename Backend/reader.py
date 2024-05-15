import time
import re

def extract_payment_amount(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
        pattern = r'Rs:(\d+\.\d{2})'
        match = re.search(pattern, content)
        if match:
            return float(match.group(1))
        else:
            return None

file_path = 'messages.txt'

while True:
    payment_amount = extract_payment_amount(file_path)
    if payment_amount is not None:
        print(f"Sending payment amount: {payment_amount}")
        import requests
        response = requests.post('http://localhost:5000/api', json={'amount': payment_amount})
        print(response.status_code)
    time.sleep(10)  # Check every 10 seconds
