import sys

from colour_runner.django_runner import ColourRunnerMixin
from django.conf import settings
import dj_database_url


settings.configure(
    # Core environmental settings
    INSTALLED_APPS=(
        'django.contrib.contenttypes',
        'django.contrib.auth',
    ),
    TEMPLATE_DIRS=('tests/templates',),
    DATABASES={
        'default': dj_database_url.config(default='postgres://localhost/incuna_mail'),
    },
)

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
