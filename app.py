from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route("/")
def index():
    response = requests.get("http://minecraft-ids.grahamedgecombe.com/items.json")
    data = response.json()

    items = []
    for item in data:
        items.append({
            'id': item['id'],
            'name': item['displayName'],
            'type': item['type'],
            'stackSize': item.get('stackSize', 64) 
        })

    return render_template("index.html", items=items)


@app.route("/item/<int:item_id>")
def item_detail(item_id):
    response = requests.get("http://minecraft-ids.grahamedgecombe.com/items.json")
    data = response.json()

    item = next((i for i in data if i['id'] == item_id), None)
    if not item:
        return "Item not found", 404

    return render_template("item.html", item=item)


if __name__ == '__main__':
    app.run(debug=True)
