from flask import Flask,render_template,request,jsonify
from main import pid_process
app = Flask(__name__)
@app.route("/")
def home():
    return render_template("hello.html")

@app.route("/start" ,methods=['GET', 'POST'] )
def start():
    if request.method == 'POST':
        kp = float(request.form['kc'])
        ki = float(request.form['taul'])
        kd = float(request.form['taud'])
        t,sp,pv = pid_process(kp,ki,kd)
        print(kp,ki,kd)
        return render_template("index.html",t=t,pv=pv,sp=sp)
    else:
        return render_template("index.html",t=[],pv=[],sp=[])


if __name__ == "__main__":
    app.run(debug=True)