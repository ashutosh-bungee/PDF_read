from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  

@app.route("/api/data", methods=["GET"])
def get_text():
    print("Fetching data...")
    try:
        with open("data/output.txt", "r", encoding="utf-8") as file:
            content = file.read()
        return jsonify({"data": content})
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
@app.route("/api/test", methods=["GET"])
def test():
    return jsonify({"message": "API is working"})

if __name__ == "__main__":
    app.run(debug=True, port=5000)
