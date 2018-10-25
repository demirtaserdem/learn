from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
def index():
    article = dict()
    article["title"] = "deneme"
    article["body"] = "Deneme123"
    article["autor"] = "erdem demirtaş"
    

    return render_template("index.html",article = article)

if __name__ == "__main__":
    app.run(debug = True)