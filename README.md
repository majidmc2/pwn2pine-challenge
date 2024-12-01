## Introduction

**pwn2pine** is a web application designed for educational purposes to help users learn and practice web security. The project includes three challenges, each featuring the following vulnerabilities:

 - Prototype Pollution
 - JSONP
 - Server-Side Template Injection (SSTI)

Built using the Django framework, this project is ideal for security enthusiasts and penetration testers. It provides a safe environment to explore and better understand these web vulnerabilities.


## Run

```bash
$ python -m venv ven
$ source env/bin/activate
$ pip install -r requirements.txt
$ python manage.py runserver 0.0.0.0:8000
```