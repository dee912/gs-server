from django.urls import path
from .views import ShoeListView, ShoeDetailView

urlpatterns = [
    path('', ShoeListView.as_view()),
    path('<int:pk>/', ShoeDetailView.as_view())
]
