
#registrasi
browser.find_element_by_link_text('Registrasi').click()
#daftar
browser.find_element_by_link_text('Daftar').click()
#daftar member
browser.find_element_by_link_text('Daftar Member').click()
#contact center
browser.find_element_by_link_text('Contact Center').click()
#link kontak wa
browser.find_element_by_xpath('//*[@id="banner-holder"]/div/div/div/ul/li[2]/a').click()

from selenium import webdriver
from time import sleep

browser = webdriver.Chrome()
sleep(1)
browser.get('https://www.tokoperhutani.com/')

sleep(1)
browser.find_element_by_xpath('//*[@id="bannerModal"]/div/div/div[1]/button').click()

browser.find_element_by_link_text('Daftar').click()
sleep(1)
browser.find_element_by_link_text('Daftar Member').click()

browser.find_element_by_xpath('//*[@id="nama"]').send_keys('Kurnia dani')
browser.find_element_by_xpath('//*[@id="alamat"]').send_keys('jalan Sariasih no 2')
browser.find_element_by_xpath('//*[@id="email_val"]').send_keys('kurniadani@gmail.com')
browser.find_element_by_id('tgl_lahir').click()
browser.find_element_by_xpath('//*[@id="ui-datepicker-div"]/table/tbody/tr[2]/td[2]').click()
browser.find_element_by_xpath('//*[@id="hp"]').send_keys('628123245343')
browser.find_element_by_xpath('//*[@id="no_ktp"]').send_keys('33101212822220005')
browser.find_element_by_xpath('//*[@id="tippe"]/option[3]').click()
browser.find_element_by_xpath('//*[@id="checklist"]').click()
browser.find_element_by_xpath('//*[@id="i_submit"]').click()

browser.find_element_by_link_text('Beranda').click()
browser.find_element_by_link_text('Contact Center').click()
browser.find_element_by_xpath('//*[@id="banner-holder"]/div/div/div/ul/li[2]/a').click()

#tutorial login
browser.get('https://www.tokoperhutani.com/')

browser.find_element_by_xpath('//*[@id="bannerModal"]/div/div/div[1]/button').click()

browser.find_element_by_xpath('/html/body/div/nav/div/div[2]/ul/li[1]/a/strong').click()

browser.find_element_by_id('email').send_keys('dindaayuprtw@gmail.com')

browser.find_element_by_id('password').send_keys("5BF5DF")

browser.find_element_by_class_name('le-button').click()

#menemukan ktp
browser.find_element_by_xpath('/html/body/div/nav/div/div[2]/ul/strong/li/a').click()

browser.find_element_by_link_text('Profile').click()
#atau
browser.get('https://www.tokoperhutani.com/member/profile')
#mendapatkan no ktp
no_ktp = browser.find_element_by_xpath('//*[@id="gaming"]/div/div/ul/li[3]/div')
print(no_ktp.text)

#mencari jenis kayu jati
browser.get('https://www.tokoperhutani.com/')
#Tutup Modal
browser.find_element_by_xpath('//*[@id="bannerModal"]/div/div/div[1]/button').click()
#Klik Login
browser.find_element_by_xpath('/html/body/div/nav/div/div[2]/ul/li[1]/a/strong').click()
#Input 
browser.find_element_by_id('email').send_keys('dindaayuprtw@gmail.com')
browser.find_element_by_id('password').send_keys("5BF5DF")
#Submit
browser.find_element_by_class_name('le-button').click()

browser.find_element_by_link_text('Beranda').click()
sleep(1)
browser.find_element_by_xpath('//*[@id="top-banner-and-menu"]/div/div[1]/div/nav/ul/li[1]/a').click()
sleep(1)

#Mencari Jenis Kayu Jati 
def cari_kayu():
    browser.find_element_by_xpath('//*[@id="wilayah"]').click()
    sleep(1)
    browser.find_element_by_xpath('//*[@id="wilayah"]/option[4]').click()
    sleep(1)
    browser.find_element_by_xpath('//*[@id="kota"]').click()
    sleep(1)
    browser.find_element_by_xpath('//*[@id="kota"]/option[2]').click()
    sleep(1)
    browser.find_element_by_xpath('//*[@id="select_kota"]').click()
    sleep(1)
    browser.find_element_by_xpath('//*[@id="select_kota"]/option[2]').click()
    sleep(2)
    browser.find_element_by_id('i_submit').click()

