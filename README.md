# Email-Verification-System<br>
A simple email verification system using flask<br>
Requirements:
You can install sqlite3 using the command
```python
pip install sqlite3
```
You can install Flask using the command
```python
pip install flask
```
You can install Flask_mail using the command
``` python
pip install Flask-Mail
```

You need to create database using sqlite3
```python
import sqlite3
conn = sqlite3.connect('sample.db')
conn.execute('Create table validate(Email email,ph number(10))')
```
