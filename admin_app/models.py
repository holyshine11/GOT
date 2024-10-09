# admin_app/models.py

from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

class Profile(models.Model):
    ROLE_CHOICES = [
        ('admin', '관리자'),
        ('superadmin', '슈퍼어드민'),
    ]
    
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name=_('아이디'))
    manager_name = models.CharField(max_length=100, verbose_name=_('담당자 이름'))
    position = models.CharField(max_length=100, blank=True, null=True, verbose_name=_('직책'))
    company = models.CharField(max_length=100, verbose_name=_('회사명'))
    department = models.CharField(max_length=100, blank=True, null=True, verbose_name=_('부서'))
    company_contact = models.CharField(max_length=20, blank=True, null=True, verbose_name=_('회사 연락처'))
    manager_contact = models.CharField(max_length=20, verbose_name=_('담당자 연락처'))
    role = models.CharField(max_length=20, choices=[('admin', '관리자'), ('superadmin', '슈퍼어드민')], verbose_name=_('역할'))
    
    class Meta:
        verbose_name = _('관리자 관리')
        verbose_name_plural =_('관리자 관리')
    
    def __str__(self):
        return self.manager_name
    
    
class MeetingRoom(models.Model):
    name = models.CharField(max_length=100)
    capacity = models.IntegerField()
    location = models.CharField(max_length=255)

    class Meta:
        verbose_name = _('미팅룸 관리')
        verbose_name_plural = _('미팅룸 관리')
    
    def __str__(self):
        return self.name

class Reservation(models.Model):
    room = models.ForeignKey(MeetingRoom, on_delete=models.CASCADE)
    reserved_by = models.CharField(max_length=100)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()

    class Meta:
        verbose_name = _('예약 관리')
        verbose_name_plural = _('예약 관리')
        
    def __str__(self):
        return f"{self.room.name} - {self.date} {self.start_time} to {self.end_time}"