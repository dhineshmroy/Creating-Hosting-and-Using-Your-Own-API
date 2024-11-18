from flask import Flask, jsonify, request

app = Flask(__name__)


# Simulated database

users = {}

# GET all users or a specific user
@app.route('/users', methods=['GET'])
def getUsers():
    user_id = request.args.get('id')

    if user_id:
        user = users.get(user_id)
        if user:
            return jsonify({'id': user_id, 'details': user}), 200
        return jsonify({'error': 'User not found'}), 404
    return jsonify(users), 200

# POST to add a new user
@app.route('/users', methods=['POST'])
def add_user():
    data = request.get_json()
    user_id = data.get('id')
    if user_id in users:
        return jsonify({'error': 'User already exists'}), 400
    users[user_id] = data.get('details')
    return jsonify({'message': 'User added successfully'}), 201

# PUT to update a user
@app.route('/users/<user_id>', methods=['PUT'])
def update_user(user_id):
    if user_id not in users:
        return jsonify({'error': 'User not found'}), 404
    data = request.get_json()
    users[user_id] = data.get('details')
    return jsonify({'message': 'User updated successfully'}), 200

@app.route('/users/<user_id>', methods=['DELETE'])
def delete_user(user_id):
    if user_id not in users:
        return jsonify({'error': 'User not found'}), 404
    del users[user_id]
    return jsonify({'message': 'User deleted successfully'}), 200


@app.route('/', methods=['GET'])
def greet():
    name = request.args.get('name', 'World')
    return jsonify({'message': f'Hello, {name}!'})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)  # for both local and fly.io use

