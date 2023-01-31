# write a python code to create flask app under render.com, Configure flask for PostgreSQL in web host render.com to connect to PostgreSQL, create a table with name "students", insert data to the table , query the data base
#
# cd  C:\Users\a2907\Desktop\pyApp\DeepLearning\Render\app_flask_postgresSql
#
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
# import psycopg2
# from psycopg2 import extensions
#
app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://username:password@hostname/dbname'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://stevegau:pCdaBZ1ehnzaSkF4sQFYgPRWQSWoVl6x@dpg-cfc9gbun6mpiero1lsbg-a.ohio-postgres.render.com/students_0h01'
db = SQLAlchemy(app)
#
class StudentTable(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    age = db.Column(db.Integer, nullable=False)
	#
    def __repr__(self):
        return '<StudentTable %r>' % self.name
#
@app.route('/')
def index():
    studentInputData = StudentTable(name='John Doe', age=25)
    db.session.add(studentInputData)
    db.session.commit()
    studentsOutputData = StudentTable.query.all()
    return str(studentsOutputData)
#
if __name__ == '__main__':
    db.create_all()
    app.run()
    