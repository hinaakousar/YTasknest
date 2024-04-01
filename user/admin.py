from django.contrib import admin

# Register your models here.
class user_s(admin.ModelAdmin):
    fields = ["name", "Email"]