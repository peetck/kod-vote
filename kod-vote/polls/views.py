from django.shortcuts import render, redirect
from .models import Poll, Poll_Vote, Poll_Choice
from django.contrib.auth.decorators import login_required, permission_required
import datetime
import pygal
from django.conf import settings

# Create your views here.
@login_required
def index_view(request):
    polls_avaliable = Poll.objects.filter(end_date__gt=datetime.datetime.now()).order_by('-start_date')
    polls_closed = Poll.objects.filter(end_date__lte=datetime.datetime.now()).order_by('-end_date')
    context = {
        'polls_avaliable' : polls_avaliable,
        'polls_closed' : polls_closed
    }

    context['now'] = datetime.datetime.now()
    return render(request, 'index.html', context)

@login_required
def create_view(request):
    if request.method == 'POST':
        subject = request.POST.get('subject')
        detail = request.POST.get('detail')
        try:
            picture = request.FILES['picture']
        except:
            picture = settings.MEDIA_ROOT + '/poll/default.png'
        start_date = datetime.datetime.strptime(request.POST.get('start_date'), '%d/%m/%Y %H:%M')
        end_date = datetime.datetime.strptime(request.POST.get('end_date'), '%d/%m/%Y %H:%M')
        password = request.POST.get('password').strip()

        poll = Poll.objects.create(
            subject=subject,
            detail=detail,
            picture=picture,
            start_date=start_date,
            end_date=end_date,
            password=password,
            create_by=request.user
        )
        return redirect('mypolls')
    time = datetime.datetime.now()
    return render(request, 'create.html', {'time' : time})

@login_required
def detail_view(request, poll_id):
    context = {}
    poll = Poll.objects.get(id=poll_id)
    context['poll'] = poll

    for vote in poll.poll_vote_set.all():
        if vote.vote_by == request.user:
            context['already_vote'] = True
            break
    choices = poll.poll_choice_set.all()
    context['choices'] = choices
    context['now'] = datetime.datetime.now()
    # pygal
    pie_chart = pygal.Pie(width=1000)
    pie_chart.title = poll.subject
    for choice in choices:
       pie_chart.add(choice.subject, choice.poll_vote_set.all().count())
    context['graph'] = pie_chart.render().decode('utf-8')

    return render(request, 'detail.html', context)

@login_required
def vote_view(request, choice_id):
    choice = Poll_Choice.objects.get(id=choice_id)
    poll = choice.poll_id
    vote = Poll_Vote.objects.create(
        poll_id=poll,
        choice_id=choice,
        vote_by=request.user
    )
    return redirect('detail', poll_id=poll.id)

@login_required
def edit_view(request, poll_id):
    poll = Poll.objects.get(id=poll_id)
    context = {'poll' : poll}
    if request.method == 'POST':
        subject = request.POST.get('subject')
        detail = request.POST.get('detail')

        password = request.POST.get('password')

        poll.subject = subject
        poll.detail = detail
        poll.password = password

        poll.save()

        context['success'] = 'แก้ไข Poll เรียบร้อยแล้ว'

    return render(request, 'edit.html', context)

@login_required
def close_view(request, poll_id):
    poll = Poll.objects.get(id=poll_id)

    if poll.create_by == request.user:
        poll.end_date = datetime.datetime.now()
        poll.save()

    return redirect('mypolls')

@login_required
def poll_delete_view(request, poll_id):
    poll = Poll.objects.get(id=poll_id)

    if poll.create_by == request.user:
        poll.delete()

    return redirect('mypolls')

@login_required
def add_choice_view(request, poll_id):
    poll = Poll.objects.get(id=poll_id)
    context = {
        'poll' : poll
    }
    if request.method == 'POST':
        try:
            image = request.FILES['picture']
        except:
            image = settings.MEDIA_ROOT + '/choice/default.png'
        choice = Poll_Choice.objects.create(
            subject = request.POST.get('subject'),
            image = image,
            poll_id=poll
        )
        return redirect('edit', poll_id=poll.id)
    return render(request, 'add_choice.html', context)

@login_required
def choice_delete_view(request, choice_id):
    choice = Poll_Choice.objects.get(id=choice_id)

    poll_id = choice.poll_id.id

    choice.delete()

    return redirect('edit', poll_id=poll_id)