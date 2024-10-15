# hotels/forms.py
import re
from django import forms
from .models import Hotel

class HotelForm(forms.ModelForm):
    class Meta:
        model = Hotel
        fields = ['name', 'postal_code', 'address', 'detail_address', 'contact_number', 'email','description']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '호텔명을 입력해주세요.'}),
            'postal_code': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '우편번호를 입력해주세요.', 'readonly': 'readonly'}),
            'address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '주소를 입력해주세요.', 'readonly': 'readonly'}),
            'detail_address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '상세 주소를 입력해주세요.'}),
            'contact_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '연락처를 입력해주세요.'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': '이메일을 입력해주세요.'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': '설명을 입력해주세요.', 'rows': 5}),
        }
        labels = {
            'name': '호텔명',
            'postal_code': '우편번호',
            'address': '주소',
            'detail_address': '상세 주소',
            'contact_number': '연락처',
            'email': '이메일',
            'description': '설명',
        }

    def clean_contact_number(self):
        contact_number = self.cleaned_data.get('contact_number')
        # 전화번호 패턴: 예시 "02-1234-1234", "010-1234-5678", "02 1234 1234" 등
        pattern = re.compile(r'^\d{2,3}[- ]?\d{3,4}[- ]?\d{4}$')
        if not pattern.match(contact_number):
            raise forms.ValidationError("올바른 연락처 형식을 입력해주세요 (예: 02-1234-1234).")
        return contact_number

    def clean_detail_address(self):
        detail_address = self.cleaned_data.get('detail_address')
        if not detail_address:
            raise forms.ValidationError("상세 주소를 입력해주세요.")
        return detail_address