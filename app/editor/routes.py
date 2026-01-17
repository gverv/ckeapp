# app/editor/routes.py

import os
from flask import (
    render_template, redirect, url_for,
    flash, request, abort, current_app
)
from flask_login import login_required, current_user
from werkzeug.utils import secure_filename

from app.extensions import db, ckeditor
from app.models.article import Article
from app.utils.permissions import can_create_article, can_edit_article
from app.utils.decorators import role_required
from app.utils.logs import log_action

from . import editor_bp

@editor_bp.route("/articles")
def articles():
    articles = Article.query.order_by(Article.created_at.desc()).all()
    return render_template("editor/articles/index.html", articles=articles)


@editor_bp.route("/articles/create", methods=["GET", "POST"])
@login_required
@role_required("editor", "admin")
def create_article():
    if request.method == "POST":
        article = Article(
            title=request.form["title"],
            body=request.form["body"],
            author_id=current_user.id
        )
        db.session.add(article)
        db.session.commit()

        log_action("created article")

        flash("Το άρθρο δημιουργήθηκε", "success")
        return redirect(url_for("editor.articles"))

    return render_template("editor/articles/create.html")




@editor_bp.route("/articles/<int:id>/edit", methods=["GET", "POST"])
@login_required
def edit_article(id):
    article = Article.query.get_or_404(id)

    if not can_edit_article(article):
        abort(403)

    if request.method == "POST":
        article.title = request.form["title"]
        article.body = request.form["body"]
        db.session.commit()

        log_action(f"edited article {id}")

        flash("Το άρθρο ενημερώθηκε", "success")
        return redirect(url_for("editor.articles"))

    return render_template(
        "editor/articles/edit.html",
        article=article
    )



@editor_bp.route("/upload", methods=["POST"])
@login_required
@role_required("editor", "admin")
def upload():
    f = request.files.get("upload")

    if not f:
        abort(400)

    ext = f.filename.rsplit(".", 1)[-1].lower()
    if ext not in current_app.config["ALLOWED_IMAGE_EXTENSIONS"]:
        abort(400)

    filename = secure_filename(f.filename)

    upload_path = os.path.join(
        current_app.config["UPLOAD_FOLDER"],
        current_app.config["CKEDITOR_UPLOAD_PATH"]
    )

    os.makedirs(upload_path, exist_ok=True)

    filepath = os.path.join(upload_path, filename)
    f.save(filepath)

    url = url_for(
        "static",
        filename=f"../instance/uploads/ckeditor/{filename}"
    )

    return {
        "uploaded": 1,
        "fileName": filename,
        "url": url
    }
