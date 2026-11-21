
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect
from django import forms
from django.contrib import messages
from django.db import IntegrityError

from accounts.models import MemberProfile

User = get_user_model()


class MemberForm(forms.Form):
    username = forms.CharField(max_length=150)
    email = forms.EmailField()
    first_name = forms.CharField(max_length=150)
    last_name = forms.CharField(max_length=150, required=False)
    password = forms.CharField(widget=forms.PasswordInput)
    member_id = forms.CharField(max_length=30)
    phone = forms.CharField(max_length=20, required=False)
    department = forms.CharField(max_length=100, required=False)


@staff_member_required
def member_list(request):
    return render(
        request,
        'members/member_list.html',
        {'members': MemberProfile.objects.select_related('user').all()}
    )


@staff_member_required
def member_create(request):
    form = MemberForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        d = form.cleaned_data

        if User.objects.filter(username=d['username']).exists():
            form.add_error(
                'username',
                'This username already exists. Please choose another.'
            )
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
                return redirect('member_list')

            except IntegrityError:
                form.add_error(
                    None,
                    'Unable to create member. Check the username and member ID.'
                )

    return render(request, 'members/member_form.html', {'form': form})
