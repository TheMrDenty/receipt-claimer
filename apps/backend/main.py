import json
import requests

url = "https://ocr.asprise.com/api/v1/receipt"



image_location1 = "./imgs/test-receipt-1.jpg"
image_location2 = "./imgs/test-receipt-2.jpg"
image_location3 = "./imgs/test-receipt-3.jpg"
image_location4 = "./imgs/test-receipt-4.jpg"
image_location5 = "./imgs/test-receipt-5.jpg"



# res = requests.post(url,
#                     data= {
#                         'api_key': 'TEST',
#                         'recognizer': 'auto',
#                         'ref_no': 'oct_python_123'
#                     },
#                     files={
#                         # replace image_location to get a new image read
#                         'file': open(image_location2, 'rb')
#                     })

# with open("response2.json", "w") as f:
#     json.dump(json.loads(res.text), f)

with open("response2.json", "r") as f:
    data = json.load(f)

print(data)
print()
print(data['receipts'][0].keys())
print()

items = data['receipts'][0]['items']

print(f"Your purchase at {data['receipts'][0]['merchant_name']}")

for item in items:
    print(f"{item['description']} - {data['receipts'][0]['currency']} {item['amount']}")

print("-" * 30)
print(f"Subtotal: {data['receipts'][0]['subtotal']}")
print("-" * 30)
print(f"Tax: {data['receipts'][0]['tax']}")
print("-" * 30)
print(f"Total: {data['receipts'][0]['total']}")