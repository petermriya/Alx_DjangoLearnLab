from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, permission_required
from django.http import HttpResponseForbidden
from .models import CustomUser
from .forms import CustomUserCreationForm  # if you’ve created a custom form

# View all users - Requires 'can_view'
@permission_required('bookshelf.can_view', raise_exception=True)
def user_list(request):
    users = CustomUser.objects.all()
    return render(request, 'bookshelf/user_list.html', {'users': users})

# Create user - Requires 'can_create'
@permission_required('bookshelf.can_create', raise_exception=True)
def create_user(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user_list')
    else:
        form = CustomUserCreationForm()
    return render(request, 'bookshelf/create_user.html', {'form': form})

# Edit user - Requires 'can_edit'
@permission_required('bookshelf.can_edit', raise_exception=True)
def edit_user(request, user_id):
    user = get_object_or_404(CustomUser, pk=user_id)
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('user_list')
    else:
        form = CustomUserCreationForm(instance=user)
    return render(request, 'bookshelf/edit_user.html', {'form': form})

# Delete user - Requires 'can_delete'
@permission_required('bookshelf.can_delete', raise_exception=True)
def delete_user(request, user_id):
    user = get_object_or_404(CustomUser, pk=user_id)
    if request.method == 'POST':
        user.delete()
        return redirect('user_list')
    return render(request, 'bookshelf/delete_user.html', {'user': user})

##Update
from django.shortcuts import render
from .models import Book  

def book_list(request):
    books = Book.objects.all()
    return render(request, 'bookshelf/book_list.html', {'books': books})
