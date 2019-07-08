import dj_database_url

from .base import *

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'

# Extra places for collectstatic to find static files.
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'

ALLOWED_HOSTS = ['*']

DEBUG = dj_database_url.config('DEBUG', default=False)

DATABASES = {
    'default': dj_database_url.config(
        default=dj_database_url.config('DATABASE_URL', default='django.db.backends.sqlite3', engine='django.db.backends.sqlite3')
    )
}
