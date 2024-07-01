from flask_bootstrap import Bootstrap5
from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email


class MyForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('LogIn')


app = Flask(__name__)
app.secret_key = "not_a_secret"
bootstrap = Bootstrap5(app)


@app.route("/", methods=["GET", "POST"])
def home():
    return render_template('index.html', bootstrap=bootstrap)


@app.route("/login", methods=["GET", "POST"])
def login():
    form = MyForm()
    if form.validate_on_submit():
        print("Validate on submit is true")
        if (form.email.data == "admin@email.com") & (form.password.data == "12345678"):
            print(f"Email: {form.email.data}")
            return render_template('success.html')
        else:
            return render_template('denied.html')

    print("Validate on submit is false")
    return render_template('login.html', form=form, bootstrap=bootstrap)


if __name__ == '__main__':
    app.run(debug=True)
