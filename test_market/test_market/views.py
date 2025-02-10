from django.shortcuts import render,redirect
from test_market.models import TestMarket
from test_market.forms import TestMarket_Form


""" 변수 설정 구분

단일 객체 : test_market
복수 객체 : test_market_list



"""


# 생성
def market_create(request):
    if request.method == "POST": # POST 요청일 경우
        form = TestMarket_Form(request.POST) # 폼 생성
        if form.is_valid(): # 폼이 유효한 경우
            test_market = form.save() # 폼 저장
            return redirect("market_info",test_market) # 수정 후 조회 페이지로 리다이렉트
    else: # GET 요청일 경우

        form = TestMarket_Form() # 폼 생성

    context = {"form": form} # 폼과 이전 글 내용을 컨텍스트에 저장
    return render(request, "market_info.html", context) # GET 요청일 경우 폼과 이전 글 내용을 불러옴


# 조회
def market_info(request):
    if request.method == "GET":
        test_market_list = TestMarket.objects.all() # 가구 리스트로 조회 후
        context = {"test_market_list": test_market_list} # 컨텍스트에 저장
        return render(request, "market_info.html", context)  # 조회 페이지로 이동


# 수정
def market_update(request, pk):  # 수정할 객체(pk) 조회
    test_market = TestMarket.objects.get(pk=pk)  # 수정할 객체 조회
    if request.method == "POST": # POST 요청일 경우
        form = TestMarket_Form(request.POST, instance=test_market) # instance=test_market : 이전 글 내용을 불러옴
        if form.is_valid(): # 폼이 유효한 경우
            form.save() # 폼 저장

            return redirect("market_info") # 수정 후 조회 페이지로 리다이렉트
    else: # GET 요청일 경우
        form = TestMarket_Form(instance=test_market) # instance=test_market : 이전 글 내용을 불러옴

    context = { "form": form } # 폼과 이전 글 내용을 컨텍스트에 저장
    return render(request, "market_info.html", context) # GET 요청일 경우 폼과 이전 글 내용을 불러옴


# 삭제          
def market_delete(request, pk):# 삭제할 객체(pk) 조회
    if request.method == "POST": # POST 요청일 경우
        test_market = TestMarket.objects.get(pk=pk) # 삭제할 객체 조회
        test_market.delete() # 객체 삭제
        return redirect("market_info") # 삭제 후 조회 페이지로 리다이렉트


