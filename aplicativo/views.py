from django.shortcuts import render
from rest_framework.decorators import api_view
#decorator são o que herdamos nas classes
from rest_framework.views import APIView

from aplicativo.models import Pessoa
from aplicativo.serializers import PessoaSerializer
from rest_framework.response import Response
#o response precisamos importar pois é exatamente o que ele vai retornar pra minha view
from rest_framework import status

from rest_framework import generics
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from rest_framework import viewsets


class PessoaViewSet(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]
    #as duas primeiras linhas serve para que a pessoa só possa acessar as info do site se estiver logada
    queryset = Pessoa.objects.all()
    serializer_class = PessoaSerializer

# Create your views here.
class PessoaList(generics.ListCreateAPIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = Pessoa.objects.all()
    #para passar todos os objetos de pessoa, na model
    serializer_class = PessoaSerializer
    #chamando a classe do serializer, onde ele passa todos as infos da model para o api poder ler

class PessoaRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Pessoa.objects.all()
    serializer_class = PessoaSerializer
































#class PessoaList(APIView):
    # def get(self, request):
    #     #estamos pegando os objetos pelo metodo get
    #     pessoa = Pessoa.objects.all()
    #     serializer = PessoaSerializer(pessoa, many=True)
    #     return Response(serializer.data)
    #     #get só pega os dados do banco

    # def post (self, request):
    #     serializer = PessoaSerializer(data = request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    #     #entre a linha 23 e 26 é uma are de conferencia ver se o que o usuario passou ta certo ou ta errado
    #     #metodo post faz tipo uma postagem dos dados que ele pega do usuario



#class PessoaRetrieveUpdateDestroy(APIView):
 #   def get(self,request,pk):
  #      serializer = PessoaSerializer(Pessoa)
   #     return Response(serializer.data)

    #def put(self,request)






# @api_view(['GET', 'PUT', 'DELETE'])
# #essas são os tipos de requisição http, que o apiview trabalja com ele
# #em sequencia, ler os dados, alterar os dados, e deletar os dados
# def pessoa_detail_change_and_delete(request, pk):
#     try:
#         pessoa = Pessoa.objects.get(pk = pk)
#     except Pessoa.DoesNotExist:
#         return Response(status = status.HTTP_404_NOT_FOUND)
        
#     if request.method == 'GET' :
#         serializer = PessoaSerializer(pessoa)
#         return Response(serializer.data)
#     elif  request.method == 'PUT':
#         serializer = PessoaSerializer(pessoa, data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
#     elif request.method == 'DELETE' :
#         pessoa.delete()
#         return Response(status = status.HTTP_204_NOT_CONTENT)
