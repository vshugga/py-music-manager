from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import InputRequired

class ExampleForm(FlaskForm):
    example_input = StringField("Example input", [InputRequired("Input required")])
    example_submit = SubmitField()


def get_error_str(form):
    '''Returns string in format: [Field label]: [error 1, error 2...]; [other errors...]'''
    errs = [f"{getattr(form, f).label.text}: {', '.join(m)}" for f, m in form.errors.items()]
    return "; ".join(errs)
