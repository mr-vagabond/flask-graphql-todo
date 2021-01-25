# from main import app
# from flask import jsonify, request
# from ariadne.constants import PLAYGROUND_HTML
# from ariadne import graphql_sync


# @app.route("/")
# def hello():
#     return "Hello!"


# @app.route("/graphql", methods=["GET"])
# def graphql_playground():
#     return PLAYGROUND_HTML


# @app.route("/graphql", methods=["POST"])
# def graphql_server():
#     data = request.get_json()
#     success, result = graphql_sync(schema, data, context_value=request, debug=app.debug)
#     status_code = 200 if success else 400

#     return jsonify(result), status_code