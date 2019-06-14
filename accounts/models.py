from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
USERNAME_REGEX = '^[a-zA-Z0-9.+-]*$'

class MyUserManager(BaseUserManager):
	def create_user(self, username, password=None):


		user = self.model(
					username = username
				)
		user.set_password(password)
		user.save(using=self._db)
		return user


	def create_superuser(self, username, password=None):
		user = self.create_user(
				username,  password=password
			)
		user.is_admin = True
		user.is_staff = True
		user.save(using=self._db)
		return user



class MyUser(AbstractBaseUser):
	username = models.CharField(max_length=300,	validators = [
		RegexValidator(regex = USERNAME_REGEX,
						message='Username must be alphanumeric or contain numbers',
						code='invalid_username')],unique=True)
	full_name = models.CharField(max_length=100, default='', blank=True)
	phone = models.CharField(max_length=20, blank=True, default='')
	city = models.CharField(max_length=100, default='', blank=True)
	nat_id = models.CharField(max_length=100, default='', blank=True)

	is_admin = models.BooleanField(default=False)
	is_staff = models.BooleanField(default=False)
	is_confirm = models.BooleanField(default=False)
	is_pack = models.BooleanField(default=False)
	is_livr = models.BooleanField(default=False)
	objects = MyUserManager()

	USERNAME_FIELD = 'username'
	REQUIRED_FIELDS = []

	def __str__(self):
    		return self.username

	def get_short_name(self):
		# The user is identified by their username
		return self.username


	def has_perm(self, perm, obj=None):
		"Does the user have a specific permission?"
		# Simplest possible answer: Yes, always
		return True

	def has_module_perms(self, app_label):
		"Does the user have permissions to view the app `app_label`?"
		# Simplest possible answer: Yes, always
		return True




