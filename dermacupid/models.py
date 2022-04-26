
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin, UserManager, AbstractUser
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.core.mail import send_mail
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


# class User(AbstractBaseUser, PermissionsMixin):
#     """
#     An abstract base class implementing a fully featured User model with
#     admin-compliant permissions.
#
#     Username and password are required. Other fields are optional.
#     """
#
#     username_validator = UnicodeUsernameValidator()
#
#     username = models.CharField(
#         _("username"),
#         max_length=150,
#         unique=True,
#         help_text=_(
#             "Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only."
#         ),
#         validators=[username_validator],
#         error_messages={
#             "unique": _("A user with that username already exists."),
#         },
#     )
#     first_name = models.CharField(_("first name"), max_length=150, blank=True)
#     last_name = models.CharField(_("last name"), max_length=150, blank=True)
#     email = models.EmailField(_("email address"), blank=True)
#     phone_number = models.IntegerField(_("phone number"), blank=True)
#     is_staff = models.BooleanField(
#         _("staff status"),
#         default=False,
#         help_text=_("Designates whether the user can log into this admin site."),
#     )
#     is_active = models.BooleanField(
#         _("active"),
#         default=True,
#         help_text=_(
#             "Designates whether this user should be treated as active. "
#             "Unselect this instead of deleting accounts."
#         ),
#     )
#     date_joined = models.DateTimeField(_("date joined"), default=timezone.now)
#
#     objects = UserManager()
#
#     EMAIL_FIELD = "email"
#     USERNAME_FIELD = "username"
#     REQUIRED_FIELDS = ["email"]
#
#     class Meta:
#         verbose_name = _("user")
#         verbose_name_plural = _("users")
#         abstract = True
#
#     def clean(self):
#         super().clean()
#         self.email = self.__class__.objects.normalize_email(self.email)
#
#     def get_full_name(self):
#         """
#         Return the first_name plus the last_name, with a space in between.
#         """
#         full_name = "%s %s" % (self.first_name, self.last_name)
#         return full_name.strip()
#
#     def get_short_name(self):
#         """Return the short name for the user."""
#         return self.first_name
#
#     def email_user(self, subject, message, from_email=None, **kwargs):
#         """Send an email to this user."""
#         send_mail(subject, message, from_email, [self.email], **kwargs)


class User(models.Model):
    phoneno = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return str(self.phoneno)


class UserProfile(models.Model):
    phoneno = models.OneToOneField(User, on_delete=models.CASCADE, primary_key= True)
    occupation = models.CharField(max_length=10, null=True, blank=True)
    marital_status = models.CharField(max_length=10, null=True, blank=True)
    religion = models.CharField(max_length=10, null=True, blank=True)
    skin_condition = models.CharField(max_length=10, null=True, blank=True)
    dob = models.CharField(max_length=10, null=True, blank=True)
    country = models.CharField(max_length=10, null=True, blank=True)
    state = models.CharField(max_length=10, null=True, blank=True)
    city = models.CharField(max_length=10, null=True, blank=True)
    highest_education = models.CharField(max_length=10, null=True, blank=True)
    education_field = models.CharField(max_length=10, null=True, blank=True)
    profession = models.CharField(max_length=10, null=True, blank=True)
    first_name = models.CharField(max_length=20, null=True, blank=True)
    last_name = models.CharField(max_length=20, null=True, blank=True)
    
    profile_picture_1 = models.ImageField(null=True, blank=True)
    profile_picture_2 = models.ImageField(null=True, blank=True)
    profile_picture_3 = models.ImageField(null=True, blank=True)
    profile_picture_4 = models.ImageField(null=True, blank=True)
    profile_picture_5 = models.ImageField(null=True, blank=True)
    profile_picture_6 = models.ImageField(null=True, blank=True)

    def __str__(self):
        return str(self.first_name)
