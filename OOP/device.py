class Router:
    '''Router Class'''
    def __init__(self, model, swversion, ip_add):
        '''initialize values'''
        self.model = model
        self.swversion = swversion
        self.ip_add = ip_add
    
    def getdesc(self):
        '''return a formatted description of the router'''
        desc = f'Router Model           :{self.model}\n'\
               f'Software Version       :{self.swversion}\n'\
               f'Router MGMT Address    :{self.ip_add}\n'
        return desc

class Switch(Router):
    def getdesc(self):
        '''return a formatted description of the router'''
        desc = f'Switch Model           :{self.model}\n'\
               f'Switch Version         :{self.swversion}\n'\
               f'Switch MGMT Address    :{self.ip_add}\n'
        return desc
