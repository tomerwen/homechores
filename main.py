from flask import Flask, render_template

app = Flask(__name__)

# Landing page
@app.route('/')
def index():
    return render_template('index.html')

# Route to display user-specific information
@app.route('/<username>')
def user_info(username):
    # In a real app, you would fetch data from the database based on the username
    # For demonstration, let's assume there is a dictionary with some user data
    user_data = {
        'jaanuk': {'name': 'Jaanuk', 'tasks': ['Task A', 'Task B']},
        'peach': {'name': 'Peach', 'tasks': ['Task C', 'Task D']}
    }

    # Check if the username exists in the user_data dictionary
    if username in user_data:
        return render_template('user_info.html', user=user_data[username])
    else:
        return "User not found"

if __name__ == '__main__':
    app.run(debug=True)
