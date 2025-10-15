from django.db import models
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.utils import timezone

User = get_user_model()


def validate_due_date(value):
    if value and value < timezone.now().date():
        raise ValidationError('Due date must be in the future')


class Task(models.Model):
    PRIORITY_LOW = 'low'
    PRIORITY_MEDIUM = 'medium'
    PRIORITY_HIGH = 'high'
    PRIORITY_CHOICES = [
        (PRIORITY_LOW, 'Low'),
        (PRIORITY_MEDIUM, 'Medium'),
        (PRIORITY_HIGH, 'High'),
    ]

    STATUS_PENDING = 'pending'
    STATUS_COMPLETED = 'completed'
    STATUS_CHOICES = [
        (STATUS_PENDING, 'Pending'),
        (STATUS_COMPLETED, 'Completed'),
    ]

    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    due_date = models.DateField(null=True, blank=True, validators=[validate_due_date])
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES, default=PRIORITY_MEDIUM)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default=STATUS_PENDING)
    owner = models.ForeignKey(User, related_name='tasks', on_delete=models.CASCADE)
    completed_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def mark_complete(self):
        if self.status == self.STATUS_COMPLETED:
            return
        self.status = self.STATUS_COMPLETED
        self.completed_at = timezone.now()
        self.save(update_fields=['status', 'completed_at'])

    def mark_incomplete(self):
        if self.status == self.STATUS_PENDING:
            return
        self.status = self.STATUS_PENDING
        self.completed_at = None
        self.save(update_fields=['status', 'completed_at'])

    def save(self, *args, **kwargs):
        if self.due_date and self.due_date < timezone.now().date():
            raise ValidationError('Due date must be in the future')
        if self.status == self.STATUS_COMPLETED and not self.completed_at:
            self.completed_at = timezone.now()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.title} ({self.priority}) - {self.status}"
