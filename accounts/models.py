import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

# Create your models here.
class customUsermanager(BaseUserManager):
    def create_user(self, email, type, password = None):
        if not email:
            raise ValueError('you must enter email in order to get')
        if not type:
            raise ValueError("you must choose a type")

        user = self.model(
            email = self.normalize_email(email),
            type = type,
            password= password
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, type, password):
        user = self.create_user(
            email = self.normalize_email(email),
            password =password,
            type = type
        )

        user.is_staff = True
        user.is_admin = True
        user.is_superuser = True
        user.save(using = self._db)
        return user


class customUser(AbstractUser):
    username = None
    email = models.EmailField(verbose_name='email', max_length=45, unique=True)
    user_id = models.UUIDField(verbose_name='Registration ID', default=uuid.uuid4, primary_key=True, unique=True)
    type = models.CharField(max_length=50, choices=(('retailer', 'retailer'), ('wholesaler', 'wholesaler'), ('manufacturer', 'manufacturer'), ('customer', 'customer '), ('admin','admin')))
    date_joined = models.DateTimeField(verbose_name='Date Joined', auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='last Login', auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    adhaar_number = models.IntegerField(max_length=12, default= 000000000000)
    bank_account_number = models.IntegerField(max_length=45, default= 000000000000)
    PAN = models.CharField(max_length=45, default= '')
    address = models.CharField(max_length=45, default='')
    PIFSC = models.CharField(max_length=45, default='')
    verified = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['type']
    objects = customUsermanager()
    def __str__(self):
        return (str(self.user_id))
    def has_perm(self, perm, obj=None):
        return self.is_admin
    def has_module_perms(self, app_label):
        return True