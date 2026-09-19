# 💻 Microcontrolador 
Esse projeto tem como principal intenção explorarmos nossos conhecimentos que estão sendo construidos na aula desse semestre, e exercer a habilidade em algo fisico, dito isso, exerceremos a linguagem Python, a linguagem usada esse semestre, além de entender o procedural e lógica de uma linguagem estruturada.

Esse projeto se baseia em um microcontrolador chamado ESP32, diferente de microcomputadores como Raspberry, o microcontrolador tem uma função especifica, seu microchip integra processador, memória e tudo que se precisa para se realizar tarefas especificas, enquanto um computador exerce a função de um sistema computacional inteiro, microcontroladores são destinados a manuseio de estudos do IOT .

# 📚 Glossário
Segue cada informação de cada palavra técnica, e sigla:

* IOT - Internet das Coisas.

* ESP32 - Microcontrolador de 32 bits da empresa Espressif Systems.

* Python - Linguagem de programação estruturada.

* CSV - Comma-Separated Values - Arquivo de texto formado de tabelas similar ao xlsx.

* API - Application Programming Interface, um conjunto de regras e protocolos que define estilos de comunicação e troca de informações entre sistemas.

* DHT22 -Sensor digital de baixo custo para detectar temperatura e umidade do ar.

* MQ135 - Sensor que detecta presença de concentração de gases pelo ar.

* LDR - Sensor que mede a intensidade da luz.

* DOM - Modelagem de objeto, uma representação de árvore o qual permite, ler modificar e analisar conteúdo do HTML.

# 🧑‍💻 Como o código funciona?

Temos duas partes, o BackEnd e a do FrontEnd, o BackEnd será o responsável por extrair as informações dos sensores e levar eles como valores, tendo um dos códigos do back que serve como um conjunto de funções que irá manusear esses dados e distribuir eles dentro de um CSV.
O javascript usado no site que irá expor esses dados ele usará conhecimentos assincronos como await para realizar um fetch e pegar dados do CSV e distribuir eles pela tela do usuário.
De resto, após a parte do Javascript, bata manipulação de DOM para que os dados sejam mostrados
