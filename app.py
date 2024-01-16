from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from urllib.parse import quote
from send_mail import send_mail

app = Flask(__name__)

ENV = 'dev'

if ENV == 'dev':
    app.debug = True
    password = "Neha@123"
    # URL-encode the password
    encoded_password = quote(password, safe='')
    app.config['SQLALCHEMY_DATABASE_URI'] = f"postgresql://postgres:{encoded_password}@localhost/netflix"
else:
    app.debug = False
    app.config['SQLALCHEMY_DATABASE_URI'] = ''

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Feedback(db.Model):
    __tablename__ = 'feedback'
    id = db.Column(db.Integer, primary_key=True)
    user = db.Column(db.String(200))
    movie = db.Column(db.String(200))
    genres = db.Column(db.String)
    rating = db.Column(db.Integer)
    comments = db.Column(db.Text())

    def __init__(self, user, movie, genres, rating, comments):
        self.user = user
        self.movie = movie
        self.rating = rating
        self.genres = genres
        self.comments = comments

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        user = request.form['user']
        movie = request.form['movie']
        genres = request.form['genres']
        rating = request.form['rating']
        comments = request.form['comments'].strip()

        data = Feedback(user, movie, genres, rating, comments)
        db.session.add(data)
        db.session.commit()

        send_mail(user, movie,genres,rating, comments)

        return render_template('success.html')

if __name__ == '__main__':
    app.run()