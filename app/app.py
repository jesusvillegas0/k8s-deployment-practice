from flask import Flask
import os
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, Kubernetes, nueva version 2.0! Version: ' + os.environ.get('APP_VERSION', '2.0.1')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
