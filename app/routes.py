from flask import (
    Blueprint,
    render_template,
    send_from_directory,
    flash,
    redirect,
    url_for,
    current_app,
    request
)
from .forms import *

main = Blueprint('main', __name__)

@main.route("/test/static/<path:filename>", methods=["GET"])
def static_dir(filename):
    return send_from_directory(current_app.static_folder, filename)

@main.route("/test")
def index():
    return render_template("index.html")

@main.route("/test/formexample", methods=["GET", "POST"])
def formexample():
    form = ExampleForm()

    try:
        if request.method == "POST":
            if not form.validate_on_submit():
                raise Exception(get_error_str(form))
            flash('Success', 'info')
            redirect(url_for('main.index'))
    except Exception as e:
        flash(str(e), 'danger')
        print(e)

    return render_template("form.html", form=form)

