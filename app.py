from flask import Flask, render_template
import requests

app = Flask(__name__)

API_KEY = "f37fdd1cfb0c461877e66a006a6d717f"
NEWS_URL = f"https://gnews.io/api/v4/top-headlines?token={API_KEY}&lang=en&country=us"

@app.route('/')
def home():
    response = requests.get(NEWS_URL)
    if response.status_code == 200:
        news_data = response.json().get("articles", [])
    else:
        news_data = []

    return render_template("index.html", news=news_data)

if __name__ == "__main__":
    app.run(debug=True)
