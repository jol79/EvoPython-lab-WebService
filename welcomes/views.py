from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from pymongo import MongoClient
# from .credentials_database import *
import os


def main(request):
    return render(request, "welcomes/home.html")

def users(request):
    """Returns all users from the database"""

    try:
        CONNECTION_STRING = f"mongodb+srv://{os.environ.get('DB_USERNAME')}:{os.environ.get('DB_PASSWORD')}@responses.awbv0.mongodb.net/{os.environ.get('DB_NAME')}?retryWrites=true&w=majority"
        client = MongoClient(CONNECTION_STRING)
        database = client[os.environ.get('DB_NAME')]
        collection = database[os.environ.get('DB_COLLECTION')]
    except:
        response = {
            'users': None,
            'error': "Unable to connect to the database!"
        }
        return JsonResponse(response)

    responseData = {
        "users": [user for user in collection.find()]
    }

    return render(request, "users/users.html", responseData)

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

        if not username or not email:
            return JsonResponse({'status': f'You have just submitted the wrong data: username="{username}", email="{email}"'})

        try:
            CONNECTION_STRING = f"mongodb+srv://{os.environ.get('DB_USERNAME')}:{os.environ.get('DB_PASSWORD')}@responses.awbv0.mongodb.net/{os.environ.get('DB_NAME')}?retryWrites=true&w=majority"
            client = MongoClient(CONNECTION_STRING)
            database = client[os.environ.get('DB_NAME')]
            collection = database[os.environ.get('DB_COLLECTION')]
        except:
            response = {
                'first_time': None,
                'username': None,
                'email': None,
                'error': "Unable to connect to the database!"
            }
            return JsonResponse(response)

        if collection.find_one(filter={'email': email, 'username': username}):
            # return data about the user
            response = {
                'first_time': False,
                'username': username,
                'email': email
            }
            return JsonResponse(response)
        collection.insert_one({
            'username': username,
            'email': email
        })

        response = {
            'first_time': True,
            'username': username,
            'email': email
        }
        return JsonResponse(response)
