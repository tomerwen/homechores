from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

# Configure the PostgreSQL database connection
db_password = os.environ.get('DB_PASSWORD')

app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://postgres:{db_password}@chores.cna20s0e8osw.il-central-1.rds.amazonaws.com:5432/postgres'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Define a Chore model for the 'chores' table
class Chores(db.Model):
    chores = db.Column(db.String(50), primary_key=True, nullable=False)
    options = db.Column(db.String(30), nullable=False)
    frequency = db.Column(db.String(30), nullable=False)
    last = db.Column(db.Date)

# Landing page
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        user_name = request.form.get('user')
        return redirect(url_for('user_info', user_name=user_name))
    return render_template('index.html', user='')

@app.route('/add-chore', methods=['GET', 'POST'])
def add_chore():
    if request.method == 'POST':
        chore_name = request.form.get('choreName')
        assignee = request.form.get('assignee')
        frequency = request.form.get('frequency')
        last_performed = request.form.get('dueDate')

        # Check if the chore already exists
        existing_chore = Chores.query.filter_by(chores=chore_name, options=assignee).first()

        if existing_chore:
            return "Chore already exists!"
        else:
            # Add a new row to the 'chores' table
            new_chore = Chores(chores=chore_name, options=assignee, frequency=frequency, last=last_performed)
            db.session.add(new_chore)
            db.session.commit()
            return "Chore added successfully!"

    return render_template('add-chore.html')

@app.route('/<user_name>')
def user_info(user_name):
    all_chores = Chores.query.all()
    return render_template('user_info.html', user=user_name, chores=all_chores)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000 , debug=True)
