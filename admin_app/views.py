# admin_app/views.py

import re
from django.db import transaction
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import Profile
from django import forms

class AdminRegistrationForm(UserCreationForm):
    username = forms.CharField(
        label=_('아이디'), 
        required=True,
        widget=forms.TextInput(attrs={'placeholder': '아이디를 입력하세요'})
    )
    
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
    email = forms.EmailField(
        label=_('이메일'), 
        required=True,
        widget=forms.EmailInput(attrs={'placeholder': '이메일을 입력하세요'})
    )
    role = forms.ChoiceField(
        label=_('관리자 유형'), 
        choices=[('admin', _('관리자')), ('superadmin', _('슈퍼어드민'))],
        widget=forms.Select(attrs={'placeholder': '관리자 유형을 선택하세요'})
    )

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'manager_name', 'position', 'company', 'department', 'company_contact', 'manager_contact', 'role')

    def clean_username(self):
            username = self.cleaned_data.get('username')
            if not re.match(r'^[A-Za-z0-9]{8,20}$', username):
                raise ValidationError(_('아이디는 8~20자의 영문 대소문자 및 숫자만 사용할 수 있습니다.'), code='invalid_username')
            return username

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            with transaction.atomic():
                user.save()
                profile = Profile.objects.create(
                    user=user,
                    manager_name=self.cleaned_data['manager_name'],
                    position=self.cleaned_data.get('position'),
                    company=self.cleaned_data['company'],
                    department=self.cleaned_data.get('department'),
                    company_contact=self.cleaned_data.get('company_contact'),
                    manager_contact=self.cleaned_data['manager_contact'],
                    role=self.cleaned_data['role'],
                )
        return user
    
# 벌보스 네임 컨텍스트 반환 함수
def get_verbose_context(model_class, **kwargs):
    """verbose_name을 포함하는 컨텍스트 반환 함수"""
    context = {'verbose_name': model_class._meta.verbose_name}
    context.update(kwargs)
    return context



@login_required
def admin_create(request):
    if request.method == 'POST':
        form = AdminRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin_list')
    else:
        form = AdminRegistrationForm()
    return render(request, 'admin/admin_create.html', {'form': form})


@login_required
def admin_list(request):
    query_username = request.GET.get('username', '')
    query_manager_name = request.GET.get('manager_name', '')
    query_company = request.GET.get('company', '')

    # 조건에 맞는 queryset 필터링
    admins = Profile.objects.all()

    if query_username:
        admins = admins.filter(user__username__icontains=query_username)

    if query_manager_name:
        admins = admins.filter(manager_name__icontains=query_manager_name)

    if query_company:
        admins = admins.filter(company__icontains=query_company)

    paginator = Paginator(admins, 20)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'admin/admin_list.html', {
        'page_obj': page_obj,
        'query_username': query_username,
        'query_manager_name': query_manager_name,
        'query_company': query_company
    })


@login_required
def admin_detail(request, pk):
    profile = Profile.objects.get(id=pk)
    return render(request, 'admin/admin_detail.html', get_verbose_context(Profile, profile=profile))

@login_required
def admin_update(request, pk):
    profile = Profile.objects.get(id=pk)
    if request.method == 'POST':
        form = AdminRegistrationForm(request.POST, instance=profile.user)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            # Profile 업데이트
            profile.manager_name = form.cleaned_data['manager_name']
            profile.position = form.cleaned_data['position']
            profile.company = form.cleaned_data['company']
            profile.department = form.cleaned_data['department']
            profile.company_contact = form.cleaned_data['company_contact']
            profile.manager_contact = form.cleaned_data['manager_contact']
            profile.role = form.cleaned_data['role']
            profile.save()
            return redirect('admin_detail', pk=profile.id)
    else:
        form = AdminRegistrationForm(instance=profile.user)
    return render(request, 'admin/admin_update.html', get_verbose_context(Profile, form=form, profile=profile))