
An AI-powered educational analytics system that predicts student dropout risk using machine learning. This project uses a Random Forest Classifier trained on academic, demographic, and financial factors to help educational institutions identify at-risk students early.A machine learning-powered web application that predicts student dropout likelihood using a pre-trained Random Forest model with 23 comprehensive factors.


---🔗 **GitHub Repository**: https://github.com/coderheist/Student_dropout_rate



## 📊 Project Overview## 🚀 Quick Start (One-Click Deployment)



This system predicts whether a student will **Dropout** or **Graduate** based on 23 key features including academic performance, financial status, and demographic information.**Easy Setup for Windows:**

1. Clone this repository: `git clone https://github.com/coderheist/Student_dropout_rate.git`

### Key Features:2. Navigate to folder: `cd Student_dropout_rate`

- 🤖 **Binary Classification**: Dropout (0) vs Graduate (1)3. Double-click `start-app.bat`

- 🎯 **23 Input Parameters**: Academic, financial, and demographic factors4. Wait for automatic setup and browser launch

- 📈 **High Accuracy**: Random Forest model optimized with GridSearchCV4. Start making predictions!

- 🔬 **Data-Driven**: Trained on 4,425 student records

**Manual Setup:**

---```bash

# Install dependencies

## 📁 Repository Structurepip install flask flask-cors pandas scikit-learn joblib numpy



```# Start backend (Terminal 1)

Student_dropout_rate/cd backend && python app.py

├── dataset.csv                          # Training dataset (4,425 records)

├── random_forest_model.pkl              # Trained Random Forest model (3.5 MB)# Start frontend (Terminal 2) 

├── sudent_dropout_rate1 (4).ipynb       # Jupyter notebook with model trainingcd frontend-simple && python -m http.server 8000

├── .gitignore                           # Git ignore rules

└── README.md                            # Project documentation (this file)# Open browser: http://localhost:8000

``````



---## 📊 System Features



## 🔬 Model Details✅ **Pre-trained ML Model** - Uses existing `random_forest_model.pkl`  

✅ **23 Input Parameters** - Comprehensive student assessment  

### Classification Type✅ **Real-time Predictions** - Instant dropout/graduation probability  

- **Type**: Binary Classification✅ **User-friendly Form** - Guided inputs with placeholder examples  

- **Classes**: ✅ **REST API** - Complete backend for integrations  

  - `0` - Dropout✅ **Deployment Ready** - Optimized file structure  

  - `1` - Graduate

- **Note**: "Enrolled" students were filtered out during training## 🎯 Input Parameters (23 Features)



### Algorithm### Basic Information

- **Model**: Random Forest Classifier- **Application Order** (0-9): e.g., 1

- **Optimization**: GridSearchCV for hyperparameter tuning- **Course** (1-17): Select from dropdown  

- **Best Parameters**:- **Attendance Type** (0/1): Daytime or Evening

  - `n_estimators`: 150- **Previous Qualification Grade** (95-190): e.g., 140.5

  - `max_depth`: 20

### Family Background  

### Preprocessing- **Mother's Occupation** (0-15): Select occupation category

- **Feature Scaling**: StandardScaler applied to all features- **Father's Occupation** (0-15): Select occupation category

- **Train-Test Split**: 67% training, 33% testing

- **Features**: 23 numerical parameters### Academic Performance

- **Admission Grade** (95-190): e.g., 150.0

---- **Displaced** (0/1): Away from home residence



## 📋 Input Features (23 Parameters)### Financial Status

- **Tuition Fees Up to Date** (0/1): Payment status

### Demographic Information- **Scholarship Holder** (0/1): Has scholarship

1. **Marital Status** - Student's marital status- **International Student** (0/1): Foreign student

2. **Age at Enrollment** - Student's age when enrolled

3. **Gender** - Male/Female### 1st Semester Performance

4. **Nationality** - Student's nationality- **Units Credited** (0-26): e.g., 0  

5. **International** - Whether student is international- **Units Enrolled** (0-26): e.g., 6

- **Units Evaluations** (0-45): e.g., 6-12

### Academic Background- **Units Approved** (0-26): e.g., 5-6

6. **Application Mode** - Method of application- **Semester Grade** (0-20): e.g., 12.5

7. **Application Order** - Order of application preference

8. **Course** - Course enrolled in### 2nd Semester Performance  

9. **Daytime/Evening Attendance** - Class attendance schedule- **Units Credited** (0-20): e.g., 0

10. **Previous Qualification** - Previous education level- **Units Enrolled** (0-23): e.g., 6  

11. **Mother's Qualification** - Mother's education level- **Units Evaluations** (0-33): e.g., 6-12

