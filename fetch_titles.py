from flask import Flask, request, jsonify
from flask_cors import CORS  # Import CORS

app = Flask(__name__)  # Define the Flask app instance
CORS(app)  # Apply CORS after the app instance is created

import requests
from bs4 import BeautifulSoup

@app.route('/fetch-titles', methods=['POST'])
def fetch_titles():
    data = request.json
    urls = data.get("urls", [])
    results = {}

    for url in urls:
        try:
            # Fetch the webpage content
            response = requests.get(url)
            response.raise_for_status()

            # Parse the HTML to extract the title
            soup = BeautifulSoup(response.text, "html.parser")
            title = soup.title.string if soup.title else "Title not found"
            results[url] = title
        except requests.RequestException as e:
            results[url] = f"Error: {str(e)}"

    return jsonify(results)

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)
