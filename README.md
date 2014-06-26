# Incuna Mail  [![Build Status](https://travis-ci.org/incuna/incuna-mail.svg?branch=i5-add-tests)](https://travis-ci.org/incuna/incuna-mail)  [![Coverage Status](https://img.shields.io/coveralls/incuna/incuna-mail.svg)](https://coveralls.io/r/incuna/incuna-mail) [![Wheel Status](https://pypip.in/wheel/incuna-mail/badge.png)](https://pypi.python.org/pypi/incuna-mail/) [![Latest Version](https://pypip.in/version/incuna-mail/badge.png)](https://pypi.python.org/pypi/incuna-mail/)

Pythonic utility for sending template based emails with Django.

## Installation
Install the package:

    pip install incuna_mail


## Usage
Import the `send` function and call it:

```python
from incuna_mail import send

send(
    to='foo@example.com',
    subject='Example email',
    template_name='email.html',
)
```

Supports `cc` and `bcc`...

```python
send(
    to='foo@example.com',
    cc='bar@example.com',
    bcc='baz@example.com',
    ...
)
```

... lists of recipients...

```python
send(
    to=['foo@example.com', 'bar@example.com'],
    cc=['spam@example.com', 'eggs@example.com'],
    ...
)
```

... multi-part emails...

```python
send(
    ...
    template_name='email.html',
    text_template_name='email.txt',
)
```

... template context...

```python
send(
    ...
    context={'user': user},
)
```

... template lists...

```python
send(
    ...
    # Uses the first template found.
    template_name=['might-exist.html', 'will-exist.html'],
)
```

... and custom email headers:

```python
send(
    ...
    headers={'Reply-To': 'another@example.com'}
)
```

The email sender can be set globally with `settings.DEFAULT_FROM_EMAIL`, and will default to `settings.SERVER_EMAIL`. It can be explicitly set on each call, if required:

```python
send(
    ...
    sender='eggy-mcspambot@example.com',
)
```
