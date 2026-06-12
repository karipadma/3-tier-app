# Employee Management Portal

## Project Overview

This project is a 3-Tier Web Application deployed on AWS.

### Architecture

User Browser → Frontend EC2 (Nginx) → Backend EC2 (Flask API) → RDS MySQL

### Components

* Frontend Server: HTML, CSS, JavaScript, Nginx
* Backend Server: Python Flask REST APIs
* Database: Amazon RDS MySQL
* Cloud Platform: AWS

---

## Features

* Add Employee
* View Employees
* Update Employee
* Delete Employee
* Health Check Endpoint
* Environment Variable Configuration
* MySQL Database Integration
* RESTful APIs

---

## AWS Architecture

### Frontend EC2

Responsibilities:

* Hosts UI
* Serves static files using Nginx
* Sends API requests to Backend EC2

### Backend EC2

Responsibilities:

* Runs Flask application
* Handles business logic
* Connects to RDS MySQL
* Provides REST APIs

### Amazon RDS MySQL

Responsibilities:

* Stores employee data
* Provides managed relational database service

---

## Database Setup

### Create Database

```sql
CREATE DATABASE companydb;
```

### Use Database

```sql
USE companydb;
```

### Create Employees Table

```sql
CREATE TABLE employees (
    id INT AUTO_INCREMENT PRIMARY KEY,
    fullname VARCHAR(100),
    email VARCHAR(100),
    department VARCHAR(100),
    salary DECIMAL(10,2),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

### Verify Table

```sql
SHOW TABLES;
```

---

## Backend Setup

### Install Dependencies

```bash
pip3 install -r requirements.txt
```

### requirements.txt

```text
Flask
PyMySQL
python-dotenv
flask-cors
gunicorn
```

### Environment Variables

Create `.env`

```text
DB_HOST=<RDS-ENDPOINT>
DB_PORT=3306
DB_USER=admin
DB_PASSWORD=<PASSWORD>
DB_NAME=companydb
```

### Run Application

```bash
python3 app.py
```

### Verify

```bash
curl http://localhost:5000/health
```

Expected Output:

```json
{
  "status":"UP"
}
```

---

## Frontend Setup

### Install Nginx

```bash
sudo yum install nginx -y
```

### Enable Nginx

```bash
sudo systemctl enable nginx
sudo systemctl start nginx
```

### Deploy UI

Copy files to:

```bash
/usr/share/nginx/html/
```

Access:

```text
http://<FRONTEND_PUBLIC_IP>
```

---

## API Endpoints

### Health Check

```http
GET /health
```

Response:

```json
{
  "status":"UP"
}
```

---

### Get All Employees

```http
GET /employees
```

Response:

```json
[
  {
    "id":1,
    "fullname":"Padma",
    "email":"padma@gmail.com",
    "department":"DevOps",
    "salary":"70000.00"
  }
]
```

---

### Get Employee By ID

```http
GET /employees/1
```

---

### Add Employee

```http
POST /employees
```

Request:

```json
{
  "fullname":"Padma",
  "email":"padma@gmail.com",
  "department":"DevOps",
  "salary":70000
}
```

---

### Update Employee

```http
PUT /employees/1
```

Request:

```json
{
  "fullname":"Padma Updated",
  "email":"padma@gmail.com",
  "department":"AWS",
  "salary":90000
}
```

---

### Delete Employee

```http
DELETE /employees/1
```

---

## Testing APIs

### Get Employees

```bash
curl http://localhost:5000/employees
```

### Add Employee

```bash
curl -X POST http://localhost:5000/employees \
-H "Content-Type: application/json" \
-d '{
"fullname":"Rahul",
"email":"rahul@gmail.com",
"department":"Cloud",
"salary":60000
}'
```

### Delete Employee

```bash
curl -X DELETE http://localhost:5000/employees/1
```

---

## Security Groups

### Frontend EC2

| Port | Purpose |
| ---- | ------- |
| 80   | HTTP    |
| 22   | SSH     |

### Backend EC2

| Port | Purpose   |
| ---- | --------- |
| 5000 | Flask API |
| 22   | SSH       |

### RDS MySQL

| Port | Purpose |
| ---- | ------- |
| 3306 | MySQL   |

---

## Troubleshooting

### Backend Not Running

```bash
curl http://localhost:5000/health
```

Error:

```text
curl: (7) Failed to connect
```

Solution:

```bash
python3 app.py
```

---

### Table Does Not Exist

Error:

```text
Table 'companydb.employees' doesn't exist
```

Solution:

```sql
CREATE TABLE employees (...);
```

---

### Database Connection Issues

Verify:

```bash
python3 test_db.py
```

Expected:

```text
Connected Successfully
```

---

## Future Enhancements

* Docker Containerization
* Jenkins CI/CD Pipeline
* Kubernetes Deployment
* Terraform Infrastructure as Code
* SSL using Nginx
* Application Monitoring with Prometheus and Grafana
* AWS Load Balancer Integration

---

## Author

Employee Management Portal

AWS | Linux | Python Flask | MySQL | Nginx | DevOps Project
