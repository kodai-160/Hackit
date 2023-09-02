from setuptools import setup, find_packages

setup(
    name='YourPackageName',       # パッケージ名
    version='0.1',                 # バージョン番号
    packages=find_packages(),      # パッケージのサブディレクトリを自動で検出
    install_requires=[             # 依存パッケージのリスト
        'Flask==2.0.1',
        'Flask-SQLAlchemy==2.5.1',
        'Flask-Login==0.5.0',
        'email-validator==1.1.3',
    ],
    author='Your Name',            # 作者名
    author_email='your@email.com', # 作者のメールアドレス
    description='Your package description',  # パッケージの説明
    url='https://github.com/yourusername/yourpackage',  # パッケージのリポジトリURL
)
