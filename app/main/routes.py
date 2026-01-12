# app/main/routes.py

import os
from flask import request, abort, render_template
from werkzeug.utils import secure_filename
from flask_login import login_required
from app import Config
from . import main_bp
from . import main_bp

@main_bp.route('/')
def index():
    return render_template('main/index.html')

@main_bp.route("/upload-image", methods=["POST"])
@login_required
def upload_image():
    f = request.files.get("upload")
    if not f:
        abort(400)
    ext = f.filename.rsplit(".", 1)[-1].lower()
    if ext not in {"png", "jpg", "jpeg", "gif"}:
        abort(403)
    filename = secure_filename(f.filename)
    path = os.path.join("instance/uploads", filename)
    f.save(path)
    return {
        "uploaded": True,
        "url": f"/{path}"
    }

@main_bp.route("/maintenance")
def maintenance():
    return render_template("main/maintenance.html"), 503

##################

@main_bp.route('/about')
def about():
    return render_template('main/about.html')

@main_bp.route('/contact')
def contact():
    return render_template('main/contact.html')

@main_bp.route('/services')
def services():
    return render_template('main/services.html')

@main_bp.route('/faq')
def faq():
    return render_template('main/faq.html')

@main_bp.route('/blog')
def blog():
    return render_template('main/blog.html')

@main_bp.route('/blog/<int:post_id>')
def blog_post(post_id):
    return render_template('main/blog_post.html', post_id=post_id)

@main_bp.route('/testimonials')
def testimonials():
    return render_template('main/testimonials.html')

