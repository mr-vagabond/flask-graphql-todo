from ariadne import (
    ObjectType,
    graphql_sync,
    load_schema_from_path,
    make_executable_schema,
    snake_case_fallback_resolvers,  # resolves camelCase to snake_case
)
from ariadne.constants import PLAYGROUND_HTML
from flask import jsonify, request

from api import app, db, models
from api.schemas.mutations import (
    resolve_create_todo,
    resolve_delete_todo,
    resolve_mark_done,
    resolve_update_due_date,
)
from api.schemas.queries import resolve_todo, resolve_todos

# Binding graphql schema to resolver

# QUERY
query = ObjectType("Query")
query.set_field("todos", resolve_todos)
query.set_field("todo", resolve_todo)

# MUTATION
mutation = ObjectType("Mutation")
mutation.set_field("createTodo", resolve_create_todo)
mutation.set_field("markDone", resolve_mark_done)
mutation.set_field("deleteTodo", resolve_delete_todo)
mutation.set_field("updateDueDate", resolve_update_due_date)

type_defs = load_schema_from_path("graphql-schema/schema.graphql")
schema = make_executable_schema(
    type_defs, query, mutation, snake_case_fallback_resolvers
)


@app.route("/")
def hello():
    return "Hello!"


@app.route("/graphql", methods=["GET"])
def graphql_playground():
    return PLAYGROUND_HTML


@app.route("/graphql", methods=["POST"])
def graphql_server():
    data = request.get_json()
    success, result = graphql_sync(schema, data, context_value=request, debug=app.debug)
    status_code = 200 if success else 400

    return jsonify(result), status_code