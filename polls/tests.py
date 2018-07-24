from django.test import TestCase, RequestFactory
from django.utils import timezone
import datetime

from .models import Question
from .views import IndexView, DetailView, ResultsView, vote


class PollsViewTestCase(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    def test_polls_index(self):
        for i in range(10):
            Question.objects.create(question_text='quest%d' % i, pub_date=timezone.now())

        request = self.factory.get("/polls/")

        response = IndexView(request=request)
        questions = response.get_queryset()

        self.assertEqual(len(questions), 5)

    def test_polls_detail(self):
        obj = Question.objects.create(question_text='test', pub_date=timezone.now())
        request = self.factory.get("/polls/%d/" % obj.id)
        response = DetailView.as_view()(request, pk=obj.id)
        self.assertEqual(response.status_code, 200)

    def test_polls_result(self):
        obj = Question.objects.create(question_text='test', pub_date=timezone.now())
        request1 = self.factory.get("/polls/%d/results/" % obj.id)
        response1 = ResultsView.as_view()(request1, pk=obj.id)
        self.assertEqual(response1.status_code, 200)

    def test_polls_voting(self):
        obj = Question.objects.create(question_text='test', pub_date=timezone.now())
        request = self.factory.get("/polls/%d/vote/" % obj.id)
        response = vote(request, question_id=obj.id)
        self.assertEqual(response.status_code, 200)

    def test_was_published_recently(self):
        future_time = timezone.now()+datetime.timedelta(days=10)
        future_question = Question(pub_date=future_time)
        self.assertIs(future_question.was_published_recently(), False)
