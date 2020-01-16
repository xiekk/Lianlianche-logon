from selenium import webdriver
from time import sleep
wd = webdriver.Chrome()
wd.get('http://test.lianlianche.com/index.html#/login')
element_account = wd.find_element_by_css_selector('.el-input input[placeholder="请输入账号"]')
element_password = wd.find_element_by_css_selector('.el-input input[placeholder="请输入密码"]')
element_logon = wd.find_element_by_css_selector('.el-form-item__content button')
element_account.send_keys('18900242712')
element_password.send_keys('123456')
element_logon.click()
#打开车金融管理菜单
#设置最大等待时间10秒
wd.implicitly_wait(10)
element_menu1 = wd.find_element_by_css_selector('.menu-wrapper > li:nth-child(5) > .el-submenu__title > i')
element_menu1.click()
#设置最大等待时间10秒
wd.implicitly_wait(10)
#打开订单管理页面
element_menu2 = wd.find_element_by_css_selector('.menu-wrapper > li:nth-child(5) > ul >a:nth-child(1)')
element_menu2.click()
wd.implicitly_wait(10)
element_new_order = wd.find_element_by_css_selector('div.el-form-item:last-child button span')
element_new_order.click()
wd.implicitly_wait(10)
element_enter_date = wd.find_element_by_css_selector('.el-form:nth-child(2) div.el-col:nth-child(1) input')
wd.implicitly_wait(10)
element_enter_date.click()
wd.implicitly_wait(10)
element_enter_date1 = wd.find_element_by_css_selector('.el-picker-panel__body-wrapper .el-date-table__row:nth-child(2) .available:nth-child(4)')
wd.implicitly_wait(10)
element_enter_date1.click()


