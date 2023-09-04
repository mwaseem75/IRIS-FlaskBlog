from flask import Blueprint, render_template, request, flash, redirect, url_for, jsonify
from flask_login import login_required, current_user
from .models import *
from . import db
from .myconfig import * 

views = Blueprint("views", __name__)

#Home Page
@views.route("/")
@views.route("/index")
def home():
    unique_tags = get_unique_tags()
    post = Post.query
    page = get_page()
    #define pagination       
    pages=post.paginate(page=page,per_page=PAGINATE_RECORDS_PER_PAG)  
    return render_template("index.html", user=current_user, posts=posts, pages=pages,tags=unique_tags,feed=1)

#View post
@views.route("/post/<id>")
@login_required
def post(id):
    post = Post.query.filter_by(id=id).first()    
    if not post:
        flash("Post does not exist.", category='error')
        return redirect(url_for('views.home'))
    else:
        return render_template("post.html", user=current_user, post=post)

#Create Post
@views.route("/create-post", methods=['GET', 'POST'])
@login_required
def create_post():
    if request.method == "POST":
        title = request.form.get('title')
        content = request.form.get('content')
        tags = request.form.get('tagval')
        if not title:
            flash('Post cannot be empty', category='error')
        else:
            post = Post(title=title,content=content,author=current_user.id)
            tags = tags.split(",")           
            for tag in tags:
                if len(tag) > 0:
                    post.tags.append(Tag(name=tag))
            db.session.add(post)
            db.session.commit()
            return redirect(url_for('views.home'))
    return render_template('create_post.html', user=current_user)

#Edit post
@views.route("/edit-post/<id>", methods=['GET', 'POST'])
@login_required
def edit_post(id):
    if request.method == "POST":
        title = request.form.get('title')
        content = request.form.get('content')
        tags = request.form.get('tagval')
        if not title:
            flash('Post cannot be empty', category='error')
        else:
            post = Post.query.filter_by(id=id).first() 
            post.title = title
            post.content = content  

            #Get old tags
            newTags = tags.split(",")
            oldTagNames = []
            oldTags = db.session.query(tags_table).filter_by(post_id=id).all()
            for row in oldTags:
                oldTag = Tag.query.filter_by(id=row[1]).first()
                if oldTag.name not in newTags:
                    db.session.delete(oldTag)
                else:
                    oldTagNames.append(oldTag.name)    
            #Add new tags
            for tag in newTags:
                if tag not in oldTagNames:
                    if len(tag) > 0:
                        post.tags.append(Tag(name=tag))     
                        
            db.session.commit()            
            return redirect(url_for('views.home'))    
    
    #Get Request
    post = Post.query.filter_by(id=id).first()
    if not post:
        flash("Post does not exist.", category='error')
    elif current_user.id != post.author:
        flash('You do not have permission to edit this post.', category='error')
        return redirect(url_for('views.post', id=id))
    else:
        #get tag lists
        tags = []
        tags_str = ''
        for tag in post.tags:
            tags.append(tags)
            if len(tags_str) > 0:
               tags_str = tags_str + "," + str(tag)   
            else:
               tags_str = str(tag)
        return render_template('edit_post.html', user=current_user, post=post, tags=tags, tags_str=tags_str)

#Delete Post
@views.route("/delete-post/<id>")
@login_required
def delete_post(id):
    post = Post.query.filter_by(id=id).first()
    if not post:
        flash("Post does not exist.", category='error')
    elif current_user.id != post.author:
        flash('You do not have permission to delete this post.', category='error')
    else:
        #delete related tags
        tags = db.session.query(tags_table).filter_by(post_id=id).all()
        for row in tags:
            tag = Tag.query.filter_by(id=row[1]).first()
            if tag:
                db.session.delete(tag)
                
        db.session.delete(post)
        db.session.commit()
        #flash('Post deleted.', category='success')
        
    return redirect(url_for('views.home'))

#Get all posts base on User
@views.route("/posts/<username>")
@login_required
def posts(username):
    user = User.query.filter_by(username=username).first()
    if not user:
        flash('No user with that username exists.', category='error')
        return redirect(url_for('views.home'))
     
    unique_tags = get_unique_tags()
    page = get_page()
    #define pagination  
    pages = Post.query.filter(Post.author==user.id).paginate(page=page, per_page=PAGINATE_RECORDS_PER_PAG)
    return render_template("index.html", user=current_user, posts=posts, pages=pages,tags=unique_tags,feed=2,feed_user=user.username)

#Get all posts base on Tag
@views.route("/tags/<tag>")
@login_required
def tag_details(tag):    
    tag = Tag.query.filter(Tag.name==tag).first()    
    posts = db.session.query(Post).all()
    tag_posts = []
    for post in posts:
       my_string = ",".join(str(val) for val in post.tags)
       my_string = ","+my_string+","
       if my_string.find(","+str(tag)+",") > -1:
           tag_posts.append(post.id)        
    unique_tags = get_unique_tags()
    page = get_page()
    pages = db.session.query(Post).filter(Post.id.in_((tag_posts))).paginate(page=page, per_page=PAGINATE_RECORDS_PER_PAG)    
    return render_template("index.html", user=current_user, posts=posts, pages=pages,tags=unique_tags,feed=3,feed_tag=str(tag))
  
#Add Comment
@views.route("/create-comment/<post_id>", methods=['POST'])
@login_required
def create_comment(post_id):
    text = request.form.get('text')

    if not text:
        flash('Comment cannot be empty.', category='error')
    else:
        post = Post.query.filter_by(id=post_id)
        if post:
            comment = Comment(
                text=text, author=current_user.id, post_id=post_id)
            db.session.add(comment)
            db.session.commit()
        else:
            flash('Post does not exist.', category='error')

    return redirect(url_for('views.post', id=post_id))

#Delete Comment
@views.route("/delete-comment/<comment_id>")
@login_required
def delete_comment(comment_id):
    comment = Comment.query.filter_by(id=comment_id).first()
    if not comment:
        flash('Comment does not exist.', category='error')
    elif current_user.id != comment.author and current_user.id != comment.post.author:
        flash('You do not have permission to delete this comment.', category='error')
    else:
        post_id = comment.post_id
        db.session.delete(comment)
        db.session.commit()

    return redirect(url_for('views.post', id=post_id))

#Like post
@views.route("/like-post/<post_id>", methods=['POST'])
@login_required
def like(post_id):
    post = Post.query.filter_by(id=post_id).first()
    like = Like.query.filter_by(
        author=current_user.id, post_id=post_id).first()

    if not post:
        return jsonify({'error': 'Post does not exist.'}, 400)
    elif like:
        db.session.delete(like)
        db.session.commit()
    else:
        like = Like(author=current_user.id, post_id=post_id)
        db.session.add(like)
        db.session.commit()

    return jsonify({"likes": len(post.likes), "liked": current_user.id in map(lambda x: x.author, post.likes)})

#Used in pagination
def get_page():
    page = request.args.get('page')
    if page and page.isdigit():
       page = int(page) 
    else:
       page = 1            
    return page

#Get unique tags to be displayed in tag section
def get_unique_tags():
    tags = Tag.query.all()
    unique_tags = []
    for x in tags:
        # check if exists in unique_list or not
        if x.name not in unique_tags:
            unique_tags.append(x.name)
    return unique_tags        