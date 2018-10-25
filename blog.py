from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Anasayfa"

@app.route("/about")
def about():
    return "Hakkında"

@app.route("/about/erdem")
def erdem():
    return "Erdem Hakkında"

if __name__ == "__main__":
    app.run(debug = True)