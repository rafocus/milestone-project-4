from django.test import TestCase
from . import forms

class TestUserRegisterForm(TestCase):
    def test_form_is_valid(self):
        form = forms.UserRegisterForm({
            'username' : 'testusername',
            'email' : 'testemail@email.com',
            'password1' : 'testpasstestpass',
            'password2' : 'testpasstestpass'
            })
        self.assertTrue(form.is_valid())