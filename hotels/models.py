# hotels/models.py

from django.db import models

class Hotel(models.Model):
    name = models.CharField(max_length=255, verbose_name="호텔명")
    postal_code = models.CharField(max_length=5, verbose_name="우편번호", default='우편번호 5자리')
    address = models.CharField(max_length=500, verbose_name="주소")
    detail_address = models.CharField(max_length=255, blank=True, null=True, verbose_name="상세 주소")
    contact_number = models.CharField(max_length=20, verbose_name="연락처")
    email = models.EmailField(verbose_name="이메일")
    description = models.TextField(blank=True, null=True, verbose_name="설명")
    business_number = models.CharField(max_length=12, verbose_name="사업자 번호", default='')
    SETTLEMENT_DATE_CHOICES = [
        ('', '선택'),
        ('익월 1일', '익월 1일'),
        ('익월 5일', '익월 5일'),
        ('익월 10일', '익월 10일'),
        ('익월 15일', '익월 15일'),
        ('익월 20일', '익월 20일'),
        ('익월 25일', '익월 25일'),
        ('익월 30일', '익월 30일'),
    ]
    settlement_date = models.CharField(
        max_length=10, 
        choices=SETTLEMENT_DATE_CHOICES, 
        verbose_name="정산일",
        default=''
    )
    logo = models.ImageField(upload_to='hotel_logos/', blank=True, null=True, verbose_name="호텔 로고 이미지")

    created_at = models.DateTimeField(auto_now_add=True, verbose_name="등록일")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="수정일")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "호텔"
        verbose_name_plural = "호텔들"