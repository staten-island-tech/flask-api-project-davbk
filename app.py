from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route("/")
def index():
    response = requests.get("https://valorant-api.com/v1/bundles")
    data = response.json()
    bundles = data.get('data', [])
    items = []
    for bundle in bundles:
        items.append({
            'uuid': bundle.get('uuid'),
            'name': bundle.get('displayName'),
            'description': bundle.get('description'),
            'image': bundle.get('displayIcon')
        })

    return render_template("index.html", items=items)


@app.route("/item/<uuid>")
def item_detail(uuid):
    response = requests.get(f"https://valorant-api.com/v1/weapons/skins{uuid}")
    data = response.json()

    item = data.get('data')
    if not item:
        return "Item not found", 404

    return render_template("skin.html", item=item)

if __name__ == '__main__':
    app.run(debug=True)
