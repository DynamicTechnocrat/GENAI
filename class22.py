from flask import Flask, request


app = Flask(__name__)


@app.route("/greeting" , methods=["POST"])
def greet():
    x =  request.json.get("name", "name not found")
    return f"Hello, {x}!"

if __name__ == "__main__":
    app.run()