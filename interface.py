from flask import Flask, render_template, request, jsonify
from utils import US_House_PP
import numpy as np




app = Flask(__name__,template_folder="template")
@app.route('/')
def hello_flask():
    print("Welcome to us housing price Prediction")
    return render_template("home.html")

@app.route('/predict_price', methods = ['POST','GET'])
def predict_price():
    if request.method == "GET":
        # user_data = request.form
        print("We are using get method")
        Income_Area = eval(request.args.get("Income_Area"))
        House_Age = eval(request.args.get("House_Age"))
        Rooms_Qty = eval(request.args.get("Rooms_Qty"))
        Bedrooms_Qty = eval(request.args.get("Bedrooms_Qty"))
        Area_Population = eval(request.args.get("Area_Population"))

        print('Income_Area', 'House_Age', 'Rooms_Qty', 'Bedrooms_Qty',
                'Area_Population',Income_Area, House_Age, Rooms_Qty, Bedrooms_Qty,
                    Area_Population)
        pc = US_House_PP(Income_Area, House_Age, Rooms_Qty, Bedrooms_Qty,
                    Area_Population)
        price = pc.get_us_house_pp()
        
        # return jsonify({"Message": f"Predicted House price is {price} $"})
        return render_template("home.html", price = price)

if __name__ == "__main__":
    app.run(host = '0.0.0.0', port = 5050)
        