from django.shortcuts import render, redirect
from .models import Poll, Poll_Vote, Poll_Choice
from django.contrib.auth.decorators import login_required, permission_required
import pygal
from datetime import datetime
import pytz
from django.contrib.auth.models import User

# Create your views here.
@login_required
def index_view(request):
    polls = Poll.objects.all().order_by('-create_date')
    available, closed = [], []
    for poll in polls:
        if poll.is_available():
            available.append(poll)
        else:
            closed.append(poll)

    context = {
        'available' : available,
        'closed' : closed,
        'polls_length' : len(available) + len(closed)
    }

    return render(request, 'index.html', context)

@login_required
def create_view(request):
    if request.method == 'POST':
        subject = request.POST.get('subject').strip()
        detail = request.POST.get('detail')

        try:
            picture = request.FILES['picture']
        except:
            picture = None

        start_date = pytz.timezone('Asia/Bangkok').localize(datetime.strptime(request.POST.get('start_date'), '%d/%m/%Y %H:%M'))
        end_date = pytz.timezone('Asia/Bangkok').localize(datetime.strptime(request.POST.get('end_date'), '%d/%m/%Y %H:%M'))
        password = request.POST.get('password').strip()

        poll = Poll(
                subject=subject,
                detail=detail,
                start_date=start_date,
                end_date=end_date,
                password=password,
                create_by=request.user
        )

        if picture != None:
            poll.picture = picture

        poll.save()

        return redirect('mypolls')

    return render(request, 'create.html')

@login_required
def detail_view(request, poll_id):
    poll = Poll.objects.get(id=poll_id)
    already_vote = False
    context = {
        'poll' : poll
    }
    votes = poll.poll_vote_set.all()
    for vote in votes:
        if vote.vote_by == request.user:
            already_vote = True
            context['vote_choice'] = vote.choice_id.subject
            break

    choices = poll.poll_choice_set.all()
    context['choices'] = choices

    # pygal
    if not poll.is_available() or already_vote:
        chart = pygal.Bar()
        for choice in choices:
            chart.add(choice.subject, choice.poll_vote_set.all().count())
            context['graph'] = chart.render().decode('utf-8')

    context['already_vote'] = already_vote

    number_of_users = User.objects.all().count()
    number_of_votes = votes.count()
    context['number_of_users'] = number_of_users
    context['number_of_votes'] = number_of_votes
    context['left'] = number_of_users - number_of_votes

    context['success'] = request.GET.get('success')

    return render(request, 'detail.html', context)

@login_required
def vote_view(request, choice_id):
    choice = Poll_Choice.objects.get(id=choice_id)
    print(choice_id)
    poll = choice.poll_id

    for vote in request.user.poll_vote_set.all():
        if vote.poll_id == poll:
            # already vote
            return redirect('detail', poll_id=poll.id)

    success = 'success'
    if poll.is_available():
        if poll.password == '':
            vote = Poll_Vote.objects.create(
                poll_id=poll,
                choice_id=choice,
                vote_by=request.user
            )
        else:
            password = request.POST.get('password').strip()
            if password == poll.password:
                vote = Poll_Vote.objects.create(
                    poll_id=poll,
                    choice_id=choice,
                    vote_by=request.user
                )
            else:
                success = 'n-success'
    else:
        success = 'n-success'

    response = redirect('detail', poll_id=poll.id)
    response['Location'] += f'?success={success}'
    return response

@login_required
def edit_view(request, poll_id):
    poll = Poll.objects.get(id=poll_id)
    if request.user != poll.create_by:
        return redirect('index')
    context = {
        'poll' : poll,
        'msg' : request.GET.get('msg')
    }
    if request.method == 'POST':
        subject = request.POST.get('subject').strip()
        detail = request.POST.get('detail')

        password = request.POST.get('password')

        start_date = pytz.timezone('Asia/Bangkok').localize(datetime.strptime(request.POST.get('start_date'), '%d/%m/%Y %H:%M'))
        end_date = pytz.timezone('Asia/Bangkok').localize(datetime.strptime(request.POST.get('end_date'), '%d/%m/%Y %H:%M'))

        try:
            picture = request.FILES['picture']
            poll.picture = picture
        except:
            pass

        poll.subject = subject
        poll.detail = detail
        poll.password = password
        poll.start_date = start_date
        poll.end_date = end_date

        poll.save()

        context['success'] = 'แก้ไขกระทู้เรียบร้อยแล้ว'

    poll.is_available()

    return render(request, 'edit.html', context)

@login_required
def close_view(request, poll_id):
    poll = Poll.objects.get(id=poll_id)

    if poll.create_by == request.user and poll.is_active == True:
        poll.is_active = False
        poll.end_date = pytz.timezone('Asia/Bangkok').localize(datetime.now())
        poll.save()
        poll.is_available()

    response = redirect('edit', poll_id=poll_id)
    response['Location'] += f'?msg=close'
    return response

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
    if request.user != poll.create_by:
        return redirect('index')
    if request.method == 'POST':
        try:
            image = request.FILES['image']
        except:
            image = None
        choice = Poll_Choice(
            subject = request.POST.get('subject'),
            poll_id=poll
        )
        if image != None:
            choice.image = image
        choice.save()

        response = redirect('edit', poll_id=poll.id)
        response['Location'] += f'?msg=success'
        return response

    return render(request, 'add_choice.html', context)

@login_required
def choice_delete_view(request, choice_id):
    choice = Poll_Choice.objects.get(id=choice_id)
    poll = choice.poll_id

    if request.user != poll.create_by:
        return redirect('index')

    choice.delete()

    response = redirect('edit', poll_id=poll.id)
    response['Location'] += f'?msg=delete'
    return response