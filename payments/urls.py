from django.conf.urls import url
from . import views

app_name = "payments"

urlpatterns = [

    url(r"^add/(?P<challan_no>[0-9a-zA-Z-]+)/$", views.add, name="add"),
]