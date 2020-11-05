from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time

#验证码处理
def veriy(driver):
    js1='$( "#verifycode" ).attr( "placeholder" , "请在此输入" );'
    driver.execute_script(js1)
    js2 = 'alert("因机器学习识别还未完成，请在10s提示框自动关闭后，手动输入验证码，如出现验证码错误，请重新打开程序")'
    driver.execute_script(js2)
    time.sleep(10)
    try:
        driver.switch_to.alert.accept()
    except:
        print('用户已选择alert关闭')

    while True:
        value = driver.find_element_by_id('verifycode').get_attribute("value")
        if len(value) == 4:
            driver.find_element_by_id('submit').click()
            break
        time.sleep(1)

#元素定位
def locate(driver,way,place,*args):
    """
    :param driver:      驱动
    :param way:         定位方式:id,name,css,tag,xpath
    :param place:       元素位置
    :param args:        鬼知道
    :return:
    为了生命健康，就不设置默认定位方式了
    """
    if way=='id':
        temp=driver.find_element_by_id(place)
    elif way=='name':
        temp=driver.find_element_by_name(place)
    elif way=='xpath':
        temp=driver.find_element_by_xpath(place)

    time.sleep(1)
    return temp

#元素操作
def handle(driver,way="click",value=None):
    """
    :param driver:  找到的实例html元素对象
    :param way:     操作方式1.点击   2.填写
    :param value:   值
    :return:
    默认点击操作
    """
    if way=='click':
        driver.click()
    elif way=='text':
        driver.clear()
        driver.send_keys(value)

def main():
    driver = webdriver.Chrome('chromedriver.exe')
    driver.maximize_window()
    driver.get('http://10.100.100.26:8001/GXGDZC/?moduleId=5f97ecb1-dfe0-11e7-8ae7-00ac1110762f')
    temp=locate(driver,way='id',place='username')
    handle(driver=temp,way='text',value='张启程')
    temp = locate(driver, way='id', place='password')
    handle(driver=temp, way='text', value='abc131216')

    '''验证码处理'''
    veriy(driver)
    '''智能等待处理'''
    try:
        driver.implicitly_wait(10)      #智能等待10s
        element = locate(driver, way='xpath', place='//*[@id="first-menu"]/li[2]/a')
        handle(driver=element, way='click')
    except:
        print('网络连接超时')
        driver.quit()

    driver.switch_to.frame('iframe_010101')
    temp = locate(driver, way='id', place='cyfl_0')
    handle(driver=temp, way='click')


    '''业务处理---表单全填写'''
    """
    资产名称，分类代码，现状，价值类型，计量单位，单价，数量，入账形式
    """
    temp = locate(driver, way='id', place='txt_yqmc')
    handle(driver=temp, way='text',value='python自动化')
    temp = locate(driver, way='id', place='txt_flh')
    handle(driver=temp, way='text', value='03000000')
    Select(driver.find_element_by_id('drp_xz')).select_by_index(1)   # 实例化Select
    Select(driver.find_element_by_id('drp_jzxs')).select_by_index(1)   # 实例化Select
    Select(driver.find_element_by_id('drp_jldw')).select_by_index(1)  # 实例化Select
    temp = locate(driver, way='id', place='txt_dj')
    handle(driver=temp, way='text', value='2000')
    temp = locate(driver, way='id', place='txt_shl')
    handle(driver=temp, way='text', value='3')
    Select(driver.find_element_by_id('drp_jzlx')).select_by_index(1)  # 实例化Select

    time.sleep(5)

if __name__ == '__main__':
    main()