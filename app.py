from flask import Flask,render_template,url_for,request,redirect, make_response
import json
import tailer
import csv
import pandas as pd
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

@app.route("/search-trends")
def search():
    return render_template("search_trends.html")

@app.route("/trends")
def trends():
    return render_template("case-based-trends.html")

@app.route("/mobility")
def mobility():
    return render_template("mobility.html")

@app.context_processor
def utility_processor():    
    def get_search_trends():
            x_list = []
            records = db['search-trends']
            cursor = records.find({})
            for document in cursor:
                e = [[x, y] for x, y in document.items()]
                x_list.append(e)
                # print(document)
        
            for x in x_list:
                for y in x:
                    print(y)
                    if(y[0]=='_id'):
                        x.remove(y)
                        
            return x_list
    
    
    def get_top_search_trends():
        df = pd.read_csv("static/graph_data/search-trends-top.csv",sep=',', encoding='utf-8')
        top20 = df.to_dict(orient='records')
        symptom_list = list(df.columns)

        return [top20, symptom_list]
    
    def get_epidemiology_strains():
        df = pd.read_csv("static/graph_data/epidemiology-strains.csv",sep=',', encoding='utf-8')
        strain_dict = df.to_dict(orient='records')
        bar_labels = list(df.columns)
        strains = list(df['strain'])

        return [strain_dict,bar_labels,strains]
    
    def get_mobility_data():
        mobility_monthly_data = []
        with open("static/graph_data/mobility_monthly.csv", mode="r") as file:
            csvFile = csv.reader(file)
            for line in csvFile:
                mobility_monthly_data.append(line)
        # print(mobility_monthly_data)
        return mobility_monthly_data
    
    def get_mobility_pie_data():
        mobility_pie_data = []
        with open("static/graph_data/mean_mobility.csv", mode="r") as file:
                csvFile = csv.reader(file)
                for line in csvFile:
                    mobility_pie_data.append(line)
        # print(mobility_pie_data)
        return mobility_pie_data
        
    return dict(
    get_search_trends           = get_search_trends,
    get_top_search_trends = get_top_search_trends,
    get_epidemiology_strains = get_epidemiology_strains,
    get_mobility_data = get_mobility_data,
    get_mobility_pie_data = get_mobility_pie_data)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
