from Conn_mysql import connect_database
from selenium import webdriver
from selenium.webdriver.common.by import By
class Test_注册模块:

    @classmethod
    def setup_class(cls):
        print("\n=====初始化类操作=====\n");
        sqls = []
        sqls.append("DELETE FROM user WHERE username LIKE 'test_%'")
        connect_database("122.112.139.207", "root", "Mysql66!", "community", sqls)

    @classmethod
    def teardown_class(cls):
        print("\n=====清除类操作=====\n");
        #清除数据库中用户名为test_xx的用户
        sqls = []
        sqls.append("DELETE FROM user WHERE username LIKE 'test_%'")
        connect_database("122.112.139.207", "root", "Mysql66!", "community", sqls)

    #注册操作
    def siginCheck(self, username, password, confirm_password, email):
        driver = webdriver.Chrome(r'D:\AutoTest\chromedriver.exe')
        driver.implicitly_wait(10)

        driver.get("http://122.112.139.207:8080/register")

        username_elem = driver.find_element(By.ID, "username")
        username_elem.clear()
        username_elem.send_keys(username)

        password_elem = driver.find_element(By.ID, "password")
        password_elem.clear()
        password_elem.send_keys(password)

        confirm_password_elem = driver.find_element(By.ID, "confirm-password")
        confirm_password_elem.clear()
        confirm_password_elem.send_keys(confirm_password)

        email_elem = driver.find_element(By.ID, "email")
        email_elem.clear()
        email_elem.send_keys(email)

        submit_btn = driver.find_element_by_xpath("//*[@class='btn btn-info text-white form-control']")
        submit_btn.click()

    #注册成功
    def test_sigin_001(self):
        self.siginCheck("test_liugang1","123456","123456","test_liugang1@qq.com")






