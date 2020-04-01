Task for remote probation work
==============================

Requirements
------------
* Python v3.8.2

Getting started
---------------
```
python manage.py collectstatic
python manage.py runserver
```

Demo datas are shipped with a SQLite database. 

There is 4 users, 1 Admin and 3 Employees.
Some projects and time entries are already created mainly on Employee_1 and Employee_2
Admin can access both on front on admin side

* Front side `http://127.0.0.1:8000/`
* Admin side `http://127.0.0.1:8000/admin/`

### Authentication 
```
Admin // test12345 
Employee_1 // test12345 
Employee_2 // test12345 
Employee_3 // test12345 
```

Librairies Used
---------------
* Django v3
* Vue.js v2
* moment.js
* bootstrap v4

