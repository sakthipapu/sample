from flask import Flask,jsonify
app=Flask(__name__)

@app.route("/")
def index():
    return "hello world"

if __name__=='__main__':
    app.run(debug=True)