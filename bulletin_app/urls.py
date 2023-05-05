from django.urls import path

from . import views
urlpatterns = [
    # User URLs
    path('users/', views.UserListCreateView.as_view(), name='user-list-create'),
    path('users/<int:pk>/', views.UserRetrieveUpdateDestroyView.as_view(), name='user-detail'),

    # Organization URLs
    path('organizations/', views.OrganizationListCreateView.as_view(), name='organization-list-create'),
    path('organizations/<int:pk>/', views.OrganizationRetrieveUpdateDestroyView.as_view(), name='organization-detail'),

    # Ship URLs
    path('ships/', views.ShipListCreateView.as_view(), name='ship-list-create'),
    path('ships/<int:pk>/', views.ShipRetrieveUpdateDestroyView.as_view(), name='ship-detail'),

    # Voyage URLs
    path('voyages/', views.VoyageListCreateView.as_view(), name='voyage-list-create'),
    path('voyages/<int:pk>/', views.VoyageRetrieveUpdateDestroyView.as_view(), name='voyage-detail'),
]
