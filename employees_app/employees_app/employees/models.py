from django.db import models
from django.urls import reverse


class AuditEntity(models.Model):
    created_on = models.DateTimeField(
        auto_now_add=True,
    )
    update_on = models.DateTimeField(
        auto_now=True,
    )

    class Meta:
        abstract = True


class Department(AuditEntity):
    name = models.CharField(
        max_length=20,
    )

    def get_absolute_url(self):
        return reverse('department details', kwargs={
            'id': self.id
        })

    def __str__(self):
        return self.name


class Employee(models.Model):
    SOFT_UNI = 'SoftUni'
    GOOGLE = 'Google'
    TWITTER = 'Twitter'
    COMPANIES = (SOFT_UNI, GOOGLE, TWITTER)

    first_name = models.CharField(
        max_length=30,
    )

    last_name = models.CharField(
        max_length=40,
        null=True,
        blank=True,
    )

    egn = models.CharField(
        max_length=10,
        unique=True,
        verbose_name='EGN',
    )

    job_title = models.IntegerField(
        choices=(
            (1, 'Software Developer'),
            (2, 'QA Engineer'),
            (3, 'DevOps Specialist'),
        )
    )

    company = models.CharField(
        max_length=max(len(c) for c in COMPANIES),
        choices=((c, c) for c in COMPANIES),
    )

    # One to Many
    department = models.ForeignKey(
        Department,
        on_delete=models.CASCADE,
    )

    class Meta:
        ordering = ('first_name', 'last_name')


class Project(models.Model):
    name = models.CharField(
        max_length=30,
    )

    dead_line = models.DateField(
        null=True,
        blank=True,
    )

    # Many to Many
    employees = models.ManyToManyField(
        to=Employee,
    )


class User(models.Model):
    email = models.EmailField()

    # One to One
    employee = models.OneToOneField(
        Employee,
        on_delete=models.CASCADE,
        primary_key=True
    )