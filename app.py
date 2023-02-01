# write a python code create a flask apps using flask_sqlalchemy to connect postgresql create a new database with name "mydatabase", a new table with name "mytable", insert data to table "mytable", query table
# using createDb.py to create database "mydatabase"
# cd  C:\Users\a2907\Desktop\pyApp\DeepLearning\Render\app_flask_postgresSql>
# flask run
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:3050Pony$@LAPTOP-MNOVF25E/mydatabase' ??????????
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:3050Pony$@localhost/mydatabase'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://stevegau:pCdaBZ1ehnzaSkF4sQFYgPRWQSWoVl6x@dpg-cfc9gbun6mpiero1lsbg-a.ohio-postgres.render.com/students_0h01'
db = SQLAlchemy(app)

class MyTable(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    age = db.Column(db.Integer, nullable=False)

@app.route('/')
def insert_data():
    # Insert data into the table
    data = MyTable(name='John02', age=32)
    db.session.add(data)
    db.session.commit()
    #
    # Query the table
    results = MyTable.query.all()
    for result in results:
        print(result.id, result.name, result.age)
    return str(results)
'''
@app.route('/')
def query_data():
    # Query the table
    results = MyTable.query.all()
    for result in results:
        print(result.id, result.name, result.age)
    return str(results)
'''

if __name__ == '__main__':
    with app.app_context():
        insert_data()
        # query_data()
        app.run()

