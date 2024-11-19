[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.14188212.svg)](https://doi.org/10.5281/zenodo.14188212)

# Connect4-Python

Este projeto é composto por dois componentes principais: 

* src: que possui a implementação do jogo e dos agentes (robôs)
* content: que possui todo o material didático sobre o assunto. 

Toda a implementação foi feita em Python. Este projeto é um fork do projeto do Keith Galli. Algumas modificações foram feitas na implementação, principalmente para permitir o jogo de robô contra robô. 

Toda a parte referente ao material didático é nova. 

A licença deste projeto é MIT License, como pode ser visto no arquivo [LICENSE](LICENSE) no repositório. Ou seja, você pode usar todo o material para o objetivo que quiser. No entanto, é necessário citar os autores deste projeto. 

Fabrício Barth é professor Tempo Integral no [Insper Instituto de Ensino e Pesquisa](https://www.insper.edu.br/). 

## Setup

Para o setup do projeto eu recomendo criar um ambiente virtual: 

````bash
python3.9 -m virtualenv venv
source venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
````

## Executando o servidor mkdocs na máquina local

Para executar o servidor da documentação em uma máquina local basta digitar:

````bash
cd content
mkdocs serve
````

## Fazendo o deploy da documentação usando o github actions

Existe um arquivo `main.yml` no diretório `.github/workflows` que define o deploy da documentação no gh-pages do github usando actions. 

## Exemplos de execução do jogo Liga4 ou Connect4

O jogo pode ser inicializado de algumas formas via `src/connect4.py` ou `src/connect4_with_ai.py`: 

* `src/connect4.py`: dois jogadores jogando de forma manual.
* `src/connect4_with_ai.py`: um jogador manual e outro artificial.
* `python connect4_with_ai.py random`: o jogador artificial tem comportamento aleatório.
* `python connect4_with_ai.py minmax 5`: o jogador artificial implementa o algoritmo min-max. O número informado é a profundidade que o algoritmo min-max irá considerar - precisa ser um valor maior ou igual a 1.

* `python connect4_with_ai.py flat`: equivale a execução do minmax com profundidade 1. É utilizado para mostrar o comportamento de um agente que avalia apenas o primeiro nível da árvore.

* `python connect4_with_ai.py complete`: equivale a execução do minmax com profundidade 20. É utilizado para mostrar o comportamento de um agente que avalia toda a árvore de busca. 

* `python connect4_ai_versus_ai.py random 0 minmax 5`: o primeiro argumento define o primeiro jogador. Se for `random` então o segundo argumento pode ser qualquer valor. O terceiro argumento define o segundo jogador. Se o jogador for `minmax` então o argumento subsequente sempre precisa ser a profundidade adotada pelo `minmax`. 


## Compilar os slides

Para visualizar os arquivos que estão na pasta slides ou gerar `pdf` a partir deles basta utilizar qualquer plugin para Markdown no VSCode. 



