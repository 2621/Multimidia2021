# Multimidia
Trabalho de código de Huffman - Multimídia 2021

Alessandra da Silva Dias Malizia

Milena Mayara Ruy

## Para compilar e rodar:
Primeiro deve-se garantir que python3 está instalado na máquina. Em seguida:

->git clone https://github.com/2621/Multimidia2021.git  ou baixar o repositório inteiro

->cd Multimidia2021

->pip3 install numpy

->python3 codificador.py

->python3 decodificador.py

->python3 psnr.py


## Resultados e Comentários:
Para a imagem da Lena, o comprimento médio obtido foi: 7.467304229736328

Para a imagem do babuíno, o comprimento médio obtido foi: 7.380626678466797

Após o resultado obtido de psnr.py, obtemos, para ambas as imagens o valor infinito, o que faz sentido, uma vez que a compressão por Huffman é sem perdas e não há ruído nesse processo.
