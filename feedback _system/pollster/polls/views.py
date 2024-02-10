from django.template import loader
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import get_object_or_404, render,redirect
from django.urls import reverse



from .models import Question, Choice,Registration


# Get questions and display them

from django.contrib.auth.decorators import login_required
@login_required(login_url='polls:login')
def index(request):
    
    latest_question_list = Question.objects.order_by('-pub_date')
    
    context = {'latest_question_list': latest_question_list}
    
    
    return render(request, 'polls/index.html', context)

# Show specific question and choices




@login_required(login_url='polls:login')
def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'polls/detail.html', {'question': question})

# Get question and display results
from django.shortcuts import render
from .models import Question


@login_required(login_url='polls:login')
def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})

@login_required(login_url='polls:login')
# Vote for a question choice
def result(request):
    all_questions = Question.objects.all()
    return render(request, 'polls/result.html', {'all_questions': all_questions})


@login_required(login_url='polls:login')
def vote(request, question_id):
    # print(request.POST['choice'])
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:index'))
    
    
    

from django.contrib.auth import authenticate, login as auth_login,logout as auth_logout
from django.shortcuts import render, redirect
from django.http import HttpResponse

def login(request):
    if request.method == "POST":
        username1 = request.POST["id"]
        password1 = request.POST["password"]
        user = authenticate(request, username=username1, password=password1)
        if user is not None:
            auth_login(request, user)
            return redirect('polls:index')
        else:
            return HttpResponse("Incorrect details")

    return render(request, 'polls/login.html')




from django.contrib.auth.models import User
def signup(request):
    if request.method=="POST":
        firstname=request.POST.get('first_name')
        lastname=request.POST.get('last_name')
        idname=request.POST.get('id_name')
        gmail=request.POST.get('gmail')
        password=request.POST.get('password')
        print(firstname,lastname,idname,gmail)
        my_user=User.objects.create_user(firstname,idname,password)
        my_user.save()
        return redirect('polls:login')
    # if request.method=='POST':
    #     form=RegistrationForm(request.POST)
    #     if form.is_valid():
    #         f_name=form.cleaned_data['first_name']
    #         l_name=form.cleaned_data['last_name']
    #         i_name=form.cleaned_data['id_name']
    #         mail=form.cleaned_data['gmail']
    #         p_word=form.cleaned_data['password']
    #         create_new=Registration(first_name=f_name,last_name=l_name,id_name=i_name,gmail=mail,password=p_word)
    #         create_new.save()
    #         return HttpResponseRedirect(reverse('polls:index'))
            
    form=RegistrationForm() 
    return render(request,"polls/signup.html",{'form':form}) 
    # return render(request,'polls/signup.html')

def logout(request):
    redirect(request)
    return render(request,'pages/index.html')




from django.contrib.auth.models import User
def signup(request):
    if request.method=="POST":
        firstname=request.POST.get('first_name')
        lastname=request.POST.get('last_name')
        idname=request.POST.get('id_name')
        gmail=request.POST.get('gmail')
        password=request.POST.get('password')
        print(firstname,lastname,idname,gmail)
        my_user=User.objects.create_user(firstname,idname,password)
        my_user.save()
        return redirect('polls:login')
    # if request.method=='POST':
    #     form=RegistrationForm(request.POST)
    #     if form.is_valid():
    #         f_name=form.cleaned_data['first_name']
    #         l_name=form.cleaned_data['last_name']
    #         i_name=form.cleaned_data['id_name']
    #         mail=form.cleaned_data['gmail']
    #         p_word=form.cleaned_data['password']
    #         create_new=Registration(first_name=f_name,last_name=l_name,id_name=i_name,gmail=mail,password=p_word)
    #         create_new.save()
    #         return HttpResponseRedirect(reverse('polls:index'))
            
    form=RegistrationForm() 
    return render(request,"polls/signup.html",{'form':form}) 
    # return render(request,'polls/signup.html')

def logout(request):
    auth_logout(request)
    return render(request,'pages/index.html')







from .forms import Sirform,Collegeform,RegistrationForm
from .models import Sir,Student,Registration

def sirform(request):
    if request.method=='POST':
        form=Sirform(request.POST)
        if form.is_valid():
            emp_name=form.cleaned_data['name']
            emp_id=form.cleaned_data['id_name']
            create_sir=Sir.objects.create(name=emp_name,rollno=emp_id)
            create_sir.save()
            return HttpResponse("data is saved")
            
    form=Sirform()
    return render(request,"polls/display_user_details.html",{'form':form})

def studentlogin(request):
    if request.method=='POST':
        new=Collegeform(request.POST)
        if new.is_valid():
            stu_name=new.cleaned_data['st_name']
            fat_name=new.cleaned_data['ft_name']
            mot_name=new.cleaned_data['mt_name']
            create_new=Student(student=stu_name,father=fat_name,mother=mot_name)
            create_new.save()
            return HttpResponse("data is saved successfully")
    new=Collegeform()
    return render(request,"polls/studentlogin.html",{'form':new})
       
def signing(request):
    if request.method=='POST':
        form=RegistrationForm(request.POST)
        if form.is_valid():
            f_name=form.cleaned_data['first_name']
            l_name=form.cleaned_data['last_name']
            i_name=form.cleaned_data['id_name']
            mail=form.cleaned_data['gmail']
            p_word=form.cleaned_data['password']
            create_new=Registration(first_name=f_name,last_name=l_name,id_name=i_name,gmail=mail,password=p_word)
            create_new.save()
            return HttpResponse("DATA IS SAVED SUCCESSFULLY")
            
    form=RegistrationForm() 
    return render(request,"polls/logout.html",{'form':form})      


# views.py

# from django.shortcuts import render, redirect
# from .models import ChoiceForm

# def add_choice(request, question_id):
#     if request.method == 'POST':
#         form = ChoiceForm(request.POST)
#         if form.is_valid():
#             new_choice = form.save(commit=False)
#             new_choice.question_id = question_id
#             new_choice.save()
#             return render(request,'poll/results.html')  # Redirect to a success page or any other desired page
#     else:
#         form = ChoiceForm()
    
#     return render(request, 'polls/login.html', {'form': form})


# polls/views.py

# from django.shortcuts import render
# from .forms import UserLoginForm

# def check(request):
#     if request.method == 'POST':
#         # Process the form data
#         form = UserLoginForm(request.POST)
#         if form.is_valid():
#             user_id = form.cleaned_data['user_id']
#             password = form.cleaned_data['password']
#             # Do something with the user_id and password, e.g., authentication
            
#             # Redirect to a success page or do other processing
#     else:
#         # Display a blank form
#         form = UserLoginForm()

#     return render(request, 'index.html', {'form': form})

