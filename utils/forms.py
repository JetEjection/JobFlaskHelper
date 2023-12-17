from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, DateField, SelectField, ValidationError
from wtforms.validators import DataRequired
from config.config import DOCTORS_LIST, DEPARTMENTS_LIST

DOCTORS = DOCTORS_LIST
DEPARTMENTS = DEPARTMENTS_LIST


class DataForm(FlaskForm):
    name = StringField(label="ФИО", validators=[DataRequired()])
    birthday = DateField(label="Дата Рождения")
    history = StringField(label="История Болезни")
    department = SelectField(label="Отделение", choices=DEPARTMENTS)
    hospitalisation_date = DateField(label="Дата Поступления В Стационар")
    diagnosis_main = StringField(label="Основной Диагноз")
    operation = StringField(label="Операция")
    operation_date = DateField(label="Дата Операции")
    diagnosis_secondary = StringField(label="Сопуствующие Заболевания")
    icu_date = DateField(label="Дата Поступления в ОРИТ")
    doctor = SelectField(label="Врач", choices=DOCTORS)
    submit = SubmitField(label="Создать")
