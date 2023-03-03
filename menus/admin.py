from django.contrib import admin

from menus.models import MenuItem,Menu


@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'parent')
    list_filter = ('menu',)
    fieldsets = (
        ('Add new item', {
            'description': "Parent should be a menu or item",
            'fields': (('menu', 'parent'), 'title')
            }),
            )


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ('title',)