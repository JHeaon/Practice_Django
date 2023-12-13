from django.test import TestCase
from .models import *

# Django에서는 TestCase를 상속받아 테스트를 작성할 수 있음.


class APITestCase(TestCase):
    # setUpTestData() 는 클래스 전체에서 사용되는 설정을 위해서 테스트 시작 때 딱 한 번만 실행된다.
    # 테스트 메소드가 실행되면서 수정되거나 변경되지 않을 객체들을 이곳에서 생성할 수 있습니다.
    @classmethod
    def setUpTestData(cls):
        post = Post.objects.create(title="test", content="test")
        comment = Comment.objects.create(post=post, content="test")

    def test_post(self):
        post = Post.objects.get(title="test")
        self.assertEqual(post.title, "test")
        self.assertEqual(post.content, "test")

    def test_comment(self):
        comment = Comment.objects.get(content="test")
        self.assertEqual(comment.post.title, "test")
        self.assertEqual(comment.content, "test")

    # setUp() 은 각각의 테스트 메소드가 실행될 때마다 실행된다. 테스트 중 내용이 변경될 수 있는 객체를 이곳에서 생성할 수 있다.
    # (모든 테스트 메쏘드는 방금 막 생성된 ("fresh") 오브젝트를 입력받게 됩니다).
    def setUp(self):
        pass
