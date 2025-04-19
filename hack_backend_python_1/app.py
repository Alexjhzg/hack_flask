from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  

# hack 1
@app.route('/users', methods=['GET'])
def get_users():
    return jsonify({'payload': 'success'})

# hack 2
@app.route('/user', methods=['POST'])
def create_user_post():
    return jsonify({'payload': 'success'})

# hack 3
@app.route('/user', methods=['DELETE'])
def delete_user():
    return jsonify({'payload': 'success'})

# hack 4
@app.route('/user', methods=['PUT'])
def update_user():
    return jsonify({
        'payload': 'success',
        'error': False
    })

# hack 5
@app.route('/api/v1/users', methods=['GET'])
def get_api_users():
    return jsonify({'payload': []})

# hack 6
@app.route('/api/v1/user', methods=['POST'])
def create_user_with_query():
    email = request.args.get('email')
    name = request.args.get('name')
    return jsonify({
        'payload': {
            'email': email,
            'name': name
        }
    })

# hack 7
@app.route('/api/v1/user/add', methods=['POST'])
def add_user_form():
    email = request.form.get('email')
    name = request.form.get('name')
    user_id = request.form.get('id')
    return jsonify({
        'payload': {
            'email': email,
            'name': name,
            'id': user_id
        }
    })

# hack 8
@app.route('/api/v1/user/create', methods=['POST'])
def create_user_json():
    if not request.is_json:
        return jsonify({"error": "Se esperaba JSON"}), 400

    data = request.get_json()
    email = data.get('email')
    name = data.get('name')
    user_id = data.get('id')

    return jsonify({
        "payload": {
            "email": email,
            "name": name,
            "id": user_id
        }
    })

if __name__ == '__main__':
    app.run(debug=True)