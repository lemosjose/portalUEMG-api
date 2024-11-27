from django.contrib import admin
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
# Register your models here.

class UserManager(BaseUserManager):
    def createUser():
        if not email or not nickname:
            raise ValueError("Os valores de e-mail e nickname são obrigatórios")
        
        email = self.normalize_email(email)
        user = 
        user.set_password(password)
        #create usuario aqui
        return user 
        
        
    def createSuperUser(self, email, nickname, password=None):
        user = self.createUser(email, nickname, password)
        user.isSuperUser = True
        #create usuario aqui 
        return user 



    
