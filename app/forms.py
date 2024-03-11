from flask_wtf import FlaskForm
from wtforms import BooleanField, StringField, TextField, TextAreaField, PasswordField
from wtforms.validators import Length, DataRequired, InputRequired, EqualTo, Email, url
from flask_babel import lazy_gettext

class RegistrationForm(FlaskForm):
    username = TextField(lazy_gettext('Username'), [Length(min=4, max=25, message=lazy_gettext("Your username should have between 4 and 25 characters."))])
    email = StringField(lazy_gettext('Email Address'), [DataRequired(), Email()])
    password = PasswordField(lazy_gettext('New Password'), [DataRequired(), Length(min=6, max=20, message=lazy_gettext("Your password should have between 6 and 20 characters.")), EqualTo('confirm', message=lazy_gettext('Passwords must match'))])
    confirm = PasswordField(lazy_gettext('Repeat Password'))
    accept_tos = BooleanField(lazy_gettext('I accept the TOS and Privacy statement'), [DataRequired()])

class LoginForm(FlaskForm):
    email = StringField(lazy_gettext('Email Address'), [DataRequired(), Email()])
    password = PasswordField(lazy_gettext('Password'), [DataRequired(), Length(min=6, max=20, message=lazy_gettext("Your password should have between 6 and 20 characters."))])

class PasswordForgottenForm(FlaskForm):
    email = StringField(lazy_gettext('Email Address'), [DataRequired(), Email()])

class PasswordChangeForm(FlaskForm):
    password = PasswordField(lazy_gettext('New Password'), [DataRequired(), Length(min=6, max=20, message=lazy_gettext("Your password should have between 6 and 20 characters.")), EqualTo('confirm', message=lazy_gettext('Passwords must match'))])
    confirm = PasswordField(lazy_gettext('Repeat Password'))

class IndexerForm(FlaskForm):
    url = StringField(lazy_gettext('The url to index'), [DataRequired(), url()])
    theme = TextField(lazy_gettext('Theme'), [DataRequired(), Length(max=50)])
    note = TextField(lazy_gettext('Optional note'), [Length(max=100)])
    accept_tos = BooleanField(lazy_gettext('I confirm that my suggestion does not contravene the Terms of Service'), [DataRequired()])

class ManualEntryForm(FlaskForm):
    title = TextField(lazy_gettext('A title for your entry'), [DataRequired(), Length(min=8, max=100, message=lazy_gettext("The title of your entry should have between 4 and 100 characters."))])
    description = TextAreaField(lazy_gettext('Description'), [DataRequired(), Length(max=200)])
    accept_tos = BooleanField(lazy_gettext('I confirm that my entry does not contravene the Terms of Service'), [DataRequired()])

class ReportingForm(FlaskForm):
    url = StringField(lazy_gettext('The url you are reporting'), [DataRequired(), url()])
    report = TextAreaField(lazy_gettext('Description of the issue'), [DataRequired(), Length(max=300)])
    accept_tos = BooleanField(lazy_gettext('I confirm that I may be contacted in relation to my report.'), [DataRequired()])

class AnnotationForm(FlaskForm):
    url = StringField(lazy_gettext('The url you wish to annotate'), [DataRequired(), url()])
    note = TextAreaField(lazy_gettext('Your note'), [DataRequired(), Length(max=300)])
    accept_tos = BooleanField(lazy_gettext('I confirm that my comment can be openly published.'), [DataRequired()])
