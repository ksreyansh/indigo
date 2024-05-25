from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("api/auth/", include("users.urls")),
    path("api/master-data/", include("master_data.urls")),
    path("admin/", admin.site.urls),
]

admin.site.site_header = "Indigo Bank Admin"
admin.site.site_title = "Indigo Bank Admin Portal"
admin.site.index_title = "Welcome to Indigo Bank Admin Portal"
