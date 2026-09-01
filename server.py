# mkdir lab
#  cd lab
# nano server.py

# Import the Flask class from the flask module
from flask import Flask

# Create an instance of the Flask class, passing in the name of the current module
app = Flask(__name__)

# Define a route for the root URL ("/")
@app.route("/")
def index():
    # Function that handles requests to the root URL
    # Return a plain text response
    return "hello world"

# flask --app server --debug run
# curl -X GET -i -w '\n' localhost:5000


## Ohers
'''
git clone / config / add / pull
 …or create a new repository on the command line
echo "# FlaskApp" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/mihamaxx/FlaskApp.git
git push -u origin main
…or push an existing repository from the command line
git remote add origin https://github.com/mihamaxx/FlaskApp.git
git branch -M main
git push -u origin main
'''
