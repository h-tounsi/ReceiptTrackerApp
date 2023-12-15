from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Receipt 
from django.contrib.auth.forms import  AuthenticationForm
from django.contrib.auth import login , authenticate , logout
from .forms import ReceiptForm , UserCreationForm
from django.contrib import messages 


# Register view 
def register_page(request):
    if request.user.is_authenticated:
        return redirect('receipt_list')
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})


# Login view
def login_page(request):
    if request.user.is_authenticated:
        return redirect('receipt_list')
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'You are now logged in as {username}.')
                return redirect('receipt_list')
            else:
                messages.error(request, "Incorrect username or password.")
        else:
            messages.error(request, "Invalid form submission. Please check your input.")
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form, 'messages': messages.get_messages(request)})


# Logout view
def logout_page(request):   
    logout(request)
    messages.success(request, f'You have been logged out.')
    return redirect('login')



# Receipt views
@login_required(login_url='login')
def receipt_list(request):
    receipts = Receipt.objects.filter(user=request.user)
    return render(request, 'receipt_list.html', {'receipts': receipts})


# Receipt delete views
@login_required(login_url='login')
def receipt_delete(request, pk):
    Receipt.objects.get(id=pk).delete()
    return redirect('receipt_list')


# Receipt delete selected views
@login_required(login_url='login')
def receipt_delete_selected(request):
    if request.method == "POST":
        receipts = Receipt.objects.filter(id__in=request.POST.getlist('receipts'))
        receipts.delete()
    return redirect('receipt_list')


# Receipt detail views
@login_required(login_url='login')
def receipt_detail(request, pk):
    receipt = Receipt.objects.get(id=pk)
    return render(request, 'receipt_detail.html', {'receipt': receipt})

# Receipt new views
@login_required(login_url='login')
def receipt_new(request):
    if request.method == "POST":
        form = ReceiptForm(request.POST)
        if form.is_valid():
            receipt = form.save(commit=False)
            receipt.user = request.user
            receipt.save()
            return redirect('receipt_list')
    else:
        form = ReceiptForm()
    return render(request, 'receipt_new.html', {'form': form})

# Receipt edit views
@login_required(login_url='login')
def receipt_edit(request, pk):
    receipt = Receipt.objects.get(pk=pk)
    
    if request.method == "POST":
        form = ReceiptForm(request.POST, instance=receipt)
        if form.is_valid():
            receipt = form.save()
            return redirect('receipt_detail', pk=receipt.pk)
    else:
        form = ReceiptForm(instance=receipt)
    
    
    return render(request, 'receipt_edit.html', {'form': form})






