"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from escola.views import AlunosViewSet, CursosViewSet, MatriculasViewSet, ListaAlunosMatriculados
from rest_framework import routers

from django.conf import settings
from django.conf.urls.static import static

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
   openapi.Info(
      title="Rnx Escola",
      default_version='v0.0.1',
      description="coisas do curso",
      terms_of_service="#",
      contact=openapi.Contact(email="rnx@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

router = routers.DefaultRouter()
router.register('alunos', AlunosViewSet, basename='Alunos')
router.register('cursos', CursosViewSet, basename='Cursos')
router.register('matriculas', MatriculasViewSet, basename='Matriculas')


urlpatterns = [
    path('controle_geral/', admin.site.urls),
    path('', include(router.urls)),
    # path('aluno/<int:pk>/matriculas/', ListaMatriculasAluno.as_view()),
    path('cursos/<int:pk>/matriculas/', ListaAlunosMatriculados.as_view()),
    
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

    path('admin/', include('admin_honeypot.urls', namespace='admin_honeypot')),
   

]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
