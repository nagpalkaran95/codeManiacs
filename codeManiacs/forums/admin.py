from django.contrib import admin
from forums.models import Forum,Answer

# Register your models here.
class ForumModelAdmin(admin.ModelAdmin):
    readonly_fields = ('pk',)

admin.site.register(Forum,ForumModelAdmin)
admin.site.register(Answer)