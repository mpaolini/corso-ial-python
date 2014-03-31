from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
import django.contrib.auth
import requests


from dropbox_test.models import DropboxUser, DropboxCode


def home(request):
    if DropboxCode.objects.count() > 0:
        show_connect = False
        if DropboxUser.objects.count() == 0:
            resp = requests.post('https://api.dropbox.com/1/oauth2/token',
                                 {'code': DropboxCode.objects.all()[0].code,
                                  'client_id': 'fsbceopy3kjwrl4',
                                  'client_secret': '2379dwp9stenea6',
                                  'redirect_uri': 'http://localhost:8000/cb',
                                  'grant_type': 'authorization_code'})
            resp.raise_for_status()
            data = resp.json()
            user = DropboxUser(access_token=data['access_token'],
                               user_id=data['uid'])
            user.save()
    else:
        show_connect = True
    return render(request, 'home.html', {'show_connect': show_connect})


def file_list(request):
    access_token = DropboxUser.objects.all()[0].access_token
    resp = requests.get('https://api.dropbox.com/1/metadata/dropbox/',
                        headers={'Authorization': 'Bearer {}'.format(
                            access_token)})
    resp.raise_for_status()
    context = {'files': [item['path'] for item in resp.json()['contents']]}
    return render(request, 'file_list.html', context)


def cb(request):
    code = request.GET['code']
    refresh_token = DropboxCode(code=code)
    refresh_token.save()
    return HttpResponseRedirect('/')
