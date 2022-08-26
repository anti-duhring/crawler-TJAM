from selenium import webdriver
from selenium.webdriver.common.by import By

navegator = webdriver.Chrome()
navegator.get('file:///C:/Users/mateu/OneDrive/Desktop/index.html');

valorDaCausa = navegator.find_element(By.CLASS_NAME, "form").find_elements(By.XPATH, "//tr")[9]
vara = navegator.find_element(By.CLASS_NAME, "form").find_elements(By.XPATH, "//tr")[1]
nomePoloAtivo = navegator.find_element(By.CLASS_NAME, "form").find_elements(By.XPATH, "//tr")[5].find_element(By.CLASS_NAME, "form").find_element(By.TAG_NAME, "li")
cpfPoloAtivo = navegator.find_element(By.CLASS_NAME, "form").find_elements(By.XPATH, "//tr")[5].find_element(By.CLASS_NAME, "form").find_element(By.XPATH, ".//td [contains(text(), 'CPF')]")
nomePoloPassivo = navegator.find_element(By.CLASS_NAME, "form").find_elements(By.XPATH, "//tr")[7].find_element(By.CLASS_NAME, "form").find_element(By.TAG_NAME, "li")
cpfPoloPassivo = navegator.find_element(By.CLASS_NAME, "form").find_elements(By.XPATH, "//tr")[7].find_element(By.CLASS_NAME, "form").find_element(By.XPATH, ".//td [contains(text(), 'CPF')]")

print('Valor da causa:', valorDaCausa.text.replace('Valor da Causa:','').replace(' ',''))
print('Vara:', vara.text.replace('Vara:',''))
print('Nome do polo ativo:', nomePoloAtivo.text)
print('CPF/CNPJ do polo ativo:', cpfPoloAtivo.text.replace('CPF/CNPJ:',''))
print('Nome do polo passivo:', nomePoloPassivo.text)
print('CPF/CNPJ do polo passivo:', cpfPoloPassivo.text.replace('CPF/CNPJ:',''))