# Implementaion of GraphQL using Flask

## Usage

### Requirements  

* Python 3
* Pip3
* Virtualenv

1. ### Creating a virtual env  

    

``` shell
    python3 -m virtualenv .venv
```

2. ### Installing Requirements  

    

``` bash
    # activate virtualenv
    source .venv/bin/activate # for windows `.venv/Scripts/activate.ps1`
    python -m pip install poetry
    python -m poetry install
```

3. ### Setting up environment variables

    setup the following as your environment variables

    

``` shell
    FLASK_APP=main.py
    FLASK_DEBUG=1
    FLASK_ENV=development
```

4. ### Runninig the app

    

``` hell
    flask run
```

## App demonstaration

1. Navigate to `/graphql` endpoint to run playground testing

**Example commands**

* Retrieve all todos with id 1

``` graphql
    query fetchTodos {
      todo(todoId: "1") {
        success
        errors
        todo { id completed description dueDate }
      }
    }
```

* Retrieve todo with id 1

    

``` graphql
    query fetchTodo {
      todo(todoId: "1") {
        success
        errors
        todo { id completed description dueDate }
      }
    }
```

* Create todo

``` graphql
    mutation newTodo {
      createTodo(description:"Go to the dentist", dueDate:"24-10-2020") {
        success
        errors
        todo {
          id
          completed
          description
        }
      }
    }
```

* Delete todo with id 1

``` graphql
    mutation {
          deleteTodo(todoId: "1") {
            success
            errors
          }
    }
```

* Update todo dueDate

``` graphql
    mutation updateDueDate {
      updateDueDate(todoId: "2", newDate: "25-10-2020") {
        success
        errors
      }
    }
```

## References

[Twilio: graphql-api-python-flask](https://www.twilio.com/blog/graphql-api-python-flask-ariadne)
