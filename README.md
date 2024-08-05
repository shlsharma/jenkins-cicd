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

# Installation of Jenkins

```bash
curl -fsSL https://pkg.jenkins.io/debian-stable/jenkins.io-2023.key | sudo tee \
  /usr/share/keyrings/jenkins-keyring.asc > /dev/null
echo deb [signed-by=/usr/share/keyrings/jenkins-keyring.asc] \
  https://pkg.jenkins.io/debian-stable binary/ | sudo tee \
  /etc/apt/sources.list.d/jenkins.list > /dev/null
sudo apt-get update
sudo apt-get install jenkins

sudo apt update
sudo apt install fontconfig openjdk-17-jre
java -version

sudo systemctl enable jenkins
sudo systemctl start jenkins
sudo systemctl status jenkins
```

`
sudo cat /var/lib/jenkins/secrets/initialAdminPassword
`

```bash
# Add Docker's official GPG key:
sudo apt-get update
sudo apt-get install ca-certificates curl gnupg
sudo install -m 0755 -d /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
sudo chmod a+r /etc/apt/keyrings/docker.gpg

# Add the repository to Apt sources:
for pkg in docker.io docker-doc docker-compose podman-docker containerd runc; do sudo apt-get remove $pkg; done

echo \
  "deb [arch="$(dpkg --print-architecture)" signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu \
  "$(. /etc/os-release && echo "$VERSION_CODENAME")" stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt-get update
sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin

sudo usermod -a -G docker jenkins
sudo usermod -a -G docker $USER

```

# Admin password Jenkins

`sudo cat /var/lib/jenkins/secrets/initialAdminPassword`

# Payload URL format in github repo webhook

`http://<public-ipv4 address>:8080/github-webhook/` #replace it with ur own public-ipv4 address

```

# Additional Improvements

docker remove $(docker ps -a -q)
docker images --format "{{.ID}} {{.CreatedAt}}" | sort -rk 2 | awk 'NR==1{print $1}'



# Create Stage Branch
`git checkout -b staging`
`git push `


