from django.contrib import admin

# Register your models here.
from auth_app.models import User

admin.site.register(User)
