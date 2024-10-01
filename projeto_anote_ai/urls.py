
from django.contrib import admin
from django.urls import path
from anote_ai import views
from usuarios import views as usuario_views
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('conta/', usuario_views.novo_usuario, name='novo_usuario'),
    path('login/',auth_views.LoginView.as_view(template_name='usuarios/login.html'), name='login'),
    path('logout/',auth_views.LogoutView.as_view(template_name='usuarios/logout.html'), name='logout'),
    path('',views.anotacoes, name='anotacoes'),
    path('nova_anotacao/', views.criar,name='nova_anotacao'),
    path('nova_anotacao/<int:id_anotacao>', views.editar, name='editar'),
    path('excluir_anotacao/<int:id_anotacao>', views.excluir, name='excluir'),
    path('/<int:id_anotacao>', views.detalhe, name='detalhe')
   
]
