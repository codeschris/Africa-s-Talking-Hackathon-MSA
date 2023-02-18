# Your code goes here
import africastalking as AT
import os
from flask import Flask, request

app = Flask(__name__)

response = ""

@app.route('/', methods=['POST', 'GET'])
def ussd_callback():
    global response
    session_id = request.values.get("sessionId", None)
    service_code = request.values.get("serviceCode", None)
    phone_number = request.values.get("phoneNumber", None)
    text = request.values.get("text", "default")
    print(text)
    if text == '':
        response = "CON Units Registration: Enter your Reg. No: (for testing purposes: BS1/123/2020)"

    elif text == 'BS1/123/2020':
        response = "CON Enter Year of study"

    elif text == 'BS1/123/2020*2':
        response = "CON Enter semester"

    elif text == 'BS1/123/2020*2*1':
        response = "CON Units for Y2S1\n 1. Calculus\n 2. Geometry\n 3. Java\n 4. PHP\n Select options below:\n (i): Register all (ii): Drop all (iii): Cancel"

    elif text == 'BS1/123/2020*2*1*1':
        response = "END You've successfully registered all units!"

    elif text == 'BS1/123/2020*2*1*ii':
        response = "END You've successfully dropped all units!"

    elif text == 'BS1/123/2020*2*1*iii':
        response = "END End of session!"

    #else:
       # response = "END Thank you very much!\n"
    return response

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=os.environ.get('PORT'))