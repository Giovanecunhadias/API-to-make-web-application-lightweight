from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def hello():
    return jsonify(message='Bem-vindo à sua API leve em Python!')

if __name__ == '__main__':
    app.run(debug=True)
