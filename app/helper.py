import json

from . import models

def UserIdFromCookie(request):
    if 'userId' not in request.COOKIES:
        return 0
    userId = int(request.COOKIES['userId'])
    return userId
    
def Verify(phone, password):
    UserQuerySet = models.User.objects.filter(u_phone=phone, u_password=password)
    if(UserQuerySet.exists()):
        return UserQuerySet[0].u_id
    else:
        return 0

def Register(name, phone, password):
    if(Verify(phone, password)!=0):
        return 0
    else:
        user = models.User(u_name=name, u_phone=phone, u_password=password)
        user.save()
        return Verify(phone, password)
        
def GetMyNotes(user):
    NotesQuerySet = models.NoteCreated.objects.filter(user=user)
    return NotesQuerySet
    
def GetSharedNotes(user):
    NotesQuerySet = models.NoteShared.objects.filter(user=user)
    return NotesQuerySet

def GetUserById(userId):
    UserQuerySet = models.User.objects.filter(u_id=userId)
    if(UserQuerySet.exists()):
        return UserQuerySet[0]
    else:
        return None

def GetNoteById(noteId):
    NotesQuerySet = models.NoteCreated.objects.filter(n_id=noteId)
    if(NotesQuerySet.exists()):
        return NotesQuerySet[0]
    else:
        return None
        
def AddNewNote(userId, newNote):
    user = GetUserById(userId)
    if(user==None):
        return 0
    try:
        note = models.NoteCreated(user=user, n_val=newNote)
        note.save()
        return 1
    except Exception as e:
        return 0
    
def UpdateNote(noteId, updatedNote):
    noteObj = GetNoteById(noteId)
    if noteObj==None:
        return 0
    try:
        noteObj.n_val = updatedNote
        noteObj.save()
        return 1
    except Exception as e:
        return 0
    
def DeleteNote(noteId):
    try:
        models.NoteCreated.objects.filter(n_id=noteId).delete()
        return 1
    except Exception as e:
        print(e)
        return 0