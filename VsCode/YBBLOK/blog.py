
from flask import Flask,render_template,redirect,url_for,session,logging,request,flash
from flask_mysqldb import MySQL
from wtforms import Form,StringField,TextAreaField,PasswordField,validators
from passlib.hash import sha256_crypt
import email_validator
from functools import wraps


app = Flask(__name__) 
app.secret_key = "cankurt"

app.config["MYSQL_HOST"]="localhost"
app.config["MYSQL_USER"]="root"
app.config["MYSQL_PASSWORD"]=""
app.config["MYSQL_DB"]="cankurt"
app.config["MYSQL_CURSORCLASS"]="DictCursor"

mysql = MySQL(app)


#Kullanıcı Giriş Decorator
from functools import wraps
from flask import g, request, redirect, url_for

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
            if "logged_in" in session :
                return f(*args, **kwargs)
            else:
                flash("Bu sayfayı görüntülemek için lütfen giriş yapınız.","danger")
                return redirect(url_for("login"))
    return decorated_function


#Kullanıcı Kayıt Formu
class RegisterForm(Form):
    name = StringField("Ad soyad:",validators=[validators.length(min=4,max=24,message="4-24 karakter aralığında olmalıdır."),])
    username = StringField("Kullanıcı adı:",validators=[validators.length(min=5,max=24,message="4-24 karakter aralığında olmalıdır.")])
    email = StringField("Email adresi:",validators=[validators.Email(message="Lütfen geçerli bir email adresi giriniz.")])
    password=PasswordField("Parola:",validators=[
        validators.data_required(message="Lütfen bir parola belirleyiniz."),
        validators.EqualTo(fieldname="confirm",message="Parolanız uyuşmuyor lütfen kontrol ediniz.")
    ])
    confirm=PasswordField("Parola doğrula:")

#Login Formu
class LoginForm(Form):
    username=StringField("Kullanıcı Adı:") 
    password=PasswordField("Parola:")

#Makale Formu
class ArticleForm(Form):
    tittle = StringField("Makale Başlığı:",validators=[validators.Length(min=4,max=100,message="Makale başlığı 4-100 karakterler arası olmalıdır.")])
    content = TextAreaField("Makale İçeriği:",validators=[validators.Length(min=10,message="Makale uzunluğu minimum 10 karakter uzunluğunda olmalıdır.")])




@app.route("/")
def index():   
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html") 

#Kayıt Olma 
@app.route("/register",methods=["GET","POST"])
def register():
    form = RegisterForm(request.form)
    if request.method=="POST" and form.validate():
        
        name=form.name.data
        username=form.username.data
        email=form.email.data 
        password=sha256_crypt.encrypt(form.password.data) 

        cursor = mysql.connection.cursor()
        sorgu="INSERT INTO users(name,email,username,password) VALUES(%s,%s,%s,%s)"
        cursor.execute(sorgu,(name,email,username,password)) 
        mysql.connection.commit() 
        cursor.close()
        flash("Başarıyla kayıt olunuz...","success")
        return redirect(url_for("login"))
    else:    
        return render_template("register.html",form=form)


#Login işlemi
@app.route("/login",methods=["GET","POST"])
def login():
    form=LoginForm(request.form)
    if request.method=="POST":
        username = form.username.data
        password_entered=form.username.data
        cursor = mysql.connection.cursor()
        sorgu="SELECT * FROM users WHERE username=%s"
        result = cursor.execute(sorgu,(username,))
        if result>0:
            data = cursor.fetchone()
            real_password=data["password"]
            if sha256_crypt.verify(password_entered,real_password):
                flash("Başarıyla giriş yaptınız","success")
                session["logged_in"]=True
                session["username"]=username
                return redirect(url_for("index"))
            else:
                flash("Parolanızı kontrol ediniz.","danger")
                return redirect(url_for("login"))
        else:
            flash("Böyle bir kullanıcı bulunmuyor.","danger")
            return redirect(url_for("login"))

    return render_template("login.html",form=form) 

#Logout İşlemi
@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("index"))

