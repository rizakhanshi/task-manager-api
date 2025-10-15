import pytest
from django.contrib.auth import get_user_model
from .models import Task
from django.utils import timezone


@pytest.mark.django_db
def test_create_task():
    User = get_user_model()
    user = User.objects.create_user(username='u1', password='pass')
    t = Task.objects.create(title='T1', owner=user, due_date=timezone.now().date() + timezone.timedelta(days=1))
    assert t.title == 'T1'
    assert t.owner == user


@pytest.mark.django_db
def test_task_complete_incomplete():
    User = get_user_model()
    user = User.objects.create_user(username='u2', password='pass')
    t = Task.objects.create(title='T2', owner=user, due_date=timezone.now().date() + timezone.timedelta(days=1))
    assert t.status == Task.STATUS_PENDING
    t.mark_complete()
    t.refresh_from_db()
    assert t.status == Task.STATUS_COMPLETED
    assert t.completed_at is not None
    t.mark_incomplete()
    t.refresh_from_db()
    assert t.status == Task.STATUS_PENDING
    assert t.completed_at is None
