import sqlite3
from random import choices
from string import ascii_letters, digits

from bcrypt import gensalt, hashpw
from flask import g

CHARACTERS = ascii_letters + digits

DATABASE_PATH = "database.db"


def get_conn():
    if not hasattr(g, "db"):
        g.db = sqlite3.connect(DATABASE_PATH)
    return g.db


def init_db_command():
    """Clear the existing data and create new tables."""
    db = sqlite3.connect(DATABASE_PATH)
    with open("schema.sql") as f:
        db.executescript(f.read())
    db.commit()

    credentials = [
        "admin",
        "".join(choices(CHARACTERS, k=10)),
        "admin@example.com",
    ]
    print("Username: {}, Password: {}".format(*credentials))
    credentials[1] = hashpw(credentials[1].encode("utf-8"), gensalt()).decode()
    db.execute(
        "insert into users (username, password, email) values (?, ?, ?)",
        credentials,
    )
    db.commit()

    print("Database initialized.")


if __name__ == "__main__":
    init_db_command()
