# 💼 Salary Predictor AI

A machine learning-powered web application that predicts salary based on experience, education, job title, and age.

## 🚀 Quick Start

### Option 1: Using the run script (Recommended)
```bash
# Install dependencies
pip install -r requirements.txt

# Run the app
python run_app.py
```

### Option 2: Direct Streamlit command
```bash
# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run app.py
```

## 📱 Using the App

1. The app will automatically open in your default web browser
2. If it doesn't open automatically, go to: http://localhost:8501
3. Enter your details:
   - Years of Experience
   - Education Level
   - Job Title
   - Age
4. Click "Predict Salary" to get your estimated salary

## 🛠️ Requirements

- Python 3.7+
- Streamlit
- Joblib
- NumPy
- Scikit-learn

## 📁 Files

- `app.py` - Main Streamlit application
- `salary_model.pkl` - Trained machine learning model
- `requirements.txt` - Python dependencies
- `run_app.py` - Helper script to run the app
- `README.md` - This file

## ⏹️ Stopping the App

Press `Ctrl+C` in the terminal to stop the Streamlit server.

## 🔧 Troubleshooting

If you encounter any issues:

1. Make sure all dependencies are installed: `pip install -r requirements.txt`
2. Ensure you're in the correct directory
3. Check that Python 3.7+ is installed: `python --version`
4. If port 8501 is busy, the app will automatically use the next available port

## 🎯 Features

- Interactive web interface
- Real-time salary predictions
- Support for multiple job titles and education levels
- Age and experience-based predictions 