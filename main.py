import datetime
import json
from flask import Flask, render_template, redirect, url_for, request
from utils.forms import DataForm
from flask_bootstrap import Bootstrap
from utils.directory_helper import create_new_directory
from utils.patient_creator import Patient
from config.config import APP_SECRET_KEY


def create_app():
    """Creates a BootStrap wrapper"""
    app = Flask(__name__)
    Bootstrap(app)
    return app


app = create_app()
app.secret_key = APP_SECRET_KEY


@app.route("/", methods=["GET", "POST"])
def main_app():
    """
    Retrieves data from forms
    :return:
    """
    data_form = DataForm()
    if data_form.validate_on_submit():
        # retrive data from form as dict, and convert datetime objects to str
        data = {field.name: field.data if not type(field.data) == datetime.date else field.data.strftime("%d.%m.%Y") for
                field in data_form}
        del data["submit"]
        del data["csrf_token"]

        str_data = json.dumps(data, indent=4)  # dumps to json string

        return redirect(url_for("creating_files", str_data=str_data))  # route str_data to creating_files

    return render_template("forms.html", form=data_form)


@app.route("/creating_files", methods=["GET", "POST"])
def creating_files():
    """
    creates folder and makes all required files
    :return:
    """
    str_data = request.args.get("str_data")
    data = json.loads(str_data)

    # creates a folder
    folder_path = create_new_directory(data["name"])

    patient = Patient(**data, path=folder_path)
    patient.word_bed()
    patient.prescription_list()
    patient.worksheet_update()

    return f"Успех!", {"Refresh": "1; url=/"}


if __name__ == '__main__':
    app.run(
        debug=True
    )
