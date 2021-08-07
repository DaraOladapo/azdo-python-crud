from flask import render_template, url_for, redirect, request
from application import app, db
from application.models import Students
from application.forms import AddStudentForm


@app.route('/')
def index():
    students = Students.query.all()
    return render_template('index.html', title="Students", students=students)

@app.route('/add', methods=['POST', 'GET'])
def add():
    form = AddStudentForm()
    if request.method=="POST":
        student = Students(
            first_name = form.first_name.data,
            last_name = form.last_name.data,
            email_address = form.email_address.data
        )
        print(student.first_name)
        print(student.last_name)
        print(student.email_address)
        db.session.add(student)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('add.html', title="Add new student", form=form)