from flask import Flask, render_template, request
import requests
import json

app = Flask(__name__)

# Configuration entries
sms_url = 'https://www.traccar.org/sms/'
sms_authorization = ''
sms_template = {
    'to': '{phone}',
    'message': '{message}'
}

# Route for the home page
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        phone_number = request.form['phone_number']
        message = request.form['message']
        token = request.form['token']
        send_sms_notification(phone_number, message, token)
        return "SMS notification sent successfully!"
    return render_template('index.html')

# Function to send an SMS notification
def send_sms_notification(phone_number, message, token):
    payload = sms_template.copy()
    payload['to'] = phone_number
    payload['message'] = message
    
    headers = {
        'Authorization': token,
        'Content-Type': 'application/json'
    }
    
    response = requests.post(sms_url, data=json.dumps(payload), headers=headers)
    
    if response.status_code != 200:
        raise Exception('Failed to send SMS notification.')

if __name__ == '__main__':
    app.run(debug=True)
