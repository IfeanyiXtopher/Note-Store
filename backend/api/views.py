from django.shortcuts import render
from django.contrib.auth.models import User
# from django.contrib.auth import get_user_model
from rest_framework import generics
from .serializers import UserSerializer, NoteSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Note


# User = get_user_model()

# Create your views here.
class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all() # This provide the list of all user already to avoid duplicate
    serializer_class = UserSerializer  ## This tell what we need to accept in creating new user
    permission_classes = [AllowAny] ## This is to all anyone to create user. you dont need to be authenticated



class NoteListCreate(generics.ListCreateAPIView): # The reason we are using ListCreateAPIView and not CreateAPIView is because we want to perfrom both listing all note from a user and creating a note by a user
    serializer_class = NoteSerializer
    permission_classes = [IsAuthenticated]  # This means you cant call this class unless you are login

    def get_queryset(self): # for getting all note by user
        user = self.request.user
        return Note.objects.filter(author=user) #we use filter so we can only see notes writen by you
    
    def perform_create(self, serializer): # For creating a note
        if serializer.is_valid():
            serializer.save(author=self.request.user)
        else:
            print(serializer.error)



class NoteDelete(generics.DestroyAPIView):
    serializer_class = NoteSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Note.objects.filter(author=user)
        