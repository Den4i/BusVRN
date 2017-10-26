from django.test import TestCase
from django.contrib.auth.models import User

from posts.models import Post


class PostMethodTests(TestCase):
    user = User.objects.get(username='wombat')

    def test_content_not_null(self):
        post = Post(user=self.user, title='test_title', slug='', content='test_content', publish='2016-08-22', read_time=1,)
        post.save()
        self.assertEqual((len(post.title) > 0), True)
        self.assertEqual((len(post.content) > 0), True)

    def test_setUp(self):
        self.posts = []
        for i in range(20):
            post = Post(user=self.user, title='test_title%d' % i, slug='', content='test_content', publish='2016-08-22', read_time=1,)
            self.posts.append(post)

        self.assertEqual(len(self.posts), 20)
