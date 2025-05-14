from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route("/")
def home():
    return (
        "<h1>Welcome to the FreeToGame API</h1>"
        "<p>Use <a href='/api/games'>/api/games</a> to get a list of shooter games.</p>"
        "<p>Use <code>/api/games/&lt;game_id&gt;</code> to get a specific game by its ID.</p>"
    )

@app.route("/api/games", methods=["GET"])
def get_games():
    response = requests.get("https://www.freetogame.com/api/games?category=shooter")
    
    if response.status_code != 200:
        return jsonify({"error": "Failed to fetch data"}), 500

    data = response.json()
    games = []

    for game in data:
        games.append({
            "id": game.get("id"),
            "title": game.get("title"),
            "thumbnail": game.get("thumbnail"),
            "short_description": game.get("short_description"),
            "game_url": game.get("game_url"),
            "genre": game.get("genre"),
            "platform": game.get("platform"),
            "publisher": game.get("publisher"),
            "developer": game.get("developer"),
            "release_date": game.get("release_date"),
            "freetogame_profile_url": game.get("freetogame_profile_url")
        })

    return jsonify(games)

@app.route("/api/games/<int:game_id>", methods=["GET"])
def get_game_by_id(game_id):
    response = requests.get("https://www.freetogame.com/api/games?category=shooter")

    if response.status_code != 200:
        return jsonify({"error": "Failed to fetch data"}), 500

    data = response.json()
    game = next((g for g in data if g.get("id") == game_id), None)

    if not game:
        return jsonify({"error": "Game not found"}), 404

    return jsonify(game)

if __name__ == "__main__":
    app.run(debug=True)