from django.shortcuts import render, redirect


def get_teeTime(request):
    if request.method == "POST":
        form = teeTimeForm(request.POST, request.FILES)
        if form.is_valid():
            return render(request.POST, {'form': form})
    else:
        return render (redirect(to='teetimeMessage.html'))


