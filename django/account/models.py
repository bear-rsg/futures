from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager


class CustomUserManager(UserManager):
    def get_by_natural_key(self, username):
        """
        Allow users to login with case-insensitive username

        E.g. both "My.Name@uni.ac.uk" and "my.name@uni.ac.uk" will allow users to login
        """
        return self.get(username__iexact=username)


class User(AbstractUser):
    """
    Custom user extends the standard Django user model, providing additional properties
    """

    email = models.EmailField()  # override default email field, not allowing it to be blank/null as used as username

    # Custom user manager used to allow for case-insensitive usernames
    objects = CustomUserManager()

    @property
    def name(self):
        if self.first_name and self.last_name:
            return ' '.join((self.first_name, self.last_name))
        elif self.first_name:
            return self.first_name
        elif self.last_name:
            return self.last_name
        else:
            # If no first or last name provided, return first half of email
            return self.username.split('@')[0]  # e.g. mike.allaway in mike.allaway@bham.ac.uk

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        # Ensure all accounts are 'staff' so can access admin dashboard
        self.is_staff = True
        # Force email and username to be lower case and identical, so users can login with email
        self.email = self.email.strip().lower()
        self.username = self.email

        super().save(*args, **kwargs)
