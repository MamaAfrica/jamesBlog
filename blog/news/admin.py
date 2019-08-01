from django.contrib import admin
from .models import Post
from .models import Trend
# Register your models here.


class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'created'


admin.site.register(Post,PostAdmin)
admin.site.register(Trend,PostAdmin)