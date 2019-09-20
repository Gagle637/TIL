import requests
from pprint import pprint
from faker import Faker
from decouple import config
from django.shortcuts import render
from .models import Jobs 




# Create your views here.
def index(request):
    # if request.method == 'POST':
    #     name=request.POST.get('name')
        
    #     past_job = Faker('ko_KR').job()
    #     jobs = Jobs(name=name, past_job=past_job)
    #     jobs.save()
    #     context = {'jobs':jobs}
    #     return render(request, 'jobs/result.html', context)
    # else:
    return render(request, 'jobs/index.html')


def past_life(request):
    #사용자로부터 이름
    name = request.POST.get('name')

    #db에 매칭되는 name 가져오기
    #Jobs.objects.get(name=name)
    #get이 간단하지만 해당 값이 없을 경우 에러가 발생한다.
    #filter : 한개던 0개던 상관없이 무조건 쿼리셋으로 가져옴
    # filter는 한개던 0개던 상관없이 가져옴
    person = Jobs.objects.filter(name=name).first()

    #db에 person이 있는지 없는지 판단
    if person:
        past_job = person.past_job
    else: #db에 기존 이름이 없다면(즉 person이 빈 쿼리셋)
        faker = Faker()
        past_job = faker.job()
        person = Jobs(name=name, past_job=past_job) #새로운 레코드를 추가한다.
        person.save()

    #GIPHY (past_job 을 API 에 요청을 보내서 응답을 받음)
    GIPHY_API_KEY = config('GIPHY_API_KEY')
    url = f'http://api.giphy.com/v1/gifs/search?api_key={GIPHY_API_KEY}&q={past_job}&limit=1'
    data = requests.get(url).json()
    try:
      image = data.get('data')[0].get('images').get('original').get('url')
    except IndexError:
        image = None

    context = {'person':person, 'image':image,}
    return render(request, 'jobs/past_life.html', context)




