import snooze
import json
import sys
import subprocess
from ficcle import Ficcle

user = subprocess.Popen(["git", "config", "--global", "github.user"], stdout=subprocess.PIPE).stdout.read().strip('\n ') 
token = subprocess.Popen(["git", "config", "--global", "github.token"], stdout=subprocess.PIPE).stdout.read().strip('\n ') 

github = snooze.Snooze('github.com/api/v2/json', secure=True)

def display_info(info):
    for x in info:
        for y in x:
            print '%s: %s' % (str(y), str(x[y]))

def display_user(info):
    for x in info:
        print '%s: %s' % (str(x), str(info[x]))

def edit(option, arg):
    resp = github.user.show.username[user](method='post', values={option: arg}, login=user, token=token)
    resp_python = json.loads(resp)
    display_user(resp_python['user'])

def show(arg):
    resp = github.user.show.username[arg](method='get')
    resp_python = json.loads(resp)
    display_user(resp_python['user'])

def create(name, description=None, homepage=None, public=1):
    args = {'name': name, 'public':public, 'login':user, 'token' : token}
    if description != None:
        args['description'] = description
    if homepage != None:
        args['homepage'] = homepage

    resp = github.repos.create(method='post', **args)
    print resp

def delete(name, delete_token=None):
    resp = github.repos.delete.repo[name](method='post', delete_token=delete_token, login=user, token=token)
    print resp

edit_options = ['name', 'email', 'blog', 'company', 'location']
        

fickle = Ficcle()

fickle.add_function(edit, options=edit_options)
fickle.add_function(show)
fickle.add_function(create)
fickle.add_function(delete)

fickle.run_ficcle()

