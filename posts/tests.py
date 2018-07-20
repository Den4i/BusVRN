from django.contrib.auth import get_user_model
from django.urls import reverse_lazy
from django.test import TestCase, RequestFactory

from posts.models import Post
from posts.views import post_update, post_create


User = get_user_model()


class PostViewTestCase(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create(
                    username='testuser',
                    email='test@gmail.com',
                    password='testpass'
                )

    def test_user_auth(self):
        obj = Post.objects.create(user=self.user, title='test_title1', content='test_content', publish='2018-08-22')
        edit_url = reverse_lazy("posts:update", kwargs={"slug": obj.slug})
        request = self.factory.get(edit_url)
        request.user = self.user
        response = post_update(request, slug=obj.slug)
        self.assertEqual(response.status_code, 200)

    def test_user_post(self):
        request = self.factory.post("/posts/create/")
        request.user = self.user
        response = post_create(request)
        self.assertEqual(response.status_code, 200)

    def test_empty_page(self):
        page = '/dont/exist/page/'
        request = self.factory.get(page)
        request.user = self.user
        response = post_create(request)
        self.assertEqual(response.status_code, 200)

    def test_create_posts(self):
        self.posts = []
        for i in range(20):
            post = Post(user=self.user, title='test_title%d' % i, content='test_content', publish='2018-07-21')
            self.posts.append(post)

        self.assertEqual(len(self.posts), 20)

    def test_content_not_null(self):
        post = Post.objects.create(user=self.user, title='test_title', content='test_content', publish='2018-08-22')
        self.assertEqual((len(post.title) > 0), True)
        self.assertEqual((len(post.content) > 0), True)

