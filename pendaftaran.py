from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

import time

driver = webdriver.Chrome()
driver.get("file:///D:/test/Mini_Project/Pendaftaran/pendaftaran.html")
wait=WebDriverWait(driver, 10)
form_element=wait.until(EC.visibility_of_all_elements_located((By.ID, "form-pendaftaran")))
print("✅ Form sudah muncul!")

nama_field = driver.find_element(By.ID, "name")
input_email=driver.find_element(By.ID, "email")
radio_PR=driver.find_element(By.XPATH, "//input[@value='Perempuan']")
hobi1=driver.find_element(By.ID, "hobi1")
hobi2=driver.find_element(By.ID, "hobi2")
hobi3=driver.find_element(By.ID, "hobi3")
dropdown_element = Select(driver.find_element(By.ID, "kota"))
submit_button = driver.find_element(By.ID, "submit-button")

# ================== 1. Verifikasi Nama ==================
nama_field.clear()
time.sleep(1)  # Waktu untuk memastikan nilai sudah dimasukkan
entered_name = nama_field.get_attribute("value")

if not entered_name:
    print("❌ Nama tidak boleh kosong")
else:
    print(f"Nama yang dimasukkan: {entered_name}")

time.sleep(1)

#isi nama
nama_field.send_keys("Im yoona")
entered_name = nama_field.get_attribute("value")
if not entered_name:
    print("❌ Nama tidak boleh kosong")
else:
    print(f"Nama yang dimasukkan: {entered_name}")

#====================2. verifikasi Email Invalid=================
input_email.send_keys("kpopgirls@examplecom") #tidak ada titik
entered_email=input_email.get_attribute("value")
print(f"Test Email tanpa '.' yaitu: {entered_email}")  

radio_PR.click()
hobi1.click()
dropdown_element.select_by_value("Bogor")
submit_button.click()
  

try:
    wait=WebDriverWait(driver,5)
    wait.until(EC.alert_is_present())

    alert=Alert(driver)
    print("🔔 Alert ditemukan! Pesan alert:", alert.text)
    time.sleep(2)
    alert.accept()
    print("✅ Alert berhasil di-close")
except:
    print("❌ Alert tidak muncul dalam waktu ditentukan")
time.sleep(2)

#tanpa '@'
input_email.clear()
time.sleep(2)
input_email.send_keys("kpopgirlsexample.com") #tidak ada titik
entered_email=input_email.get_attribute("value")
print(f"Test Email tanpa '@' yaitu: {entered_email}")  

radio_PR.click()
hobi2.click()
dropdown_element.select_by_value("Jakarta")
submit_button.click()
  

try:
    wait=WebDriverWait(driver,5)
    wait.until(EC.alert_is_present())

    alert=Alert(driver)
    print("🔔 Alert ditemukan! Pesan alert:", alert.text)
    time.sleep(2)
    alert.accept()
    print("✅ Alert berhasil di-close")
except:
    print("❌ Alert tidak muncul dalam waktu ditentukan")
time.sleep(2)

#====================3. verifikasi Email Valid=================
input_email.clear()
input_email.send_keys("kpopgirls@example.com")
entered_email=input_email.get_attribute("value")
print(f"email yang di input sudah benar : {entered_email}")
time.sleep(1)

#=====================4. memilih radio button (Jenis Kelamin)============
radio_PR.click()
if radio_PR.is_selected():
    print("Radio button Perempuan terpilih!")
else:
    print("Radio button Perempuan tidak terpilih")

time.sleep(1)
#======================5. verifikasi Checkbox======================
# checkboxes=driver.find_elements(By.XPATH, "//input[@type='checkbox']")

# #mencentang semuanya
# for checkbox in checkboxes:
#     if not checkbox.is_selected():
#         checkbox.click()
#         print(f"checkbox dengan value '{checkbox.get_attribute('value')}' dicentang")
#         time.sleep(1)
# #uncheck satu (misal yang pertama)
# if checkboxes[0].is_selected():
#     checkboxes[0].click()
#     print(f"Checkbox pertama dengan value '{checkboxes[0].get_attribute('value')}' di-uncheck")

# #mencentang dua pertama secara bergantian
# for checkbox in checkboxes[:2]:
#     if not checkbox.is_selected():
#         checkbox.click()
#         print(f"Checkbox {checkbox.get_attribute('value')} dicentang")
# time.sleep(1)


#checklist semua
hobi1.click()
hobi2.click()
hobi3.click()
print("Checkbox semuanya terceklis")
time.sleep(1)

if hobi1.is_selected():
    hobi1.click()
    print("Hobi 1 di-uncheck")
else:
    print("hobi 1 sudah tidak tercentang")

if hobi2.is_selected():
    hobi1.click()
    hobi2.click()
    print("Hobi 2 di-uncheck dan hobi 1 terceklis kembali")
else:
    print("hobi 2 masih tercentang")

if hobi3.is_selected():
    hobi2.click()
    hobi3.click()
    print("hobi 3 di-uncheck dan hobi 2 terceklis kembali")
else:
    print("hobi 3 masih tercentang")

time.sleep(1)
#=========================6. verifikasi dropdown==================
selected=dropdown_element.first_selected_option.get_attribute("value")
if selected =="":
    print("❌ Kota belum dipilih")
else:
    print("✅ Kota sudah dipilih : {selected}")

time.sleep(2)

all_options=dropdown_element.options #otomatis keambil semua kota yang ada
for option in all_options:
    dropdown_element.select_by_value(option.get_attribute("value"))
    print(f"Kota yang terpilih: {dropdown_element.first_selected_option.get_attribute('value')}")
time.sleep(1)

# dropdown=Select(driver.find_element(By.ID, "kota"))
# dropdown.select_by_value("Bogor")

# selected_option=dropdown.first_selected_option
# kota_value=selected_option.get_attribute("value")
# print(f"Kota yang terpilih: {kota_value}")
# time.sleep(1)
# selected_option=dropdown.first_selected_option
# dropdown.select_by_value("Surabaya")
# kota_value=selected_option.get_attribute("value")
# print(f"Kota yang terpilih: {kota_value}")
# time.sleep(1)
# selected_option=dropdown.first_selected_option
# dropdown.select_by_value("Jakarta")
# kota_value=selected_option.get_attribute("value")
# print(f"Kota yang terpilih: {kota_value}")
# time.sleep(1)
# selected_option=dropdown.first_selected_option
# dropdown.select_by_value("Bandung")
# kota_value=selected_option.get_attribute("value")
# print(f"Kota yang terpilih: {kota_value}")
# time.sleep(1)
# selected_option=dropdown.first_selected_option
# dropdown.select_by_value("Solo")
# kota_value=selected_option.get_attribute("value")
# print(f"Kota yang terpilih: {kota_value}")
# time.sleep(1)
# selected_option=dropdown.first_selected_option
# dropdown.select_by_value("Depok")
# kota_value=selected_option.get_attribute("value")
# print(f"Kota yang terpilih: {kota_value}")

#=========================7. verikasi submit input lengkap================
is_disabled = submit_button.get_attribute("disabled") is not None
if is_disabled:
    print("Tombol submit masih disabled karena ada field yang belum diisi")
   
else:
    print("Tombol submit sudah aktif dan bisa diklik.")
    submit_button.click()
    print("Tombol submit berhasil diklik!")


time.sleep(5)
driver.quit()