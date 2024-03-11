from flask import Flask, request
import subprocess

app = Flask(__name__)

@app.route('/scan', methods=['POST'])
def scan():
    target = request.form.get('target')
    result = subprocess.run(['nmap', '-sV', target], capture_output=True, text=True)
    return result.stdout

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
