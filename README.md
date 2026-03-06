# AutoValue AI: Smart Car Price Predictor 🏎️

[![Live Demo](https://img.shields.io/badge/Demo-Live-brightgreen)](https://car-price-predict-auto.onrender.com)
[![Python 3.10](https://img.shields.io/badge/Python-3.10-blue)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Framework-Flask-lightgrey)](https://flask.palletsprojects.com/)

AutoValue AI is a high-precision car valuation tool powered by Machine Learning. Using historical data on thousands of vehicle sales, it provides an instant, data-driven estimate for your car's market value.

## ✨ Features
- **Instant Valuation**: Get a price estimate in seconds.
- **Data-Driven**: Trained on extensive car sales data.
- **Premium UI**: Modern glassmorphic interface with fluid animations.
- **Responsive**: Fully optimized for mobile and desktop screens.

## 🛠️ Technology Stack
- **Backend**: Flask (Python)
- **Machine Learning**: Scikit-learn (Linear Regression)
- **Data Processing**: Pandas, NumPy
- **Frontend**: HTML5, Vanilla CSS3, JavaScript (ES6+)
- **Icons**: FontAwesome 6

## 🚀 How to Run Locally

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd car-price-prediction
   ```

2. **Create a virtual environment**:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Train the model (Optional)**:
   ```bash
   python train_model.py
   ```

5. **Start the application**:
   ```bash
   python app.py
   ```

## 📊 Dataset Information
The model accounts for:
- **Vehicle Model & Make**
- **Year of Manufacture**
- **Distance Covered (Kms)**
- **Fuel Type (Petrol/Diesel/CNG)**
- **Seller Type (Dealer/Individual)**
- **Transmission System (Manual/Automatic)**

## 🛡️ License
Distributed under the MIT License. See `LICENSE` for more information.

---
Created with ❤️ by R. RITHIKA
