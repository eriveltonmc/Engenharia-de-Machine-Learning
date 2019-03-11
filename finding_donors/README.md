# Projeto 'Finding Donors'
Projeto orientado de aprendizagem supervisionada do curso de Engenheiro de Machine Learning da Udacity.

## Descrição
Neste projeto, empreguei vários algoritmos supervisionados de minha escolha para modelar com precisão a renda dos indivíduos usando dados coletados do Censo de 1994 nos EUA. Depois, escolhi o melhor algoritmo candidato a partir de resultados preliminares e otimizei ainda mais esse algoritmo para modelar melhor os dados. Assim, construí um modelo que prevê com precisão se um indivíduo ganha mais de US$ 50.000. Esse tipo de tarefa pode surgir em um ambiente sem fins lucrativos, onde as organizações sobrevivem com doações. Compreender a renda de um indivíduo pode ajudar uma organização sem fins lucrativos a entender melhor o tamanho de uma doação a ser solicitada ou se deve ou não entrar em contato. Embora possa ser difícil determinar a faixa de renda geral de um indivíduo diretamente de fontes públicas, com esse modelo pudemos inferir esse valor de outros recursos disponíveis publicamente. O 'dataset' (conjunto de dados) para este projeto é originário do Repositório de Aprendizado de Máquina do portal UCI.

Este projeto está dividido, de forma resumida, nas seguintes partes:
- '**Exploração dos dados**': conhecimento do conjunto de dados.
- '**Preparação dos dados**': transformação de 'features' contínuos enviesados, normalização numérica de 'features', pré-processamento dos dados, embaralhamento e divisão dos dados
- '**Avaliação do desempenho do modelo**': métricas e 'Naive Predictor', desempenho do 'Naive Predictor', modelos de aprendizado supervisionado, criação e treino de um 'pipeline' para predição, avaliação inicial dos modelos.
- '**Melhoria dos resultados**': escolhendo o melhor modelo, ajustando o modelo, avaliação do modelo final.
- '**Importância dos** '**features**': observação das relevâncias dos 'features', extraíndo as importâncias dos 'features', seleção dos 'features'.

## Arquivos utilizados neste projeto
- '**finding_donors.ipynb**': códigos de programa na linguagem 'python' para uso na plataforma 'Jupyter Notebook' com descrição técnica em cada passo do projeto.
- '**census.csv**': conjunto de dados.
- '**visuals.py**': códigos de programa na linguagem 'python' para uso como biblioteca de funções de plotagem de gráficos referentes ao projeto.
