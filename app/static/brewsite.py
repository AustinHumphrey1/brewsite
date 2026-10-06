from flask import Flask

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return "<p>Hello, ICT 362 World!</p>"

@app.route("/breweries")
def breweries():
    return "<p>Welcome to Breweries!</p>"

@app.route("/beer")
def beer_():
    return "<p>Welcome to Beer Types!</p>"

@app.route("/about")
def hello_world():
    return "<p>Welcome to about us</p>"


if __name__ == "__main__":
    app.run(debug=True)
