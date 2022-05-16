from django.contrib import admin
from db.models import user_model


admin.site.register(user_model.User)
