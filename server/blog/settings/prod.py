try:
    from .base import *
except ImportError:
    raise ImportError("Oops,can't find base settings")

# only for testing and development
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'prodkey'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False
# change it
ALLOWED_HOSTS = ['*']
