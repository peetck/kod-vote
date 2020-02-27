from django.shortcuts import render
from .models import Poll, Poll_Vote, Poll_Choice
from django.contrib.auth.decorators import login_required, permission_required
import datetime

# Create your views here.
@login_required
def index_view(request):
    polls_avaliable = Poll.objects.filter(end_date__gt=datetime.datetime.now())
    polls_closed = Poll.objects.filter(end_date__lte=datetime.datetime.now())
    context = {
        'polls_avaliable' : polls_avaliable,
        'polls_closed' : polls_closed
    }
    return render(request, 'index.html', context)

@login_required
def create_view(request):
    if request.method == 'POST':
        subject = request.POST.get('subject')
        detail = request.POST.get('subject')
        picture = request.FILES['picture']
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')
        password = request.POST.get('password')

        Poll.objects.create(
            subject=subject,
            detail=detail,
            picture=picture,
            start_date=start_date,
            end_date=end_date,
            password=password,
            create_by=request.user
        )
    return render(request, 'create.html')

@login_required
def vote_view(request, poll_id):
    context = {}
    poll = Poll.objects.get(id=poll_id)
    if request.method == 'POST': # check what choice that ppl vote
        choice = Poll_Choice.objects.get(id=request.POST.get('choice'))
        vote = Poll_Vote.objects.create(
            poll_id=poll,
            choice_id=choice,
            vote_by=request.user
        )
    if poll.password != '': # if poll have password
        print(poll.subject)

    for vote in poll.poll_vote_set.all():
        if vote.vote_by == request.user:
            context['already_vote'] = f'คุณได้โหวตไปแล้ว : {vote.choice_id.subject}'
            break

    choices = poll.poll_choice_set.all()
    context['poll'] = poll
    context['choices'] = choices
    return render(request, 'vote.html', context)

@login_required
def edit_view(request, poll_id):
    poll = Poll.objects.get(id=poll_id)
    context = {'poll' : poll}
    return render(request, 'edit.html', context)
