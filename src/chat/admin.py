from django.contrib import admin


from .models import Thread, ChatMessage

class ChatMessage(admin.TabularInline):
    model = ChatMessage

class ThreadAdmin(admin.ModelAdmin):
    inlines = [ChatMessage]
    class Meta:
        model = Thread 


admin.site.register(Thread, ThreadAdmin)
