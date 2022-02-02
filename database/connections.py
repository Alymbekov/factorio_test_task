from distutils.command.config import config

from peewee import PostgresqlDatabase

user = config('DB_USER')
password = config('DB_PASSWORD')
db_name = config('DB_NAME')
host = config('DB_HOST')
port = config('DB_PORT')

db_handle = PostgresqlDatabase(
    db_name, user=user, password=password,
    host=host, port=port
)
