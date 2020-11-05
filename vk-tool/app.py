from auth import authvk
from getpass import getpass as gp
import os
import webbrowser
from progress.bar import IncrementalBar
from tqdm import tqdm
from collections import OrderedDict
from operator import itemgetter




class Application():
    vk = authvk.auth()
    v='5.124'
    """
    Main application class
    """
    def renderfunclist(self):
        self.cls()
        print("""
     __ __  __  _         _____  __ __  ____     __ 
    |  |  ||  |/ ]       |     ||  |  ||    \   /  ]
    |  |  ||  ' /  _____ |   __||  |  ||  _  | /  / 
    |  |  ||    \ |     ||  |_  |  |  ||  |  |/  /  
    |  :  ||     ||_____||   _] |  :  ||  |  /   \_ 
     \   / |  .  |       |  |   |     ||  |  \     |
      \_/  |__|\_|       |__|    \__,_||__|__|\____|
                                                
                     Функционал
         
             1) Узнать скрытых друзей
     
             Введите номер нужной функции
    """)
        
        return int(input('... '))

    def funcselector(self, i):
        """
        Select function
        """
        switcher = {

        1: self.shf()

                    }

        return switcher.get(i)


    def cls(self):
        if os.name == 'nt': 
            os.system('cls') 
        else: 
            os.system('clear')

    def resolvename(self, target):
        """
        resolving vkid from alias 
        """
        try:
            target = int(target)
        except:
            target = self.vk.utils.resolveScreenName(
                screen_name=target,
                v="5.124"
                )['object_id']
        return target

    def shf(self):
        self.cls()
        hiddenlist = []
        target = self.resolvename(input('Введите ID человека: '))
        flist = self.vk.friends.get(user_id=target, v=self.v)['items']
        for friend in tqdm(flist, desc='Поиск скрытых друзей', leave=False, unit='друг'):
            try:
                fflist = self.vk.friends.get(user_id = friend, v='5.124')['items']
                if target not in fflist:
                    hiddenlist.append(friend)
            except authvk.vk_api.exceptions.VkApiError as e:
                pass
        if len(hiddenlist)!=0:
            report = f"\nВас скрыли:"
            for i in hiddenlist:
                report+=f"\n vk.com/id{str(i)}"
        else:
            report = "Вас никто не скрыл"
        print(report)
        input('Нажмите Enter что бы вернуться в главное меню.')
        self.__init__()

    def __init__(self):
        s = self.renderfunclist()
        self.funcselector(s)


if __name__ == "__main__":
    Application()
