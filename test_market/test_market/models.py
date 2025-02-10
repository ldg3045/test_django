from django.db import models

# 테스트 마켓
class TestMarket(models.Model):
    test_market_id = models.CharField(max_length= 50, primary_key= True)
    test_market_location = models.CharField(max_length= 50)
    test_market_manager = models.CharField(max_length= 50)
    test_market_tell = models.CharField(max_length= 50)
    test_market_open = models.DateField(auto_now_add= True)
    test_market_staff = models.IntegerField()