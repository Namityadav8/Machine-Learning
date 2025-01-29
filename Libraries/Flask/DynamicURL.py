from flask import Flask,render_template,request,redirect,url_for

app=Flask(__name__)

# @app.route("/URL/<variable>")
# def URL(variable):
#     return "hi the number is " + variable

@app.route("/form/<result>")
def form1(result):
    res=""
    if int(result)>50:
        res="Passed"
    else:
        res="Failed"
    return render_template("forms.html",result=res)
        #Here this result is being given value as we have passed this result onto the html file that is why we have done like that 

@app.route("/namit",methods=["POST","GET"])
def url():
    y=0
    if request.method=="POST":
        y=int(request.form['name'])

    return redirect(url_for("form1",result=y))
   


if __name__=="__main__":
    app.run(debug=True) 