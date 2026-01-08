# app/main/routes.py
from flask import render_template
from . import main_bp

@main_bp.route('/')
def index():
    return render_template('main/index.html')

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

