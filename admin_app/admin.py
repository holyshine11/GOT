# admin_app/admin.py

from django.contrib import admin
from .models import MeetingRoom, Profile
from .views import AdminRegistrationForm

from django.urls import reverse
from django.http import HttpResponseRedirect

from hotels.models import Hotel


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
    
    def changelist_view(self, request, extra_context=None):
        # 목록 뷰로 사용자 정의 URL로 리다이렉트
        return HttpResponseRedirect(reverse('admin_list'))

admin.site.register(Profile, ProfileAdmin)


@admin.register(Hotel)
class HotelAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'contact_number', 'email', 'created_at', 'updated_at')
    search_fields = ('name', 'address', 'email')
    list_filter = ('created_at', 'updated_at')
    
    def add_view(self, request, form_url='', extra_context=None):
        # 사용자 정의 호텔 생성 뷰로 리다이렉트
        return HttpResponseRedirect(reverse('hotel_create'))
    
    def changelist_view(self, request, extra_context=None):
        # 사용자 정의 호텔 리스트 뷰로 리다이렉트
        return HttpResponseRedirect(reverse('hotel_list'))