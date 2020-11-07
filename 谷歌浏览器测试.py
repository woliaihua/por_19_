from helium import *
import configparser
import chardet
from selenium.webdriver.chrome.options import Options
from  selenium import webdriver
from kill_prot import *
from send_request import SendRequest
from selenium.webdriver.support.ui import Select
from url_2_png import get_src_img
from img_2_text import png_2_text
from  time import sleep
from helium import *
from time import  sleep
import configparser
from itertools import zip_longest
import chardet
from kill_prot import *
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from locale import atof,setlocale,LC_NUMERIC
from email_oper import *
from get_template import get_temp_dict
from send_request import SendRequest
from selenium.webdriver.support.ui import Select
from yanzhengqi_oper import get_make_code
from base64_to_img import to_png
from chick_proxy import servers_chick_ip
from del_txt_line import del_line#用一行删除一行
from url_2_png import get_src_img
import datetime
"""
滑动图片验证
"""
from get_template import get_temp_dict

temp_dict  = get_temp_dict() #模板
def get_file_code(filename):
    f3 = open(filename, 'rb')
    data = f3.read()
    encode = chardet.detect(data).get('encoding')
    f3.close()
    return encode

#path1 = os.path.dirname(os.path.abspath(__file__))  # 获取当前目录
path2 ='config.ini'
encode = get_file_code(path2)
config = configparser.RawConfigParser()
config.read(path2, encoding=encode)
chrome_path = config.get('month', "chrome_path")  # 0-12 如果是0 就表示不指定月份

port =9022
#关闭浏览器
# kill_pid(port)
# # 关闭进程
# cmd = r'"{chrome_path}" --remote-debugging-port={port} --user-data-dir="C:\selenum\AutomationProfile{port}" --window-size=1080,800 '.format(chrome_path=chrome_path,port=port)  # --headless
# os.popen(cmd)
#接管浏览器
chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:{port}".format(port=port))
driver = webdriver.Chrome(executable_path="./chromedriver.exe", chrome_options=chrome_options)
script = '''
Object.defineProperty(navigator, 'webdriver', {
    get: () => undefined
})
'''
set_driver(driver)
driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {"source": script})
#driver.get('https://sellercentral.amazon.co.uk/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fsellercentral.amazon.co.uk%2Fhome&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=sc_uk_amazon_v2&openid.mode=checkid_setup&language=zh_CN&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&pageId=sc_uk_amazon_v2&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&ssoResponse=eyJ6aXAiOiJERUYiLCJlbmMiOiJBMjU2R0NNIiwiYWxnIjoiQTI1NktXIn0.a5mUI1lQr80X3ikb1RfOscCl9fzyVVqmwXRr7HiL8LvGu6_LPzJA3w.T45gQk4uPvjQ7NW0.Na-asGEBLFxeUQFlqMQgwJNXHMC74exdYEpDoxF-LZ9sURBQONC_tTvjCK5Rsr781XOY-SMbZMSmm3q4UhtKJKJVN3tYK-vsOlfm01WkIwsztXXVAtPK50U3GNL1TdWt83BC2gUPzCVvkSVunLWRqUtS3yqesp5rCOyBl4SKfhHTQs2581J8-15xVwQ7LiN1vVYU_tMMJWMimFq2SITB6lvXS9cm8Hs8Rv81scAwDMJUtyHMddsgLnOSZ3wRbY_YmVcS.IwaDHOGL2wtpgIvB_we95A')
#write('854639',into=S('//*[@name="verifyOTPButton"]'))
#write('+86 18040377309',into=S('//*[@id="country-phone-input"]'))
# click(S('//*[@id="go"]'))
print(driver.title)
# click(S('//*[@id="sia-otp-accordion-totp-header"]/i'))
#wait_until(S('//*[@name="addCreditCardNumber"]').exists, timeout_secs=1, interval_secs=0.4)  # 需要安全验证
#write('kejv0059',into=S('//*[@id="ap_password"]'))
wait_until(Text("We're sorry!").exists, timeout_secs=2, interval_secs=0.4)  ## 是否没货
print(datetime.datetime.now())
#if not CheckBox("is a beneficial owner of the business").is_checked():  # 复选框没有被选中
# click(CheckBox("is a beneficial owner of the business"))
# print(datetime.datetime.now())
# if not CheckBox("Don't require OTP on this browser").is_checked():
#     click(CheckBox("Don't require OTP on this browser"))
# write(temp_dict.get('银行卡号'), into=S('//*[@name="addCreditCardNumber"]'))
# Select(S('//*[@name="ccExpirationMonth" and not(@disabled)]').web_element).select_by_visible_text(temp_dict.get('到期日'))#有效期 日
# Select(S('//*[@name="ccExpirationYear" and not(@disabled)]').web_element).select_by_visible_text(temp_dict.get('到期年'))#有效期 日
# write(temp_dict.get('英文姓')+temp_dict.get('英文名'), into=S('//*[@name="ccHolderName"]'))

