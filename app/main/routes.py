from flask import Blueprint, request, render_template, redirect, url_for, flash
import flask_login
from app.main.forms import PostForm, CommentForm
from app.models import Post, User, Review
from app.extensions import app, db
from flask_login import login_user, logout_user, login_required, current_user

main = Blueprint('main', __name__)

# Create your routes here.
@main.route('/')
def index():
  posts = Post.query.all()
  return render_template('home.html', posts = posts)


@main.route('/user/<user_id>')
def user_details(user_id):
  user = User.query.get(user_id)
  return render_template('user_detail.html', user=user)

@main.route('/new_post', methods=['GET', 'POST'])
@login_required
def new_post():
  form = PostForm()

  if form.validate_on_submit():
    post = Post(
      name = form.name.data,
      address = form.address.data,
      created_by = flask_login.current_user
    )
    db.session.add(post)
    db.session.commit()

    flash('Post added!')
    return redirect(url_for('main.index'))

  return render_template('new_post.html', form=form)
 
@main.route('/post/<post_id>', methods=['GET', 'POST'])
def post_detail(post_id):
  post = Post.query.get(post_id)
  form = PostForm(obj=post)
  comment_form = CommentForm()

  if comment_form.validate_on_submit():
    review = Review(
      reviewer = flask_login.current_user,
      comment = comment_form.comment.data,
      post = post
    )
    db.session.add(review)
    db.session.commit()

    return redirect(url_for('main.post_detail', post_id=post_id))

  if form.validate_on_submit():
    post.name = form.name.data
    post.address = form.address.data
    db.session.add(post)
    db.session.commit()

    flash('Post Updated!')
    return redirect(url_for('main.post_detail', post_id=post_id))
  
  return render_template('post_detail.html', post=post, comment_form=comment_form, form=form)
