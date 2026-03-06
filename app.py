from flask import Flask, render_template, request, jsonify
import pandas as pd
import pickle
import numpy as np

app = Flask(__name__)

# Load the model
try:
    model = pickle.load(open('model/car_price_model.pkl', 'rb'))
    df = pd.read_csv('data/car_data.csv')
except Exception as e:
    print(f"Error loading model or data: {e}")

@app.route('/')
def index():
    # Get unique values for dropdowns
    car_names = sorted(df['Car_Name'].unique())
    fuel_types = sorted(df['Fuel_Type'].unique())
    seller_types = sorted(df['Seller_Type'].unique())
    transmissions = sorted(df['Transmission'].unique())
    years = sorted(df['Year'].unique(), reverse=True)
    
    return render_template('index.html', 
                          car_names=car_names,
                          fuel_types=fuel_types,
                          seller_types=seller_types,
                          transmissions=transmissions,
                          years=years)

@app.route('/predict', methods=['POST'])
def predict():
    try:
        car_name = request.form.get('car_name')
        year = int(request.form.get('year'))
        kms_driven = int(request.form.get('kms_driven'))
        fuel_type = request.form.get('fuel_type')
        seller_type = request.form.get('seller_type')
        transmission = request.form.get('transmission')

        # Create DataFrame for prediction
        input_data = pd.DataFrame([[car_name, year, kms_driven, fuel_type, seller_type, transmission]],
                                columns=['Car_Name', 'Year', 'Kms_Driven', 'Fuel_Type', 'Seller_Type', 'Transmission'])
        
        prediction = model.predict(input_data)
        
        # Round prediction to 2 decimal places
        result = round(prediction[0], 2)
        
        # If result is negative (unlikely with LR but possible with bad data), set to 0
        if result < 0:
            result = 0.05
            
        return jsonify({'prediction': f"₹ {result} Lakhs"})
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
