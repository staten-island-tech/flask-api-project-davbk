from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route("/")
def index():
    response = requests.get("https://valorant-api.com/v1/weapons/skins")
    data = response.json()
    skins = data.get('data', [])

    items = []
    for skin in skins:
        items.append({
            'uuid': skin.get('uuid'),
            'name': skin.get('displayName'),
            'image': skin.get('displayIcon')
        })

    return render_template("index.html", items=items)


@app.route("/item/<uuid>")
def item_detail(uuid):
    response = requests.get("https://valorant-api.com/v1/weapons/skins")
    data = response.json()
    skins = data.get('data', [])

    item = next((skin for skin in skins if skin.get('uuid') == uuid), None)

    if not item:
        return "Skin not found", 404

    return render_template("skinbundles.html", item=item)


if __name__ == '__main__':
    app.run(debug=True)
