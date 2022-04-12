from django.shortcuts import render

QUESTIONS = [
    {
        "title": f"Question №{i}",
        "text": f"# {i} Question text"
    } for i in range(1, 4)
]

def index(request):
    return render(request, 'index.html', {"questions": QUESTIONS})

def ask(request):
    return render(request, 'ask.html')

def question(request, i: int):
    return render(request, 'question.html', {"question": QUESTIONS[i-1]})