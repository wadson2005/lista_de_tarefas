from django.test import TestCase
from django.urls import reverse

from .forms import TaskForm
from .models import Task


class TaskModelTests(TestCase):
	def test_task_default_completed_is_false(self):
		task = Task.objects.create(title='Nova')
		self.assertFalse(task.completed)

	def test_task_str_returns_title(self):
		task = Task.objects.create(title='Titulo da tarefa')
		self.assertEqual(str(task), 'Titulo da tarefa')


class TaskFormTests(TestCase):
	def test_task_form_valid_with_title(self):
		form = TaskForm(data={'title': 'Tarefa valida'})
		self.assertTrue(form.is_valid())

	def test_task_form_invalid_without_title(self):
		form = TaskForm(data={'title': ''})
		self.assertFalse(form.is_valid())


class TodoViewsTests(TestCase):
	def test_index_page_loads(self):
		response = self.client.get(reverse('index'))
		self.assertEqual(response.status_code, 200)

	def test_create_task_on_index_post(self):
		response = self.client.post(reverse('index'), {'title': 'Nova tarefa'})

		self.assertEqual(response.status_code, 302)
		self.assertTrue(Task.objects.filter(title='Nova tarefa').exists())

	def test_complete_task_marks_task_as_completed(self):
		task = Task.objects.create(title='Tarefa pendente', completed=False)

		response = self.client.get(reverse('complete_task', args=[task.id]))
		task.refresh_from_db()

		self.assertEqual(response.status_code, 302)
		self.assertTrue(task.completed)

	def test_complete_task_returns_404_for_missing_task(self):
		response = self.client.get(reverse('complete_task', args=[9999]))
		self.assertEqual(response.status_code, 404)

	def test_delete_task_flow(self):
		task = Task.objects.create(title='Tarefa para excluir', completed=False)

		get_response = self.client.get(reverse('delete_task', args=[task.id]))
		self.assertEqual(get_response.status_code, 200)

		post_response = self.client.post(reverse('delete_task', args=[task.id]))
		self.assertEqual(post_response.status_code, 302)
		self.assertFalse(Task.objects.filter(id=task.id).exists())

	def test_delete_task_returns_404_for_missing_task(self):
		response = self.client.get(reverse('delete_task', args=[9999]))
		self.assertEqual(response.status_code, 404)

	def test_legacy_delete_route_returns_404(self):
		response = self.client.get('/delet/1/')
		self.assertEqual(response.status_code, 404)
