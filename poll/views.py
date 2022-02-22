from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import CreatePollForm
from .models import Poll

# Create your views here.
"""
    - home and create don't depend on the number of polls
    - vote and results have to work with a single poll
"""


def home(request):
    # getting all available polls 
    polls = Poll.objects.all()
    context = {
        'polls' : polls
    }
    return render(request, 'poll/home.html', context)


# using form from forms.py
def create(request):
    if request.method == 'POST':
        # instantiating form
        form = CreatePollForm(request.POST)

        # validate form & save it, then home
        if form.is_valid():
            # print(form.cleaned_data['question']) #prints data on console
            form.save()
            return redirect('home')
    else:
        # on GET request 
        form = CreatePollForm()

    context = {
        'form' : form
    }
    return render(request, 'poll/create.html', context)

# sqlite3 db.sqlite3 'select * from poll_poll' - to check polls in db.sqlite via command line


def vote(request, poll_id):
    poll = Poll.objects.get(pk=poll_id)

    if request.method == 'POST':

        selected_option = request.POST['poll']
        if selected_option == 'option1':
            poll.option_one_count += 1
        elif selected_option == 'option2':
            poll.option_two_count += 1
        elif selected_option == 'option3':
            poll.option_three_count += 1
        else:
            return HttpResponse(400, 'Invalid form')

        poll.save()

        return redirect('results', poll.id)

    context = {
        'poll' : poll
    }
    return render(request, 'poll/vote.html', context)


def results(request, poll_id):
    poll = Poll.objects.get(pk=poll_id)
    context = {
        'poll' : poll
    }
    return render(request, 'poll/results.html', context)