from django.shortcuts import render, redirect


def get_teeTime(request):
    if request.method == "POST":
        form = teeTimeForm(request.POST, request.FILES)
        if form.is_valid():
            return render(request.POST, {'form': form})
    else:
        return render (redirect(to='teetimeMessage.html'))


#
#
# def sendteeTime(request):
#     if request.method == "POST":
#         form = get_teeTime(request.POST, request.FILES)
#         if form.is_valid():
#             post = form.save(commit=False)
#             post.author = request.user
#             post.published_date = timezone.now()
#             post.save()
#             return redirect(post_detail, post.pk)
#     else:
#         form = get_teeTime()
#     return render(request, 'teetime.html', {'form': form})