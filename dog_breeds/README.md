# Projeto 'Dog Breeds'
Projeto orientado do módulo de Deep Learning do curso de Engenheiro de Machine Learning da Udacity.

## Descrição
Neste projeto, desenvolvi um preditor de raças de cães treinado com imagens de diversos deles já classificados, bem como de pessoas também, sendo que se a imagem for de uma pessoa, a predição desta mostrará a raça de cães mais parecida. As imagens obtidas foram fornecidas pela Udacity através de links e por serem muito grandes, somando mais de 1GB, não foi possível disponibilizálos aqui. Portanto, aqui segue os códigos de programa python do projeto e alguns dos arquivos necessários e criados na execução desse código.

Uma rede neural precisa ser treinada com uma parte das imagens (conjuntos de imagens de treinamento e de validação) e neste projeto usei camadas convolucionais, formando uma CNN. Nos modelos iniciais deste projeto, foi realizado um treinamento apenas para verificação da lentidão sem uso de uma GPU (Graphic Processor unit), mas o modelo final não foi treinado. Em vez disso, foi feito uma transferência de aprendizado de uma CNN já treinada e com seus dados aprendidos fornecidos em arquivo pela Udacity, onde tive que apenas transferir esses dados para minha CNN. Executei todos os códigos na plataforma jupyter notebook.

Este projeto está dividido, de forma resumida, nas seguintes partes:
- '**Import Datasets**': conhecimento do conjunto de dados de pessoas e cães, separação dos dados em treino, validação e teste.
- '**Detect Humans**': desenvolvimento de uma função que detecta pessoas numa imagem.
- '**Detect Dogs**': desenvolvimento de uma função que detecta cães numa imagem.
- '**Create a CNN to Classify Dog Breeds (from Scratch)**': desenvolvimento de uma CNN com treinamento a partir do zero para classificação de raças de cães em imagens.
- '**Use a CNN to Classify Dog Breeds**': aplicação da CNN de classificação de raças de cães.
- '**Create a CNN to Classify Dog Breeds (using Transfer Learning)**': desenvolvimento de uma CNN com treinamento a partir de transferência de apredizado para classificação de raças de cães em imagens.
- '**Write your Algorithm**': desenvolvimento de uma função que determina se há cães ou pessoas numa imagem e qual a raça do cão detectada ou qual a raça de cão mais parecida com a pessoa detectada.
- '**Test Your Algorithm**': aplicação da função acima.

## Arquivos utilizados neste projeto
- '**dog_app.ipynb**': códigos de programa na linguagem 'python' para uso na plataforma 'Jupyter Notebook' com descrição técnica em cada passo do projeto.
- '**extract_bottleneck_features.py**': códigos de programa na linguagem 'python' para uso como biblioteca de funções internas.
