from vista import *


class client:

    def login(token):
        if vista.check is True:
            print("Status = 101, Login True")
        if vista.check is False:
            print("Status = 404, Login False")
            vista.returnStatus(Status)
            return