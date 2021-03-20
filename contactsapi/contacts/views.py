from django.shortcuts import render
from rest_framework import serializers
from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Contact
from .serializer import ContactSerializer
from rest_framework import permissions

# Create your views here.
class ContactList(ListCreateAPIView):
    
    serializers_class = ContactSerializer
    permission_class = (permissions.IsAuthenticated,)


    def perform_create(self, serializer):
        serializer.save(owner = self.request.user)

    def get_queryset(self):
        return Contact.objects.filter(owner=self.request.user)

class ContactDetailView(RetrieveUpdateDestroyAPIView):

    serializer_class = ContactSerializer
    permission_class = (permissions.IsAuthenticated,)
    lookup_field = "id"

    def get_queryset(self):
        return Contact.objects.filter(owner=self.request.user)

