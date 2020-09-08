<h1 align="center">Welcome to LFA Implemetation 👋</h1>
<p>
  <img alt="Version" src="https://img.shields.io/badge/version-1.0.0-blue.svg?cacheSeconds=2592000" />
  <img src="https://img.shields.io/badge/Python-%3E%3D.svg" />
  <a href="https://github.com/ErikDCAlmeida/LFA_Implemetation/#readmme#" target="_blank">
    <img alt="Documentation" src="https://img.shields.io/badge/documentation-yes-brightgreen.svg" />
  </a>
  <a href="https://github.com/ErikDCAlmeida/LFA_Implemetation/graphs/commit-activity" target="_blank">
    <img alt="Maintenance" src="https://img.shields.io/badge/Maintained%3F-yes-green.svg" />
  </a>
  <a href="https://github.com/ErikDCAlmeida/LFA_Implemetation/blob/master/LICENSE" target="_blank">
    <img alt="License: MIT" src="https://img.shields.io/github/license/ErikDCAlmeida/LFA_Implemetation" />
  </a>
</p>

> Aplicação desenvolvida em python para teste de liguagens com uso de automatos finitos determinísticos e não-determinísticos.

### 🏠 [Pagina Inicial](https://github.com/ErikDCAlmeida/LFA_Implemetation)

## Pré-requisitos

- Python
- GraphModels

## Usabilidade


> - Para executar a aplicação, inicialmente será necessário executar no terminal dentro da pasta no projeto o comando: pip install -e GraphModels.</br>
> - GraphModels é uma biblioteca criada por [@matheusnalmeida](https://github.com/matheusnalmeida) que possui uma implementação orientada a objetos de grafos e alguns algoritimos relacionados a grafos. O codigo fonte para a biblioteca pode ser encontrado no repositorio [GraphModels](https://github.com/matheusnalmeida/GraphModelsLIB).

## Modo de Escrita do .TXT para Testar o Autômato

> - Os arquivos de teste dos dois tipos de autômatos pode sem encontrados clicando aqui e você poderá seguir como base para criar o seu <b>.txt</b>, além de visualizar a imagem dos mesmos já criado no <b>JFLAP</b>: [Autômato Finito Determinístico](https://github.com/ErikDCAlmeida/LFA_Implemetation/blob/master/teste_dfa.txt) ([Imagem DFA!](https://github.com/ErikDCAlmeida/LFA_Implemetation/blob/master/TestAutomatonImages/Automaton_DFA_Image_Test.png)) e [Autômato Finito Não-determinístico](https://github.com/ErikDCAlmeida/LFA_Implemetation/blob/master/teste_nfa.txt) ([Imagem NDFA!](https://github.com/ErikDCAlmeida/LFA_Implemetation/blob/master/TestAutomatonImages/Automaton_NFA_Image_Test.png)).</br>
> - Para escrever um arquivo <b>.txt</b> no qual o algoritmo reconheça é necessário seguir alguns passos que são:</br>
> <b>1-</b> A primeira linha do arquivo serve para o algoritmo reconhecer o alfabeto do autômato.</br>
> <b>2-</b> As linhas a seguir servem para reconhecer as conexões dos estados e quantos estados serão utilizados para criar o autômato.</br>
> <b>3-</b> Após terminar a inserção das linhas do <b>passo 2</b> é necessário inserir uma linha que contenha <b>"um . seguido de ;" (somente os símbolos)</b>, isso permitirá que o algoritmo reconheça que o <b>passo 2</b> foi finalizado e siga para o <b>passo 4</b>.</br>
> <b>4-</b> Nas linhas a seguir o algoritmo reconhecerá quem é o estado inicial e o(s) estado(s) final(is) do algoritmo. Os símbolos usados para reconhecer quem é o inicial é o sinal de <b>maior (>)</b> e quem é o final é o símbolo de <b>menor (<)</b>. O <b>traço (-)</b> no final da linha serve apenas para identificar que a linha terminou e pode ir pra próxima.</br>
> <b>5-</b> Após inserir todos os estados que são início e fim, você não poderá deixar nenhuma linha vazia, pois com isso o algoritmo saberá que o arquivo foi terminado.

## Autores

👤 **Matheus Nunes De Almeida e Erik Danilo Costa De Almeida**

* GitHub: [@matheusnalmeida](https://github.com/matheusnalmeida) e [@ErikDCAlmeida](https://github.com/ErikDCAlmeida)
* LinkedIn: [@matheusnalmeida](https://www.linkedin.com/in/matheus-nunes-de-almeida-387980194/) e [@ErikDCAlmeida](https://www.linkedin.com/in/erik-almeida-7b7358172/)

## Demonstre seu suporte

Dê uma ⭐️ se este projeto te ajudou!

## 📝 Licença

Copyright © 2020 [Erik Danilo Costa De Almeida](https://github.com/ErikDCAlmeida).<br />
Esse projeto possui [MIT](https://github.com/ErikDCAlmeida/LFA_Implemetation/blob/master/LICENSE) license.

***
_This README was generated with ❤️ by [readme-md-generator](https://github.com/kefranabg/readme-md-generator)_