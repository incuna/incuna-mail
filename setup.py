from setuptools import setup


setup(
    name='incuna-mail',
    version='3.0.0',
    url='https://github.com/incuna/incuna-mail',
    license='MIT',
    author='Incuna Ltd',
    author_email='admin@incuna.com',
    description='Pythonic utility for sending template based emails with Django.',
    py_modules=['incuna_mail'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Topic :: Communications :: Email',
        'Topic :: Utilities',
    ],
)
