from django.urls import path
from .views import person_list, person_new, person_update, person_delete, PersonList, PersonDetail, PersonCreate, \
    PersonUpdate, PersonDelete, ProdutoBulk

urlpatterns = [
    path('listar/', person_list, name='person_list'),
    path('novo/', person_new, name='person_new'),
    path('atualizar/<int:id>/', person_update, name='person_update'),
    path('deletar/<int:id>/', person_delete, name='person_delete'),
    path('person-list/', PersonList.as_view(), name='person_list_cbv'),
    path('person-detail/<int:pk>/', PersonDetail.as_view(), name='person_detail_cbv'),
    path('person-create/', PersonCreate.as_view(), name='person_create_cbv'),
    path('person-update/<int:pk>/', PersonUpdate.as_view(), name='person_update_cbv'),
    path('person-delete/<int:pk>/', PersonDelete.as_view(), name='person_delete_cbv'),
    path('person_bulk/', ProdutoBulk.as_view(), name='person_bulk_cbv'),

]