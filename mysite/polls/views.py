from django.http import HttpResponse
from django.http import Http404
from django.template import loader
from django.shortcuts import get_object_or_404, render

from .models import Question


# When somebody requests a page from your website – say, “/polls/34/”, Django will load the mysite.urls Python module 
# because it’s pointed to by the ROOT_URLCONF setting. It finds the variable named urlpatterns and traverses the patterns in order. 
# After finding the match at 'polls/', it strips off the matching text ("polls/") and sends the remaining text – "34/" – to the ‘polls.urls’ URLconf 
# for further processing. There it matches '<int:question_id>/', resulting in a call to the detail() view like so:

# def index(request):
#     return HttpResponse("Hello, world. You're at the polls index.")

# #option 1
# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     output = ', '.join([q.question_text for q in latest_question_list])
#     return HttpResponse(output)

# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     template = loader.get_template('polls/index.html')
#     context = {
#         'latest_question_list': latest_question_list,
#     }
#     return HttpResponse(template.render(context, request))

#option 2
# The render() function takes the request object as its first argument, a template name as its second argument 
# and a dictionary as its optional third argument. It returns an HttpResponse object of the given template rendered with the given context.
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)



#default
# def detail(request, question_id):
#     return HttpResponse("You're looking at question %s." % question_id)

#raise 404 error
def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'polls/detail.html', {'question': question})

#with idiom
# def detail(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/detail.html', {'question': question})






def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)