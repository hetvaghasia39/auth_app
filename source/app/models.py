from django.db import models
from django.contrib.auth.models import AbstractUser, User
from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _
import sys
from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile


class CustomUser(User):
    profile_img = models.ImageField(
        _("profile image"),
        upload_to="images/",
        null=True,
        blank=True,
    )
    dob = models.DateField(_("date of birth"), auto_now=False, auto_now_add=False)
    designation = models.CharField(_("designation"), max_length=50)

    def __str__(self):
        return self.username

    def compressImage(self, uploadedImage):
        imageTemproary = Image.open(uploadedImage)
        outputIoStream = BytesIO()
        imageTemproaryResized = imageTemproary.resize((1020, 573))
        imageTemproaryResized.save(outputIoStream, format="JPEG", quality=60)
        outputIoStream.seek(0)
        profile_img = InMemoryUploadedFile(
            outputIoStream,
            "ImageField",
            "%s.jpg" % profile_img.name.split(".")[0],
            "image/jpeg",
            sys.getsizeof(outputIoStream),
            None,
        )
        return profile_img
