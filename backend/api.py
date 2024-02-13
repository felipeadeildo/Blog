from bcrypt import checkpw
from db import get_conn
from flask import Blueprint, request, session
from utils import login_required, message

bp = Blueprint("api", __name__, url_prefix="/api")


@bp.post("/login")
def login():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    if any(not x for x in (username, password)):
        return message("Missing credentials", 400)

    db = get_conn()
    user = db.execute(
        "select id, password from users where username = ?", (username,)
    ).fetchone()
    if user is None:
        return message("Username / password incorrect", 401)
    user_id, user_password = user
    if not checkpw(
        f"{password}".encode("utf-8"), user_password.encode("utf-8")
    ):
        return message("Username / password incorrect", 401)

    session["user_id"] = user_id
    return message("Success", 200)


@bp.get("/logout")
@login_required()
def logout():
    session.pop("user_id")
    return message("Success", 200)


@bp.get("/me")
@login_required()
def me():
    db = get_conn()
    user = db.execute(
        "select id, username, email from users where id = ?",
        (session["user_id"],),
    ).fetchone()
    return message(
        "Success",
        200,
        id=user[0],
        username=user[1],
        email=user[2],
    )


@bp.post("/post")
@login_required()
def create_post():
    data = request.get_json()
    title = data.get("title")
    content = data.get("content")
    banner = data.get("banner")

    if any(not x for x in (title, content, banner)):
        return message("Missing title or content", 400)

    db = get_conn()
    db.execute(
        "insert into posts (post_by_user_id, title, content, banner) values (?, ?, ?, ?)",
        (session["user_id"], title, content, banner),
    )
    db.commit()
    last_row_id = db.execute(
        "select last_insert_rowid() from posts"
    ).fetchone()[0]
    post = db.execute(
        "select posts.id, posts.title, posts.content, posts.banner, users.id, users.username, users.email from posts join users on posts.post_by_user_id = users.id where posts.id = ?",
        (last_row_id,),
    ).fetchone()

    return message(
        "Success",
        200,
        id=post[0],
        title=post[1],
        content=post[2],
        banner=post[3],
        user={
            "id": post[4],
            "username": post[5],
            "email": post[6],
        },
    )


@bp.get("/post")
@login_required()
def get_posts():
    db = get_conn()
    post_by = request.args.get("post_by")
    if post_by:
        user_id = db.execute(
            "select id from users where username = ?", (post_by,)
        ).fetchone()
        if not user_id:
            return message("User not found", 404)
        user_id = user_id[0]
        posts = db.execute(
            "select id, title, content, banner from posts where post_by_user_id = ?",
            (user_id,),
        ).fetchall()
    else:
        posts = db.execute(
            "select posts.id, posts.title, posts.content, posts.banner, users.id, users.username, users.email from posts join users on posts.post_by_user_id = users.id"
        ).fetchall()

    return message(
        "Success",
        200,
        posts=[
            {
                "id": x[0],
                "title": x[1],
                "content": x[2],
                "banner": x[3],
                "user": {"id": x[4], "username": x[5], "email": x[6]},
            }
            for x in posts
        ],
    )
