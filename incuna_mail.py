from django.conf import settings
from django.core.mail import EmailMessage, EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils import six


def send(sender=None, to=(), cc=(), bcc=(), subject='mail',
         attachments=(), template_name=(), text_template_name=(),
         context=None, headers=None):
    """
    Render and send an email.

    If `text_template_name` is passed then a multipart email will be sent using
    `template_name` for the html part and `text_template_name` for the plain part.
    The context will include any `context` specified.

    If no `sender` is specified then the DEFAULT_FROM_EMAIL or SERVER_EMAIL setting will be used.

    Extra email headers can be passed in to `headers` as a dictionary.
    """
    to, cc, bcc = map(lambda v: [v] if isinstance(v, six.string_types) else v, [to, cc, bcc])

    if sender is None:
        sender = getattr(settings, 'DEFAULT_FROM_EMAIL', settings.SERVER_EMAIL)

    attachment_list = [[a.name, a.read(), a.content_type] for a in attachments]

    email_kwargs = {
        'from_email': sender,
        'to': to,
        'cc': cc,
        'bcc': bcc,
        'subject': six.text_type(subject),
        'attachments': attachment_list,
        'headers': headers or {},
    }
    if not text_template_name:
        email_kwargs['body'] = render_to_string(template_name, context)
        msg = EmailMessage(**email_kwargs)
    else:
        email_kwargs['body'] = render_to_string(text_template_name, context)
        msg = EmailMultiAlternatives(**email_kwargs)

        html_content = render_to_string(template_name, context)
        msg.attach_alternative(html_content, 'text/html')

    msg.send()
