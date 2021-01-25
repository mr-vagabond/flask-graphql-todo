from datetime import datetime

from ariadne import convert_kwargs_to_snake_case

from api import db
from api.models.todo import Todo


@convert_kwargs_to_snake_case
def resolve_create_todo(obj, info, description, due_date):
    try:
        due_date = datetime.strptime(due_date, "%d-%m-%Y").date()
        todo = Todo(description=description, due_date=due_date)
        db.session.add(todo)
        db.session.commit()
        payload = {"success": True, "todo": todo.to_dict()}
    except ValueError:  # date format errors
        payload = {
            "success": False,
            "errors": [
                f"Incorrect date format provided. Date should be in "
                f"the format dd-mm-yyyy"
            ],
        }

    return payload


@convert_kwargs_to_snake_case
def resolve_mark_done(obj, info, todo_id):
    try:
        update_todo = Todo.query.get(todo_id)
        update_todo.completed = not update_todo.completed
        db.session.add(update_todo)
        db.session.commit()

        payload = {"success": True, "todo": update_todo.to_dict()}

    except AttributeError:
        payload = {
            "success": False,
            "errors": [f"Todo matching id {todo_id} was not found!"],
        }

    return payload


@convert_kwargs_to_snake_case
def resolve_delete_todo(obj, info, todo_id):
    try:
        delete_todo = Todo.query.get(todo_id)
        if delete_todo:
            db.session.delete(delete_todo)
            db.session.commit()

        payload = {"success": True, "todo": delete_todo.to_dict()}

    except AttributeError:
        payload = {
            "success": False,
            "errors": [f"Todo matching id {todo_id} was not found!"],
        }

    return payload


@convert_kwargs_to_snake_case
def resolve_update_due_date(obj, info, todo_id, new_date):
    try:
        update_todo = Todo.query.get(todo_id)
        if update_todo:
            update_todo.due_date = datetime.strptime(new_date, "%d-%m-%Y").date()
        db.session.add(update_todo)
        db.session.commit()

        payload = {"success": True, "todo": update_todo.to_dict()}

    except AttributeError:
        payload = {
            "success": False,
            "errors": [f"Todo matching id {todo_id} was not found!"],
        }

    return payload