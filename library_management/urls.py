from django.contrib import admin
from django.urls import path, include
from accounts import views as av
from books import views as bv
from members import views as mv
from circulation import views as cv
urlpatterns = [
path('admin/',admin.site.urls), path('',av.dashboard,name='dashboard'),
path('login/',av.login_view,name='login'), path('logout/',av.logout_view,name='logout'),
path('books/',bv.book_list,name='book_list'), path('books/add/',bv.book_create,name='book_create'),
path('members/',mv.member_list,name='member_list'), path('members/add/',mv.member_create,name='member_create'),
path('circulation/',cv.circulation_list,name='circulation_list'), path('circulation/issue/',cv.issue_book,name='issue_book'),
path('circulation/<int:pk>/return/',cv.return_book,name='return_book'), path('api/',include('library_management.api_urls'))]
