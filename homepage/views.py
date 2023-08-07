from django.shortcuts import render,  get_object_or_404, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponse,HttpResponseRedirect,JsonResponse;
from .forms import ImageForm,MembershipForm,EventForm;
from .models import CustomUser,Events,Image,Membership,Feedback,Achievement
from django.db.models import Q;
from django.urls import reverse;
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

# Create your views here.
def index(request):
    return render (request,"index.html")

def loginpage(request):
    return render (request,"loginpage.html")

def register(request):
    return render (request,"loginpage.html")

def mainpage(request):
    return render (request,"mainpage.html")



def feedback(request):
    return render (request,"feedback.html")

def viewachievements(request):
    return render (request,"viewachievements.html")

def about(request):
    return render (request,"about.html")

def manageevents(request):
    return render (request,"manageevents.html")

def updateevent(request):
    return render (request,"updateevent.html")

def viewach(request):
    return render (request,"viewach.html")

def membershiplogin(request):
    return render (request,"membershiplogin.html")

def managemember(request):
    return render (request,"managemember.html")

def updatemember(request):
    return render (request,"updatemember.html")

@login_required(login_url='loginpage')
def userhomepage(request):
    return render (request,"userhomepage.html")

def loginpage(request):
    if request.method == 'POST':
        student_id = request.POST['student_id']
        password = request.POST['password']
        user = authenticate(request, username=student_id, password=password)
        if user is not None:
            login(request, user)
            return redirect('userhomepage')  # Replace 'home' with your desired homepage URL
        else:
            error_message = "Invalid credentials. Please try again."
            return render(request, 'loginpage.html', {'error_message': error_message})
    return render(request, 'loginpage.html')

def register(request):
    if request.method == 'POST':
        student_id = request.POST['student_id']
        email_id = request.POST['email_id']
        password = request.POST['password']
        agreed = request.POST.get('agreed', False)
        if agreed:
            # Create a new user
            user = CustomUser.objects.create_user(username=student_id, email=email_id, password=password)
            # Perform additional registration logic if needed
            return redirect('loginpage')  # Replace 'register_success' with your desired success page URL
        else:
            error_message = "Please agree to the terms and conditions."
            return render(request, 'loginpage.html', {'error_message': error_message})
    return render(request, 'loginpage.html')

def register_success(request):
    return render(request, 'index.html')  # Create a registration success page and adjust the template name



def addevents(request):
    if request.method == 'POST':
        a_eventsID = request.POST['eventsID']
        a_eventsName = request.POST['eventsName']
        a_eventsDesc = request.POST['eventsDesc']
        a_eventsDate = request.POST['eventsDate']
        data = Events(eventsID=a_eventsID, eventsName=a_eventsName, eventsDesc=a_eventsDesc, eventsDate=a_eventsDate)
        data.save()
        message = 'Data Saved'
        return render(request, "addevents.html", {'message': message})
    else:
        return render(request, 'addevents.html', {'message': ''})



def membership(request):
    if request.method == 'POST':
        memberid = request.POST['memberid']
        studentid = request.POST['studentid']
        membernohp = request.POST['membernohp']
        memberpassword = request.POST['memberpassword']
        memberdate = request.POST['memberdate']
        musicinstrument = request.POST['musicinstrument']
        
        data = Membership(
            memberid=memberid,
            studentid=studentid,
            membernohp=membernohp,
            memberpassword=memberpassword,
            memberdate=memberdate,
            musicinstrument=musicinstrument
        )
        data.save()
        
        dict = {
            'message': 'Data Saved'
        }
        return render(request, "membership.html", dict)
    else:
        return render(request, 'membership.html')

def adminhomepage(request):
    return render (request,"adminhomepage.html")

def adminloginpage(request):
    return render (request,"adminloginpage.html")

def achievement(request):
    if request.method == "POST":
        forms=ImageForm(data=request.POST,files=request.FILES)
        if forms.is_valid():
            forms.save()
            obj=forms.instance
            return render(request,"achievement.html",{"obj":obj})
    else:
        forms=ImageForm()
        img=Image.objects.all()
    return render(request,"achievement.html",{"img":img,"forms":forms})


def viewachievements(request):
    if request.method == "POST":
        forms = ImageForm(data=request.POST, files=request.FILES)
        if forms.is_valid():
            forms.save()
            obj = forms.instance
            return render(request, "viewachievements.html", {"obj": obj})
    else:
        forms = ImageForm()
        img = Image.objects.all()
    return render(request, "viewachievements.html", {"img": img, "forms": forms})


