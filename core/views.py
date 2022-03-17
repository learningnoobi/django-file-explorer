from django.shortcuts import render,redirect
import os
from pathlib import Path
import shutil
from django.views import View
from core.utils import (check_data,
                        create_file, 
                        create_folder, 
                        file_or_folder_dict)

cwd = os.getcwd()
home_path = os.path.join(cwd,'manager')
os.chdir(home_path)

def inHome():
    return home_path == os.getcwd()


def home(request):
    if request.method=="GET":
        val=check_data()
        context ={"all_data":val,"inHome":inHome()}
        return render(request,'core/home.html',context)
        
    if request.method=="POST":
        data = request.POST
        name = data.get("filename")
        if "folder" in data:
            create_folder(name)
        if "file" in data:
            create_file(name)
        val=check_data()
        context ={"all_data":val,"inHome":inHome()}
        return render(request,'core/home.html',context)

class GoHome(View):
    def post (self,request):
        os.chdir(home_path)
        val=check_data()
        context ={"all_data":val,"inHome":inHome()}
        return render(request,'core/home.html',context)

class GetFolderData(View):

    def post(self,request):
        folder = request.POST.get("folder")
        path=os.path.join(os.getcwd(),folder)
        os.chdir(path)
        all_data = os.listdir()
        val = file_or_folder_dict(all_data)
        context ={"all_data":val,"inHome":inHome()}
        return render(request,'core/home.html',context)


class GoBackFolder(View):
    def post(self,request):
        os.chdir('..')
        all_data = os.listdir()
        val = file_or_folder_dict(all_data)
        context ={"all_data":val,"inHome":inHome()}
        return render(request,'core/home.html',context)

class DeleteFileFolder(View):

    def post(self,request):
        print(request.POST)
        folder = request.POST.get("folder")
        path=os.path.join(os.getcwd(),folder)
        if os.path.isdir(path):
            shutil.rmtree(path)
        if os.path.isfile(path):
            os.remove(path)
        # os.chdir('..')
        all_data = os.listdir()
        val = file_or_folder_dict(all_data)
        context ={"all_data":val,"inHome":inHome()}
        return render(request,'core/home.html',context)