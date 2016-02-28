"""Configures MySQL Database.
    :Fields:
    - 'SQLALCHEMY_DATABASE_URI': Address of database
    - 'SQLALCHEMY_MIGRATE_REPO': Sets database migration repository
    - 'SQLALCHEMY_TRACK_MODIFICATIONS:': Suppresses warnings 
    - 'SECRET_KEY': Key that allows access to database
    
    :Database Login:
    - 'username': url
    - 'password': url
    - 'name': url
"""

import os
basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'mysql://url:url@localhost/url'
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
SQLALCHEMY_TRACK_MODIFICATIONS = True

ACCOUNT_SID = "AC067524dad918b6a9db9867f79aaa30de"
AUTH_TOKEN = "fc941e15bd560bd15dd9ec17d6bdb9e4"


SECRET_KEY = 'person'
