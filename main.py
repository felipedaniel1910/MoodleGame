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
        username.send_keys('')
        password = self.driver.find_element_by_id("password")
        password.send_keys('' + Keys.RETURN)
        time.sleep(5)

    #Função que manda a disciplina
    def subject(self):
        subj_titles = ['"ET39H.2020_02 - Robotica - A81 (2020_02)"',
        '"ET68B - Oficina de Integração 2 - A81 (2020_02)"',
        '"ET67C - Modelagem e Controle de Sistemas Automatizados - A71 (2020_02)"']


    #função que entra na disciplina

    #Função que entra nos avisos

    #Função que verifica se existem avisos não lidos

    #Função que retorna o navegador para a pagina inicial do moodle

    #controlar as ações - função principal
    def Navegar(self):

        self.driver.get("https://moodle.utfpr.edu.br/login/index.php")
        self.login()
        time.sleep(6)
        
        subj_titles = '"ET39H.2020_02 - Robotica - A81 (2020_02)"'

        course = self.driver.find_element_by_xpath(f'//*[@title={subj_titles}]')
        course.click()
        '''
        try:
            nlido = self.driver.find_element_by_class_name('unread')
        except:
            nlido = 0

        if turn == True:
            if nlido != 0:
                nlido.click()
                time.sleep(3)
                try:
                    msg = self.driver.find_element_by_xpath(
                        '//*[@title="2 mensagens não lidas"]')
                    msg.click()
                except:
                    print('Nenhuma mensagem não lida...')
                turn = not turn

        else:
            if nlido != 0:
                nlido.click()
                time.sleep(3)
                try:
                    msg = self.driver.find_element_by_xpath(
                        '//*[@title="1 mensagens não lidas"]')
                    msg.click()
                except:
                        print('Nenhuma mensagem não lida...')
                    turn = not turn

        # <a href="https://moodle.utfpr.edu.br/my/">Painel</a>
        time.sleep(5)
        self.driver.quit()
        time.sleep(70)'''

    


bot = MoodleBot()
bot.Navegar()
time.sleep(15)

