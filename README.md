# 🏡 House Price Prediction - Flask Web App

A simple Flask-based web application that predicts house prices based on user-inputted features using a trained Machine Learning model.

## 🚀 Project Overview
This web application takes house features such as **median income, house age, number of rooms, bedrooms, population, and occupancy** as inputs and predicts the house price using a trained machine learning model.

The project includes:
- A **Flask Web App** for user input and predictions.
- A **Machine Learning Model** trained on an open-source housing price dataset.
- A user-friendly **form-based UI** for entering house features.

---

## 🛠️ Tech Stack
- **Backend**: Flask (Python)
- **Frontend**: HTML, CSS (Bootstrap)
- **Machine Learning**: Scikit-Learn, Pandas, NumPy
- **Deployment**: Localhost (for now)

---

## 📂 Project Structure
Housing_price_prediction/ │── model/ # Stores trained ML model │ ├── model.pkl # Serialized model using joblib │── templates/ # HTML templates │ ├── index.html # Web UI for input │── static/ # CSS/JS files (if any) │── app.py # Flask backend for predictions │── train_model.py # Python script to train and save the ML model │── requirements.txt # Dependencies for the project │── README.md # Project documentation │── venv/ # Virtual environment (not uploaded to GitHub) │── .gitignore # Ignored files like venv and pycache

## 📦 Installation & Setup
Follow these steps to run the project locally:

### **1️⃣ Clone the Repository**
```sh
git clone  https://github.com/1289RA/House_price_prediction.git
cd House-Price-Prediction

2️⃣ Set Up Virtual Environment (Recommended)
sh
Copy
Edit
python -m venv venv
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate     # Windows
3️⃣ Install Dependencies
sh
Copy
Edit
pip install -r requirements.txt
4️⃣ Train the Machine Learning Model
Before running the app, train the model:

sh
Copy
Edit
python train_model.py
This will generate a model.pkl file inside the model/ folder.

5️⃣ Run the Flask Application
sh
Copy
Edit
python app.py
You should see output like:

nginx
Copy
Edit
Running on http://127.0.0.1:5000/
6️⃣ Open in Browser
Go to http://127.0.0.1:5000/ in your browser.

🔧 How It Works
User enters house details in the form.
The Flask app sends input to the trained ML model.
Model predicts the house price and displays it on the web page.

📌 Features
✔️ Simple and user-friendly UI
✔️ Flask-based backend for easy deployment
✔️ Machine Learning model for price prediction
✔️ Well-documented GitHub repository



📄 License
This project is open-source and free to use.

🔗 Connect with Me
📧 Email: rautradhika079@gmail.com.com
🌎 GitHub: https://github.com/1289RA/House_price_prediction.git


