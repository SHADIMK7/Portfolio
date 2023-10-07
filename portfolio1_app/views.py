from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import redirect
from django.shortcuts import render
from django.http import HttpResponse
import random


# Create your views here.

def port(request):
    return render(request, 'index.html', )


def generate_question():
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    question = f"What is {num1} + {num2}?"
    correct_answer = num1 + num2

    return {'question': question, 'correct_answer': correct_answer}


def modals(request):
    if request.method == 'POST':
        answer = int(request.POST.get('answer'))
        correct_answer = request.session.get('correct_answer')

        if answer == correct_answer:
            # Redirect to 'homepage' for a correct answer
            return redirect('/')
        else:
            print("Incorrect answer")
            return HttpResponse('Answer is wrong! TRY AGAIN')

    # Handle GET requests (initial page load)
    question_data = generate_question()
    request.session['correct_answer'] = question_data['correct_answer']
    return render(request, 'index.html', question_data)


def send_email(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']

        subject = 'Contact Form Submission from ' + name
        message_body = 'Name: {}\nEmail: {}\nMessage: {}'.format(name, email, message)
        recipient = 'muhammedshadimk111@gmail.com'  # Replace with your email

        send_mail(subject, message_body, settings.EMAIL_HOST_USER, [recipient],
                  fail_silently=False)  # Replace with the recipient's email address
        return redirect('/')