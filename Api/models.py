from django.db import models
from django.contrib.auth import get_user_model

from django.contrib.auth.models import BaseUserManager
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('Email is required')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('role_id', 1)
        if 'role' in extra_fields:
            del extra_fields['role']

        return self.create_user(email, password, **extra_fields)

class Role(models.Model):
    title = models.CharField(max_length=20, unique=True, null=False, verbose_name='Название роли')

    class Meta:
        verbose_name = 'Роль'
        verbose_name_plural = 'Роли'

    def __str__(self):
        return self.title

class User(AbstractBaseUser, PermissionsMixin):
    email = models.CharField(max_length=50, unique=True, null=False, verbose_name='Email')
    password = models.CharField(max_length=30, null=False, verbose_name='Пароль')
    full_name = models.CharField(max_length=70, null=False, verbose_name='ФИО')
    role = models.ForeignKey(Role, on_delete=models.CASCADE, default=3, null=False, verbose_name='Роль')
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['full_name']

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.full_name

class Ticket(models.Model):
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, verbose_name='Выложивший билеты')
    title = models.CharField(max_length=50, null=False, unique=True, verbose_name='Титульник билета')
    description = models.TextField(null=False, verbose_name='Описание')
    visiting_time = models.DateTimeField(auto_now_add=True, verbose_name='Время посещения')
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0, null=False, verbose_name='Цена')
    ticket_count = models.PositiveSmallIntegerField(default=0, null=False, verbose_name='Количество билетов')

    #Обновление количества оставшихся билетов после заказа
    def item_count_update(self, order_ticket_count):
        self.ticket_count -= order_ticket_count
        if self.ticket_count > 0:
            self.save()
        else:
            return f'Не хватает {self.ticket_count * -1}'

    class Meta:
        verbose_name = 'Билет'
        verbose_name_plural = 'Билеты'

    def __str__(self):
        pass