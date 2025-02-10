from django.db import models
from test_market.models import TestMarket

class Product(models.Model):
    product_id = models.CharField(max_length=50)
    product_name = models.CharField(max_length=50)
    product_price = models.IntegerField()
    product_stock = models.IntegerField()
    # 외래키 변수명을 똑같이 지어준다(test_market_id)
    test_market_id = models.ForeignKey(TestMarket, on_delete=models.CASCADE, related_name= 'product')

""" customer 코드 설명
primary_key= True : 기본 키 설정(지정하여 유일성 보장,중복 방지)

CharField: 문자열을 저장
max_length : 문자열의 최대 길이

IntegerField: 정수를 저장

DateField : 날짜 필드
auto_now_add= True : 모델이 생성될 때 자동으로 현재 날짜와 시간을 설정

ForeignKey : 외래키 설정
on_delete= models.CASCADE : 삭제 했을 때= 참조하는 모델도 삭제(부모 테이블 삭제시 자식도 삭제)
related_name= 'product' : 역방향 참조 이름

"""