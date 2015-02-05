# encoding: utf-8
from django.core import mail
from django.test import TestCase

import incuna_mail


class TestIncunaMail(TestCase):
    def send_and_assert_email(self, html_template_name=None):
        """Runs send() on proper input and checks the result."""
        kwargs = {
            'sender': ['email@example.com'],
            'to': ['email2@example.com'],
            'cc': ['cc@example.com'],
            'bcc': ['bcc@example.com'],
            'subject': 'Test email',
            'template_name': 'dummy_template.html',
            'html_template_name': html_template_name,
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

    def test_default_email(self):
        with self.settings(DEFAULT_FROM_EMAIL='default@example.com'):
            incuna_mail.send(
                to='recipient@example.com',
                template_name='dummy_template.html',
            )
        email = mail.outbox[0]
        self.assertEqual(email.from_email, 'default@example.com')

    def test_send_email(self):
        email = self.send_and_assert_email()
        self.assertEqual(email.body, u'hello!\n')

    def test_send_multipart_email(self):
        email = self.send_and_assert_email('dummy_html_template.html')
        self.assertEqual(email.body, u'hello!\n')
        self.assertEqual(email.alternatives[0], (u'<p>hi!</p>\n', 'text/html'))

    def test_do_not_send_empty_email(self):
        """Regression test to assert empty email can't be send."""
        with self.assertRaises(TypeError):
            incuna_mail.send()


class TestListify(TestCase):
    def test_passed_string(self):
        """Strings should be wrapped in a list"""
        string = u'(╯°□°）╯︵ ┻━┻'
        self.assertEqual(incuna_mail.listify(string), [string])

    def test_passed_list(self):
        """Lists should not be wrapped in lists"""
        array = [u'string']
        self.assertEqual(incuna_mail.listify(array), array)
