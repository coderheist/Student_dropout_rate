@echo off
echo Starting Student Dropout Prediction System...
echo.

echo [1/3] Starting Flask Backend...
cd backend
start "Flask Backend" cmd /k "python app.py"
cd ..

echo [2/3] Waiting for backend to initialize...
timeout /t 5 /nobreak > nul

echo [3/3] Starting Simple Frontend...
cd frontend-simple
start "Simple Frontend" cmd /k "python server.py"
cd ..

echo.
echo ===================================================
echo  Student Dropout Prediction System is starting!
echo ===================================================
echo  Backend:  http://localhost:5000
echo  Frontend: http://localhost:3000
echo  
echo  Both services are starting in separate windows.
echo  Please wait for them to fully load.
echo ===================================================
pause