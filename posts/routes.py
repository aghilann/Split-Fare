from flask import (render_template, url_for, flash, redirect, request, abort,
                   Blueprint)
from flask_login import current_user, login_required
from flaskblog import db
from flaskblog.models import Post
from posts.forms import PostForm, SearchForm

posts = Blueprint('posts', __name__)


@posts.route("/post/new", methods=['GET', 'POST'])
@login_required
def new_post():
    form = PostForm()
    if form.validate_on_submit():
        post = Post(title=form.title.data,
                    content=form.content.data,
                    date_time=form.date_time.data,
                    author=current_user)

        db.session.add(post)
        db.session.commit()

        flash('Your post has been created!', 'success')
        return redirect(url_for('main.home'))
    return render_template('create_post.html',
                           title='New Post',
                           form=form,
                           legend="New Post")


@posts.route("/post/<int:post_id>", methods=['GET', 'POST'])
def post(post_id):
    post = Post.query.get_or_404(post_id)
    return render_template('post.html', title=post.title, post=post)


@posts.route("/post/<int:post_id>/update", methods=['GET', 'POST'])
@login_required
def update_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user and current_user.username != "SUPERUSER":
        abort(403)
    form = PostForm()
    if form.validate_on_submit():
        post.title = form.title.data
        post.content = form.content.data
        post.date_time = form.date_time.data
        db.session.commit()
        flash('Your post has been updated!', 'success')
        return redirect(url_for('posts.post', post_id=post.id))
    elif request.method == 'GET':
        form.title.data = post.title
        form.content.data = post.content
        form.date_time.data = post.date_time
    return render_template('create_post.html',
                           title='Update Post',
                           form=form,
                           legend='Update Post')


@posts.route("/post/<int:post_id>/delete", methods=['POST', 'GET'])
@login_required
def delete_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user and current_user.username != "SUPERUSER":
        abort(403)
    db.session.delete(post)
    db.session.commit()
    flash('Your post has been deleted!', 'success')
    return redirect(url_for('main.home'))


@posts.route('/search', methods=['POST'])
def search():
    form = SearchForm()
    post.searched = form.searched.data
    posts = Post.query
    posts = posts.filter(Post.content.like('%' + post.searched + '%'))
    posts = posts.order_by(Post.title).all()
    if form.validate_on_submit():
        post.searched = form.searched.data
        return render_template("search.html",
                               form=form,
                               searched=post.searched,
                               posts=posts)
    return render_template("search.html",
                           form=form,
                           searched=post.searched,
                           posts=posts)
