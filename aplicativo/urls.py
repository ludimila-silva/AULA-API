# from django.urls import path
# from aplicativo import views
from aplicativo.views import PessoaViewSet, PessoaList, PessoaRetrieveUpdateDestroy

from rest_framework.routers import DefaultRouter
#router, é uma biblioteca do rest framework que trata das rotas

router = DefaultRouter()
router.register(r'pessoa', PessoaViewSet)
#registrar as minhas urls dentro da minha variavel rota, ai dentro das aspas é como eu quero chamar no navegador
#se nao colocar nada nas aspas ele ja vai pra pagina inicial que contem os dados inseridos
urlpatterns = router.urls
#eu atribuo as urls que estao registradas na variavel rota


# urlpatterns = [
#     path('pessoa/list', view = views.PessoaList.as_view(), name='pessoa-list'),
#     #path('<int:pk>/', pessoa_detail_change_and_delete)
#     path('pessoa/rud/<int:pk>/', view = views.PessoaRetrieveUpdateDestroy.as_view(), name='pessoa-rud'),
#     #quando é uma FBV não precisa do .as_view
# ]

