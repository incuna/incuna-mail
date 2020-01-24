from django.conf import settings
from django.core.mail import EmailMessage, EmailMultiAlternatives
from django.template.loader import render_to_string
import six


def listify(obj):
    return [obj] if isinstance(obj, six.string_types) else obj


def send(template_name, sender=None, to=None, cc=None, bcc=None, subject='mail',
         attachments=(), html_template_name=None, context=None, headers=None,
         reply_to=None):
    """
    Render and send an email.  `template_name` is a plaintext template.

    If `html_template_name` is passed then a multipart email will be sent using
    `template_name` for the text part and `html_template_name` for the HTML part.
    The context will include any `context` specified.

    If no `sender` is specified then the `DEFAULT_FROM_EMAIL` or `SERVER_EMAIL`
    setting will be used.

    Extra email headers can be passed in to `headers` as a dictionary.
    """
    to, cc, bcc, reply_to = map(listify, [to, cc, bcc, reply_to])

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
        'reply_to': reply_to,
        'headers': headers or {},
    }

    text_content = render_to_string(template_name, context)
    email_kwargs['body'] = text_content

    if html_template_name is None:
        msg = EmailMessage(**email_kwargs)
    else:
        msg = EmailMultiAlternatives(**email_kwargs)
        html_content = render_to_string(html_template_name, context)
        msg.attach_alternative(html_content, 'text/html')

    msg.send()
