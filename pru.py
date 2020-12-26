from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def hello():
    return str(datetime.utcnow())


@app.route('/api', methods=['GET'])
def api():
    return jsonify({"time":str(datetime.utcnow())})

if __name__ == '__main__':
    app.run()
