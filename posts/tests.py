from django.test import TestCase

# Create your tests here.

from posts.models import Post
from django.contrib.auth.models import User


class PostMethodTests(TestCase):
    user = User.objects.get(username='john2')

    def test_content_not_null(self):
        post = Post(user=self.user, title='', slug='', content='', publish='2016-08-22', read_time=1, )
        post.save()
        self.assertEqual((len(post.title) > 0), True)
        self.assertEqual((len(post.content) > 0), True)