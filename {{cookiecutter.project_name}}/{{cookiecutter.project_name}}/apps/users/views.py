from django.views import View
from django.conrib.auth import authenticate, login


class UserView(View):
    def post(self, request):
        email, password = request.POST.get("email"), request.POST.get("password")
        user = authenticate(request, username=email, password=password)
        if user is not None:
            return login(request, user)
        else:
            return {"success": False}
