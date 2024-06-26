import logging
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import SurveyForm
from .models import SurveyResponse

# Initialize logger
logger = logging.getLogger(__name__)

# Define a view function for the home page
def home(request):
    return render(request, 'home.html')

# Define a view function for the login page
def login_page(request):
    # Check if the HTTP request method is POST (form submission)
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Check if a user with the provided username exists
        if not User.objects.filter(username=username).exists():
            # Display an error message if the username does not exist
            messages.error(request, 'Invalid Username')
            return redirect('/login/')

        # Authenticate the user with the provided username and password
        user = authenticate(username=username, password=password)

        if user is None:
            # Display an error message if authentication fails (invalid password)
            messages.error(request, "Invalid Password")
            return redirect('/login/')
        else:
            # Log in the user and redirect to the home page upon successful login
            login(request, user)
            return redirect('/home/')

    # Render the login page template (GET request)
    return render(request, 'login.html')

# Define a view function for the registration page
def register_page(request):
    # Check if the HTTP request method is POST (form submission)
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Check if a user with the provided username already exists
        user = User.objects.filter(username=username)

        if user.exists():
            # Display an information message if the username is taken
            messages.info(request, "Username already taken!")
            return redirect('/register/')

        # Create a new User object with the provided information
        user = User.objects.create_user(
            first_name=first_name,
            last_name=last_name,
            username=username
        )

        # Set the user's password and save the user object
        user.set_password(password)
        user.save()

        # Display an information message indicating successful account creation
        messages.info(request, "Account created Successfully!")
        return redirect('/register/')

    # Render the registration page template (GET request)
    return render(request, 'register.html')

@login_required
def survey_view(request):
    if request.method == 'POST':
        form = SurveyForm(request.POST)
        if form.is_valid():
            SurveyResponse.objects.create(
                user=request.user,
                question1=form.cleaned_data['question1'],
                question2=form.cleaned_data['question2'],
                question3=form.cleaned_data['question3'],
                question4=form.cleaned_data['question4'],
                question5=form.cleaned_data['question5'],
                question6=form.cleaned_data['question6'],
                question7=form.cleaned_data['question7'],
                question8=form.cleaned_data['question8'],
                question9=form.cleaned_data['question9'],
                question10=form.cleaned_data['question10'],
            )
            logger.info(f"Survey response saved for user {request.user.username}")
            return redirect('survey_thanks')
        else:
            logger.warning("Form is not valid")
    else:
        form = SurveyForm()

    return render(request, 'home.html', {'form': form})

@login_required
def survey_thanks_view(request):
    return render(request, 'survey_thanks.html')

@login_required
def survey_thanks_view(request):
    # Retrieve the latest SurveyResponse object
    latest_response = SurveyResponse.objects.latest('id')
    return render(request, 'survey_thanks.html', {'latest_response': latest_response})

@login_required
def survey_thanks_view(request):
    # Retrieve the latest SurveyResponse object
    latest_response = SurveyResponse.objects.latest('id')

    # Calculate the sum of digits in questions 1, 2, and 3
    question1_sum = sum(int(digit) for digit in str(latest_response.question1))
    question2_sum = sum(int(digit) for digit in str(latest_response.question2))
    question3_sum = sum(int(digit) for digit in str(latest_response.question3))
    question4_sum = sum(int(digit) for digit in str(latest_response.question4))
    question5_sum = sum(int(digit) for digit in str(latest_response.question5))
    question6_sum = sum(int(digit) for digit in str(latest_response.question6))
    question7_sum = sum(int(digit) for digit in str(latest_response.question7))
    question8_sum = sum(int(digit) for digit in str(latest_response.question8))
    question9_sum = sum(int(digit) for digit in str(latest_response.question9))
    question10_sum = sum(int(digit) for digit in str(latest_response.question10))

    a = question1_sum + question2_sum + question3_sum
    b = question4_sum + question5_sum + question6_sum
    c = question7_sum + question8_sum + question9_sum
    d = question10_sum
    total_sum = a + b + c + d 


    if total_sum <= 10:
            result = "Inefficient"
    else:
            result = "Efficient"


    # Pass the total_sum to the template
    return render(request, 'survey_thanks.html', {
        'latest_response': latest_response,
        'a' : a,
        'b' : b,
        'c' : c,
        'd' : d,
        'total_sum': total_sum,
        'result' : result
    })
