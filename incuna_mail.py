from django.conf import settings
from django.core.mail import EmailMessage, EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils import six

try:
    # Django >=1.5
    from django.contrib.auth import get_user_model
except ImportError:
    # Django < 1.5
    from django.contrib.auth.models import User
else:
    User = get_user_model()


def get_manager_emails():
    """Get a list of the managers' email addresses."""
    staff = User.objects.filter(is_staff=True)
    manager_emails = staff.exclude(email='').distinct().values_list('email', flat=True)
    return manager_emails or [m[1] for m in settings.MANAGERS]


def send(sender=None, to=(), cc=(), bcc=(), subject='mail',
         attachments=(), template_name=(), text_template_name=(),
         context=None, **kwargs):
    """
    Render and send a (mail) template.
    if text_template_name is not None then a multipart email will be sent using
    template for the html part and text_template_name for the plain part.
    The context will include any extra_context specified.
    If no sender is specified then the DEFAULT_FROM_EMAIL or SERVER_EMAIL setting will be used.
    Any extra items passed in with kwargs will be added to the email headers.
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
        'headers': kwargs,
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
