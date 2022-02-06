from rest_framework.serializers import HyperlinkedModelSerializer

from notes.models import Project, Note


class ProjectModelSerializer(HyperlinkedModelSerializer):
    """
    A serializer (i.e. convert querysets and model instances to Python datatypes or back) that corresponds to the
    Project model field
    HyperlinkedModelSerializer - hyperlinks are used for representation instead of primary keys (unlike ModelSerializer)
    """

    class Meta:
        model = Project
        fields = ['id', 'username', 'first_name', 'last_name', 'email']


class NoteModelSerializer(HyperlinkedModelSerializer):
    """
    A serializer (i.e. convert querysets and model instances to Python datatypes or back) that corresponds to the Note
    model field
    HyperlinkedModelSerializer - hyperlinks are used for representation instead of primary keys (unlike ModelSerializer)
    """

    class Meta:
        model = Note
        fields = ['url', 'username', 'first_name', 'last_name', 'email']
