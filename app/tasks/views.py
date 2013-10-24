from flask import Blueprint
from flask import render_template, request, redirect, url_for
from app import db
from .models import Task
from .forms import CreateTaskForm

tasks = Blueprint('tasks', __name__, url_prefix='/tasks')

@tasks.route('/', methods=['GET', 'POST'])
def index():
    form = CreateTaskForm()
    if request.method == 'POST' and form.validate_on_submit():
        # Add the entry to Database
        task = Task()
        task.title = form.title.data
        task.description = form.description.data
        db.session.add(task)
        db.session.commit() # One commit after you insert into all the tables
    tasks = Task.query.all()
    return render_template('tasks/index.html', tasks=tasks, form=form)


@tasks.route('/delete/<int:task_id>', methods=['POST'])
def delete(task_id):
    task = Task.query.get_or_404(task_id)
    db.session.delete(task)
    db.session.commit()
    return redirect(url_for('.index'))
