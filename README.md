# Incuna Mail

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
