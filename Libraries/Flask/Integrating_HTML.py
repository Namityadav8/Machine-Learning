from flask import Flask ,render_template , request

app=Flask(__name__)

@app.route("/")
def welcome():
    return render_template("index.html")

@app.route("/Index")
def index():
    return "<html><h1> Welcome to the index Page</h1></html>"   #One way to do the web thing but not good way


if __name__ == "__main__":
    app.run(debug=True)