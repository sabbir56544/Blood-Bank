from django.core.files.base import equals_lf
from django.shortcuts import redirect, render
from .models import About, GalleryPhoto, DonationProcess, DonorRegister, ShareExperience
from .forms import DonorRegistration, DonorSearch, ShareExperienceForm
from django.contrib import messages



def home_view(request):
    about = About.objects.all()
    photo = GalleryPhoto.objects.all()
    d_process = DonationProcess.objects.all()
    context = {
        'abouts': about,
        'photos': photo,
        'process': d_process,
    }
    return render(request, 'index.html', context)


def register_view(request):
    form = DonorRegistration()
    if request.method == 'POST':
        form = DonorRegistration(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Thank You for being part in this Blood Bank')
            return redirect('home')    
    context = {
        'form': form,
    }    

    return render(request, 'registration.html', context)



def search_view(request):
    search_forms = DonorSearch()
    if request.method == "POST":
        search_forms = DonorSearch(request.POST)
        if search_forms.is_valid():
            blood_group = search_forms.cleaned_data['blood_group']
            
            donor_filter = DonorRegister.objects.filter(blood_group__icontains=blood_group)
            
            context = {
                'donor_filter': donor_filter,
            }

            return render(request, 'donor_list.html', context)

    context = {
        'forms': search_forms,
    }     

    return render(request, 'search.html', context)   




def share_experinece(request):
    form = ShareExperienceForm()
    if request.method == "POST":
        form = ShareExperienceForm(request.POST)
        if form.is_valid():
            appointmentform = form.save(commit=False)
            appointmentform.log_user = request.user
            print(appointmentform.log_user )
            appointmentform.save()
            # appointment_form.user = request.user
            # appointment_form.save()
         
            return redirect('home')
        else:
            form = ShareExperienceForm()

    context = {
        'form': form,
    }            

    return render(request, 'share_experience_form.html', context)


