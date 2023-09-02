from main import app, db

# アプリケーションコンテキストを設定
with app.app_context():
    # データベースの初期化
    db.create_all()
