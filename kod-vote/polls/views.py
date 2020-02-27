from django.shortcuts import render
from .models import Poll
import datetime

# Create your views here.
def index_view(request):
    polls_avaliable = Poll.objects.filter(end_date__gt=datetime.datetime.now())
    polls_closed = Poll.objects.filter(end_date__lte=datetime.datetime.now())
    context = {
        'polls_avaliable' : polls_avaliable,
        'polls_closed' : polls_closed
    }
    return render(request, 'index.html', context)

def create_view(request):
    return render(request, 'create.html')

def vote_view(request, poll_id):
    poll = Poll.objects.get(id=poll_id)
    if (request.method == 'POST'): # check what choice that ppl vote
        print(request.POST)
    if (poll.password != ''): # if poll have password
        print(poll.subject)
    choices = poll.poll_choice_set.all()
    context = {'poll' : poll, 'choices' : choices}
    return render(request, 'vote.html', context)

def edit_view(request, poll_id):
    poll = Poll.objects.get(id=poll_id)
    context = {'poll' : poll}
    return render(request, 'edit.html', context)
