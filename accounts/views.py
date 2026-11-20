
from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.db import IntegrityError
from .forms import MemberForm
from .models import MemberProfile


def member_create(request):
    if request.method == 'POST':
        form = MemberForm(request.POST)

        if form.is_valid():
            d = form.cleaned_data

            if User.objects.filter(username=d['username']).exists():
                form.add_error('username', 'This username already exists. Please choose another username.')
            else:
                try:
                    u = User.objects.create_user(
                        username=d['username'],
                        email=d['email'],
                        first_name=d['first_name'],
                        last_name=d['last_name'],
                        password=d['password']
                    )

                    MemberProfile.objects.create(
                        user=u,
                        member_id=d['member_id'],
                        phone=d['phone'],
                        department=d['department']
                    )

                    messages.success(request, 'Member created successfully!')
                    return redirect('members:list')

                except IntegrityError:
                    form.add_error(None, 'Unable to create member. Please check the details.')

    else:
        form = MemberForm()

    return render(request, 'members/member_form.html', {'form': form})
