from django.shortcuts import redirect


def index(request):
    # 곧바로 /polls/로 redirect 되도록 설정
    return redirect('index')