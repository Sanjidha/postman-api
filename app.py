from flask import Flask, jsonify
import requests
app = Flask(__name__)
# Replace with your Postman API endpoint
POSTMAN_API_URL = "https://api.postman.com/collections/<your_collection_id>"
API_KEY = "<your_postman_api_key>"  # Replace with your key
@app.route("/myapi", methods=["GET"])
def my_api():
   headers = {"X-Api-Key": API_KEY}
   response = requests.get(POSTMAN_API_URL, headers=headers)
   return jsonify(response.json())
if __name__ == "__main__":
   app.run(host="0.0.0.0", port=5000)