cari_kayu()
#menekan beli
browser.find_element_by_xpath('/html/body/div/strong/div[8]/div/div/form/input').click()
sleep(10)
#Konﬁrmasi Pesanan
browser.find_element_by_xpath('//*[@id="example"]/tbody/tr[2]/td[1]/input').click()
sleep(1)
browser.find_element_by_xpath('//*[@id="frm-example"]/input').click()
sleep(2)
browser.find_element_by_xpath('//*[@id="listTrolley"]/div/div/div[3]/a/button').click()
sleep(5)
browser.find_element_by_xpath('//*[@id="channelPayment"]/div/ul/li[4]/label').click()

browser.find_element_by_id('confirmOrder').click()

from selenium import webdriver
from time import sleep

browser = webdriver.Chrome()

browser.get('https://www.tokoperhutani.com/')

#Tutup Modal
browser.find_element_by_xpath('//*[@id="bannerModal"]/div/div/div[1]/button').click()

#Klik Login
sleep(2)
browser.find_element_by_xpath('/html/body/div/nav/div/div[2]/ul/li[1]/a/strong').click()

#Input 
sleep(2)
browser.find_element_by_id('email').send_keys('dindaayuprtw@gmail.com')
browser.find_element_by_id('password').send_keys("5BF5DF")

#Submit
browser.find_element_by_class_name('le-button').click()

#Masuk halaman beranda
sleep(1)
browser.get('https://tokoperhutani.com/beranda')

#Mencari Jenis Kayu Jati 
def cari_kayu():
    browser.find_element_by_xpath('//*[@id="wilayah"]').click()
    sleep(1)
    browser.find_element_by_xpath('//*[@id="wilayah"]/option[4]').click()
    sleep(1)
    browser.find_element_by_xpath('//*[@id="kota"]').click()
    sleep(1)
    browser.find_element_by_xpath('//*[@id="kota"]/option[2]').click()
    sleep(1)
    browser.find_element_by_xpath('//*[@id="select_kota"]').click()
    sleep(1)
    browser.find_element_by_xpath('//*[@id="select_kota"]/option[2]').click()
    sleep(2)
    browser.find_element_by_id('i_submit').click()

cari_kayu()
browser.find_element_by_xpath('/html/body/div/strong/div[8]/div/div/form/input').click()

#pengambilan data
table = browser.find_element_by_id('example')
for row in table.find_elements_by_css_selector('tr'):
    for cell in row.find_elements_by_tag_name('td'):
        print(cell.text)

browser.find_element_by_xpath('/html/body/div/nav/div/div[2]/ul/strong/li/a').click()
browser.find_element_by_xpath('/html/body/div/nav/div/div[2]/ul/strong/li/ul/li[3]/a').click()
#pengambilan data
table = browser.find_element_by_id('example')
for row in table.find_elements_by_css_selector('tr'):
    for cell in row.find_elements_by_tag_name('td'):
        print(cell.text)

#status user
browser = webdriver.Chrome()
browser.get('https://www.tokoperhutani.com/')

#Tutup Modal
browser.find_element_by_xpath('//*[@id="bannerModal"]/div/div/div[1]/button').click()

#Klik Login
browser.find_element_by_xpath('/html/body/div/nav/div/div[2]/ul/li[1]/a/strong').click()

#Input 
browser.find_element_by_id('email').send_keys('dindaayuprtw@gmail.com')
browser.find_element_by_id('password').send_keys("5BF5DF")

#Submit
browser.find_element_by_class_name('le-button').click()

#Masuk halaman beranda
browser.find_element_by_link_text('Beranda').click()

# Mengambil data status user
status_user = browser.find_element_by_xpath('/html/body/div[1]/nav/div/div[2]/ul/strong/li/a/img').get_attribute("title")

# print status user
print(status_user)