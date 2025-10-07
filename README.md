# 🎓 Student Dropout Prediction System

[![GitHub](https://img.shields.io/github/license/coderheist/Student_dropout_rate)](https://github.com/coderheist/Student_dropout_rate)
[![Python](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Flask](https://img.shields.io/badge/flask-2.0+-green.svg)](https://flask.palletsprojects.com/)

A machine learning-powered web application that predicts student dropout likelihood using a pre-trained Random Forest model with 23 comprehensive factors.

🔗 **GitHub Repository**: https://github.com/coderheist/Student_dropout_rate

## 🚀 Quick Start (One-Click Deployment)

**Easy Setup for Windows:**
1. Clone this repository: `git clone https://github.com/coderheist/Student_dropout_rate.git`
2. Navigate to folder: `cd Student_dropout_rate`
3. Double-click `start-app.bat`
4. Wait for automatic setup and browser launch
4. Start making predictions!

**Manual Setup:**
```bash
# Install dependencies
pip install flask flask-cors pandas scikit-learn joblib numpy

# Start backend (Terminal 1)
cd backend && python app.py

# Start frontend (Terminal 2) 
cd frontend-simple && python -m http.server 8000

# Open browser: http://localhost:8000
```

## 📊 System Features

✅ **Pre-trained ML Model** - Uses existing `random_forest_model.pkl`  
✅ **23 Input Parameters** - Comprehensive student assessment  
✅ **Real-time Predictions** - Instant dropout/graduation probability  
✅ **User-friendly Form** - Guided inputs with placeholder examples  
✅ **REST API** - Complete backend for integrations  
✅ **Deployment Ready** - Optimized file structure  

## 🎯 Input Parameters (23 Features)

### Basic Information
- **Application Order** (0-9): e.g., 1
- **Course** (1-17): Select from dropdown  
- **Attendance Type** (0/1): Daytime or Evening
- **Previous Qualification Grade** (95-190): e.g., 140.5

### Family Background  
- **Mother's Occupation** (0-15): Select occupation category
- **Father's Occupation** (0-15): Select occupation category

### Academic Performance
- **Admission Grade** (95-190): e.g., 150.0
- **Displaced** (0/1): Away from home residence

### Financial Status
- **Tuition Fees Up to Date** (0/1): Payment status
- **Scholarship Holder** (0/1): Has scholarship
- **International Student** (0/1): Foreign student

### 1st Semester Performance
- **Units Credited** (0-26): e.g., 0  
- **Units Enrolled** (0-26): e.g., 6
- **Units Evaluations** (0-45): e.g., 6-12
- **Units Approved** (0-26): e.g., 5-6
- **Semester Grade** (0-20): e.g., 12.5

### 2nd Semester Performance  
- **Units Credited** (0-20): e.g., 0
- **Units Enrolled** (0-23): e.g., 6  
- **Units Evaluations** (0-33): e.g., 6-12
- **Units Approved** (0-20): e.g., 5-6
- **Semester Grade** (0-20): e.g., 13.2

### Economic Indicators
- **Unemployment Rate** (0-30%): e.g., 8.5
- **GDP Growth Rate** (-10 to +10%): e.g., 2.1

## 📁 Deployment Structure

```
Student_drpout/
├── 📁 backend/
│   ├── 🐍 app.py              # Flask API server
│   └── 📄 requirements.txt    # Python dependencies  
├── 📁 frontend-simple/
│   └── 🌐 index.html         # Web application
├── 🤖 random_forest_model.pkl # Pre-trained ML model
├── 🚀 start-app.bat          # One-click launcher
└── 📖 README.md              # This file
```

## 🔌 API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/` | GET | Health check & API info |
| `/features` | GET | List all 23 features |
| `/predict` | POST | Make prediction |
| `/model-info` | GET | Model details |

### Sample API Call
```bash
curl -X POST http://localhost:5000/predict \
  -H "Content-Type: application/json" \
  -d '{
    "Application_order": 1,
    "Course": 7,
    "Daytime_evening_attendance": 1,
    "Previous_qualification_grade": 140.5,
    "Mothers_occupation": 5,
    "Fathers_occupation": 5,
    "Admission_grade": 150.0,
    "Displaced": 0,
    "Tuition_fees_up_to_date": 1,
    "Scholarship_holder": 0,
    "International": 0,
    "Curricular_units_1st_sem_credited": 0,
    "Curricular_units_1st_sem_enrolled": 6,
    "Curricular_units_1st_sem_evaluations": 6,
    "Curricular_units_1st_sem_approved": 6,
    "Curricular_units_1st_sem_grade": 12.5,
    "Curricular_units_2nd_sem_credited": 0,
    "Curricular_units_2nd_sem_enrolled": 6,
    "Curricular_units_2nd_sem_evaluations": 6,
    "Curricular_units_2nd_sem_approved": 6,
    "Curricular_units_2nd_sem_grade": 13.2,
    "Unemployment_rate": 8.5,
    "GDP": 2.1
  }'
```

## ⚡ System Requirements

- **Python 3.8+** with pip
- **2GB RAM** minimum  
- **Modern browser** with JavaScript
- **Internet connection** (for initial setup)

## 🎯 Usage Flow

1. **📝 Input Data** - Fill all 23 parameters using helpful placeholders
2. **🔮 Get Prediction** - Click "Predict Outcome" button  
3. **📊 View Results** - See probability scores and final prediction
4. **🔄 Repeat** - Make multiple predictions as needed

## 🚀 Production Deployment

This system is ready for:
- ✅ **Educational institutions**
- ✅ **Student counseling services** 
- ✅ **Academic research**
- ✅ **Risk assessment tools**

## 🔒 Model Details

- **Type**: Random Forest Classifier (pre-trained)
- **Input**: 23 numerical features
- **Output**: Binary classification (0=Dropout, 1=Graduate)  
- **Format**: Scikit-learn pickle file
- **Performance**: Optimized for educational data

---

**🚀 Ready to deploy! Just run `start-app.bat` and start predicting!**