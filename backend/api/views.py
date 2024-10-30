from django.db import transaction
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from api.serializers import (GoodSerializer, PriceSerializer,
                             ReduceSerializer, TypeSerializer)
from goods.models import Good, Price, Type


class GoodViewSet(viewsets.ModelViewSet):
    queryset = Good.objects.all()
    http_method_names = ('get', 'post', 'put', 'delete')
    serializer_class = GoodSerializer

    @transaction.atomic()
    def perform_destroy(self, instance):
        instance.price.delete()
        super().perform_destroy(instance)

    @action(methods=['POST'], detail=True, serializer_class=ReduceSerializer)
    def reduce(self, request, pk):
        good = Good.objects.get(id=pk)

        serializer = ReduceSerializer(data=request.data, context={'good': good})
        serializer.is_valid(raise_exception=True)

        good.qty -= serializer.validated_data['value']
        good.save()

        return Response(GoodSerializer(good).data, status=status.HTTP_200_OK)


class PriceViewSet(viewsets.ModelViewSet):
    queryset = Price.objects.all()
    serializer_class = PriceSerializer


class TypeViewSet(viewsets.ModelViewSet):
    queryset = Type.objects.all()
    serializer_class = TypeSerializer
