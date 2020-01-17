from selenium import webdriver
opsi = webdriver.firefox.options.Options()
opsi.headless = False
binary = webdriver.firefox.firefox_binary.FirefoxBinary('C:\\Program Files\\Mozilla Firefox\\firefox.exe')
cap = webdriver.common.desired_capabilities.DesiredCapabilities().FIREFOX
cap['marionette'] = True
browser=webdriver.Firefox(options=opsi,capabilities=cap,firefox_binary=binary)
browser.get('https://tokoperhutani.com/')

pembayaran= browser.get('https://tokoperhutani.com/article/static_art/cara-pembayaran')

sertperhutani= browser.get('https://tokoperhutani.com/SertifikatPerhutani') 

browser.find_element_by_xpath('/html/body/div/nav/div/div[2]/ul/li[1]/a/strong').click()

browser.find_element_by_id('email').send_keys('nsfthrn@gmail.com')
browser.find_element_by_id('password').send_keys("C4CA2F")
browser.find_element_by_class_name('le-button').click() 

browser.find_element_by_xpath('/html/body/div/nav/div/div[2]/ul/li[1]/a/strong').click()
browser.find_element_by_id('email').send_keys('novinurinabb25@gmail.com')
browser.find_element_by_id('password').send_keys("86083F")
browser.find_element_by_class_name('le-button').click()

browser.find_element_by_xpath('/html/body/div/nav/div/div[2]/ul/strong/li/a').click()
browser.find_element_by_link_text('Profile').click()

from selenium import webdriver
opsi = webdriver.firefox.options.Options()
opsi.headless = False
binary = webdriver.firefox.firefox_binary.FirefoxBinary
('C:\\Program Files\\Mozilla Firefox\\firefox.exe')
cap = webdriver.common.desired_capabilities.Desired
Capabilities().FIREFOX
cap['marionette'] = True
browser=webdriver.Firefox(options=opsi,capabi
lities=cap,firefox_binary=binary)
browser.get('https://tokoperhutani.com/')
pemberitahuan = browser.find_element_by_xpath('//*[@id="bannerModal"]/div/div/div[1]/button').click()
retail = browser.get('https://tokoperhutani.com/beranda')

login = browser.find_element_by_xpath('/html/body/div/nav/div/div[2]/ul/li[1]/a/strong').click()email = browser.find_element_by_id('email').send_keys('novinurinabb25@gmail.com')
password = browser.find_element_by_id('password').send_keys("86083F")
tombol = browser.find_element_by_class_name('le-button').click()
browser.find_element_by_link_text('Beranda').click()

retail = browser.get('https://tokoperhutani.com/beranda')
wilayah = browser.find_element_by_id('wilayah').click()
plh_wilayah = browser.find_element_by_xpath('//*[@id="wilayah"]/option[4]').click()
kota = browser.find_element_by_id('kota').click()
plh_kota = browser.find_element_by_xpath('//*[@id="kota"]/option[3]').click()
tpk = browser.find_element_by_id('select_kota').click()
plh_tpk = browser.find_element_by_xpath('//*[@id="select_kota"]/option[3]').click()
cari = browser.find_element_by_id('i_submit').click()

beli_sekarang = browser.find_element_by_xpath('/html/body/div/strong/div[8]/div/div/form/input').click()

lanjut_belanja = browser.find_element_by_xpath('/html/body/div[1]/strong/div[5]/div/div/div[3]/a/button').click()
bank_bri = browser.find_element_by_xpath('/html/body/div/strong/section[2]/div/div[2]/div/div/form/div/ul/li[2]/label/img').click()

konfirmasi_pemesanan = browser.find_element_by_xpath('//*[@id="confirmOrder"]')

browser.get('https://tokoperhutani.com/beranda')
browser.find_element_by_id('wilayah').click()
browser.find_element_by_xpath('//*[@id="wilayah"]/option[4]').click()
browser.find_element_by_id('kota').click()
browser.find_element_by_xpath('//*[@id="kota"]/option[3]').click()
browser.find_element_by_id('select_kota').click()
browser.find_element_by_xpath('//*[@id="select_kota"]/option[3]').click()
browser.find_element_by_id('i_submit').click()

