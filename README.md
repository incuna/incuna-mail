# Incuna Mail  [![Build Status](https://travis-ci.org/incuna/incuna-mail.svg?branch=i5-add-tests)](https://travis-ci.org/incuna/incuna-mail)  [![Coverage Status](https://img.shields.io/coveralls/incuna/incuna-mail.svg)](https://coveralls.io/r/incuna/incuna-mail)

A collection of mail utilities for Incuna Django projects.

## Installation
Install the package:

    pip install incuna_mail


## Usage
Import a function and call it:

    from incuna_mail import send

    kwargs = {
        'to': ['foo@example.com'],
        'bcc': ['bar@example.com'],
        'subject': 'Test email',
        'template_name': 'email.html',
    }
    send(**kwargs)


More email headers can be passed in using kwargs.
