from flask import Flask

app=Flask(__name__)

@app.route("/")
def welcome():
    return "welcome"
@app.route("/index")
def index():
    return "Index!"

if __name__ == "__main__":
    app.run(debug=True)