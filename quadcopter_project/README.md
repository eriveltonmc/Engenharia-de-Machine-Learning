# Projeto 'Finding Donors'
Projeto orientado de aprendizagem por reforço do curso de Engenheiro de Machine Learning da Udacity.

## Descrição
A ideia deste projeto é fazer com que um quadricóptero aprenda a se mover (movimento de minha escolha) num ambiente virtual. Para entender melhor a estrutura deste projeto, é importante conhecer os seguintes arquivos:
- '**task_not_modified.py**': códigos de programa na linguagem 'python' para uso como biblioteca de uma classe que representa uma tarefa padrão (levantar vôo até uma altura determinada).
- '**task_modified.py**': códigos de programa na linguagem 'python' para uso como biblioteca de uma classe onde escrevi um tarefa diferente do padrão ( neste caso, escolhi a tarefa pousar numa determinada cordenada com altura sempre zero).
- Diretório '**agents**': pasta contendo agentes de aprendizagem por reforço.
  - '**policy_search.py**': códigos de programa na linguagem 'python' para uso como biblioteca de uma classe que representa um agente de amostra.
  - '**agent.py**': códigos de programa na linguagem 'python' para uso como biblioteca de uma classe onde desenvolvi um agente específico para executar minha tarefa escolhida e escrita no arquivo 'task_modified.py'.
- '**physics_sim.py**': códigos de programa na linguagem 'python' para uso como biblioteca de uma classe que representa o simulador para o quadricóptero.

Este projeto está dividido, de forma resumida, nas seguintes partes:
- '**Controle do quadricóptero**': uso da tarefa e do agente padrões, plotagem dos resultados do movimento.
- '**A tarefa**': explicação das funções da classe de tarefa.
- '**O agente**': uso e explicação das funções da classe de agente padrão do arquivo 'policy_search.py'.
- '**Definição da tarefa, construção e treinamento do agente**'.
- '**Plotagem das recompensas**'.

## Outros arquivos deste projeto
- '**data.txt**': arquivo de dados gerados na execução do projeto.
- '**data_reward.txt**': arquivo de dados gerados na execução do projeto.
