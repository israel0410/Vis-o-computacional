# Seleção Automatica de Peças

Com a introdução da automação em variados setores das industrias, a inspeção e seleção de componentes físicos, muitas das vezes, ficam a cargo de processos manuais. Existem vários métodos e técnicas de inspeção, tais como método pulso-eco, método por transparência, método por ressonância, técnica por contato, técnica por imersão, inspeção manual e inspeção automática

>Segundo Denis (2007) “a classificação se dá em organizar um produto por tamanho, cor, formato e qualidade, afim de formar um grupo”. As inspeções seguem padrões normatizados, que por sua vez, seguem um série de normas nacionais e internacionais, ou até mesmo internas de uma determinada organização, que podem ser gerada ou interpretada de forma diferente a partir de sua aplicação, ou do indivíduo que a manipula.
![Sistema de visão](https://github.com/israel0410/Vis-o-computacional/assets/69548438/2293a8da-6c54-4139-9a18-f85eab0595e3)


## Importância
A análise histórica mostra que erros pertinentes a qualidade podem estar ligados a inúmeros incidentes, desde perdas financeiras, até a ricos fatais a vida de consumidores finais. 

## Protótipo 

Para que a seleção automática de peças utilizando visão computacional seja realizada, é necessário que um ciclo seja seguido. O processo inicia-se a partir da aquisição de uma imagem, que posteriormente será processada e analisada pelo algoritmo neural, que por sua vez, consiste em torna um modelo treinado testado e validado.

###Aquisição de imagem
Foi utilizado um camera que pode ser conectada ao raspberry e configurada pra short ou live.
![Camera](https://github.com/israel0410/Vis-o-computacional/assets/69548438/bfcd80dc-8e06-4a42-ac8b-01fef185bcd6)

### Processamento de imagens 
Para o desenvolvimento de código em python com a ferramenta Open cv, foi utilizado no editor de texto VSCode para separação de pontos de interesse nas imagens. O framework Darknet e YOLO foi utilizado na plataforma Node Red, sendo suportada pelo sistema operacional Diet Pi para raspiberry. Node Red para treinamento da rede, para classificação das imagens e o pacote de arquivos YOLO com as configurações de arquitetura da rede com a câmera para raspiberry. 

### Yolo e Darknet
Darknet é um framework de código aberto para a execução de redes neurais escrito em C e CUDA. Sua implementação suporta modelos computacionais em CPU e GPU.
Arquitetura YOLO e método amplamente utilizado para detectar objetos em tempo real, por passar apenas uma vez pela imagem para realizar a sua verificação. Uma aplicação muito usual deste método são em câmeras de trânsito, onde o elevado número de classes podem ser melhor indicado, sendo possível realizar treinamento em um novo banco de dados para treinamento de imagens. 
Enquanto as estratégias anteriores utilizam uma rede neural projetada para classificação, na tarefa de detecção de objeto, a mesma apresenta um método focado em detecção dinâmica sob machine learning. YOLO é um sistema de detecção de objetos em tempo real, capaz de identificar objetos em vídeos e em imagens.

![image](https://github.com/israel0410/Vis-o-computacional/assets/69548438/a083aa5f-40ae-42c4-ad9f-00996fbb5d83)

### Resultado 
Para classificação de imagens foi utilizado o software VSCODE fermenta open cv para realizar corte e marcação, através deste é possível localizar e delimitar objetos na imagem a fim de gerar o data set requerido para o treinamento da rede. Open Cv é uma ferramenta interativa de anotação de vídeo e imagem para visão computacional. É usado por dezenas de milhares de usuários e empresas em todo o mundo.




