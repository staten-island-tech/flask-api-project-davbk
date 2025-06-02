from flask import Flask, jsonify, render_template
import requests

app = Flask(__name__)

@app.route("/")
def show_games():
    response = requests.get("https://www.freetogame.com/api/games?category=shooter")
    
    if response.status_code != 200:
        return "Failed to fetch games", 500

    games = response.json()
    return render_template("index.html", games=games)

@app.route("/games/<int:game_id>")
def game_details(game_id):
    response = requests.get(f"https://www.freetogame.com/api/game?id={game_id}")

    if response.status_code != 200:
        return "Failed to fetch game details", 500

    game = response.json()
    return render_template("items.html", game=game)

if __name__ == "__main__":
    app.run(debug=True)