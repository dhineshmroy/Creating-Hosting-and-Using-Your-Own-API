from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/', methods=['GET'])
def greet():
    name = request.args.get('name', 'World')
    return jsonify({'message': f'Hello, {name}!'})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)  # for both local and fly.io use

