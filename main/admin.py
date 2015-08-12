from django.contrib import admin

from main.models import Cereal, Manufacturer, Nutritional_Information

# Register your models here.

admin.site.register(Cereal)
admin.site.register(Manufacturer)
admin.site.register(Nutritional_Information)
