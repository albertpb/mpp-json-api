from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from django.core.files.storage import FileSystemStorage
from .serializers import UploadSerializer
import jpype
import mpxj
import os
import json


class UploadViewSet(ViewSet):
    serializer_class = UploadSerializer

    def list(self, request):
        return Response("Ok")

    def create(self, request):
        """
        from net.sf.mpxj.reader import UniversalProjectReader
        from net.sf.mpxj.json import JsonWriter

        file = request.FILES['file'].read()

        ByteArrayInputString = jpype.JClass("java.io.ByteArrayInputStream")
        input_stream = ByteArrayInputString(file)
        project = UniversalProjectReader().read(input_stream)

        FileOutputStream = jpype.JClass("java.io.FileOutputStream")
        fileStream = FileOutputStream('out.json')

        JsonWriter().write(project, fileStream)

        f = open('out.json', 'r')
        data = json.load(f)
        f.close()

        return Response(data)
        """

        """
        from net.sf.mpxj.reader import UniversalProjectReader
        from net.sf.mpxj.json import JsonWriter

        file = request.FILES['file'].read()

        ByteArrayInputString = jpype.JClass("java.io.ByteArrayInputStream")
        input_stream = ByteArrayInputString(file)

        project = UniversalProjectReader().read(input_stream)

        ByteArrayOutputStream = jpype.JClass("java.io.ByteArrayOutputStream")
        output_stream = ByteArrayOutputStream()

        JsonWriter.write(project, output_stream)

        data = json.loads(output_stream.toByteArray())

        return Response(data)
        """

        from net.sf.mpxj.reader import UniversalProjectReader
        from net.sf.mpxj.json import JsonWriter

        file = request.FILES['file'].read()

        ByteArrayInputString = jpype.JClass("java.io.ByteArrayInputStream")
        input_stream = ByteArrayInputString(file)
        project = UniversalProjectReader().read(input_stream)

        ByteArrayOutputStream = jpype.JClass("java.io.ByteArrayOutputStream")
        output_stream = ByteArrayOutputStream()

        JsonWriter().write(project, output_stream)

        jstr = output_stream.toString()
        
        data = json.loads(str(jstr))

        return Response(data)