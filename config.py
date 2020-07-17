
DEBUG = True

# Define the application directory
import os
BASE_DIR = os.path.abspath(os.path.dirname(__file__))  


SQLALCHEMY_DATABASE_URI = "postgresql://postgres:Om@shantiom123@localhost:5432/domitos"
DATABASE_CONNECT_OPTIONS = {}

THREADS_PER_PAGE = 2
SESSION_TYPE = 'sqlalchemy'

SESSION_SQLALCHEMY_TABLE = 'sessions'
SESSION_SQLALCHEMY = ''

CSRF_ENABLED     = True

CSRF_SESSION_KEY = "secret"
SECRET_KEY = "secret"