#click(S('//*[@id="cancelOTPLink"]/span'))  # 点击提交，但是提交后可能没货
# txt = S('//*[@id="container"]//img').web_element.get_attribute('src')
def save_txt( txt):
    def get_file_code():
        f3 = open('结果.txt', 'rb')
        data = f3.read()
        encode = chardet.detect(data).get('encoding')
        f3.close()
        return encode

    with open('结果.txt', 'a', encoding=get_file_code()) as f:
        f.write(txt + '\n')


def liucheng3(self):
    print('开始第三步流程')
    wait_until(S('//*[@name="addCreditCardNumber"]').exists, timeout_secs=100, interval_secs=0.5)  # 需要安全验证
    write(temp_dict.get('银行卡号'), into=S('//*[@name="addCreditCardNumber"]'))
    Select(S('//*[@name="ccExpirationMonth" and not(@disabled)]').web_element).select_by_visible_text(
        temp_dict.get('到期日'))  # 有效期 日
    Select(S('//*[@name="ccExpirationYear" and not(@disabled)]').web_element).select_by_visible_text(
        temp_dict.get('到期年'))  # 有效期 日
    write(temp_dict.get('英文姓') + temp_dict.get('英文名'), into=S('//*[@name="ccHolderName"]'))
    # write('854639', into=S('//*[@name="otpInput"]'))  # 输入验证码
    click('Save')
    wait_until(S('//*[@name="Submit"]').exists, timeout_secs=60, interval_secs=0.5)
    click(S('//*[@name="Submit"]'))  # 保存并继续


def liucheng4():
    print('开始第四步流程')
    click(Link('listing your products'))
    name = temp_dict.get('商品英文名')
    write(name, into=S('//*[@name="displayNameField"]'))
    click(S('//*[@name="Submit"]'))  # 点击提交，但是提交后可能没货

    def chick():  # 检查是否有货
        for i in range(1, 1000):
            try:
                wait_until(Text('Not available').exists, timeout_secs=4, interval_secs=0.4)  ## 没保存表示没货
                write(name + str(i), into=S('//*[@name="displayNameField"]'))
                click(S('//*[@name="Submit"]'))  # 点击提交，但是提交后可能没货
            except:  # 有货
                return

    chick()
    click('Start listing your products')
    wait_until(Text('View Credit Card Info').exists, timeout_secs=100, interval_secs=0.5)
    click(Button('View Credit Card Info'))  # 查看信用卡信息
    click(Button('Enable Two-Step Verification'))  # 启动两步验证
    # 这里要输入密码
    click(S('//*[@id="sia-otp-accordion-totp-header"]/i'))  # 点击充应用器注册
    sleep(1.5)
    click(Link("Can't scan the barcode?"))
    sleep(0.2)
    tet = S('//*[@id="sia-auth-app-formatted-secret"]').web_element.text  # 这个是生成玛
    print(tet)
    code = get_make_code(tet)
    write(code, S('//*[@id="ch-auth-app-code-input"]'))
    # APP转码这里留着下次做
    base64_str = S('//*[@id="container"]//img').web_element.get_attribute('src')
    to_png(base64_str, './img2/{}.png'.format(name))  # 保存图片
    # 存储
    save_txt(name)
    save_txt('123123123213')
    save_txt(tet)
    save_txt('*' * 70)
    click(S('//*[@id="ch-auth-app-submit"]'))  # 点击验证
    if not CheckBox("Don't require OTP on this browser").is_checked():  # 勾选请勿记住密码
        click(CheckBox("Don't require OTP on this browser"))
    click(S('//*[@id="enable-mfa-form-submit"]'))  # 提交


#liucheng4()
#wait_until(Text('验证码输入有误，请重新输入').exists, timeout_secs=2, interval_secs=0.4)  # 需要安全验证