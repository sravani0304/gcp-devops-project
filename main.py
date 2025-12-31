from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "Hello This app is deployed using github + GCP Cloud Build + Docker!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)