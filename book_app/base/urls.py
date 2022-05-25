from django.urls import path
from .views import bookList, bookDetail, bookCreate, bookUpdate, DeleteView, CustomLoginView, RegisterPage, bookReorder
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', RegisterPage.as_view(), name='register'),

    path('', bookList.as_view(), name='books'),
    path('book/<int:pk>/', bookDetail.as_view(), name='book'),
    path('book-create/', bookCreate.as_view(), name='book-create'),
    path('book-update/<int:pk>/', bookUpdate.as_view(), name='book-update'),
    path('book-delete/<int:pk>/', DeleteView.as_view(), name='book-delete'),
    path('book-reorder/', bookReorder.as_view(), name='book-reorder'),
]
