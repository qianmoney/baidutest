from time import sleep
import unittest,random,sys
from baidu.test_case.models import myunit,function
from baidu.test_case.page_obj.loginPage import login


class loginTest(myunit.MyTest):
    """百度登录测试"""
    #测试用户登录
    def user_login_verify(self,username='',password=''):
        login(self.driver).user_login(username,password)

    def test_login1(self):
        #用户名、密码为空登录
        self.user_login_verify()
        po = login(self.driver)
        self.assertEqual(po.login_error_hint(),'请您输入手机/邮箱/用户名')
        function.insert_img(self.driver,'用户名密码为空.png')

    def test_login2(self):
        #密码为空
        self.user_login_verify(username='908852378@qq.com')
        po = login(self.driver)
        self.assertEqual(po.login_error_hint(), '请您输入密码')
        function.insert_img(self.driver, '密码为空.png')

    def test_login3(self):
        #账号有误
        self.user_login_verify(username='908852378@qq.',password='1111')
        po = login(self.driver)
        function.insert_img(self.driver, '账号格式不正确.png')
        self.assertEqual(po.login_error_hint(), '您输入的帐号格式不正确')
        function.insert_img(self.driver, '账号格式不正确.png')

if __name__ == '__main__':
    test = loginTest()
    test.test_login1()
