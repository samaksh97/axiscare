from flask import Flask,render_template,url_for,request,redirect, make_response
import json
import tailer
from flask import Flask, render_template, make_response
app = Flask(__name__)

da_connections = {}
collected_vals = []

@app.route('/', methods=["GET", "POST"])
def main():
    return render_template('index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
