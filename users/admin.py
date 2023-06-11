from django.contrib import admin
from .models import *


from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .resources import UserResource

class UserAdmin(ImportExportModelAdmin):
    resource_class = UserResource

admin.site.unregister(User)  # Unregister the default User admin
admin.site.register(User, UserAdmin) 



admin.site.register(Profile)


