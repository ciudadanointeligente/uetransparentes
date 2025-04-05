from django.urls import path
from .views import LeyListView, LeyDetailView

urlpatterns = [
    path("", LeyListView.as_view(), name="ley_list"),
    path("<int:pk>/", LeyDetailView.as_view(), name="ley_detail"),
]
