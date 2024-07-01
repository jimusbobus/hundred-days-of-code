from flask import Flask, render_template
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, ValidationError, SelectField
from wtforms.validators import DataRequired, URL, InputRequired, AnyOf
import csv
import re

'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''
coffee_ratings = ['☕', '☕☕', '☕☕☕', '☕☕☕☕', '☕☕☕☕☕']
wifi_ratings = ['✘', '💪', '💪💪', '💪💪💪', '💪💪💪💪', '💪💪💪💪💪']
power_ratings = ['✘', '🔌', '🔌🔌', '🔌🔌🔌', '🔌🔌🔌🔌', '🔌🔌🔌🔌🔌']


class TimeValidator:
    def __call__(self, form, field):
        # Regular expression to match the time format "HH:MM AM/PM"
        time_pattern = re.compile(r'^(1[0-2]|0?[1-9]):([0-5]?[0-9])\s?(AM|PM)$', re.IGNORECASE)
        if not time_pattern.match(field.data):
            raise ValidationError('Time must be in the format "HH:MM AM/PM".')


app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)


class CafeForm(FlaskForm):
    cafe = StringField('Cafe name', validators=[DataRequired()])
    location = StringField('Cafe Location On Google Maps (URL)', validators=[URL()])
    opening = StringField('Opening Time e.g. 7:00 AM', validators=[InputRequired(), TimeValidator()])
    closing = StringField('Closing Time e.g. 7:00 PM', validators=[InputRequired(), TimeValidator()])
    coffee = SelectField('Coffee Rating', choices=[(x, x) for x in coffee_ratings],
                         validators=[AnyOf(coffee_ratings)])
    wifi = SelectField('Wifi Strength Rating', choices=[(x, x) for x in wifi_ratings],
                       validators=[AnyOf(wifi_ratings)])
    power = SelectField('Power Socket Availability Rating', choices=[(x, x) for x in power_ratings],
                        validators=[AnyOf(power_ratings)])
    submit = SubmitField('Submit')


# Exercise:
# add: Location URL, open time, closing time, coffee rating, wifi rating, power outlet rating fields
# make coffee/wifi/power a select element with choice of 0 to 5.
# e.g. You could use emojis ☕️/💪/✘/🔌
# make all fields required except submit
# use a validator to check that the URL field has a URL entered.
# ---------------------------------------------------------------------------


# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods=["GET", "POST"])
def add_cafe():
    form = CafeForm()
    print("Try Add")
    if form.validate_on_submit():
        print("All Validated")
        with open('cafe-data.csv', 'a', newline='', encoding='utf-8') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow([
                form.cafe.data,
                form.location.data,
                form.opening.data,
                form.closing.data,
                form.coffee.data,
                form.wifi.data,
                form.power.data
            ])
    else:
        print(form.errors)
    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    with open('cafe-data.csv', newline='', encoding='utf-8') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
    return render_template('cafes.html', cafes=list_of_rows)


if __name__ == '__main__':
    app.run(debug=True)
