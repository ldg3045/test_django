from django.contrib import admin
from django.urls import include, path
from . import views 


urlpatterns = [
    path("admin/", admin.site.urls), # 관리자 페이지
    path("market_info/",views.market_info, name="market_info"), # 마켓 정보 페이지
    path("market_create/",views.market_create, name="market_create"), # 마켓 정보 생성 페이지
    path("market_update/",views.market_update, name="market_update"), # 마켓 정보 수정 페이지
    path("market_delete/",views.market_delete, name="market_delete"), # 마켓 정보 삭제 페이지
    # include 함수를 사용하여 다른 앱의 urls.py 파일을 포함
    path("customers/", include("customers.urls")), # 고객 정보 페이지
    path("products/",include("products.urls")), # 제품 정보 페이지
]