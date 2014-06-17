from unittest import TestCase

import incuna_mail


class TestIncunaMail(TestCase):

    def test_send_email(self):
        incuna_mail.send()