#Dashboard
@app.route("/dashboard")
@login_required
def dashboard():
    cursor=mysql.connection.cursor()
    sorgu="SELECT* FROM article WHERE author=%s"
    result=cursor.execute(sorgu,(session["username"],)) 

    if result>0:
        articles = cursor.fetchall()
        return render_template("dashboard.html",articles=articles)
    else:
        return render_template("dashboard.html")


#Makale Ekleme
@app.route("/addarticle",methods=["GET","POST"])
def addarticle():  
    form = ArticleForm(request.form)
    if request.method=="POST" and form.validate():
        tittle = form.tittle.data
        content=form.content.data

        cursor = mysql.connection.cursor()
        sorgu = ("INSERT INTO article(tittle,author,content) VALUES(%s,%s,%s)")
        cursor.execute(sorgu,(tittle,session["username"],content))
        mysql.connection.commit()
        cursor.close()
        flash("Makale Başarıyla Eklendi.","success")
        return redirect(url_for("dashboard"))
    else:
        return render_template("addarticle.html",form = form)

#Makale listeleme
@app.route("/articles")
def articles():
    cursor=mysql.connection.cursor()
    sorgu="SELECT * FROM article"
    result = cursor.execute(sorgu)
    if result > 0:
        articles=cursor.fetchall()
        return render_template("articles.html",articles=articles)
    else:
        return render_template("articles.html")

#Detay sayfası
@app.route("/article/<string:id>")
def article(id):
    cursor=mysql.connection.cursor()
    sorgu="SELECT * FROM article WHERE id=%s"
    result=cursor.execute(sorgu,(id,))

    if result>0:
        article = cursor.fetchone()
        return render_template("article.html",article = article)
    else:    
        return render_template("article.html")

#Makale silme
@app.route("/delete/<string:id>")
@login_required
def delete(id):
    cursor = mysql.connection.cursor()
    sorgu="SELECT * FROM article WHERE author=%s and id=%s"
    result = cursor.execute(sorgu,(session["username"],id))
    if result>0:
        delete_sorgu="DELETE FROM article where id=%s"
        cursor.execute(delete_sorgu,(id,))
        mysql.connection.commit()
        flash("Makale silindi.","warning")
        return redirect(url_for("dashboard"))
    else:
        flash("Böyle bir makale yok veya yetkiniz yok.","danger")
        return redirect(url_for("index"))


#Makale güncelle
@app.route("/edit/<string:id>",methods=["GET","POST"])
@login_required
def update(id):
    if request.method=="GET":
        cursor = mysql.connection.cursor()
        sorgu="SELECT* FROM article where id=%s and author=%s"
        result = cursor.execute(sorgu,(id,session["username"]))
        if result==0:
            flash("Böyle bir makale yok veya yetkiniz yok","danger")
            return redirect(url_for("index"))
        else:
            article = cursor.fetchone()
            form=ArticleForm()
            form.tittle.data=article["tittle"]
            form.content.data=article["content"]
            return render_template("update.html",form=form)
    else: 
        #POST REQUEST
        form = ArticleForm(request.form)
        newTitle=form.tittle.data
        newContent=form.content.data
        update_sorgu="UPDATE article SET tittle=%s,content=%s WHERE id=%s"
        cursor = mysql.connection.cursor()
        cursor.execute(update_sorgu,(newTitle,newContent,id))
        mysql.connection.commit()
        flash("Makale güncellendi.","success")
        return redirect(url_for("dashboard"))

#Arama URL 
@app.route("/search",methods=["GET","POST"])
def search():
    if request.method=="GET":
        return redirect(url_for("index"))
    else:
        keyword=request.form.get("keyword")
        cursor = mysql.connection.cursor()
        sorgu = "SELECT * FROM article WHERE tittle like '%" +keyword+ "%'"
        result = cursor.execute(sorgu)
        if result==0:
            flash("Aranan kelimeye uygun makale bulunamadı.","warning")
            return redirect(url_for("articles"))
        else:
            articles = cursor.fetchall() 
            return render_template("articles.html",articles=articles)


if __name__ =="__main__":
    app.run(debug=True) 