from django.shortcuts import render
from rest_framework import viewsets
from .serializers import SurfJournalSerializer
from .models import SurfJournal


class SurfJournalView(viewsets.ModelViewSet):
    serializer_class = SurfJournalSerializer
    queryset = SurfJournal.objects.all()
