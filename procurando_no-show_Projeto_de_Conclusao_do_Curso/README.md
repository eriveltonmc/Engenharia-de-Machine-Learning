
# Projeto 'Procurando No-Show'
Proposta e Projeto Final para conclusão do curso de Engenheiro de Machine Learning da Udacity.

## Descrição
### Visão Geral do Projeto

O não comparecimento de pacientes em consultas e procedimentos médicos marcados previamente, conhecido como '**no-show**', é um problema global que pode ocasionar perda de receita para qualquer empresa da área como clínicas e hospitais públicos ou privados. Quando o paciente não comparece, profissionais ficam ociosos, materiais são comprados e não utilizados, estourando limites de estoque, equipamentos médicos são preparados desnecessariamente, além do consumo desnecessário de energia, entre outros problemas que geram custo. Esse custo pode ser evitado se soubermos de forma antecipada se o paciente vai comparecer.

Neste projeto, desenvolvi um sistema baseado em um classificador treinado, utilizando a linguagem de programação '**Python**' na plataforma de desenvolvimento '**Jupyter Notebook**', capaz de prever com alta taxa de acerto se um determinado paciente vai comparecer à consulta. Esse classificador foi treinado baseado em informações históricas extraídas de um conjunto de dados ('**dataset**') de agendamento de consultas e procedimentos médicos que contém registros de pacientes, como idade, especialidade médica, local, data e hora da consulta, entre outros, incluindo se compareceram ou não.

### Descrição do problema

O problema numa visão macro é a **perda de receita**  em casos de 'no show'. Numa visão específica, o problema é a **incerteza sobre o comparecimento do cliente**. As causas podem ser muitas, como data da consulta muito distante, horário indesejado, etc. A equipe deve se preparar para uma possível substituição de paciente, liberação de empregados ou cancelamento de pedidos de materiais, mas para isso ela tem que saber de forma antecipada se ele vai comparecer. O sistema proposto fará essa previsão através da análise de dados históricos registrados desde o agendamento até o comparecimento ou não na consulta. Isso será feito verificando a relação entre as características prévias (idade, especialidade médica, loca, data, hora, etc), registradas no momento de agendamento e chamadas de '**features**', e o resultado (compareceu ou não), registrado no ato da consulta e chamado de **rótulo**. Cada dado do registro tem sua importância no resultado e isso será usado pelo sistema para prever a partir de qualquer agendamento em andamento se o paciente vai comparecer. Trata-se de um processo de previsão por **classificação binária** (show ou no-show) que usa um modelo de **aprendizagem supervisionada** a partir de dados de consultas já realizadas e classificadas.

### Etapas
Este projeto está dividido, de forma resumida, nas seguintes partes:
- **Exploração dos dados**: carregamento do 'dataset', exploração das 'features', estatística do 'dataset'.
- **Visualização exploratória**.
- **Algoritmos e técnicas**.
- **Pré-Processamento de Dados**: transformação de 'features' contínuos enviesados, normalização de 'features' numéricas, divisão dos dados, balanceamento dos dados.
- **Benchmark**: métricas, obtenção do benchmark, 'naive predictor'.
- **Implementação**: pipeline de treinamento e previsão, modelo inicial de avaliação, escolha do melhor modelo de aprendizagem.
- **Refinamento**: ajuste do modelo, avaliação do modelo final.
- **Importância das** '**features**': extração das importâncias das features, seleção das features mais importantes.
- **Resultados finais**.

## Arquivos utilizados neste projeto
- '**procurando_no-show.ipynb**': códigos de programa na linguagem 'python' para uso na plataforma 'Jupyter Notebook' com descrição técnica em cada passo do projeto.
- '**2017.csv**': conjunto de dados.
- '**proposta.pdf**': documento de apresentação de uma proposta para o projeto final.
- '**relatório.pdf**': documento de apresentação dos desenvolvimentos e resultados de cada etapa do projeto.
