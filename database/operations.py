from database.connections import db_handle
from database.models import Author, Information


def add_author(author):
    author_name = author.get('Author')
    created = author.get('Created')
    updated = author.get('LastUpdated')
    favorites = author.get('Favorites')
    with db_handle.atomic():
        author = Author(
            author=author_name,
            favorites=favorites,
            created_at=created,
            updated_at=updated
        )
        author.save()
        return author


def add_information(information, blue_print_string, file_path, author):
    with db_handle.atomic():
        info = Information(
            body=information,
            blue_print_string=blue_print_string,
            author=author,
            image=file_path
        )
        info.save()


def get_information(skip: int = 0, limit: int = 100):
    return list(Information.select().offset(skip).limit(limit))


def get_authors(skip: int = 0, limit: int = 100):
    return list(Author.select().offset(skip).limit(limit))

