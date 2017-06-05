from django.test import TestCase


class PostTests(TestCase):


    def test_str(self):
        test_title = Post(title='Latest Blog Post')
        self.assertEqual(str(test_title),
                         'Latest Blog Post')
