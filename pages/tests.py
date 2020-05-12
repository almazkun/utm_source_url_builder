from django.contrib.auth import get_user_model
from django.test import SimpleTestCase, TestCase
from django.urls import reverse
from users.models import CustomUser

from .models import UTM_source
from .utils import urllizer, all_to_bytes, all_to_str


class ModelsTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="testuser", email="test@email.com", password="secret"
        )
        self.utm = UTM_source.objects.create(
            utm_url="https://akun.dev",
            utm_source="google",
            utm_medium="organic",
            utm_user=self.user,
        )
        self.test_link = "https://akun.dev/?utm_source=google&utm_medium=organic"

    def test_build_link(self):
        assert self.utm.build_link() == self.test_link

    def test_build_link_with_end(self):
        self.utm_url = "https://akun.dev/"
        assert self.utm.build_link() == self.test_link


class UtilsTest(TestCase):
    def setUp(self):
        self.test_strings = [
            "Stanford University",
            """~!@#$%^&*()_+`[]\\;',./{}|:"<>?
~""",
            "'",
            "qwerty",
        ]
        self.expected_results = [
            "Stanford%20University",
            "~%21%40%23%24%25%5E%26%2A%28%29_%2B%60%5B%5D%5C%3B%27%2C./%7B%7D%7C%3A%22%3C%3E%3F%0A~",
            "%27",
            "qwerty",
        ]

    def test_urllizer(self):
        i = 0
        while i < len(self.test_strings):
            assert urllizer(self.test_strings[i]) == self.expected_results[i]
            i += 1

    def test_all_to_bytes(self):
        test_case = ["abc", 1, 2.0, b"cba"]
        assert all_to_bytes(test_case[0]) == b"abc"
        assert all_to_bytes(test_case[1]) == b"1"
        assert all_to_bytes(test_case[2]) == b"2.0"
        assert all_to_bytes(test_case[3]) == b"cba"

    def test_all_to_str(self):
        test_case = ["abc", 1, 2.0, b"cba"]
        assert all_to_str(test_case[0]) == "abc"
        assert all_to_str(test_case[1]) == "1"
        assert all_to_str(test_case[2]) == "2.0"
        assert all_to_str(test_case[3]) == "cba"
