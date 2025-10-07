@echo off
echo ============================================
echo  Student Dropout Prediction System
echo ============================================
echo.
echo Starting application components...
echo.

:: Check if Python is installed
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Error: Python is not installed or not in PATH
    echo Please install Python 3.8+ from https://python.org
    pause
    exit /b 1
)

:: Install required packages
echo Installing required Python packages...
pip install flask flask-cors pandas scikit-learn joblib numpy --quiet --user

:: Start backend server
echo.
echo Starting Flask backend server...
start "Backend Server" cmd /k "cd backend && python app.py"

:: Wait a moment for backend to start
timeout /t 3 /nobreak >nul

:: Start frontend server
echo Starting frontend server...
start "Frontend Server" cmd /k "cd frontend-simple && python -m http.server 8000"

:: Wait a moment for frontend to start
timeout /t 2 /nobreak >nul

:: Open the application in default browser
echo.
echo Opening application in browser...
timeout /t 2 /nobreak >nul
start http://localhost:8000

echo.
echo ============================================
echo  Application Started Successfully!
echo ============================================
echo  Frontend: http://localhost:8000
echo  Backend API: http://localhost:5000
echo ============================================
echo.
echo Press any key to close this window...
pause >nul