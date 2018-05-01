
del /s /q Win64
mkdir Win64 
cd Win64

cmake .. -G "Visual Studio 14 2015 Win64"
msbuild Isl.sln /t:Build /p:Configuration=Release
if %errorlevel% neq 0 goto :ERROR_
cd ..

python run_tests.py
if %errorlevel% neq 0 goto :ERROR
exit /b 0
:ERROR_
cd ..
:ERROR
ECHO FAILURE
exit /b %errorlevel%
