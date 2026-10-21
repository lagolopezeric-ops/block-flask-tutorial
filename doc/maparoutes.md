# `__init__.py`

| Endpoint | Método |
|---|---|
| `/hello` | GET |
| `/` | GET |

# `auth.py`

| Endpoint | Método |
|---|---|
| `/auth/register` | GET, POST |
| `/auth/login` | GET, POST |
| `/auth/logout` | GET |

# `blog.py`

| Endpoint | Método |
|---|---|
| `/` | GET |
| `/create` | GET, POST |
| `/<int:id>/update` | GET, POST |
| `/<int:id>/delete` | POST |