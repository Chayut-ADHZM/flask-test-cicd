from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    print("Test the Workflow")
    return "<p>Hello, World! Test Commit</p>"