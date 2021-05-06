Setup the database:

1- Install MS SQL Express.
2- Install MS SQL Server Management Studio 18.8.
3- Start SQL Server Management and connect to server (usually localhost\SQLEXPRESS)).
4- Open script.sql in SQL Server. This file located in the project's root directory.
5- Press 'Execute' in the top bar to create the database along with its tables
and populate the tables with values.
6- Make sure the database was properly created.

Setup Flask:
1- Open main.py in a text editor or IDE.
2- Modify the server name in the connection string to match the name of your server.
3- Save and close.
4- Open CMD as admin
5- cd into /proj430/scripts
6- Type 'activate' in CMD then press enter
7- cd back to the project's root directory
8- Run set FLASK_APP=main.py
9- Run set FLASK_ENV=development
10- Run python -m flask run
11- Open your browser at localhost:5000/login
