import sqlite3
from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length


class MyForm(FlaskForm):
    email = StringField(label='Email', validators=[DataRequired(), Email()],
                        render_kw={"placeholder": "Email / Username"})
    password = PasswordField(label='Password', validators=[DataRequired(), Length(min=8)],
                             render_kw={"placeholder": "Password"})
    submit = SubmitField(label='Log In')


app = Flask(__name__)
app.secret_key = "Thisisasecret"

DATABASE = 'UTS.db'
@app.route("/")
def index():
    return render_template("index.html")


@app.route("/userLogin", methods=["GET", "POST"])
def user_login():
    form = MyForm()
    if request.method == "POST" and form.validate_on_submit():
        if form.email.data == "admin@uts.com" and form.password.data == "12345678":
            return render_template("account.html")
        else:
            return render_template("userlogin.html", form=form)
    else:
        return render_template("userlogin.html", form=form)


@app.route("/volunteerLogin")
def vol_login():
    return render_template("vollogin.html")


@app.route("/driverLogin")
def driver_login():
    return render_template("driverLogin.html")


@app.route("/userSignup", methods=["GET", "POST"])
def user_signup():
    if request.method == 'POST':
        # Get form data
        first_name = request.form.get('firstName')
        last_name = request.form.get('lastName')
        email = request.form.get('email')
        password = request.form.get('password')

        # Update the SQLite database
        try:
            conn = sqlite3.connect(DATABASE)
            cursor = conn.cursor()

            # Assuming you have a 'users' table in your database
            cursor.execute('''
        INSERT INTO users (first_name, last_name, email, password)
        VALUES (?, ?, ?, ?);
    ''', (first_name, last_name, email, password))

            conn.commit()
            cursor.close()
            conn.close()

            print("new user signup")
            return render_template("account.html")

        except Exception as e:
            print("Database failed")
            return f'Error updating information: {str(e)}'

    return render_template("userSignup.html")


@app.route("/volunteerSignup")
def volunteer_signup():
    return render_template("volSignup.html")


@app.route("/driverSignup")
def driver_signup():
    return render_template("driverSignup.html")


@app.route("/account")
def account():
    return render_template("account.html")


if __name__ == "__main__":
    app.run(debug=True)
