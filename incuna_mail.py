from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.sites.models import Site
from django.core.mail import EmailMessage, EmailMultiAlternatives
from django.template.loader import render_to_string

try:
    basestring
except NameError:
    basetring = str  # py3k
    string_type = str
else:
    string_type = unicode

def get_manager_emails():
    """
    Get a list of the managers email addresses.
    """
    addresses = User.objects.filter(is_staff=True).exclude(email='').distinct().values_list('email')
    manager_emails = [m[0] for m in addresses]
    if not manager_emails:
        manager_emails = [m[1] for m in settings.MANAGERS]

    return manager_emails


def send(sender=None, to=(), cc=(), bcc=(), subject='mail',
         attachments=(), template_name=(), text_template_name=(),
         extra_context=None, **kwargs):
    """
    Render and send a (mail) template.
    if text_template_name is not None then a multipart email will be sent using
    template for the html part and text_template_name for the plain part.
    The context will include the current site (and any extra_context specified).
    If no sender is specified then the DEFAULT_FROM_EMAIL or SERVER_EMAIL setting will be used.
    Any extra items passed in with kwargs will be added to the email headers.
    """
    if isinstance(to, basestring):
        to = [to]

    if isinstance(cc, basestring):
        cc = [cc]

    if isinstance(bcc, basestring):
        bcc = [bcc]

    if sender is None:
        sender = getattr(settings, 'DEFAULT_FROM_EMAIL', settings.SERVER_EMAIL)

    context = {'site': Site.objects.get_current()}
    if extra_context is not None:
        context.update(extra_context)

    attachment_list = [[a.name, a.read(), a.content_type] for a in attachments if attachments]

    email_kwargs = {
        'from_email': sender,
        'to': to,
        'cc': cc,
        'bcc': bcc,
        'subject': string_type(subject),
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
