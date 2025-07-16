🫀 Heart Disease Prediction App
A simple and interactive Machine Learning web app built using Streamlit. It predicts the risk of heart disease based on medical inputs provided by the user.

📌 Features
📝 Easy-to-use sidebar form to input patient details

⚙️ Trained Logistic Regression model

📊 Real-time prediction with probability score

🎨 Clean and styled interface with emojis and layout

🌐 Deployable with Streamlit Cloud

🚀 Live Demo
🔗 [Add your Streamlit link here once deployed]

📁 Project Structure
bash
Copy
Edit
heart-disease-app/
├── app.py                # Streamlit web app
├── requirements.txt      # Python dependencies
└── models/               # Trained model and scaler
    ├── logistic_model.pkl
    └── scaler.pkl

🔧 How to Run Locally
Clone the repository

bash
Copy
Edit
git clone https://github.com/your-username/heart-disease-app.git
cd heart-disease-app
Install the dependencies

nginx
Copy
Edit
pip install -r requirements.txt
Run the app

arduino
Copy
Edit
streamlit run app.py

📊 Input Features
Age

Sex

Chest Pain Type (cp)

Resting Blood Pressure (trestbps)

Cholesterol (chol)

Fasting Blood Sugar (fbs)

Resting ECG (restecg)

Maximum Heart Rate Achieved (thalach)

Exercise Induced Angina (exang)

ST Depression (oldpeak)

Slope of the ST Segment

Number of Major Vessels (ca)

Thalassemia (thal)

💡 Model Used
Logistic Regression (Accuracy ~81.6%)

Preprocessing: One-Hot Encoding + Standard Scaling

📦 Requirements
streamlit

numpy

scikit-learn

joblib

🙋‍♀️ Author
Khushi
Built with 💖 using Python & Streamlit

