from django.contrib import admin
from profiles import models
from django.contrib.auth.models import Group


admin.site.register(models.UserProfile)
#admin.site.unregister(Group)
