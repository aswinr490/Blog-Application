from django.test import TestCase
from django.urls import reverse
from .models import Post

class PostTests(TestCase):

    def test_post_list_view(self):
        response = self.client.get(reverse('post_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Blog Posts")

    def test_post_detail_view(self):
        post = Post.objects.create(title='Test Post', content='Test Content')
        response = self.client.get(reverse('post_detail', args=[post.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, post.title)

    def test_post_create_view(self):
        response = self.client.post(reverse('post_create'), {'title': 'New Post', 'content': 'New Content'})
        self.assertEqual(response.status_code, 302)

    def test_post_edit_view(self):
        post = Post.objects.create(title='Test Post', content='Test Content')
        response = self.client.post(reverse('post_edit', args=[post.pk]), {'title': 'Updated Post', 'content': 'Updated Content'})
        self.assertEqual(response.status_code, 302)

    def test_post_delete_view(self):
        post = Post.objects.create(title='Test Post', content='Test Content')
        response = self.client.post(reverse('post_delete', args=[post.pk]))
        self.assertEqual(response.status_code, 302)