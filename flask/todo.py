from flask import Flask , jsonify , request

app = Flask(__name__)
#making a to do list
items = [
    {
        "id": 1,"name": "item1", "description": "This is item 1"
    },
    {
        "id": 2,"name": "item2", "description": "This is item 2"
    }
]
@app.route('/')
def home():
    return "welcome to todo list"

@app.route('/items')
def get_items():
    return jsonify(items)

@app.route('/items/<int:item_id>', methods=['GET'])
def get_item(item_id):
    item = next((item for item in items if item['id'] == item_id), None)
    if item is None:
        return jsonify({"message": "item not found"}), 404
    return jsonify(item)

@app.route('/items', methods=['POST'])
def create_item():
    data = request.get_json()
    if not data or 'name' not in data or 'description' not in data:
        return jsonify({"message": "invalid data"}), 400
    item = {
        "id": items[-1]['id'] + 1,
        "name": data['name'],
        "description": data['description']
    }
    items.append(item)
    return jsonify(item), 201

@app.route('/items/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    item = next((item for item in items if item['id'] == item_id), None)
    if item is None:
        return jsonify({"message": "item not found"}), 404
    data = request.get_json()
    if not data or 'name' not in data or 'description' not in data:
        return jsonify({"message": "invalid data"}), 400
    item['name'] = data['name']
    item['description'] = data['description']
    return jsonify(item)

@app.route('/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    global items
    items = [item for item in items if item['id'] != item_id]
    return jsonify({"message": "item deleted"}), 204
    


if __name__ == '__main__':
    app.run(debug=True)