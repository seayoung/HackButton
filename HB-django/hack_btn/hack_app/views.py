from django.shortcuts import render

# Create your views here.
def home(request):

	print request.method
   # if request.method == "POST":
   #     username = request.POST['username']
   #     password = request.POST['password']
   #     user = authenticate(username=username, password=password)
   #     if user is not None:
   #         if user.is_active:
   #             login(request, user)
   #             return HttpResponseRedirect('/lookup')
   #         else:
   #             return HttpResponse("Inactive user.")
   #     else:
   #         return HttpResponseRedirect(settings.LOGIN_URL)
	return render(request, "hack_app/home.html", {})