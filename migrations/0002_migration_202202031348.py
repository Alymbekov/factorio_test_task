# auto-generated snapshot
from peewee import *
import datetime
import peewee


snapshot = Snapshot()


@snapshot.append
class Author(peewee.Model):
    id = PrimaryKeyField(primary_key=True)
    author = CharField(max_length=255)
    favorites = IntegerField(default=0)
    created_at = CharField(max_length=100, null=True)
    updated_at = CharField(max_length=100, null=True)
    class Meta:
        table_name = "authors"


@snapshot.append
class Information(peewee.Model):
    id = PrimaryKeyField(primary_key=True)
    body = TextField(null=True)
    blue_print_string = TextField(null=True)
    image = CharField(max_length=255, null=True)
    author = snapshot.ForeignKeyField(backref='fk_author_info', index=True, model='author', on_delete='cascade', on_update='cascade')
    class Meta:
        table_name = "informations"


