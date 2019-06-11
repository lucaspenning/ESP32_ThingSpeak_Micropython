Monitoramento na IoT
Atividade da Disciplina de Sistemas Operacionais II
Embarcado utilizado: ESP32

Linguagem de Programação: MicroPython

Ambiente de Desenvolvimento: uPyCraft

Plataforma de Nuvem na IoT utilizada: ThingSpeak

Tutoriais utilizados:
  >https://mjrobot.org/2018/06/13/iot-feito-facil-esp-micropython-mqtt-thingspeak/

Resumo das Funcionalidades:
  Por meio do protocolo MQTT, enviaremos dados capturados de sensores, à um serviço de IoT, o ThingSpeak.

Funcionalidades no embarcado:
  >Ler os valores dos sensores (temperatura, umidade e luminosidade) do local e conectado a uma rede mandar essas informações para a plataforma de nuvem IoT ThingSpeak.
  
Funcionalidades na Plataforma de Nuvem na IoT:
  >Receber os dados do embarcado e mostrar por meio de gráficos as variações das leituras dos sensores.

Comentários sobre os Códigos:
  >Foram utilizadas as bibliotecas: DHT, umqtt.simple, WIFI e Machine.
  >Devem ser alteradas as variáveis CHANNEL_ID (ID do canal) e WRITE_API_KEY (Chave de escrita do canal) respectivamente do seu canal ThingSpeak.
  >Código consiste em uma rotina onde ficará lendo os valores dos sensores e enviando para a nuvem IoT a um determinado intervalo de tempo (valor de tempo que deverá ser definido em segundos).
