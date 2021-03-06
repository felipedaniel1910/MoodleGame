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
        self.number_time = int(input("Quantas vezes deseja repetir o processo? "))
        options = webdriver.ChromeOptions()
        options.add_argument('lang=pt-br')
        self.driver = webdriver.Chrome(executable_path=r'chromedriver.exe')

    #controlar as ações - função principal
    def central_command(self):
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
        for i in range(0,self.number_time):
            for index in range(9,10): #Possível aumentar disciplinas percorridas
                try:
                    course = self.driver.find_element_by_xpath(f'//*[@id="label_3_1{index}"]')
                    course.click()
                    time.sleep(3)
                    self.viewing_news()
                except: 
                    None         
        self.driver.quit()
   
    #Função que verifica se existem avisos não lidos e se tiver, abre eles
    def viewing_news(self):
        try:
            self.driver.find_element_by_xpath(f'//*[@id="module-450482"]/div/div/div[2]/div/a/span').click()
            #self.driver.find_element_by_class_name('instancename').click()
        except:
            None

        while(1):
            try:
                nlido = self.driver.find_element_by_xpath('//*[@id="next-activity-link"]')
                nlido.click()
                time.sleep(3)
            except:
                self.inicial_page()
                time.sleep(60)
                return 
        #return

    #Função que retorna o navegador para a pagina inicial do moodle
    def inicial_page(self):
        self.driver.get("https://moodle.utfpr.edu.br/my/")
        time.sleep(8)
        return   

bot = MoodleBot()
bot.central_command()


