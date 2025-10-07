# 🚀 Heroku Deployment Guide

## 📋 Project Overview
Student Dropout Prediction System optimized for **Heroku deployment** with full ML capabilities.

### ✅ Current Structure (Heroku-Ready)
```
Student_dropout_rate/
├── 🌐 Frontend
│   ├── index.html              # Main application
│   └── frontend-simple/        # Complete 23-parameter form
├── 🔧 Backend  
│   └── backend/app.py          # Flask server with ML model
├── 🤖 Model & Data
│   ├── random_forest_model.pkl # Pre-trained model
│   └── dataset.csv            # Training data
├── ⚙️ Heroku Configuration
│   ├── Procfile               # Heroku startup command
│   ├── runtime.txt            # Python version
│   └── requirements.txt       # All ML dependencies
└── 📚 Documentation
    └── README.md              # Main docs
```

## 🚀 Quick Heroku Deployment

### Method 1: Heroku CLI (Recommended)

1. **Install Heroku CLI**:
   ```bash
   # Windows (using chocolatey)
   choco install heroku-cli
   
   # Or download from: https://devcenter.heroku.com/articles/heroku-cli
   ```

2. **Login to Heroku**:
   ```bash
   heroku login
   ```

3. **Create Heroku App**:
   ```bash
   heroku create student-dropout-prediction
   # Or use your preferred app name
   ```

4. **Deploy**:
   ```bash
   git add .
   git commit -m "Deploy to Heroku"
   git push heroku main
   ```

5. **Open App**:
   ```bash
   heroku open
   ```

### Method 2: Heroku Dashboard

1. **Connect Repository**:
   - Go to [Heroku Dashboard](https://dashboard.heroku.com/)
   - Create New App → Connect to GitHub
   - Select your `Student_dropout_rate` repository

2. **Configure Deployment**:
   - Choose `main` branch for deployment
   - Enable Automatic Deploys (optional)
   - Click "Deploy Branch"

3. **Monitor Deployment**:
   - Check build logs in the Activity tab
   - Once deployed, click "Open app"

## ⚙️ Configuration Files

### `Procfile` (Heroku Startup)
```
web: gunicorn --chdir backend --bind 0.0.0.0:$PORT app:app
```

### `runtime.txt` (Python Version)
```
python-3.9.18
```

### `requirements.txt` (Dependencies)
```
Flask==2.3.2
Flask-CORS==4.0.0
numpy==1.24.3
scikit-learn==1.3.0
pandas==2.0.3
joblib==1.3.2
gunicorn==21.2.0
```

## 🎯 Features Available

### 🌐 Web Interface
- **Main App**: `your-app.herokuapp.com/`
- **Complete Form**: `your-app.herokuapp.com/frontend-simple/`

### 📡 API Endpoints
- **Health Check**: `GET /` 
- **Make Prediction**: `POST /predict`
- **Get Features**: `GET /features`
- **Model Info**: `GET /model-info`

### 🤖 ML Capabilities
- **Real ML Model**: Uses `random_forest_model.pkl`
- **23 Features**: Complete academic and demographic analysis
- **High Accuracy**: Production-trained Random Forest classifier
- **Feature Importance**: Insights into prediction factors

## 📊 API Usage Examples

### Health Check
```bash
curl https://your-app.herokuapp.com/
```

### Make Prediction
```bash
curl -X POST https://your-app.herokuapp.com/predict \
  -H "Content-Type: application/json" \
  -d '{
    "Application_order": 1,
    "Course": 33,
    "Daytime_evening_attendance": 1,
    "Previous_qualification_grade": 15.5,
    "Mothers_occupation": 4,
    "Fathers_occupation": 3,
    "Admission_grade": 142.5,
    "Displaced": 0,
    "Tuition_fees_up_to_date": 1,
    "Scholarship_holder": 0,
    "International": 0,
    "Curricular_units_1st_sem_credited": 6,
    "Curricular_units_1st_sem_enrolled": 6,
    "Curricular_units_1st_sem_evaluations": 6,
    "Curricular_units_1st_sem_approved": 6,
    "Curricular_units_1st_sem_grade": 13.8,
    "Curricular_units_2nd_sem_credited": 6,
    "Curricular_units_2nd_sem_enrolled": 6,
    "Curricular_units_2nd_sem_evaluations": 6,
    "Curricular_units_2nd_sem_approved": 6,
    "Curricular_units_2nd_sem_grade": 14.2,
    "Unemployment_rate": 8.1,
    "GDP": 1.8
  }'
```

### Response Format
```json
{
  "prediction": "Graduate",
  "prediction_numeric": 1,
  "confidence": {
    "dropout": 25.3,
    "graduate": 74.7
  },
  "input_data": { ... },
  "processed_features": { ... }
}
```

## 🔧 Environment Variables

Heroku automatically provides:
- `PORT`: Server port (handled automatically)
- `FLASK_ENV`: Set to 'production' for optimized performance

## 📈 Performance & Scaling

### Free Tier Capabilities
- **Memory**: 512MB RAM (sufficient for ML model)
- **CPU**: Shared (adequate for moderate traffic)
- **Sleep Mode**: App sleeps after 30min inactivity
- **Hours**: 550 free dyno hours/month

### Scaling Options
```bash
# Scale to multiple instances
heroku ps:scale web=2

# Upgrade to paid tier for always-on
heroku addons:create heroku-postgresql:hobby-dev
```

## 🐛 Troubleshooting

### Common Issues

**Build Failed**:
```bash
# Check build logs
heroku logs --tail

# Common fixes
git add .
git commit -m "Fix build"
git push heroku main
```

**Memory Issues**:
- Upgrade to hobby tier: $7/month
- Optimize model loading in `app.py`

**Timeout Issues**:
- Model loading takes ~30s on first request
- Subsequent requests are fast (~100ms)

### Useful Commands
```bash
# View logs
heroku logs --tail

# Restart app
heroku restart

# Run commands
heroku run python --version

# Check dyno status
heroku ps
```

## 🎉 Advantages of Heroku

✅ **Full ML Environment**: Complete scikit-learn + pandas support  
✅ **Real Model**: Uses actual `random_forest_model.pkl`  
✅ **Easy Deployment**: Git-based deployment workflow  
✅ **Automatic HTTPS**: SSL certificates included  
✅ **Monitoring**: Built-in logs and metrics  
✅ **Scalability**: Easy to scale up when needed  
✅ **No Configuration**: Works out of the box  

## 🔗 Resources

- **Heroku Dev Center**: https://devcenter.heroku.com/
- **Python on Heroku**: https://devcenter.heroku.com/categories/python
- **Flask Deployment**: https://devcenter.heroku.com/articles/getting-started-with-python

---

**Your ML-powered student dropout prediction system is ready for production on Heroku! 🚀**