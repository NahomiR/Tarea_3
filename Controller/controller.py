from flask import Flask, request, jsonify, abort
from repository import ItemRepository

app = Flask(__name__)
item_repo = ItemRepository()

@app.route('/item', methods=['GET'])
def get_all_items():
    items = item_repo.get_all_items()
    return jsonify(items), 200

@app.route('/item', methods=['POST'])
def add_item():
    data = request.json
    if 'SKU' in data and 'name' in data:
        item_repo.add_item(data)
        return 'Item added', 201
    else:
        return 'Invalid data format', 400

@app.route('/item/<string:sku>', methods=['DELETE'])
def delete_item(sku):
    if item_repo.delete_item(sku):
        return 'Item deleted', 204
    else:
        return 'Item not found', 404

if __name__ == '__main__':
    app.run(debug=True) 