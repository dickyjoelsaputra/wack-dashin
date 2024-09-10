from django.shortcuts import render, redirect
from django.contrib.auth import authenticate , login, logout

# Create your views here.

    
def authLogin(request):
    
    print("request diterima")
    print(request.method == 'POST')
    print(request.method)
    print("Current URL path:", request.path)
    # print(request.POST['username'])

    if request.method == 'POST':
        print("POST request diterima")
        
        username = request.POST.get('username') or request.POST['username']
        password = request.POST.get('password') or request.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect(to="dashboard-index")
        else:
            return redirect(to="login")


    return render(request,template_name='auth/login.html')


def authLogout(request):
    
    if request.method == 'POST':
        logout(request)
    
        return redirect(to='login')
    
    return redirect(to="login")