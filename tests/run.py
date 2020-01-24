import sys

import django
from colour_runner.django_runner import ColourRunnerMixin
from django.conf import settings


settings.configure(
    DATABASES={
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': ':memory:',
        }
    },
    MIDDLEWARE_CLASSES=(),
    TEMPLATES=[
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'APP_DIRS': False,
            'DIRS': ('tests/templates',),
        },
    ]
)


if django.VERSION >= (1, 7):
    django.setup()


try:
    from django.test.runner import DiscoverRunner
except ImportError:
    # Django < 1.6
    from discover_runner import DiscoverRunner


class Runner(ColourRunnerMixin, DiscoverRunner):
    pass

test_runner = Runner(verbosity=1)
failures = test_runner.run_tests(['tests'])
if failures:
    sys.exit(1)
