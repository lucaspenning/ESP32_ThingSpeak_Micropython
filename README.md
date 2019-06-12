# Monitoramento na IoT
**Atividade da Disciplina de Sistemas Operacionais II**

Embarcado utilizado: ESP32

<img src="https://br.mouser.com/images/espressifsystems/lrg/ESP32-DevKitC-32D_t.jpg" width="100" height="200"/>

Linguagem de Programação: MicroPython

Ambiente de Desenvolvimento: uPyCraft

Plataforma de Nuvem na IoT utilizada: ThingSpeak

Tutorial utilizado:
  >https://mjrobot.org/2018/06/13/iot-feito-facil-esp-micropython-mqtt-thingspeak/

Resumo das Funcionalidades:
  >Por meio do protocolo MQTT, enviaremos dados capturados de sensores, à um serviço de IoT, o ThingSpeak.
  
  <img src="https://cdn-images-1.medium.com/max/800/0*Fi8M5h2DXa6HgdS4" width="350" height="350"/>

Funcionalidades no embarcado:
  >Ler os valores dos sensores (temperatura, umidade e luminosidade) do local e conectado a uma rede mandar essas informações para a plataforma de nuvem IoT ThingSpeak.
  
Funcionalidades na Plataforma de Nuvem na IoT:
  >Receber os dados do embarcado e mostrar por meio de gráficos as variações das leituras dos sensores.
  <img src="https://i0.wp.com/electronicshobbyists.com/wp-content/uploads/2018/01/ThingSpeak-output.png?resize=750%2C359&ssl=1" width="700" height="350"/>

Comentários sobre os Códigos:
  * Foram utilizadas as bibliotecas: DHT, umqtt.simple, WIFI e Machine.
  * No arquivo texto de código ThingSpeak_Pub.py devem ser alteradas as variáveis CHANNEL_ID (ID do canal) e WRITE_API_KEY (Chave de escrita do canal) respectivamente do seu canal ThingSpeak.
  * No arquivo texto de código Wifi.py devem ser alteradas as variáveis ssid (Nome da rede) e password (senha da rede) respectivamente da sua rede.
  * Código consiste em uma rotina onde ficará lendo os valores dos sensores e enviando para a nuvem IoT a um determinado intervalo de tempo (valor de tempo que deverá ser definido em segundos).
