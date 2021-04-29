from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import pyautogui as pag
import pyperclip as ppc

#classe principal
class MoodleBot:
    #configurar o navegador
    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_argument('lang=pt-br')
        self.driver = webdriver.Chrome(
        executable_path=r'C:\Users\felip\Desktop\Bot_WhatsApp\chromedriver.exe')

    #Realizar o login
    def login(self):
        username = self.driver.find_element_by_id("username")
        time.sleep(3)
        username.send_keys('') #CAMPO DE LOGIN
        password = self.driver.find_element_by_id("password")
        password.send_keys('' + Keys.RETURN) #CAMPO DE SENHA
        time.sleep(5)

    #Função que abre a disciplina
    def subject_enter(self):
        subj_titles = ['felipe daniel',
        '"ET39H.2020_02 - Robotica - A81 (2020_02)"',
        '"ET68B - Oficina de Integração 2 - A81 (2020_02)"',
        '"ET67C - Modelagem e Controle de Sistemas Automatizados - A71 (2020_02)"',
        '"IF68E - Sistemas Embarcados - A91 (2020_02)"',
        '"ET51G - Circuitos Eletrônicos para Instrumentação - MEE11 (2021_01)"',
        '"Comunidade Moodle UTFPR"']
        for subj in subj_titles:
            try:
                course = self.driver.find_element_by_xpath(f'//*[@title={subj}]')
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

    #controlar as ações - função principal
    def control(self):
        self.driver.get("https://moodle.utfpr.edu.br/login/index.php")
        self.login()
        time.sleep(6)
        #self.index = 0
        self.subject_enter()

bot = MoodleBot()
bot.control()


