from django import forms
from .models import TestMarket

class TestMarket_Form(forms.ModelForm):
    class Meta: 
        model = TestMarket
        fields = [ "test_market_id", # 마켓 아이디
                   "test_market_location", # 마켓 위치
                   "test_market_manager", # 마켓 관리자
                   "test_market_tell", # 마켓 전화번호
                   "test_staff_num", # 마켓 직원 수
            ]

        # 제외할 필드 : 마켓 오픈한 날짜 여부 제외
        exclude = ["test_market_open",
            ] 