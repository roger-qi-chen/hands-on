# Import the necessary modules
from flask import Flask

# Define the Flask app
app = Flask(__name__)

# Define the view
@app.route('/')
def home():
    return "Welcome to Roger's first container app."

# Run the app on port 80, with debug
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)

