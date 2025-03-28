from django.shortcuts import render, get_object_or_404, redirect
from .models import Poll, Choice


# Create your views here.
def poll_list(request):
    polls = Poll.objects.all()
    return render(request, 'polls/poll_list.html', {'polls': polls})

def poll_detail(request, poll_id):
    poll = get_object_or_404(Poll, pk=poll_id)
    if request.method == 'POST':
        selected_choice = poll.choice_set.get(pk=request.POST['choice'])
        selected_choice.votes += 1
        selected_choice.save()
        return redirect('poll_results', poll_id=poll.id)
    return render(request, 'polls/poll_detail.html', {'poll': poll})

def poll_results(request, poll_id):
    poll = get_object_or_404(Poll, pk=poll_id)
    return render(request, 'polls/poll_results.html', {'poll': poll})
   