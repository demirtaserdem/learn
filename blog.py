from flask import Flask,render_template,flash,redirect,url_for,session,logging,request
from flask_mysqldb import MySQL
from wtforms import Form,StringField,TextAreaField,PasswordField,validators
from passlib.hash import sha256_crypt

#Kullanıcı kayıt Formu
class RegisterForm(Form):
    name = StringField("İsim Soyisim",validators = [validators.Length(min = 4,max = 25,message = "Alan 4 ve 25 aralığında olmalıdır")])
    username = StringField("Kullanıcı Adı",validators = [validators.Length(min = 5,max = 35,message = "Alan 5 ve 35 aralığında olmalıdır")])
    email = StringField("Email: ",validators = [validators.Email(message = "Lütfen Geçerli Bir Mail Adresi Giriniz...")])
    password = PasswordField("Parola: ",validators = [
        validators.DataRequired(message = "Lütfen bir parola belirleyin"),
        validators.EqualTo(fieldname = "confirm",message = "Parolanız uyuşmuyor...")
    ])
    confirm = PasswordField("Parolayı Doğrula...")


app = Flask(__name__)
app.secret_key = "edblog"
app.config["MYSQL_HOST"] = "localhost"
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = ""
app.config["MYSQL_DB"] = "edblog"
app.config["MYSQL_CURSORCLASS"] = "DictCursor"

mysql = MySQL(app)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/article/<string:id>")
def detail(id):
    return "Atrical id:" + id

#Kayıt olma
@app.route("/register",methods =["GET","POST"])
def register():
    form = RegisterForm(request.form)
    
    if request.method == "POST" and form.validate():
        name = form.name.data
        username = form.username.data
        email = form.email.data
        password = sha256_crypt.encrypt(form.password.data)

        cursor = mysql.connection.cursor()
        sorgu = "insert into users(name,email,username,password) values(%s,%s,%s,%s)"
        cursor.execute(sorgu,(name,email,username,password))
        mysql.connection.commit()
        cursor.close()

        

        return redirect(url_for("index"))
        flash("Başarıyla kayıt oldunuz...","success")
    else:
        return render_template("register.html",form = form)

if __name__ == "__main__":
    app.run(debug = True)