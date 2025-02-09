# Generic single-database configuration.

provide simple documentation for using alembic

## reference

[tutorial](https://alembic.sqlalchemy.org/en/latest/tutorial.html)

## usage

creating a new revison

```sh
alembic revision -m "create accounts table"
```

applying a new revision

```sh
alembic upgrade head
```

downgrade last revision

```sh
alembic downgrade -1
```
