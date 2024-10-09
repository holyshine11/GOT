# admin_app/admin.py

from django.contrib import admin
from .models import MeetingRoom, Profile
from .views import AdminRegistrationForm

from django.urls import reverse
from django.http import HttpResponseRedirect
from .models import Profile


@admin.register(MeetingRoom)
class MeetingRoomAdmin(admin.ModelAdmin):
    list_display = ('name', 'capacity', 'location')
    search_fields = ('name', 'location')

class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'manager_name', 'company', 'manager_contact', 'role']
    readonly_fields = ['user']

    def add_view(self, request, form_url='', extra_context=None):
        # 사용자 정의 뷰로 리다이렉트하기 위해 HttpResponseRedirect 사용
        return HttpResponseRedirect(reverse('admin_create'))

admin.site.register(Profile, ProfileAdmin)