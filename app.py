from flask import Flask, render_template, request, redirect, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/mydatabase"  # MongoDB 연결 URI
mongo = PyMongo(app)

# 게시글 컬렉션 이름 정의
# 이거 써가지고 html에서 게시글 폼 목록 불러오는데 사용예정
POSTS_COLLECTION = 'posts'

@app.route('/', methods=['GET', 'POST'])
def index():
    # 게시글 작성 로직 POST, form에서 post제출 시 작동
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        # DB에 게시글 저장
        mongo.db[POSTS_COLLECTION].insert_one({'title': title, 'content': content, 'like': 0})
        return redirect(url_for('index'))
    # 게시글 조회 로직 GET, 맨처음 실행하면 index.html로 이동
    else:
        posts = mongo.db[POSTS_COLLECTION].find().sort([('created_at', -1)])
        return render_template('index.html', posts=posts)

@app.route('/edit/<post_id>', methods=['GET', 'POST'])
def post_edit(post_id):
    # DB에서 해당 post_id와 같은 게시글 조회
    post = mongo.db[POSTS_COLLECTION].find_one_or_404({'_id': ObjectId(post_id)})
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        mongo.db[POSTS_COLLECTION].update_one({'_id': ObjectId(post_id)}, {'$set': {'title': title, 'content': content}})
        return redirect(url_for('index'))  # 수정 후 index 페이지로 리다이렉트
    return redirect(url_for('index'))

@app.route('/delete/<post_id>')
def post_delete(post_id):
    mongo.db[POSTS_COLLECTION].delete_one({'_id': ObjectId(post_id)})
    return redirect(url_for('index'))  # 삭제 후 index 페이지로 리다이렉트

@app.route('/like/<post_id>')
def post_like(post_id):
    # 좋아요 처리 로직 (추후 구현)
    mongo.db[POSTS_COLLECTION].update_one({'_id': ObjectId(post_id)}, {'$inc': {'like': 1}})
    return redirect(url_for('index'))  # 좋아요 후 index 페이지로 리다이렉트

if __name__ == '__main__':
    app.run(debug=True)