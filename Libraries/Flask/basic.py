from flask import Flask

app=Flask(__name__)


@app.route("/KK")
def home():
    return "Welcome to the home page . Now we have used debug function "

if __name__ == "__main__":
    app.run(debug=True)