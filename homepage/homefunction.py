from homepage.models import *
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.core.files.storage import FileSystemStorage
import os

def tokenFile(image, path_mod, username, mod = 0):
    if image != None:
        path_img = path_mod + '/' + username
        fs = FileSystemStorage(location = path_img)
        if mod == 1:
            try:
                list_old_files = os.listdir(path_img)
                for oldfile in list_old_files:
                    fs.delete(oldfile)
            except:
                pass
        # fs = FileSystemStorage()
        # fs = FileSystemStorage(location='/media/users')
        avatar_name = fs.save(image.name, image)
        # avatar_url = fs.url(avatar_name)
        avatar_url = '/' + path_img + '/' + avatar_name #/media/users/
        print(avatar_url)
        return avatar_url
    else:
        return '/media/users/' + 'default.png'
    return None