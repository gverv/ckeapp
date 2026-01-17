# app/utils/permissions.py

from flask import abort, redirect, url_for
from flask_login import current_user

def can_comment():
    return current_user.is_authenticated

def can_edit_comment(comment):
    return (
        current_user.is_admin()
        or comment.user_id == current_user.id
    )

def can_create_article():
    return current_user.is_editor() or current_user.is_admin()

def can_edit_article(article):
    return (
        current_user.is_admin()
        or article.author_id == current_user.id
    )

def editor_protected():
    if not current_user.is_authenticated:
        return redirect(url_for("auth.login"))
    if not current_user.is_editor():
        abort(403)
