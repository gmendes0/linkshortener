import hashlib
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect, Http404
from .models import Link
from .serializers import LinkSerializer


class LinkView(APIView):
    def get(self, request, shortened=None):
        if shortened is None:
            raise Http404

        link = get_object_or_404(Link, hashed=shortened)

        link.clicks += 1
        link.save(update_fields=['clicks'])

        return HttpResponseRedirect(link.original)

    def post(self, request):
        json_data = LinkSerializer(data=request.data)

        json_data.is_valid(raise_exception=True)

        link, created = Link.objects.get_or_create(
            original=json_data.validated_data['original'],
            hashed=hashlib.blake2b(
                json_data.validated_data['original'].encode('utf8'),
                digest_size=5
            ).hexdigest()
        )

        return Response(LinkSerializer(link).data)
