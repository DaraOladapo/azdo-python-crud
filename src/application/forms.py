from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SubmitField, SelectField
from wtforms.validators import DataRequired, ValidationError

from application.models import Students

class AddStudentForm(FlaskForm):
    first_name = StringField('First Name', validators = [DataRequired()])
    last_name=StringField('Last Name', validators = [DataRequired()])
    email_address=StringField('Email Address', validators = [DataRequired()])
    submit = SubmitField('Submit')

    def validate_task(self, task):
        students = Students.query.all()
        for student in students:
            if student.first_name == first_name.data and student.last_name==last_name.data and student.email_address==email_address:
                raise ValidationError('You already added this student')