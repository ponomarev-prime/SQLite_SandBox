import os

basedir = os.path.abspath(os.path.dirname(__file__))

print(basedir)

print('sqlite:///' + os.path.join(basedir, 'database.db'))