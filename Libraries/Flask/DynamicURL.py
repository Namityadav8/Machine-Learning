from flask import Flask,render_template,request

app=Flask(__name__)

# @app.route("/URL/<variable>")
# def URL(variable):
#     return "hi the number is " + variable

@app.route("/form/<result>")
def ans(result):
    res=""
    if int(result)>50:
        res="Passed"
    else:
        res="Failed"
    return render_template("var.html",result=res)
        #Here this result is being given value as we have passed this result onto the html file that is why we have done like that 




if __name__=="__main__":
    app.run(debug=True)