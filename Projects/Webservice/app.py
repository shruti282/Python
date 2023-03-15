from flask import Flask
from homepage import homepage

# flask web framework for python

# Initialize the application
app = Flask(__name__)

# # Setting route
# @app.route("/")
# def home():
#     return "This is the homepage."

app.register_blueprint(homepage, url_prefix="/home")

# run flask website
# debug reloads the changes
if __name__ == '__main__':
    app.run(debug=True, port=8000)


