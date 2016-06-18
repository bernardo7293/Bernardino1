import telepot
import Arduino
import traceback
import time
# VARIAVEIS PARA ENVIAR AO ARDUINO DEPENDENDO DO COMANDO
lampadaSala = b"SaF"
lampadaCozinha = b'CaF'
lampadaQuarto1 = b'QaF'
lampadaQuarto2 = b'qaF'
temperatura = b'Z'
luminozidade = b''
seguranca = b's'
STT = b''


class TelegramTutorial(telepot.Bot):
    def __init__(self, token):
        super(TelegramTutorial, self).__init__(token)
        self.serial = Arduino.start_communication()

    def handle_message(self, msg):
        if 'text' not in msg:
            return

        if msg['text'].startswith('*'):
          self.handle_command(msg)

    def handle_Comandos(self, msg):
        self.sendMessage(msg['chat']['id'], " OS COMAMDOS VALIDOS SÃO:\nLampadaSala, LampadaCozinha, LampadaQuarto1, LampadaQuarto2, Temperatura, Luminozidade, Segurança \n LEMBRANDO QUE PARA RECONHECER UM COMANDO VALIDO DEVE INSERIR * ANTES DO COMANDO... ")

    def handle_LampadaSala(self, msg):
        #self.sendMessage(msg['chat']['id'], "Calma que a poha vai ligar")

        self.serial.write(lampadaSala)

        response = self.serial.readline()

        if not response:
            response = 'No response received'
        else:
            response = 'arduino: ' + response.decode('utf-8')

        self.sendMessage(msg['chat']['id'], response)

    def handle_LampadaCozinha(self, msg):
            # self.sendMessage(msg['chat']['id'], "Calma que a poha vai ligar")

            self.serial.write(lampadaCozinha)

            response = self.serial.readline()

            if not response:
                response = 'No response received'
            else:
                response = 'arduino: ' + response.decode('utf-8')

            self.sendMessage(msg['chat']['id'], response)

    def handle_LampadaQuarto1(self, msg):
        # self.sendMessage(msg['chat']['id'], "Calma que a poha vai ligar")

        self.serial.write(lampadaQuarto1)

        response = self.serial.readline()

        if not response:
            response = 'No response received'
        else:
            response = 'arduino: ' + response.decode('utf-8')

        self.sendMessage(msg['chat']['id'], response)

    def handle_LampadaQuarto2(self, msg):
        # self.sendMessage(msg['chat']['id'], "Calma que a poha vai ligar")

        self.serial.write(lampadaQuarto2)

        response = self.serial.readline()

        if not response:
            response = 'No response received'
        else:
            response = 'arduino: ' + response.decode('utf-8')

        self.sendMessage(msg['chat']['id'], response)

    def handle_Temperatura(self, msg):
        # self.sendMessage(msg['chat']['id'], "Calma que a poha vai ligar")

        self.serial.write(temperatura)
        self.sendMessage(msg['chat']['id'], "Aguarde a leitura da Temperatura")
        time.sleep(1)

        response = self.serial.readline()


        if not response:
            response = 'No response received'
        else:
            response = 'A temperatura atual é de: ' + response.decode('utf-8')+' °C'

        self.sendMessage(msg['chat']['id'], response)

    def handle_Seguranca(self, msg):
        teste = self.serial.readline()
        self.sendMessage(msg['chat']['id'], "Aguarde")
        if teste =='socoro':
            time.sleep(1)
            self.sendMessage(msg['chat']['id'], "Socorro")

    def handle_command(self, msg):

        method = 'handle_' + msg['text'][1:]

        if hasattr(self, method):
            getattr(self, method)(msg)

    def runBot(self):
        last_offset = 0
        print('Executando...')

        while True:
            try:
                updates = self.getUpdates(timeout=60, offset=last_offset)

                if updates:
                    for u in updates:
                        self.handle_message(u['message'])

                    last_offset = updates[-1]['update_id'] + 1

            except KeyboardInterrupt:
                break
            except:
                traceback.print_exc()



bot = TelegramTutorial('139688568:AAFd8NPqWyNJ4eRnhr0bF_eP9vHfqurZVjE')
bot.runBot()