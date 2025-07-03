import os
from flask import Flask, request

app = Flask(__name__)

@app.route('/ping', methods=['GET'])
def ping():
    host = request.args.get('host')
    os.system(f"ping -c 1 {host}")
    return f"Pinging {host}..."

if __name__ == '__main__':
    app.run()
