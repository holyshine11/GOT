# admin_app/forms.py

from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm
from django.utils.translation import gettext_lazy as _
import re
from django.core.exceptions import ValidationError
from .models import Profile 


# 사용자 정보 수정 폼(수정만)
class UserUpdateForm(UserChangeForm):
    password = None  # 비밀번호 필드를 숨깁니다.

    email = forms.EmailField(
        label=_('이메일'), 
        required=True,
        widget=forms.EmailInput(attrs={'placeholder': '이메일을 입력하세요'})
    )
    
    class Meta:
        model = User
        fields = ('email',)  # 'username' 필드 제외

class ProfileUpdateForm(forms.ModelForm):
    manager_name = forms.CharField(
        label=_('담당자 명'), 
        required=True,
        widget=forms.TextInput(attrs={'placeholder': '담당자 이름을 입력하세요'})
    )
    position = forms.CharField(
        label=_('직책/직급'), 
        required=False,
        widget=forms.TextInput(attrs={'placeholder': '직책을 입력하세요'})
    )
    company = forms.CharField(
        label=_('회사명'), 
        required=True,
        widget=forms.TextInput(attrs={'placeholder': '회사명을 입력하세요'})
    )
    department = forms.CharField(
        label=_('부서'), 
        required=False,
        widget=forms.TextInput(attrs={'placeholder': '부서를 입력하세요'})
    )
    company_contact = forms.CharField(
        label=_('회사 연락처'), 
        required=False,
        widget=forms.TextInput(attrs={'placeholder': '회사 연락처를 입력하세요'})
    )
    manager_contact = forms.CharField(
        label=_('담당자 연락처'), 
        required=True,
        widget=forms.TextInput(attrs={'placeholder': '담당자 연락처를 입력하세요'})
    )
    role = forms.ChoiceField(
        label=_('관리자 유형'), 
        choices=[('admin', _('관리자')), ('superadmin', _('슈퍼어드민'))],
        widget=forms.Select(attrs={'placeholder': '관리자 유형을 선택하세요'})
    )

    class Meta:
        model = Profile
        fields = ('manager_name', 'position', 'company', 'department', 'company_contact', 'manager_contact', 'role')