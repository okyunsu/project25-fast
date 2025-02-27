from com.okyunsu.auth.user.service.abstract_user import AbstractUser


class HelloAdmin(AbstractUser):
    
    def handle(slef, **kwargs):
        return "Hello User"    