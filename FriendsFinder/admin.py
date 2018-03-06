from django.contrib import admin
from FriendsFinder.models import *


#admin.site.register(Category)
admin.site.register(UserProfile)
admin.site.register(Character)
admin.site.register(Question)
admin.site.register(Thread)
admin.site.register(ThreadComment)


#class PageAdmin(admin.ModelAdmin):
#	list_display = ('title', 'category', 'url')
#admin.site.register(Page, PageAdmin)

	
#class CategoryAdmin(admin.ModelAdmin):
#	prepopulated_fields = {'slug':('name',)}
# Update the registration to include this customised interface
#admin.site.unregister(Category)
#admin.site.register(Category, CategoryAdmin)
	
	
