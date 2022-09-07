from django.contrib import admin
from .models import aparteman , aparteman_images
# Register your models here.
class BookInline(admin.TabularInline):
    model = aparteman_images
    extra = 0

class customeaparteman(admin.ModelAdmin):
    inlines = [
        BookInline,
    ]
admin.site.register(aparteman,customeaparteman)
