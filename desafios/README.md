# Desafios

Repositório com as soluções dos desafios da Imersão Arquitetura Web com IA da Alura. Cada seção apresenta o enunciado da atividade, o prompt utilizado e o resultado obtido durante a resolução.

---

## 📑 Índice
- [Desafio 1](#desafio-1-um-bot%C3%A3o-para-alternar-o-tema-do-%C3%A1lbum)
- [Desafio 2](#desafio-2)

---

## Desafio 1: Um botão para alternar o tema do álbum

Hoje o álbum tem um tema fixo (azul tech sobre fundo escuro), definido pelas variáveis de cor no bloco :root do style.css. O desafio é instruir a IA a criar um segundo tema (claro) e um botão "🌓 Trocar tema" que alterne entre os dois temas ao ser clicado — sem recarregar a página.

Isso envolve as três camadas do frontend de uma vez:

HTML → adicionar o botão no index.html

CSS → criar uma variação de tema no style.css

JS → fazer o clique alternar o tema no app.js

O objetivo não é você escrever esse código, e sim descrever a tarefa para a IA de forma que ela entregue tudo conectado e funcionando.

### 💬 Prompt criado
```text
Crie um sistema de troca de tema para a aplicação. No @[index.html], adicione um botão com o texto "🌓 Trocar tema" em um local apropriado da interface. No @[style.css], mantenha o tema escuro atual e crie um tema claro utilizando variáveis CSS, sem remover as existentes. No @[app.js], implemente a lógica para que, ao clicar no botão, o tema seja alternado entre escuro e claro, sem recarregar a página. Utilize uma classe no elemento <body> para controlar o tema e mantenha o código organizado e integrado entre HTML, CSS e JavaScript.
```

### 📸 Resultado

#### Capa

<p align="center">
  <img src="../imagens/Print da capa em tema escuro (desafio 01).png" alt="Tema escuro" width="45%">
  <img src="../imagens/Print da capa em tema claro (desafio 01).png" alt="Tema claro" width="45%">
</p>

#### Botão de troca de tema

<p align="center">
  <img src="../imagens/Print do botão em tema escuro (desafio 01).png" alt="Botão tema escuro" width="15%">
  <img src="../imagens/Print do botão em tema claro (desafio 01).png" alt="Botão tema claro" width="15%">
</p>

---

## Desafio 2: ...

---

> [!NOTE]
> Os prompts apresentados neste README foram utilizados para gerar as implementações dos desafios. Os códigos resultantes foram mantidos na pasta [projeto](../projeto), onde é possível visualizar a versão final da aplicação.
