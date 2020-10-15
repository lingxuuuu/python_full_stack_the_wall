import bcrypt
from django.contrib import messages
from django.shortcuts import redirect, render
from .models import *


def index(request):
    return render(request, 'index.html')

def wall (request):
    context = {
        'user': User.objects.get(id=request.session['user_id']),
    #request.sesssion, request.POST
        'posts':Post.objects.all()
    }
    return render (request, 'wall.html', context)

def register(request):
    print(request.POST)
    errors = User.objects.basic_validator(request.POST)
    #validate
    if len(errors) > 0:
        # if the errors dictionary contains anything, loop through each key-value pair and make a flash messagecopy
        for key, value in errors.items():
            messages.error(request, value)
        # redirect the user back to the form to fix the errors
        return redirect('/')
    else:
        #hashes the password
        hash_password = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()).decode()
        print('hash password: ', hash_password)

    #create a user
    new_user = User.objects.create(
        first_name=request.POST['first_name'],
        last_name=request.POST['last_name'], 
        email=request.POST['email'], 
        password=hash_password
    )
    #set up a session
    request.session['user_id'] = new_user.id
    return redirect('/wall')

def login (request):
    print(request.POST)

    errors = User.objects.login_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    else:
        user = User.objects.get(email=request.POST['email'])
        # set up user in session
        request.session['user_id'] = user.id
        return redirect('/wall')

def add_post (request):
    logged_user =  User.objects.get(id=request.session['user_id'])
    Post.objects.create(
        user = logged_user,
        post = request.POST['post']
    )
    return redirect('/wall')

def logout (request):
    request.session.flush()
    # del request.session['user_id']

    return redirect('/')

def comment (request, post_id):
    print('Comment some post!')
    Comment.objects.create(
        comment = request.POST['comment'],
        user = User.objects.get(id=request.session['user_id']),
        post = Post.objects.get(id=post_id)
    )
    return redirect('/wall')
    
