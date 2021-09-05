from django.urls import path
from .views import ShoeListView

urlpatterns = [
    path('', ShoeListView.as_view())
]
