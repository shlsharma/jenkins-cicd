# CI-CD
CI/CD Pipeline with Jenkins

```python
python -m venv jenkins-env
source jenkins-env/bin/activate
pip install -r requirements.txt
pip install .
```

1. gunicorn is required to expose the local system to internet
2. uvicorn is required to deploy the fastapi application

```json
Test Data
{
  "Gender": "Male",
  "Married": "No",
  "Dependents": "2",
  "Education": "Graduate",
  "Self_Employed": "No",
  "ApplicantIncome": 5849,
  "CoapplicantIncome": 0,
  "LoanAmount": 1000,
  "Loan_Amount_Term": 1,
  "Credit_History": "1.0",
  "Property_Area": "Rural"
}
```

# Docker Commands

docker build -t shlsharma/cicd:v1 .

docker run -d -it --name modelv1 -p 8005:8005 shlsharma/cicd:v1 bash

docker exec modelv1 python prediction_model/training_pipeline.py

docker exec modelv1 pytest -v --junitxml TestResults.xml --cache-clear

docker cp modelv1:/code/src/TestResults.xml .

docker exec -d -w /code modelv1 python main.py

docker exec -d -w /code modelv1 uvicorn main:app --proxy-headers --host 0.0.0.0 --port 8005

# Jenkins 
1. Launch ubuntu server with port 8080 (jenkins server is assesbile here) & 8005 availability
2. Install Jenkins
3. Install Docker Service
4. Validation of Installation 