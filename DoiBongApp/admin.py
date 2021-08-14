from django.contrib import admin

# Register your models here.
from .models import Doibong
from .models import Cauthu

admin.site.register(Doibong)
admin.site.register(Cauthu)
