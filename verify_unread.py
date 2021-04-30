from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import pyautogui as pag
import pyperclip as ppc
import login #arquivo que contém as senhas (username,password)

#classe principal
class MoodleBot:
    #configurar o navegador
    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_argument('lang=pt-br')
        self.driver = webdriver.Chrome(executable_path=r'chromedriver.exe')

    #controlar as ações - função principal
    def control(self):
        self.driver.get("https://moodle.utfpr.edu.br/login/index.php")
        self.login()
        time.sleep(6)
        self.subject_enter()

    #Realizar o login
    def login(self):
        username = self.driver.find_element_by_id("username")
        time.sleep(3)
        username.send_keys(login.username) #CAMPO DE LOGIN
        password = self.driver.find_element_by_id("password")
        password.send_keys(login.password + Keys.RETURN) #CAMPO DE SENHA
        time.sleep(5)

    #Função que abre a disciplina
    def subject_enter(self):

        for index in range(2,9):
            try:
                course = self.driver.find_element_by_xpath(f'//*[@id="label_3_1{index}"]')
                course.click()
                time.sleep(3)
                self.verify_unread()
            except: 
                None
    
        self.driver.quit()
 
    #Função que verifica se existem avisos não lidos e se tiver, abre eles
    def verify_unread(self):
        try:
            nlido = self.driver.find_element_by_class_name('unread')
        except:
            nlido = 0
                   
        if nlido!=0:
            nlido.click()
            time.sleep(3)
            try:
                msg = self.driver.find_element_by_xpath(
                    '//*[@title="2 mensagens não lidas"]')
                msg.click()
            except:
                msg = self.driver.find_element_by_xpath(
                    '//*[@title="1 mensagens não lidas"]')
                msg.click()
        time.sleep(5)
        self.inicial_page()
        return 
        #self.index = self.index + 1
    

    #Função que retorna o navegador para a pagina inicial do moodle
    def inicial_page(self):
        self.driver.get("https://moodle.utfpr.edu.br/my/")
        time.sleep(8)
        return   

bot = MoodleBot()
bot.control()
