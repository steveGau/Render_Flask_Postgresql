from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
import gunicorn
#
app = Flask(__name__)
#
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://stevegau:pCdaBZ1ehnzaSkF4sQFYgPRWQSWoVl6x@dpg-cfc9gbun6mpiero1lsbg-a.ohio-postgres.render.com:1000/students_0h01'
#
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
    print(studentsOutputData)
    return str(studentsOutputData)
#
if __name__ == '__main__':
    with app.app_context():
        index()
        # app.run(port=1000)
        app.run()

# export FLASK_RUN_PORT=1000; flask run
'''
method 1: in app.py (not work)
    app.run(port=1000)

method 2: in render, deploy (not work)
    flask run --port=1000

methos 3: in render, deploy (not work)
    #!/bin/bash
    export FLASK_RUN_PORT=1000
    flask run
    # run_flask.sh
    # chmod +x run_flask.sh
    # ./run_flask.sh

methos 3: in render env and deploy
    set enviroment for connection in render, add
        DATABASE_URL=postgresql://stevegau:pCdaBZ1ehnzaSkF4sQFYgPRWQSWoVl6x@dpg-cfc9gbun6mpiero1lsbg-a/students_0h01
    gunicorn app:app
'''
