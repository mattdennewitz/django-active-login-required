def pytest_configure():
    """Configures pytest for Django-aware testing"""
    from django.conf import settings

    settings.configure(
        AFFIRMATIVE = 'ok',

        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': ':memory:'
            },
        },

        SECRET_KEY = 'sssshhhhhh',
        USE_TZ = True,

        ROOT_URLCONF = 'tests.urls',

        INSTALLED_APPS=(
            'django.contrib.auth',
            'django.contrib.contenttypes',
            'django.contrib.sessions',
            'django.contrib.sites',
            'django.contrib.messages',

            'active_login_required',
            'tests',
        ),

        MIDDLEWARE_CLASSES = (
            'django.middleware.common.CommonMiddleware',
            'django.contrib.sessions.middleware.SessionMiddleware',
            'django.middleware.csrf.CsrfViewMiddleware',
            'django.contrib.auth.middleware.AuthenticationMiddleware',
            'django.contrib.messages.middleware.MessageMiddleware',
        ),
    )

    try:
        import django
        django.setup()
    except AttributeError:
        pass
