import sqlite3
from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length

db = sqlite3.connect("user-data.db")
cursor = db.cursor()
# cursor.execute("CREATE TABLE users (id INTEGER PRIMARY KEY, name varchar(50) NOT NULL, age INTEGER" "NOT NULL,
# DOB DATE, sex varchar(20) NOT NULL, address varchar(250) NOT NULL, postal INTEGER NOT NULL, " "state varchar(50)
# NOT NULL, city varchar(50) NOT NULL, contact BIGINT NOT NULL )")
class MyForm(FlaskForm):
    email = StringField(label='Email', validators=[DataRequired(), Email()],render_kw={"placeholder": "Email / Username"})
    password = PasswordField(label='Password', validators=[DataRequired(), Length(min=8)],render_kw={"placeholder": "Password"})
    submit = SubmitField(label='Log In')


app = Flask(__name__)
app.secret_key = "Thisisasecret"

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/userLogin", methods=["GET","POST"])
def user_login():
    form = MyForm()
    if request.method == "POST" and form.validate_on_submit():
        if form.email.data == "admin@uts.com" and form.password.data == "12345678":
            return render_template("addInfo.html")
        else:
            return render_template("userlogin.html",form=form)
    else:
        return render_template("userlogin.html", form=form)


@app.route("/volunteerLogin")
def vol_login():
    return render_template("vollogin.html")


@app.route("/driverLogin")
def driver_login():
    return render_template("driverLogin.html")


@app.route("/userSignup")
def user_signup():
    return render_template("userSignup.html")


@app.route("/volunteerSignup")
def volunteer_signup():
    return render_template("driverSignup.html")


@app.route("/driverSignup")
def driver_signup():
    return render_template("volSignup.html")


@app.route("/Account")
def account():
    return render_template("account.html")


if __name__ == "__main__":
    app.run(debug=True)
