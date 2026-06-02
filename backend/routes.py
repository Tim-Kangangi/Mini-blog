from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, create_access_token, get_jwt_identity
from models import db, User, Post, Like

bp = Blueprint("bp", __name__)

# REGISTER
@bp.route("/register", methods=["POST"])
def register():
    data = request.json
    user = User(username=data["username"], email=data["email"])
    user.set_password(data["password"])
    db.session.add(user)
    db.session.commit()
    return jsonify({"msg": "registered"})


# LOGIN
@bp.route("/login", methods=["POST"])
def login():
    data = request.json
    user = User.query.filter_by(email=data["email"]).first()

    if not user or not user.check_password(data["password"]):
        return jsonify({"msg": "invalid"}), 401

    token = create_access_token(identity=user.id)
    return jsonify({"token": token})


# GET ALL POSTS (PUBLIC)
@bp.route("/posts")
def posts():
    all_posts = Post.query.all()
    return jsonify([
        {"id": p.id, "title": p.title, "content": p.content}
        for p in all_posts
    ])


# CREATE POST (PROTECTED)
@bp.route("/posts", methods=["POST"])
@jwt_required()
def create_post():
    uid = get_jwt_identity()
    data = request.json

    post = Post(title=data["title"], content=data["content"], user_id=uid)
    db.session.add(post)
    db.session.commit()

    return jsonify({"msg": "created"})


# UPDATE POST (PROTECTED)
@bp.route("/posts/<int:id>", methods=["PUT"])
@jwt_required()
def update_post(id):
    post = Post.query.get(id)
    data = request.json

    post.title = data["title"]
    post.content = data["content"]

    db.session.commit()
    return jsonify({"msg": "updated"})


# DELETE POST (PROTECTED)
@bp.route("/posts/<int:id>", methods=["DELETE"])
@jwt_required()
def delete_post(id):
    post = Post.query.get(id)
    db.session.delete(post)
    db.session.commit()
    return jsonify({"msg": "deleted"})


# LIKE (PROTECTED M-M)
@bp.route("/like/<int:post_id>", methods=["POST"])
@jwt_required()
def like(post_id):
    uid = get_jwt_identity()

    existing = Like.query.filter_by(user_id=uid, post_id=post_id).first()
    if existing:
        return jsonify({"msg": "already liked"})

    db.session.add(Like(user_id=uid, post_id=post_id))
    db.session.commit()

    return jsonify({"msg": "liked"})


# MY POSTS (PROTECTED)
@bp.route("/my-posts")
@jwt_required()
def my_posts():
    uid = get_jwt_identity()
    posts = Post.query.filter_by(user_id=uid).all()

    return jsonify([
        {"id": p.id, "title": p.title} for p in posts
    ])