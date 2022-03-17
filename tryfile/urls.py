
from django.contrib import admin
from django.urls import path
from core.views import (home,GetFolderData,
GoBackFolder,GoHome,DeleteFileFolder)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home,name="home"),
    path('go-home/',GoHome.as_view(),name="go-home"),
    path('folder/',GetFolderData.as_view(),name="folder"),
    path('back=folder/',GoBackFolder.as_view(),name="back-folder"),
    path('delete-folder/',DeleteFileFolder.as_view(),name="delete-folder"),
]
