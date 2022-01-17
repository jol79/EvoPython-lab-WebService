from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt


def main(request):
    return render(request, "welcomes/home.html")

def users(request):
    return render(request, "users/users.html")

@csrf_exempt 
def createNewUser(request):
    """
    Verifies that user doesn't exist in the db
    and creates the user, otherwise returns data 
    associated with a given email/username
    """

    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']

        if username and email:
            response = {
                'msg': f'Given username: {username}, email: {email}'
            }
            return JsonResponse(response)
