import os


def file_or_folder_dict(all_data):
    val=[]
    for i in all_data:
        if(os.path.isfile(i)):
            val.append({"name":i,"type":"file"})
        else:
            val.append({"name":i,"type":"folder"})
    return val


def create_folder(folder_name):
    os.mkdir(folder_name)


def create_file(file_name):
    with open(file_name,'w') as f:
        pass


def check_data():
    all_data = os.listdir()
    val = file_or_folder_dict(all_data)
    return val

