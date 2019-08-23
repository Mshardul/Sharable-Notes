# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_protect, csrf_exempt

import json

from . import helper

def Home(request):
    return render_to_response('home.html')
    
def MyNotes(request):
    data = {}
    userId = helper.UserIdFromCookie(request)
    data['userId'] = userId
    if(userId!=0):
        data['myNotes'] = helper.GetMyNotes(userId)
    return render_to_response('my_notes.html', data)
    
def SharedNotes(request):
    data = {}
    userId = helper.UserIdFromCookie(request)
    data['userId'] = userId
    if(userId!=0):
        data['sharedNotes'] = helper.GetSharedNotes(userId)
    return render_to_response('shared_notes.html', data)
    
def LogOut(request):
    response = render_to_response('home.html')
    response.set_cookie('userId', 0)
    return response

@csrf_exempt
def UpdateNote(request):
    userId = helper.UserIdFromCookie(request)
    if(userId==0):
        return HttpResponse(0)
    data = json.loads(request.POST.get('data'))
    noteId = data['noteId']
    updatedNote = data['updatedNote']
    x = helper.UpdateNote(noteId, updatedNote)
    return HttpResponse(x)
    
@csrf_exempt
def AddNewNote(request):
    userId = helper.UserIdFromCookie(request)
    if(userId==0):
        return HttpResponse(0)
    data = json.loads(request.POST.get('data'))
    newNote = data['newNote']
    x = helper.AddNewNote(userId, newNote)
    return HttpResponse(x)
    
@csrf_exempt
def DeleteNote(request):
    userId = helper.UserIdFromCookie(request)
    if(userId==0):
        return HttpResponse(0)
    data = json.loads(request.POST.get('data'))
    noteId = int(data['noteId'])
    print("*"*30, noteId)
    x = helper.DeleteNote(noteId)
    return HttpResponse(x)
    
@csrf_exempt
def Register(request):
    data = json.loads(request.POST.get('data'))
    print(data)
    name = data['name']
    phone = data['phone']
    password = data['password'] 
    x = helper.Register(name, phone, password)
    return HttpResponse(x)

@csrf_exempt
def Login(request):
    data = json.loads(request.POST.get('data'))
    print(data)
    phone = data['phone']
    password = data['password']
    x = int(helper.Verify(phone, password))
    response = HttpResponse(x)
    response.set_cookie('userId', x)
    return response