from rest_framework import serializers
from .models import SurfJournal


class SurfJournalSerializer(serializers.ModelSerializer):

    class Meta:
        model = SurfJournal
        fields = (
            "pk",
            "country",
            "region",
            "surfbreak",
            "description",
            "notes",
            "author",
        )
