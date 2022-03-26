import os
import sys



imageType = [".png",".jpg",".jpeg",".JPG",".JPEG",".SVG",".svg"]


def giveDict(i,filetype="nothing",url=None):
    slug = '-'.join(i.split(' '))
    return {"name":i,"type":"file","filetype":filetype,"slug":slug,'url':url}

def file_or_folder_dict(all_data):
    val=[]
    for i in all_data:
        _,type = os.path.splitext(i)
        
        
        if(os.path.isfile(i)):
            if ".py" in i: 
                dict = giveDict(i,"python")
                val.append(dict)
            elif ".html" in i:
                dict = giveDict(i,"html")
                val.append(dict)
            
            elif ".js" in i:
                dict = giveDict(i,"js")
                val.append(dict)

            elif ".sql" in i:
                dict = giveDict(i,"sql")
                val.append(dict)

            elif type in imageType:
                path = os.path.join(os.getcwd(),i).strip()
                print(sys.platform)
                url ='/'.join(path.split('/')[3:])

                print('image  is ',url)
                dict = giveDict(i,"image",url)
                val.append(dict)
            else:
                dict = giveDict(i)
                val.append(dict)
        else:
            slug = '-'.join(i.split(' '))
            val.append({"name":i,"type":"folder","slug":slug})
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

