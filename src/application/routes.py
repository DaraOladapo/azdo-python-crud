from flask import render_template, url_for, redirect, request
from application import app, db
from application.models import Students
from application.forms import AddStudentForm, UpdateStudentForm

#create
@app.route('/add', methods=['POST', 'GET'])
def add():
    form = AddStudentForm()
    if request.method=="POST":
        student = Students(
            first_name = form.first_name.data,
            last_name = form.last_name.data,
            email_address = form.email_address.data
        )
        db.session.add(student)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('add.html', title="Add new student", form=form)

#read   
@app.route('/')
def index():
    students = Students.query.all()
    return render_template('index.html', title="Students", students=students)

@app.route('/details/<int:id>')
def details(id):
    student = Students.query.get(id)
    return render_template('details.html', title=student.first_name, student=student)

#update    
@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    form = UpdateStudentForm()
    student = Students.query.get(id)
    if form.validate_on_submit():
        student.first_name = form.first_name.data
        student.last_name = form.last_name.data
        student.email_address = form.email_address.data
        db.session.commit()
        redirect(url_for('index'))
    elif request.method == 'GET':
        form.first_name.data = student.first_name
        form.last_name.data = student.last_name
        form.email_address.data = student.email_address
    return render_template('update.html', title='Update student details', form=form)

#delete
@app.route('/delete/<int:id>')
def delete(id):
    student = Students.query.get(id)
    db.session.delete(student)
    db.session.commit()
    return redirect(url_for('index'))