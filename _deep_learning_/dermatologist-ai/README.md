# Projeto 'Dermatologist AI'
Projeto orientado de Rede Neural Convolucional (CNN) do curso de Engenheiro de Machine Learning da Udacity.

## Descrição
Neste projeto, desenvolvi um preditor de dois tipos de doênças de pele, dentre três, a partir de milhares de imagens tiradas de manchas na pele. As imagens obtidas foram fornecidas pela Udacity através de links e por serem muito grandes, somando quase 12GB, não foi possível disponibilizálos aqui. Portanto, aqui segue os códigos de programa python do projeto e alguns dos arquivos necessários e criados na execução desse código.

Uma rede neural precisa ser treinada com uma parte das imagens (conjuntos de imagens de treinamento e de validação) e neste projeto usei camadas convolucionais, formando uma CNN. Para treinar, foi executado todos os códigos na plataforma estilo notebook chamada 'Colaboratory', também conhecida somente por 'Colab', da 'Google'. Essa escolha foi feita devido o recurso de GPU (Grafic Processor Unit) oferecido pela plataforma, fazendo uma aceleração no processo de treinamento da CNN.

Este projeto está dividido, de forma resumida, nas seguintes partes:
- '**Carregando as imagens**': conhecimento do conjunto de dados, redimencionamento das imagens, visualização.
- '**Filtragem das imagens**': aplicação de um ou mais filtros para tentar melhorar o desempenho no futuro treinamento da CNN, conversão das imagens para arrays.
- '**Separação dos rótulos'**: separação dos resultados de cada imagem ('melanoma', 'nevus' ou 'seborrheic keratosis') de seus arrays representando as imagens.
- '**Reescalonamento**': transformação dos valores de cada pixel (de 0 a 255) para a escala entre 0 e 1.
- '**Conversão dos rótulos para dados categóricos**': aplicação de função da biblioteca 'keras' para transformação dos resultados dos rótulos para dados categóricos.
- '**Criando e configurando gerador de imagem aumentada**': aplicação de ferramenta para ampliar a quantidade de imagens, criando outras a partir das mesma já existentes mas com pequenas alterações nas novas, como deslocamento e giro.
- '**Definindo a arquitetura do modelo de CNN**': inserindo camadas como as convolucionais, as de 'pooling', as 'denses', entre outras, para formar a melhor rede neural.
- '**Compilando o modelo**': uso do 'backend' chamado 'tensorflow', sendo uma ferramenta especializada em redes neurais.
- '**Treinando o modelo**': aqui foi executada de fato o treinamento para ajuste dos pesos internos com alterações de parâmetros até encontrar a melhor acuracidade no teste futuro.
- '**Carregando o modelo com a melhor avaliação de acurácia**': após o treinamento, os pesos da melhor avaliação são carregados num arquivo específico.
- '**Calculando a classificação de acurácia no conjunto de teste**': após o treinamento, é aplicado a predição com as imagens do conjunto de imagens separadas para teste.
- '**Calculando as probabilidades para cada resultado de predição**': aqui cada imagem do conjunto de teste é aplicada à CNN e esta prediz qual doença de pele está presente, retornando uma probabilidade para cada uma delas.
- '**Criando e carregando o arquivo de resultados**': a lista de probabilidades de doenças de pele de cada imagem do cunjunto de teste é carregada num arquivo para comparação com resultados de outros desafiadores do mesmo problema, disponibilizado pela Udacity.

## Arquivos utilizados neste projeto
- '**dermatologist-ai.ipynb**': códigos de programa na linguagem 'python' para uso na plataforma 'Colaboratory' com descrição técnica em cada passo do projeto.
- '**sample_predictions.csv**': conjunto padrão de dados de probabilidades de duas doenças de pele ('melanoma' e 'seborrheic keratosis') para cada imagem do conjunto de teste, fornecido pela Udacity, para comparação com o conjunto a ser construído na execução do projeto.
- '**my_sample_predictions.csv**': conjunto de dados de probabilidades de duas doenças de pele ('melanoma' e 'seborrheic keratosis') para cada imagem do conjunto de teste, construído durante a execução do projeto, para comparação com o conjunto padrão fornecido pela Udacity.
- '**get_results.py**': programa 'python' para avaliação dos resultados do projeto com uso de curva ROC aplicado aos conjuntos de dados de probabilidades.
- '**requirements.txt**': lista de módulos a serem instalados para a correta execução deste projeto.
