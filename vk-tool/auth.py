class authvk():
    import vk_api
    import getpass
    """
    Auth vk
    """
    def auth_handler():
        key = input("Введите код аутентификации: ")
        remember_device = True
        return key, remember_device

    def captcha_handler(self, captcha):
        key = input("Введите captcha код : ")
        webbrowser.open(captcha.get_url())
        return captcha.try_again(key)
    
    @classmethod
    def auth(cls):
        vk_session = cls.vk_api.VkApi(
            login=input('Login: '), 
            password=cls.getpass.getpass(),
            captcha_handler=cls.captcha_handler,
            auth_handler=cls.auth_handler)
        try:
            vk_session.auth()
        except cls.vk_api.AuthError as error_msg:
            print(error_msg)
            exit()
        vk = vk_session.get_api()
        return vk

    