12. **Father's Qualification** - Father's education level- **Units Approved** (0-20): e.g., 5-6

- **Semester Grade** (0-20): e.g., 13.2

### Academic Performance

13. **1st Semester Credits** - Credits completed in semester 1### Economic Indicators

14. **1st Semester Grade** - Average grade in semester 1 (0-20 scale)- **Unemployment Rate** (0-30%): e.g., 8.5

15. **2nd Semester Credits** - Credits completed in semester 2- **GDP Growth Rate** (-10 to +10%): e.g., 2.1

16. **2nd Semester Grade** - Average grade in semester 2 (0-20 scale)

## 📁 Deployment Structure

### Financial Status

17. **Tuition Fees Up to Date** - Whether fees are current```

18. **Debtor** - Whether student has debtsStudent_drpout/

19. **Scholarship Holder** - Whether student has scholarship├── 📁 backend/

│   ├── 🐍 app.py              # Flask API server

### Family Background│   └── 📄 requirements.txt    # Python dependencies  

20. **Mother's Occupation** - Mother's occupation code├── 📁 frontend-simple/

21. **Father's Occupation** - Father's occupation code│   └── 🌐 index.html         # Web application

├── 🤖 random_forest_model.pkl # Pre-trained ML model

### Special Circumstances├── 🚀 start-app.bat          # One-click launcher

22. **Displaced** - Whether student is displaced└── 📖 README.md              # This file

23. **Educational Special Needs** - Whether student has special needs```



---## 🔌 API Endpoints



## 🚀 Getting Started| Endpoint | Method | Description |

|----------|--------|-------------|

### Prerequisites| `/` | GET | Health check & API info |

```bash| `/features` | GET | List all 23 features |

Python 3.11+| `/predict` | POST | Make prediction |

Jupyter Notebook| `/model-info` | GET | Model details |

```

### Sample API Call

### Required Libraries```bash

```pythoncurl -X POST http://localhost:5000/predict \

numpy  -H "Content-Type: application/json" \

pandas  -d '{

matplotlib    "Application_order": 1,

seaborn    "Course": 7,

scikit-learn    "Daytime_evening_attendance": 1,

joblib    "Previous_qualification_grade": 140.5,

```    "Mothers_occupation": 5,

    "Fathers_occupation": 5,

### Installation    "Admission_grade": 150.0,

    "Displaced": 0,

1. **Clone the repository**    "Tuition_fees_up_to_date": 1,

```bash    "Scholarship_holder": 0,

git clone https://github.com/coderheist/Student_dropout_rate.git    "International": 0,

cd Student_dropout_rate    "Curricular_units_1st_sem_credited": 0,

```    "Curricular_units_1st_sem_enrolled": 6,

    "Curricular_units_1st_sem_evaluations": 6,

2. **Install dependencies**    "Curricular_units_1st_sem_approved": 6,

```bash    "Curricular_units_1st_sem_grade": 12.5,

pip install numpy pandas matplotlib seaborn scikit-learn joblib    "Curricular_units_2nd_sem_credited": 0,

```    "Curricular_units_2nd_sem_enrolled": 6,

    "Curricular_units_2nd_sem_evaluations": 6,

3. **Open Jupyter Notebook**    "Curricular_units_2nd_sem_approved": 6,

```bash    "Curricular_units_2nd_sem_grade": 13.2,

jupyter notebook "sudent_dropout_rate1 (4).ipynb"    "Unemployment_rate": 8.5,

```    "GDP": 2.1

  }'

---```



## 💻 Usage## ⚡ System Requirements



### Training the Model (Jupyter Notebook)- **Python 3.8+** with pip

- **2GB RAM** minimum  

```python- **Modern browser** with JavaScript

import pandas as pd- **Internet connection** (for initial setup)

from sklearn.ensemble import RandomForestClassifier

from sklearn.model_selection import GridSearchCV## 🎯 Usage Flow

import joblib

1. **📝 Input Data** - Fill all 23 parameters using helpful placeholders

# Load data2. **🔮 Get Prediction** - Click "Predict Outcome" button  

data = pd.read_csv("dataset.csv")3. **📊 View Results** - See probability scores and final prediction

4. **🔄 Repeat** - Make multiple predictions as needed

# Filter enrolled students

data_filtered = data[data['Target'] != 'Enrolled']## 🚀 Production Deployment



# Map target: Dropout=0, Graduate=1This system is ready for:

data_filtered['Target'] = data_filtered['Target'].map({- ✅ **Educational institutions**

    'Dropout': 0,- ✅ **Student counseling services** 

    'Graduate': 1- ✅ **Academic research**

})- ✅ **Risk assessment tools**



# Split features and target## 🔒 Model Details

X = data_filtered.drop('Target', axis=1)

