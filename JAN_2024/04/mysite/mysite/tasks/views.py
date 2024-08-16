from django.http import HttpResponse
from django.shortcuts import render

from mysite.tasks.models import Task

# Create your views here.
"""
Function Base View:
needs
1. Func that has one or more parameters
2. returns response
"""


# def index(request):
#     tasks_list = Task.objects.all()
#     output = "<p>".join(f"<h2>{t.title}: </h2> <p>{t.text}"for t in tasks_list)
#     if not output:
#         output = "There are no created tasks!"
#
#     return HttpResponse(output)

# def index(request):
#     tasks_list = Task.objects.all()
#     output = "<p>".join(f"<h2>{t.title}: </h2> <p>{t.text}"for t in tasks_list)
#     if not output:
#         output = "There are no created tasks!"
#
#     return render(request, 'tasks/index.html')
def index(request):
    tasks_list = Task.objects.all()
    output = "; ".join(f"{t.title}: {t.text}"for t in tasks_list)
    if not output:
        output = "There are no created tasks!"

    content = {
        'title': 'The tasks app.',
        'tasks': output,
        'tasks_count': tasks_list.count(),
    }

    return render(
        request,
        'tasks/index.html',
        content,
    )
