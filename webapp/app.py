from flask import Flask
app=Flask(__name__)
@app.route("/")
def index():
    return "hello"
@app.route("/home")
def home():
    return "welcome"
@app.route("/hai")
def hoome():
    return"welcome to "
if (__name__=="__main__"):
    app.run(debug=True)