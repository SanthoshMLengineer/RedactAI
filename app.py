import sys
import os

# Make sure the src package is importable
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "src"))

from flask import Flask, render_template, request, jsonify
from src.get_prediction_model import get_prediction

app = Flask(__name__)


@app.route("/")
def index():
    """Serve the main prediction UI."""
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():
    """
    Accepts JSON: { "text": "<user input>" }
    Returns  JSON: { "result": "<model output>" }
    """
    data = request.get_json(force=True, silent=True)

    if not data or "text" not in data:
        return jsonify({"error": "Missing 'text' field in request body."}), 400

    text = data["text"].strip()
    if not text:
        return jsonify({"error": "Text cannot be empty."}), 400

    try:
        result = get_prediction(text=text)
        return jsonify({"result": result})
    except Exception as exc:
        return jsonify({"error": str(exc)}), 500


if __name__ == "__main__":
    # debug=False for production; set debug=True for local development
    app.run(host="0.0.0.0", port=5000, debug=True)
