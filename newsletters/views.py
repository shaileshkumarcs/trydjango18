from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render

from .forms import ContactForm,SignUpForm
from .models import SignUp

# Create your views here.
def home(request):
    title = 'Sign Up Now'

    form = SignUpForm(request.POST or None)

    context = {
        "title": title,
        "form": form
    }


    if form.is_valid():
        #form.save()
        instance = form.save(commit=False)
        full_name = form.cleaned_data.get("full_name")
        if not full_name:
            full_name = "New full name"
        instance.full_name = full_name

        # if not instance.full_name:
        #     instance.full_name = "Shailesh"
        instance.save()
        title = "Thank You"
        context = {
            "title": title,
        }

    if request.user.is_authenticated() and request.user.is_staff:
        #print(SignUp.objects.all())
        if instance in SignUp.objects.all()
            print(instance)
        context = {
            "queryset":[123,456]
        }

    return render(request, "home.html", context)


def contact(request):
    title = "Contact Us"
    title_align_center = True
    form = ContactForm(request.POST or None)
    if form.is_valid():
        # for key in form.cleaned_data:
        #     print(key)
        #     print(form.cleaned_data.get(key))
        # for key, value in form.cleaned_data.items():
        #     print(key, value)
        form_email = form.cleaned_data.get("email")
        form_message = form.cleaned_data.get("message")
        form_full_name = form.cleaned_data.get("full_name")
        # print(email, message, full_name)
        subject = "Site contact form"
        from_email = settings.EMAIL_HOST_USER
        to_email = [form_email,'shailesh.kumarcs@gmail.com']
        context_message = "%s: %s via %s"%(form_full_name,form_message, form_email)
        some_html_message = """
        <h1>HELLO HI</h1>
        """
        send_mail(subject,
                  context_message,
                  from_email,
                  to_email,
                  html_message=some_html_message,
                  fail_silently=False)
    context = {
        "form":form,
        "title":title,
        "title_align_center":title_align_center
    }

    return render(request, "forms.html", context)