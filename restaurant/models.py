from django.db import models

# Create your models here.
class Restaurant(models.Model):
    # 이름
    name = models.CharField(max_length=50)
    # 주소
    address = models.CharField(max_length=255)
    # 전화번호
    phone = models.CharField(max_length=20)
    # 위도 전체 자릿수 : 9, 최대 소숫점 자리수: 6
    latitude = models.DecimalField(max_digits=9, decimal_places=6) 
    # 경도
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    # 점수. SmallIntegerField: -32,768부터 32,767 사이의 정수
    rating = models.SmallIntegerField()
    # 생성 시간. auto_now_add 는 객체가 처음 생성될때 시간
    created_at = models.DateTimeField(auto_now_add=True)
    # 업데이트 시간. auto_now 는 객체가 저장될때마다 현재 시간
    updated_at = models.DateTimeField(auto_now=True)