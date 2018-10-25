from flask import Flask,render_template,flash,redirect,url_for,session,logging,request
from flask_mysqldb import MySQL
from wtforms import Form,StringField,TextAreaField,PasswordField,validators
from passlib.hash import sha256_crypt

#Kullanıcı kayıt Formu
class RegisterForm(Form):
    name = StringField("İsim Soyisim",validators = [validators.Length(min = 4,max = 25)])
    username = StringField("Kullanıcı Adı",validators = [validators.Length(min = 5,max = 35)])
    email = StringField("İsim Soyisim",validators = [validators.Email(message = "Lütfen Geçerli Bir Mail Adresi Giriniz...")])
    password = PasswordField("Parola: ",validators=[
        validators.data_required(message="Lütfen bir parola belirleyin"),
        validators.EqualTo(fieldname = "confirm",message="Parolanız uyuşmuyor...")
    ])
    confirm = PasswordField("Parolayı Doğrula...")

app = Flask(__name__)
app.config["MYSQL_HOST"] = "localhost"
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = ""
app.config["MYSQL_DB"] = "edblog"
app.config["MYSQL_CURSORCLASS"] = "DictCursor"

mysql = MySQL(app)


@app.route("/")
def index():
    articles = [
        {"id":1,"title":"Deneme1","content":"Deneme1 içerik"},
        {"id":2,"title":"Deneme2","content":"Deneme2 içerik"},
        {"id":3,"title":"Deneme3","content":"Deneme3 içerik"}
    ]
    return render_template("index.html", articles = articles)


@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/article/<string:id>")
def detail(id):
    return "Atrical id:" + id

if __name__ == "__main__":
    app.run(debug = True)