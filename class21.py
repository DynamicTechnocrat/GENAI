### libaries 
### api >>> 
### fastapi , flask , starlette

### flask sychronous web framework
### fastapi asynchronous web framework
### starlette asynchronous web framework

### pip install Flask

### create an instance ## gunincorn , waitress
from flask import Flask 

app = Flask(__name__)

@app.route("/greeting" , methods=["GET"])
def greet():
    x =  "bello"
    return f"Hello, {x}!"

if __name__ == "__main__":
    app.run()





