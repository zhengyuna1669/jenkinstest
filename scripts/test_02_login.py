import allure


def test_a():
    print("aaa")

@allure.step(title="测试登录的流程")
def test_login():
    allure.attach('登录','输入用户名')
    print("aaa")

    allure.attach('登录','输入密码')
    print("bbb")

    allure.attach('登录','点击登录')
    print("ccc")
    assert 1
