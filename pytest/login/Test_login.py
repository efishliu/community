from selenium import webdriver
from selenium.webdriver.common.by import By

class Test_登录模块:

    def loginCheck(self, username, password, verify_code):
        driver = webdriver.Chrome(r'D:\AutoTest\chromedriver.exe')
        driver.implicitly_wait(10)

        driver.get("http://122.112.139.207:8080/login")

        if username is not None:
            username_elem = driver.find_element(By.ID, "username")
            if username_elem is None:
                print("\nERROR:找不到username元素\n")
            username_elem.clear()
            username_elem.send_keys(username)
        if password is not None:
            password_elem = driver.find_element(By.ID, "password")
            if password_elem is None:
                print("\nERROR:找不到password元素\n")
            password_elem.clear()
            password_elem.send_keys(password)
        if verify_code is not None:
            code_elem = driver.find_element(By.ID, "verifycode");
            if code_elem is None:
                print("\nERROR:找不到verifycode元素\n")
            code_elem.clear()
            code_elem.send_keys(verify_code)
        submit_btn = driver.find_element_by_xpath("//*[@class='btn btn-info text-white form-control']")
        if submit_btn is None:
            print("\nERROR:找不到submit元素\n")
        submit_btn.click()

        #判断返回值
        driver.implicitly_wait(100)
        current_url = driver.current_url
        if current_url == "http://122.112.139.207:8080/login":
            res_elem = driver.find_elements(By.XPATH, "//*[@class='invalid-feedback']")
            index = 0
            result = []
            for res in res_elem:
                result.append(res.text)
        else:
            result = current_url
        driver.quit()
        return result

    #用户名不存在
    def test_login_001(self):
        result = self.loginCheck("liu","123456","1234")
        #print(result)
        assert result[0] == "该账号不存在!"

    #密码错误
    def test_login_002(self):
        result = self.loginCheck("liugang","1234566","1234")
        assert result[1] == "密码不正确!"
    #验证码错误
    def test_login_003(self):
        result = self.loginCheck("liugang","123456","1233")
        assert result[2] == "验证码不正确!"
    #登录成功
    def test_login_004(self):
        result = self.loginCheck("liugang", "123456", "1234")
        assert result == "http://122.112.139.207:8080/index"