ketersediaan = browser.find_element_by_xpath('/html/body/div/div[8]/div/div/form/div/div[3]/div[2]/table/tbody/tr[1]/td[2]/span')
print('Ketersediaan: ',ketersediaan.text)
no_kapling = browser.find_element_by_xpath('/html/body/div/div[8]/div/div/form/div/div[3]/div[2]/table/tbody/tr[1]/td[3]/a')
print('No Kapling: ',no_kapling.text)
harga_awal_rp = browser.find_element_by_xpath('/html/body/div/div[8]/div/div/form/div/div[3]/div[2]/table/tbody/tr[1]/td[4]/div')
print('Harga Awal Rp: ',harga_awal_rp.text)dif = browser.find_element_by_xpath('/html/body/div/div[8]/div/div/form/div/div[3]/div[2]/table/tbody/tr[1]/td[5]')
print('Dif: ',dif.text)
total_dif_rp = browser.find_element_by_xpath('/html/body/div/div[8]/div/div/form/div/div[3]/div[2]/table/tbody/tr[1]/td[6]')
print('Total Dif RP: ',total_dif_rp.text)
harga_akhir_rp = browser.find_element_by_xpath('/html/body/div/div[8]/div/div/form/div/div[3]/div[2]/table/tbody/tr[1]/td[7]/span')
print('Harga Akhir RP: ',harga_akhir_rp.text)
jenis_kayu = browser.find_element_by_xpath('/html/body/div/div[8]/div/div/form/div/div[3]/div[2]/table/tbody/tr[1]/td[9]')
print('Jenis Kayu: ',jenis_kayu.text)
sortimen = browser.find_element_by_xpath('/html/body/div/div[8]/div/div/form/div/div[3]/div[2]/table/tbody/tr[1]/td[10]')
print('Sortimen: ',sortimen.text)
panjang = browser.find_element_by_xpath('/html/body/div/div[8]/div/div/form/div/div[3]/div[2]/table/tbody/tr[1]/td[11]')
print('Panjang: ',panjang.text)lebar = browser.find_element_by_xpath('/html/body/div/div[8]/div/div/form/div/div[3]/div[2]/table/tbody/tr[1]/td[12]')
print('Lebar: ',lebar.text)
tebal_atau_diameter = browser.find_element_by_xpath('/html/body/div/div[8]/div/div/form/div/div[3]/div[2]/table/tbody/tr[1]/td[13]')
print('Tebal Atau Diameter: ',tebal_atau_diameter.text)
mutu = browser.find_element_by_xpath('/html/body/div/div[8]/div/div/form/div/div[3]/div[2]/table/tbody/tr[1]/td[14]')
print('Mutu: ',mutu.text)
jumlah = browser.find_element_by_xpath('/html/body/div/div[8]/div/div/form/div/div[3]/div[2]/table/tbody/tr[1]/td[15]')
print('Jumlah: ',jumlah.text)
status = browser.find_element_by_xpath('/html/body/div/div[8]/div/div/form/div/div[3]/div[1]/div/table/thead/tr/th[16]')
print('Status: ',status.text)
cacat_kayu = browser.find_element_by_xpath('/html/body/div/div[8]/div/div/form/div/div[3]/div[2]/table/tbody/tr[1]/td[18]')
print('Cacat Kayu: ',cacat_kayu.text)
jenis_tebangan = browser.find_element_by_xpath('/html/body/div/div[8]/div/div/form/div/div[3]/div[2]/table/tbody/tr[1]/td[19]')
print('Jenis Tebangan: ',jenis_tebangan.text)
usia_tayang_kapling = browser.find_element_by_xpath('/html/body/div/div[8]/div/div/form/div/div[3]/div[2]/table/tbody/tr[1]/td[20]')
print('Usia Tayang Kapling: ',usia_tayang_kapling.text)
tahun_kapling = browser.find_element_by_xpath('/html/body/div/div[8]/div/div/form/div/div[3]/div[2]/table/tbody/tr[1]/td[21]')
print('Tahun Kapling: ',tahun_kapling.text)
tahun_produksi = browser.find_element_by_xpath('/html/body/div/div[8]/div/div/form/div/div[3]/div[2]/table/tbody/tr[1]/td[22]')print('Tahun Produksi: ',tahun_produksi.text)

browser.find_element_by_xpath('/html/body/div/nav/div/div[2]/ul/strong/li/a').click()browser.find_element_by_link_text('Pesanan').click()

tanggal_pesan = browser.find_element_by_xpath('/html/body/div/strong/div[6]/div[2]/section[2]/div/div/div[1]/form/div/div[3]/div[2]/table/tbody/tr/td[1]')
print('Tanggal Pesanan: ',tanggal_pesan.text)
invoice = browser.find_element_by_xpath('/html/body/div/strong/div[6]/div[2]/section[2]/div/div/div[1]/form/div/div[3]/div[2]/table/tbody/tr/td[2]')
print('Invoice: ',invoice.text)
lokasi = browser.find_element_by_xpath('/html/body/div/strong/div[6]/div[2]/section[2]/div/div/div[1]/form/div/div[3]/div[2]/table/tbody/tr/td[3]')
print('Lokasi: ',lokasi.text)
volume = browser.find_element_by_xpath('/html/body/div/strong/div[6]/div[2]/section[2]/div/div/div[1]/form/div/div[3]/div[2]/table/tbody/tr/td[4]')
print('Voume: ',volume.text)
total_harga_rp = browser.find_element_by_xpath('/html/body/div/strong/div[6]/div[2]/section[2]/div/div/div[1]/form/div/div[3]/div[2]/table/tbody/tr/td[5]')
print('Total Harga: ',total_harga_rp.text)
saluran_bayar = browser.find_element_by_xpath('/html/body/div/strong/div[6]/div[2]/section[2]/div/div/div[1]/form/div/div[3]/div[2]/table/tbody/tr/td[6]')
print('Saluran Bayar: ',saluran_bayar.text)

from selenium import webdriver
from time import sleep
opsi = webdriver.firefox.options.Options()
opsi.headless = False
binary = webdriver.firefox.firefox_binary.Firefox
Binary('C:\\Program Files\\Mozilla Firefox\\firefox.exe')
cap = webdriver.common.desired_capabilities.
DesiredCapabilities().FIREFOX
cap['marionette'] = True
browser=webdriver.Firefox(options=opsi,capabilities
=cap,firefox_binary=binary)
web_pht = 'https://www.tokoperhutani.com/'
browser.get(web_pht)

#metutup navigasi
browser.find_element_by_xpath('//*[@id="bannerModal"]/div/div/div[1]/button').click()

#login
browser.find_element_by_xpath('/html/body/div/nav/div/div[2]/ul/li[1]/a/strong').click()
browser.find_element_by_id('email').send_keys('novinurinabb25@gmail.com')
browser.find_element_by_id('password').send_keys("86083F")
browser.find_element_by_class_name('le-button').click()
sleep(10)

#mengecek status user
status = browser.find_element_by_xpath('/html/body/div[1]/nav/div/div[2]/ul/strong/li/a/img').get_attribute("title")
print(status)