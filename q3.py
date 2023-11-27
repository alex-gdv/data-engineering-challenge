from flask import Flask, request
import pandas as pd

app = Flask(__name__)

dataset = pd.read_csv("officer_snapshot.csv")

@app.route("/data", methods=["GET"])
def get_data():
    company_number = int(request.args.get("company_number"))
    town = request.args.get("town")
    
    filtered_data = dataset[(dataset["Company Number"] == company_number) & (dataset["Town"] == town)].to_json()

    return filtered_data

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)