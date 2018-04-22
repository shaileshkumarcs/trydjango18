from django.shortcuts import render

from .forms import ContactForm,SignUpForm
# Create your views here.
def home(request):
    title = 'Welcome'

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

    return render(request, "home.html", context)

def contact(request):
    form = ContactForm(request.POST or None)

    context = {

    }

    return render(request, "forms.html", context)