from flask import Flask , render_template , request

app=Flask(__name__)


@app.route('/form',methods=['GET','POST'])
def home():
    if request.method=='POST':
        name = request.form['name']
        return f"Hello {name}"
        pass
    return render_template('index.html')    

if __name__ == "__main__":
    app.run(debug=True)