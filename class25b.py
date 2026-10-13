from flask import Flask , request


app = Flask(__name__)

@app.route("/book")
def place_order():
    return "francis has placed your order"


if __name__ == "__main__":
    app.run(debug = True , port = 5000)

