from django.db import models

# Create your models here.
from django.utils import timezone
import random

# Create your models
class GuessNumbers(models.Model):
    name = models.CharField(max_length= 24)# 로또 번호 리스트의 이름
    text = models.CharField(max_length= 255)# 로또 번호 리스트에 대한 설명
    lottos = models.CharField(max_length=255, default='[1, 2, 3, 4, 5, 6]') # 로또 번호들이 담길 str
    num_lotto = models.IntegerField(default=5) # 6 개 번호 set 의 갯수
    update_date = models.DateTimeField()
    
    def generate(self): # 로또 번호를 자동으로 생성
        self.lottos = ""
        origin = list(range(1,46)) # 1~4 5 의 숫자 리스트 [1, 2, 3, ..., 43, 44,
        # 6 개 번호 set 갯수만큼 1~46 뒤섞은 후 앞의 6 개 골라내어 sorting
        for _ in range(0, self.num_lotto):
            random.shuffle(origin) # [10, 21, 36, 2, ... , 1,
            guess = origin[:6] # [10, 21, 36, 2, 15,
            guess.sort() # [2, 10, 15, 21, 23,
            self.lottos += str(guess) +'\n' # 로또 번호 str 에 6 개 번호 set 추가 '[2, 10, 15, 21, 23, n'
            # self.lottos : '[2, 10, 15, 21, 23, n[1, 15, 21 , 27, 30, n...'
        self.update_date = timezone.now()
        self.save() # GuessNumbers object 를 DB 에 저장
        
    def __str__(self):
        return "pk {} : {} - {}".format(self.pk, self.name, self.text) # pk는 자동생성됨
        
            