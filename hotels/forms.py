# hotels/forms.py

import re
from django import forms
from .models import Hotel

class HotelForm(forms.ModelForm):
    class Meta:
        model = Hotel
        fields = [
            'name', 'postal_code', 'address', 'detail_address',
            'contact_number', 'email', 'description',
            'business_number', 'settlement_date', 'logo'
        ]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '호텔명을 입력해주세요.'}),
            'postal_code': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '우편번호를 입력해주세요.', 'readonly': 'readonly'}),
            'address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '주소를 입력해주세요.', 'readonly': 'readonly'}),
            'detail_address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '상세 주소를 입력해주세요.'}),
            'contact_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '연락처를 입력해주세요.'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': '이메일을 입력해주세요.'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': '설명을 입력해주세요.', 'rows': 5}),
            'business_number': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '사업자 번호를 입력해주세요 (예: 123-45-67890).',
                'pattern': r'\d{3}-\d{2}-\d{5}',
                'title': '사업자 번호 형식: 123-45-67890',
            }),
            'settlement_date': forms.Select(attrs={'class': 'form-control'}),
            'logo': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'name': '호텔명',
            'postal_code': '우편번호',
            'address': '주소',
            'detail_address': '상세 주소',
            'contact_number': '연락처',
            'email': '이메일',
            'description': '설명',
            'business_number': '사업자 번호',
            'settlement_date': '정산일',
            'logo': '호텔 로고 이미지',
        }

    def clean_contact_number(self):
        contact_number = self.cleaned_data.get('contact_number')
        pattern = re.compile(r'^\d{2,3}[- ]?\d{3,4}[- ]?\d{4}$')
        if not pattern.match(contact_number):
            raise forms.ValidationError("올바른 연락처 형식을 입력해주세요 (예: 02-1234-1234).")
        return contact_number

    def clean_detail_address(self):
        detail_address = self.cleaned_data.get('detail_address')
        if not detail_address:
            raise forms.ValidationError("상세 주소를 입력해주세요.")
        return detail_address

    def clean_business_number(self):
        business_number = self.cleaned_data.get('business_number')
        pattern = re.compile(r'^\d{3}-\d{2}-\d{5}$')  # 형식: 123-45-67890
        if not pattern.match(business_number):
            raise forms.ValidationError("올바른 사업자 번호 형식을 입력해주세요 (예: 123-45-67890).")
        return business_number


    def clean_logo(self):
        logo = self.cleaned_data.get('logo')
        if logo:
            if logo.size > 5 * 1024 * 1024:
                raise forms.ValidationError("파일 크기가 5MB를 초과합니다.")
            if not logo.name.lower().endswith(('.jpg', '.jpeg', '.png')):
                raise forms.ValidationError("jpg 또는 png 파일만 업로드 가능합니다.")
        return logo