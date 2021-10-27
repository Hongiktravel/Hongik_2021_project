from django.db import models

class Post(models.Model):#파이썬에서 제공하는 모델 사용
    title=models.CharField(max_length=50)#장고에서 제공하는기능 (보통 짧은 내용)
    content = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True) # 데이터베이스에 이런것들을 저장할수있도록 가능
    # author: 추후 작성 예정정
    updated_at=models.DateTimeField(auto_now=True)#수정됬을때는 수정된시간만 저장, 추가됬을때는 저절로 입력
    def __str__(self):
        return f'[{self.pk}]{self.title}'