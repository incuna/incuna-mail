from django.test import TestCase

from django.core import mail

import incuna_mail


class TestIncunaMail(TestCase):

    def tearDown(self):
        mail.outbox = []

    def send_and_assert_email(self, text_template_name=()):
        """Runs send() on proper input and checks the result."""
        kwargs = {
            'sender': ['email@example.com'],
            'to': ['email2@example.com'],
            'cc': ['cc@example.com'],
            'bcc': ['bcc@example.com'],
            'subject': 'Test email',
            'template_name': 'dummy_template.html',
            'text_template_name': text_template_name,
        }

        incuna_mail.send(**kwargs)

        # Assert that the email exists and has the correct parameters
        self.assertEqual(len(mail.outbox), 1)
        email = mail.outbox[0]

        self.assertEqual(email.to, kwargs['to'])
        self.assertEqual(email.from_email, kwargs['sender'])
        self.assertEqual(email.cc, kwargs['cc'])
        self.assertEqual(email.bcc, kwargs['bcc'])
        self.assertEqual(email.subject, kwargs['subject'])

        return email

    def test_get_manager_emails(self):
        with self.settings(MANAGERS=[('manager1', 'm1@example.com')]):
            managers = incuna_mail.get_manager_emails()
        self.assertEqual(managers, ['m1@example.com'])

    def test_default_email(self):
        with self.settings(DEFAULT_FROM_EMAIL='default@example.com'):
            incuna_mail.send(to='recipient@example.com', template_name='dummy_template.html')
        email = mail.outbox[0]
        self.assertEqual(email.from_email, 'default@example.com')

    def test_send_email(self):
        email = self.send_and_assert_email()
        self.assertEqual(email.body, u'<p>hi!</p>\n')

    def test_send_multipart_email(self):
        email = self.send_and_assert_email('dummy_text_template.html')
        self.assertEqual(email.body, u'hello!\n')
        self.assertEqual(email.alternatives[0], (u'<p>hi!</p>\n', 'text/html'))
