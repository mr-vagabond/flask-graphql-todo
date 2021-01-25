from datetime import datetime

from ariadne import convert_kwargs_to_snake_case

from api.models.todo import Todo


def resolve_todos(obj, info):
    """
    GrapghQL resolver. Resolves queries made for TODO

    To know more about resolvers:
    https://medium.com/paypal-engineering/graphql-resolvers-best-practices-cd36fdbcef55

    Parameters
    ----
    obj ():
    info ():


    Returns
    ----
    dict: A dictionary containing {success, errors, todos}
    """
    try:
        todos = [todo.to_dict() for todo in Todo.query.all()]
        payload = {"success": True, "todos": todos}
    except Exception as error:
        payload = {"success": False, "errors": [str(error)]}

    return payload


@convert_kwargs_to_snake_case
def resolve_todo(obj, info, todo_id):
    try:
        todo = Todo.query.get(todo_id)
        payload = {"success": True, "todo": todo.to_dict()}
    except AttributeError:
        payload = {
            "success": False,
            "errors": [f"Todo item with id {todo_id} not found"],
        }

    return payload
