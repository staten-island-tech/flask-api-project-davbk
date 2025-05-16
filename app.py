from flask import Flask, jsonify, render_template
import requests
import os

app = Flask(__name__)

@app.route("/")
def show_games():
    response = requests.get("https://www.freetogame.com/api/games?category=shooter")
    
    if response.status_code != 200:
        return "Failed to fetch games", 500

    games = response.json()
    return render_template("index.html", games=games)

@app.route("/api/games", methods=["GET"])
def get_games():
    response = requests.get("https://www.freetogame.com/api/games?category=shooter")
    
    if response.status_code != 200:
        return jsonify({"error": "Failed to fetch data"}), 500

    return jsonify(response.json())

if __name__ == "__main__":
    app.run(debug=True)
