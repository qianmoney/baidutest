from time import sleep

from selenium.webdriver.common.by import By

from baidu.test_case.page_obj.base import Page


class login(Page):

    """用户登录页面"""

    url = '/'
    baidu_login_button_loc = (By.XPATH,'// *[ @ id = "u1"] / a[7]')
    baidu_login_user_name_loc = (By.XPATH,'//*[@id="TANGRAM__PSP_10__footerULoginBtn"]')
    #登录页面
    def baidu_login(self):
        self.find_element(*self.baidu_login_button_loc).click()
        sleep(2)
        self.find_element(*self.baidu_login_user_name_loc).click()

    login_username_loc = (By.XPATH,'//*[@id="TANGRAM__PSP_10__userName"]')
    login_password_loc = (By.XPATH,'//*[@id="TANGRAM__PSP_10__password"]')
    login_button_loc = (By.XPATH,'//*[@id="TANGRAM__PSP_10__submit"]')

    #登录用户名
    def login_username(self,username):
        self.find_element(*self.login_username_loc).send_keys(username)

    #登录密码
    def login_password(self,password):
        self.find_element(*self.login_password_loc).send_keys(password)

    #登录按钮
    def login_button(self):
        self.find_element(*self.login_button_loc).click()

    #定义统一登录入口
    def user_login(self,username,password):
        self.open()
        sleep(2)
        self.baidu_login()
        self.login_username(username)
        self.login_password(password)
        self.login_button()
        sleep(1)


    login_error_hint_loc = (By.XPATH,'//*[@id="TANGRAM__PSP_10__error"]')
    #登录有误提示信息
    def login_error_hint(self):
        return self.find_element(*self.login_error_hint_loc).text






