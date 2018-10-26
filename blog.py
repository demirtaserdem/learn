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

class LoginForm(Form):
    username = StringField("Kullanıcı Adı: ")
    password = PasswordField("Parola")


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

        
        flash("Başarıyla kayıt oldunuz...","success")
        return redirect(url_for("login"))
    else:
        return render_template("register.html",form = form)

#login İşlemi
@app.route("/login",methods = ["GET","POST"])
def login():
    form = LoginForm(request.form)

    if request.method == "POST":
        username = form.username.data
        password_entired = form.password.data
        cursor = mysql.connection.cursor()
        sorgu = "select * from users where username = %s"

        result = cursor.execute(sorgu,(username,))

        if result > 0 :
            data = cursor.fetchone()
            real_password = data["password"]
            if sha256_crypt.verify(password_entired,real_password):
                flash("Başarıyla Giriş Yaptınız","success")

                session["logged_in"] = True
                session["username"] = username
                return redirect(url_for("index"))
            else:
                flash("Parolanızı Yanlış Girdiniz....","danger")
                return redirect(url_for("login"))


        else:
            flash("böyle bir kullanıcı bulunmuyor","danger")
            return redirect(url_for("login"))



    return render_template("login.html",form = form)

#Logout işlemi
@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug = True)