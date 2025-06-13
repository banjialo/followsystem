from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

@login_required
def follow_toggle(request, username):
    target_user = get_object_or_404(User, username=username)
    user_profile = request.user.profile

    if target_user.profile in user_profile.follows.all():
        user_profile.follows.remove(target_user.profile)
    else:
        user_profile.follows.add(target_user.profile)

    return redirect('profile_detail', username=username)


def profile_detail(request, username):
    user = get_object_or_404(User, username=username)
    return render(request, 'userfollow/profile_detail.html', {'user': user})