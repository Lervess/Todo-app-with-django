from django.contrib import admin
from .models import Todo,Category,Tag

class CategoryAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'pk',
        'is_active',
    ]
 
class TodoAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'pk',
        'category',
        'is_active',
        # 'created_at',
        # 'updated_at',
    ]

    list_display_links = [
        'pk',
        'title',
        'category',
    ]

admin.site.register(Todo,TodoAdmin)
admin.site.register(Category,CategoryAdmin)
admin.site.register(Tag)