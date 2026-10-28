classDiagram
    direction TB

    class InitPy {
        <<file: __init__.py>>
        +create_app(test_config)
        +hello()
    }

    class auth {
        <<Blueprint>>
        +register() : View
        +login() : View
        +logout() : View
        +load_logged_in_user() : Function
        +login_required(view) : Decorator
    }

    class blog {
        <<Blueprint>>
        +index() : View
        +create() : View
        +update(id) : View
        +delete(id) : View
        +get_post(id, check_author) : Post
    }

    class db {
        <<Mòdul>>
        +get_db() : sqlite3.Connection
        +close_db() : None
        +init_db() : None
        +init_db_command() : CLI Command
    }

    class User {
        +INTEGER id PK
        +TEXT username UNIQUE
        +TEXT password
    }

    class Post {
        +INTEGER id PK
        +INTEGER author_id FK
        +TIMESTAMP created
        +TEXT title
        +TEXT body
    }

    InitPy --> db : db.init_app(app)
    InitPy --> auth : registra blueprint
    InitPy --> blog : registra blueprint
    auth --> db : get_db()
    blog --> db : get_db()
    blog ..> Post : utilitza / modifica
    User "1" --> "*" Post : author_id