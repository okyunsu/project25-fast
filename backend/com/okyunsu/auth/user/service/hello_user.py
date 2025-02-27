from com.okyunsu.auth.user.service.abstract_user import AbstractUser


class HelloUser(AbstractUser):
    
    def handle(slef, **kwargs):
        return "Hello User"    