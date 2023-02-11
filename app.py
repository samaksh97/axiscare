from flask import Flask,render_template,url_for,request,redirect, make_response
import json
import tailer
from flask import Flask, render_template, make_response
app = Flask(__name__)

from pymongo import MongoClient
client = MongoClient("mongodb+srv://schezfaz:schezeenf10@cluster0.dga2lhm.mongodb.net/?retryWrites=true&w=majority")
db = client.get_database("AxisCare")
records = db.covid
print("Documents:" , records.count_documents({}))


@app.route('/', methods=["GET", "POST"])
def main():
    return render_template('index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
