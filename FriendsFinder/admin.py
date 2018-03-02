from django.contrib import admin
from FriendsFinder.models import Category, Page
from FriendsFinder.models import UserProfile


admin.site.register(Category)
admin.site.register(UserProfile)


class PageAdmin(admin.ModelAdmin):
	list_display = ('title', 'category', 'url')
#admin.site.register(Page, PageAdmin)

	
class CategoryAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug':('name',)}
# Update the registration to include this customised interface
admin.site.unregister(Category)
admin.site.register(Category, CategoryAdmin)	
	
	
