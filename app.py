from flask import Flask, render_template,request,redirect,url_for
app = Flask(__name__)

@app.route('/')
def hello():
      return render_template('index.html')
@app.route("/check",methods=["GET","POST"])
def check():
    c1=False
    c2=False
    c3=False
    c4=False
    c5=False
    ans1=""
    ans2=""
    ans3=""
    ans4=""
    ans5=""
    if request.method=="POST":
        pwd=request.form['pwd']
        if pwd =="pwd1":
            c1=True
            ans1="first link"
        elif pwd =="pwd2":
            c2=True
            ans2="second link"
        elif pwd =="pwd3":
            c3=True
            ans3="third link"
        elif pwd =="pwd4":
            c4=True
            ans4="fourth link"
        elif pwd =="pwd5":
            c5=True
            ans5="fifth link"
    return render_template("index.html", c1=c1,c2=c2,c3=c3,c4=c4,c5=c5,ans1=ans1,ans2=ans2,ans3=ans3,ans4=ans4,ans5=ans5)
    