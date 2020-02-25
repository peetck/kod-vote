from django.shortcuts import render

# Create your views here.
def index_view(request):
    return render(request, 'index.html')

def create_view(request):
    return render(request, 'create.html')

def vote_view(request, poll_id):
    context = {'poll_id' : poll_id}
    return render(request, 'vote.html', context)

def edit_view(request, poll_id):
    context = {'poll_id' : poll_id}
    return render(request, 'edit.html', context)
