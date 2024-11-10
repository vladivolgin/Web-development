from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, DateField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = '111'  
db = SQLAlchemy(app)

# Route for the homepage
@app.route('/')
def home():
    return render_template('home.html')

# Route for the about page
@app.route('/about')
def about():
    return render_template('about.html')

# Dynamic route for user profiles
@app.route('/user/<username>')
def user(username):
    return render_template('user.html', username=username)

class Booking(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(100), nullable=False)
    hotel_name = db.Column(db.String(100), nullable=False)
    check_in = db.Column(db.Date, nullable=False)
    check_out = db.Column(db.Date, nullable=False)

    def __repr__(self):
        return f'<Booking {self.hotel_name} by {self.user_name}>'

class BookingForm(FlaskForm):
    user_name = StringField('User Name', validators=[DataRequired()])
    hotel_name = StringField('Hotel Name', validators=[DataRequired()])
    check_in = DateField('Check-in Date', format='%Y-%m-%d', validators=[DataRequired()])
    check_out = DateField('Check-out Date', format='%Y-%m-%d', validators=[DataRequired()])
    submit = SubmitField('Submit')


@app.before_request
def create_tables():
    db.create_all()


@app.route('/bookings')
def booking_list():
    bookings = Booking.query.all()
    return render_template('booking_list.html', bookings=bookings)


@app.route('/bookings/create', methods=['GET', 'POST'])
def booking_create():
    form = BookingForm()
    if form.validate_on_submit():
        new_booking = Booking(
            user_name=form.user_name.data,
            hotel_name=form.hotel_name.data,
            check_in=form.check_in.data,
            check_out=form.check_out.data
        )
        db.session.add(new_booking)
        db.session.commit()
        return redirect(url_for('booking_list'))
    return render_template('booking_form.html', form=form)


@app.route('/bookings/<int:id>/edit', methods=['GET', 'POST'])
def booking_update(id):
    booking = Booking.query.get_or_404(id)
    form = BookingForm(obj=booking)
    if form.validate_on_submit():
        booking.user_name = form.user_name.data
        booking.hotel_name = form.hotel_name.data
        booking.check_in = form.check_in.data
        booking.check_out = form.check_out.data
        db.session.commit()
        return redirect(url_for('booking_list'))
    return render_template('booking_form.html', form=form, booking=booking)


@app.route('/bookings/<int:id>/delete', methods=['GET', 'POST'])
def booking_delete(id):
    booking = Booking.query.get_or_404(id)
    if request.method == 'POST':
        db.session.delete(booking)
        db.session.commit()
        return redirect(url_for('booking_list'))
    return render_template('booking_confirm_delete.html', booking=booking)

if __name__ == '__main__':
    app.run(debug=True)