y = data_filtered['Target']- **Type**: Random Forest Classifier (pre-trained)

- **Input**: 23 numerical features

# Train model- **Output**: Binary classification (0=Dropout, 1=Graduate)  

rf = RandomForestClassifier()- **Format**: Scikit-learn pickle file

param_grid = {- **Performance**: Optimized for educational data

    'n_estimators': [50, 100, 150, 200],

    'max_depth': [5, 10, 20, 30]---

}

grid_search = GridSearchCV(rf, param_grid, cv=5, scoring='accuracy')**🚀 Ready to deploy! Just run `start-app.bat` and start predicting!**
grid_search.fit(X_train, y_train)

# Save model
best_rf = grid_search.best_estimator_
joblib.dump(best_rf, 'random_forest_model.pkl')
```

### Loading and Using the Model

```python
import joblib
import numpy as np

# Load trained model
model = joblib.load('random_forest_model.pkl')

# Prepare input (23 features)
student_data = np.array([[
    1,    # marital_status
    1,    # application_mode
    1,    # application_order
    9238, # course
    1,    # daytime_evening_attendance
    1,    # previous_qualification
    1,    # nationality
    13,   # mothers_qualification
    10,   # fathers_qualification
    6,    # mothers_occupation
    10,   # fathers_occupation
    0,    # displaced
    0,    # educational_special_needs
    0,    # debtor
    1,    # tuition_fees_up_to_date
    1,    # gender
    0,    # scholarship_holder
    20,   # age_at_enrollment
    0,    # international
    6,    # curricular_units_1st_sem_credited
    14.5, # curricular_units_1st_sem_grade
    6,    # curricular_units_2nd_sem_credited
    13.8  # curricular_units_2nd_sem_grade
]])

# Make prediction
prediction = model.predict(student_data)
probability = model.predict_proba(student_data)

print(f"Prediction: {'Dropout' if prediction[0] == 0 else 'Graduate'}")
print(f"Confidence: {max(probability[0]):.2%}")
```

---

## 📊 Model Performance

The model was evaluated using various metrics:

- ✅ **Accuracy**: High accuracy achieved through GridSearchCV optimization
- ✅ **Precision**: Reliable positive predictions
- ✅ **Recall**: Effective identification of at-risk students
- ✅ **F1-Score**: Balanced performance across classes

*Detailed metrics available in the Jupyter notebook*

---

## ⚠️ Important Notes

### 1. StandardScaler Preprocessing
The model was trained on **scaled data** using StandardScaler. For production deployment:
- Option A: Save the scaler during training and apply it before prediction
- Option B: Implement rule-based fallback for unscaled inputs
- Option C: Retrain model without scaling (not recommended)

### 2. Binary Classification
- Model predicts only **Dropout** or **Graduate**
- "Enrolled" students are **not included** in the model
- This is by design - the goal is to predict final outcomes

### 3. Feature Order
Features must be provided in the **exact order** used during training (see list above)

---

## 🎯 Use Cases

This system can be used by:

- 🏫 **Educational Institutions**: Identify at-risk students early
- 📚 **Academic Advisors**: Provide targeted support interventions
- 📊 **Policy Makers**: Understand factors influencing dropout rates
- 🔬 **Researchers**: Analyze educational outcomes and patterns

---

## 🔮 Future Enhancements

- [ ] Web-based interface for easy predictions
- [ ] Real-time monitoring dashboard
- [ ] Integration with student information systems
- [ ] Additional features (attendance, extracurricular activities)
- [ ] Multi-class classification (including "Enrolled" status)
- [ ] Explainable AI features (SHAP values, feature importance)

---

## 📈 Dataset Information

### Source
Educational institution student records

### Size
- **Records**: 4,425 students
- **Features**: 36 input features + 1 target
- **Target Distribution**: 
  - Dropout: ~32%
  - Graduate: ~47%
  - Enrolled: ~21% (filtered out)

### Data Quality
- ✅ No missing values
- ✅ No duplicate records
- ✅ Numerical features (no categorical encoding needed)

---

## 🛠️ Tech Stack

- **Language**: Python 3.11
- **ML Framework**: scikit-learn
- **Data Processing**: pandas, numpy
- **Visualization**: matplotlib, seaborn
- **Model Serialization**: joblib
- **Development**: Jupyter Notebook

---

## 📝 License

This project is available for educational and research purposes.

---

## 👤 Author

**GitHub**: [@coderheist](https://github.com/coderheist)

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📧 Contact

For questions or feedback, please open an issue on GitHub.

---

## ⭐ Acknowledgments

- Educational data providers
- scikit-learn community
- Open-source ML community

---

**Made with ❤️ for better education outcomes**
