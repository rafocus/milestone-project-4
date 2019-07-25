from django.test import TestCase
from . import forms

class TestUserRegisterForm(TestCase):
    def test_form_is_valid(self):
        data= {
            'username' : 'testusername',
            'email' : 'testemail@email.com',
            'password1' : 'testpasstestpass',
            'password2' : 'testpasstestpass'
            }
        form = forms.UserRegisterForm(data)
        self.assertTrue(form.is_valid())