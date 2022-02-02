from peewee import *

from database.connections import db_handle


class BaseModel(Model):
    class Meta:
        database = db_handle
