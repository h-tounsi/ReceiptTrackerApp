from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Receipt 
from django.contrib.auth.forms import  AuthenticationForm
from django.contrib.auth import login , authenticate , logout
from .forms import ReceiptForm , userCreationForm
from django.contrib import messages 
from django.http import Http404



def register_page(request):
    if request.user.is_authenticated:
        return redirect('receipt_list')
    if request.method == 'POST':
        form = userCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('login')
    else:
        form = userCreationForm()
    return render(request, 'register.html', {'form': form})



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



def logout_page(request):   
    logout(request)
    messages.success(request, f'You have been logged out.')
    return redirect('login')




@login_required(login_url='login')
def receipt_list(request):
    receipts = Receipt.objects.filter(user=request.user)
    return render(request, 'receipt_list.html', {'receipts': receipts})



@login_required(login_url='login')
def receipt_delete(request, pk):
    Receipt.objects.get(id=pk).delete()
    return redirect('receipt_list')


@login_required(login_url='login')
def receipt_delete_selected(request):
    if request.method == "POST":
        receipts = Receipt.objects.filter(id__in=request.POST.getlist('receipts'))
        receipts.delete()
    return redirect('receipt_list')



@login_required(login_url='login')
def receipt_detail(request, pk):
    receipt = Receipt.objects.get(id=pk)
    return render(request, 'receipt_detail.html', {'receipt': receipt})


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
    
    print("Receipt Date:", receipt.date_of_purchase)  # Add this line for debugging
    
    
    return render(request, 'receipt_edit.html', {'form': form})





