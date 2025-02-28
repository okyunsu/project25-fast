
from com.okyunsu.auth.admin.web.admin_factory import AdminFactory


class AdminController:
    def __init__(self):
        pass

    def hello_user(self,**kwargs):
        return AdminFactory.create(strategy="hello_user",**kwargs)  