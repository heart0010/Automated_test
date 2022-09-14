from selenium import webdriver
from selenium.webdriver.common.by import By
from PIL import Image
from baidu_orc import baiduOCR

path = 'D:/pic1.png'


def get_verify_code():
    option = webdriver.ChromeOptions()

    option.add_experimental_option('useAutomationExtension', False)
    option.add_experimental_option("excludeSwitches", ['enable-automation'])

    base_url = 'http://192.168.108.210/etp/login/1'
    browser = webdriver.Chrome(options=option)
    browser.maximize_window()

    browser.get(base_url)
    browser.implicitly_wait(10)

    # 登录页面截图
    browser.save_screenshot("D:/pic.png")

    # 获取图片验证码坐标
    code_ele = browser.find_element(by=By.XPATH, value='//*[@id="app"]/div/div/form/div[4]/div/img')

    print("验证码的坐标为：", code_ele.location)
    print("验证码的大小为：", code_ele.size)

    # 图片4个点的坐标位置
    left = code_ele.location['x']
    # left = 1232.237548828125
    top = code_ele.location['y']
    # top = 310.7749938964844
    right = code_ele.size['width'] + left
    down = code_ele.size['height'] + top
    print("left =", left)
    print('top =', top)
    print('right =', right)
    print('down =', down)
    image = Image.open('D:/pic.png')
    browser.implicitly_wait(5)
    # 将图片验证码截取
    code_image = image.crop((left, top, right, down))
    code_image.save(path)

    # 调用百度文字识别技术，识别图片中的文字
    res = baiduOCR(path)
    return res


if __name__ == '__main__':
    res = get_verify_code()
    print(res)
