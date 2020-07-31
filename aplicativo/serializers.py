from rest_framework import serializers
from aplicativo.models import Pessoa

class PessoaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pessoa
        fields = ['id', 'name', 'sexo', 'cpf', 'idade']
        #na fields colocamos o que queremos utilizar
        #da classe pessoa criada no models.py, por padrao a id é dada pelo django