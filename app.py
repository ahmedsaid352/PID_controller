from flask import Flask,render_template,request
from main import pid_run
app = Flask(__name__)
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/start" ,methods=['GET', 'POST'] )
def start():
    if request.method == 'POST':
        pid_run()
        return render_template("result.html")
    else:
        return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)