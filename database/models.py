from peewee import *
from database.base_model import BaseModel


class Author(BaseModel):
    id = PrimaryKeyField(null=False)
    author = CharField(max_length=255)
    favorites = IntegerField(default=0)
    created_at = CharField(max_length=100, null=True)
    updated_at = CharField(max_length=100, null=True)

    def __str__(self):
        return f'{self.id}, {self.author}'

    class Meta:
        db_table = "authors"
        order_by = ('author', )


class Information(BaseModel):
    id = PrimaryKeyField(null=False)
    body = TextField(null=True)
    blue_print_string = TextField(null=True)
    image = CharField(null=True, max_length=255)
    author = ForeignKeyField(Author, related_name='fk_author_info', to_field='id',
                             on_delete='cascade',
                             on_update='cascade')

    class Meta:
        db_table = "informations"
        order_by = ('author',)
