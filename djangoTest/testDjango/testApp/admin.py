from django.contrib import admin
from .models import Example, Task, UserProfile, Room, Message

admin.site.register(Example)
admin.site.register(Task)


class UserProfileAdmin(admin.ModelAdmin):

    list_display = ["data", "genre", "address", "age", "email", "image", "bit", "birth_date"]


admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(Room)
admin.site.register(Message)
