from . import views
from django.conf.urls import url


urlpatterns = [
    url(r'^$', views.first, name='first'),
    url(r'^register/$', views.register,name='register'),
    url(r'^register/success/$',views.register_success,name='register_success'),
    url(r'^admin$', views.admin, name='admin'),
    url(r'^getData$', views.getData, name='getData'),
    url(r'^addItem/(?P<id>\d+)$', views.addItem, name='addItem'),
    url(r'^editItem/(?P<id>\d+)$', views.editItem, name='editItem'),
    url(r'^editItem/updateItem/(?P<id>\d+)$', views.updateItem, name='updateItem'),
    url(r'^delItem/(?P<id>\d+)$', views.delItem, name='delItem'),
    url(r'^saveItem$', views.saveItem, name='saveItem'),
    url(r'^first$', views.first, name='first'),
    url(r'^saveData$', views.saveData, name='saveData'),
    url(r'^second$', views.second, name='second'),
    url(r'^mainSave$', views.mainSave, name='mainSave'),
    url(r'^drinkSave$', views.drinkSave, name='drinkSave'),
    url(r'^dessertSave$', views.dessertSave, name='dessertSave'),
    url(r'^sideSave$', views.sideSave, name='sideSave'),
    url(r'^calc$', views.calc, name='calc')
]
