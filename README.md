Student Dropout Prediction

This project focuses on predicting student academic outcomes (Dropout or Graduate) using machine learning models. The dataset contains socio-demographic, academic, and economic features of students, and the goal is to identify patterns that contribute to dropouts.

📂 Project Structure

dataset.csv → Raw dataset containing student records.

notebook/code.py → Preprocessing, visualization, and model training.

README.md → Project documentation.

📊 Dataset

Rows: 4424

Columns: 37

Target variable:

Dropout (0)

Graduate (1)

(Enrolled records were removed for analysis)

Key Features

Demographics: Marital status, Gender, Age at enrollment, Nationality.

Academic: Previous qualification, Admission grade, Curriculum units, Course.

Family: Parent’s qualification & occupation.

Economic: Unemployment rate, Inflation rate, GDP.

Outcome (Target): Dropout / Graduate.

🛠️ Libraries Used
numpy
pandas
matplotlib
seaborn
scikit-learn

🔎 Workflow
1. Data Exploration

Checked dataset shape, column info, summary statistics.

Verified missing values (.isnull().sum() → none).

Checked duplicates (none found).

2. Data Cleaning & Transformation

Removed records with Target = Enrolled.

Encoded Target:

Dropout → 0

Graduate → 1

Converted Target to numeric format.

3. Feature Selection

Correlation heatmap with Target variable.

Selected features with positive correlation to the target.

4. Outlier Handling

Applied IQR-based filtering across features.

Visualized before/after with boxplots.

5. Exploratory Data Analysis (EDA)

Heatmaps for feature-target correlation.

Boxplots to analyze distributions per target class.

6. Modeling (Next Steps)

Implemented classification models:
Logistic Regression
Decision Tree
Random Forest
Support Vector Machine (SVM)
K-Nearest Neighbors (KNN)
Evaluation Metrics:
Accuracy
Precision, Recall, F1-score
ROC-AUC Score
Confusion Matrix
📈 Visualizations
Correlation Heatmap → Identifies strongest predictors of dropout.
Boxplots → Highlight feature distributions across Dropout vs Graduate.
🚀 How to Run
Clone this repository:
git clone https://github.com/your-username/student-dropout-prediction.git
cd student-dropout-prediction
Install dependencies:
pip install -r requirements.txt
Run Jupyter Notebook or Python script:
jupyter notebook notebook.ipynb
# OR
python code.py
✅ Results (Expected)
Identified key predictors (Admission grade, Curricular units performance, Age at enrollment).
Built baseline ML models for classification.
Random Forest/Logistic Regression expected to perform well.
📌 Future Improvements
Hyperparameter tuning with GridSearchCV.
SMOTE or class balancing if target distribution is imbalanced.
Deploy as a web app (Flask/Streamlit) for real-time predictions.