class MembershipRegister(LoginRequiredMixin, CreateView):
    model = Membership
    template_name = "membership2.html"
    form_class = MembershipForm
    
    def form_valid(self, form):
        user = self.request.user
        user.role = "member"
        user.save()
        form.instance.student_id = self.request.user
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse_lazy("userhomepage")  # Replace "mainpage" with the actual URL or view name of your main page

def viewevents(request):
    events = Events.objects.all()
    return render(request, 'viewevents.html', {'events': events})

from django.http import HttpResponseRedirect

def feedback(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        feedback = Feedback(name=name, email=email, message=message)
        feedback.save()
        return HttpResponseRedirect(request.path)  # Redirect to the current page
    return render(request, 'feedback.html')


def adminloginpage(request):
    if request.method == 'POST':
        student_id = request.POST['student_id']
        password = request.POST['password']
        user = authenticate(request, username=student_id, password=password)
        if user is not None and user.is_superuser:
            login(request, user)
            return redirect('adminhomepage')  # Replace 'home' with your desired homepage URL
        else:
            error_message = "Invalid credentials. Please try again."
            return render(request, 'adminloginpage.html', {'error_message': error_message})
    return render(request, 'adminloginpage.html')



def manageevents(request):
    events = Events.objects.all()
    context = {
        'events': events
    }
    return render(request, 'manageevents.html', context)

def deleteevent(request, eventName):
    event = Events.objects.get(eventsName=eventName)
    event.delete()
    return HttpResponseRedirect(reverse('manageevents'))

def deleteevent(request, eventName):
    if request.method == 'POST':
        event = Events.objects.get(eventsName=eventName)
        event.delete()
        return JsonResponse({'message': 'Event deleted successfully.'})

def updateevent(request, eventName):
    event = Events.objects.get(eventsName=eventName)
        
    if request.method == 'POST':
        form = EventForm(request.POST, instance=event)
        if form.is_valid():
            form.save()
            return redirect('manageevents')  # Redirect to the homepage or any other desired page
    else:
        form = EventForm(instance=event)

    return render(request, 'updateevent.html', {'form': form})

def addachievement(request):
    if request.method == 'POST':
        achname = request.POST['achname']
        achdesc = request.POST['achdesc']
        achvenue = request.POST['achvenue']
        achdate = request.POST['achdate']
        achstanding = request.POST['achstanding']
        achcategory = request.POST['achcategory']

        # Create a new Achievement object
        achievement = Achievement(achname=achname, achdesc=achdesc, achvenue=achvenue, achdate=achdate, achstanding=achstanding, achcategory=achcategory)
        achievement.save()

        message = "Achievement saved successfully!"
        return render(request, 'addachievement.html', {'message': message})
    else:
        return render(request, 'addachievement.html')

def viewach(request):
    achievements = Achievement.objects.all()
    return render(request, 'viewach.html', {'achievements': achievements})

def delete_member(request, memberid):
    member = Membership.objects.get(memberid=memberid)

    if request.method == 'POST':
        member.delete()
        return redirect('managemember')  # Redirect to the page showing the remaining members or any other desired page

    return render(request, 'managemember.html', {'members': members})  # Pass the members context variable to the template


def managemember(request):
    members = Membership.objects.all()
    return render(request, 'managemember.html', {'members': members})

def updatemember(request, memberid):
    member = get_object_or_404(Membership, student_id = memberid)
    
    if request.method == 'POST':
        form = MembershipForm(request.POST, instance=member)
        if form.is_valid():
            form.save()
            return redirect('membership')  # Redirect to the membership page or any other desired page
    else:
        form = MembershipForm(instance=member)

    return render(request, 'updatemember.html', {'form': form, 'member': member})


def membershiplogin(request):
    if request.method == 'POST':
        form = MembershipForm(request.POST)
        if form.is_valid():
            return redirect('feedback')
            memberid = form.cleaned_data('memberid')
            membernohp = form.cleaned_data('membernohp')
            musicinstrument = form.cleaned_data('musicinstrument')

            membership = authenticate(request, memberid=memberid, membernohp=membernohp, musicinstrument=musicinstrument)
            
            if membership is not None:
                return redirect('feedback')
            else:
                message.info(request,'salah oi')

    else:
        form = MembershipForm()
    
    return render(request, 'membershiplogin.html', {'form': form})


