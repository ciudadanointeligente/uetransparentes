from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    # path("", LeyListView.as_view(), name="ley_list"),
    # path("<int:pk>/", LeyDetailView.as_view(), name="ley_detail"),
]
