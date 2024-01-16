from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configure the PostgreSQL database connection
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:${{ secrets.DB_PASSWORD }}@chores.cna20s0e8osw.il-central-1.rds.amazonaws.com:5432/your_database'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Define a Chore model for the 'chores' table
class Chore(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    chore = db.Column(db.String(100), nullable=False)
    frequency = db.Column(db.String(50), nullable=False)
    options = db.Column(db.String(200))
    last_performed = db.Column(db.String(50))

# Landing page
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add-chore')
def addChore():
    return render_template('add-chore.html')

if __name__ == '__main__':
    app.run(debug=True)
