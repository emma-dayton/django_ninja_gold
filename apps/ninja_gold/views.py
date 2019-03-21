from django.shortcuts import render, HttpResponse, redirect
from random import randint

# Create your views here.
def index(request):
    if 'score' not in request.session:
        request.session['score'] = 0
    if 'lives' not in request.session:
        request.session['lives'] = 10
    if 'attempts' not in request.session:
        request.session['attempts'] = 0
    if 'activity' not in request.session:
        request.session['activity'] = []
    return render(request, 'index.html')

def process_money(request):
    score_dict = {
    'farm':randint(8,12),
    'cave':randint(10,30),
    'house':randint(5,15),
    'casino':randint(-47,50), # wanted to be friendly with the odds
    }
    cave_danger = randint(2,4) # cave risks losing extra turns, justifying the higher rewards
    request.session['attempts'] += 1
    attempt = request.session['attempts']
    building = request.POST['building']
    score = score_dict[request.POST['building']]
    activity = f'{attempt}. Found {score} pieces of gold in the {building}.'
    if request.method == 'POST':
        request.session['score'] += score
        if request.POST['building'] == 'cave':
            request.session['lives'] -= cave_danger
            activity = activity + ' You lost ' + str(cave_danger) + ' tries in the Cave!'
        else:
            request.session['lives'] -= 1
        request.session['activity'].insert(0, activity)
    print(request.session['activity'], '%%%%%%%%%%%%%%%%%%%%%%')
    return redirect('/')

def reset(request):
    request.session.flush()
    return redirect('/')
