from django.http import HttpResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt 
@require_POST
def example(request):
	return HttpResponse('Hello, world. This is the wejfkldsajfldskjbhook response.')