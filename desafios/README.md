# Desafios

Repositório com as soluções dos desafios da Imersão Arquitetura Web com IA da Alura. Cada seção apresenta o enunciado da atividade, o prompt utilizado e o resultado obtido durante a resolução.

---

## 📑 Índice
- [Desafio 1](#desafio-1-um-bot%C3%A3o-para-alternar-o-tema-do-%C3%A1lbum)
- [Desafio 2](#desafio-2-buscar-uma-figurinha-pelo-id-com-erro-404)
- [Desafio 3](#desafio-3-endpoint-de-contagem-e-estat%C3%ADstica-do-%C3%A1lbum)

---

## Desafio 1: Um botão para alternar o tema do álbum

Hoje o álbum tem um tema fixo (azul tech sobre fundo escuro), definido pelas variáveis de cor no bloco :root do style.css. O desafio é instruir a IA a criar um segundo tema (claro) e um botão "🌓 Trocar tema" que alterne entre os dois temas ao ser clicado — sem recarregar a página. </br>

Isso envolve as três camadas do frontend de uma vez:

HTML → adicionar o botão no index.html </br>
CSS → criar uma variação de tema no style.css </br>
JS → fazer o clique alternar o tema no app.js </br>

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

## Desafio 2: Buscar uma figurinha pelo id (com erro 404)
No Dia 2, o main.py tem dois endpoints: GET / e GET /figurinhas (que devolve a lista das 2 figurinhas em JSON). Seu desafio é instruir a IA a adicionar um terceiro endpoint que busca uma única figurinha pelo seu id: 

GET /figurinhas/1 → devolve a figurinha do Alan Turing </br>
GET /figurinhas/2 → devolve a figurinha do John McCarthy </br>
GET /figurinhas/99 → devolve erro 404 (não encontrado), porque esse id não existe </br>

O segredo aqui é o parâmetro de rota dinâmico ({id}) e o status code 404 — conceitos que apareceram na aula do Dia 1 </br>

**→ Dica para solucionar** 

Seu prompt precisa deixar claro que é para adicionar ao arquivo existente, mantendo os endpoints / e /figurinhas. Cole o conteúdo atual do main.py no prompt para dar contexto. </br>
Especifique o comportamento dos dois caminhos: quando o id existe (retorna a figurinha) e quando não existe (retorna 404). </br>
Mencione que, no FastAPI, o erro 404 se faz com HTTPException — ou simplesmente peça "retorne erro 404 se o id não existir" e deixe a IA escolher a forma. </br>

### 💬 Prompt criado
```text
No mesmo arquivo @[main.py], adicione um terceiro endpoint, mantendo os endpoints já existentes (`/` e `/figurinhas`) sem alterar seu funcionamento.
O novo endpoint deve buscar uma única figurinha pelo seu ID utilizando um parâmetro de rota dinâmico.

O comportamento esperado é:
- GET /figurinhas/1 → retorna a figurinha do Alan Turing.
- GET /figurinhas/2 → retorna a figurinha do John McCarthy.
- GET /figurinhas/99 → retorna erro 404 (não encontrado), pois esse ID não existe.

Utilize o recurso apropriado do FastAPI para retornar o erro 404 e mantenha o código organizado e consistente com a estrutura atual do arquivo.
```

### 📸 Resultado

#### Requisição com figurinha encontrada
<img src="../imagens/Print da figurinha encontrada (desafio 2).png" alt="Print da figurinha encontrada" width="80%">

#### Requisições com figurinha não encontrada
<img src="../imagens/Print da figurinha não encontrada (desafio 2).png" alt="Print da figurinha não encontrada" width="80%">

---

## Desafio 3: Endpoint de contagem e estatística do álbum
No Dia 3, o main.py tem a lista figurinhas (hoje com 2 itens) e o endpoint GET /figurinhas que a devolve em JSON. Mas o álbum completo tem 25 slots para preencher. </br>

Seu desafio é instruir a IA a adicionar um novo endpoint GET /figurinhas/total que não devolve a lista, e sim uma estatística calculada a partir dela: 

```json
{ 
  "total_album": 25, 
  "coladas": 2, 
  "faltam": 23 
} 
```

O pulo do gato: o número de coladas e o de faltam devem ser calculados a partir da lista (não escritos "na mão"). Assim, quando alguém adicionar uma figurinha à lista, a estatística se atualiza sozinha. </br>

**→ Dica para solucionar**

No prompt, deixe claro que é para adicionar o endpoint, mantendo o GET /figurinhas que já existe. Cole a lista atual para dar contexto. </br>
O total do álbum (25) é uma constante — diga isso. Já as coladas saem de len(figurinhas) e faltam é 25 - len(figurinhas). </br>
Reforce que os valores devem ser calculados a partir da lista, e não valores fixos — é isso que torna o endpoint "vivo". </br>
Peça para a IA usar uma função com nome claro (ex: estatisticas_album).


### 💬 Prompt criado
```text
Faça no @[main.py] um novo endpoint GET /figurinhas/total, mantendo o endpoint GET /figurinhas que já existe.

O novo endpoint deve devolver uma estatística calculada a partir da lista de figurinhas:
{
  "total_album": 25,
  "coladas": 2,
  "faltam": 23
}

O valor de "total_album" deve ser uma constante igual a 25.
Os valores de "coladas" e "faltam" devem ser calculados dinamicamente a partir da lista de figurinhas, para que sejam atualizados automaticamente sempre que uma nova figurinha for adicionada.
Utilize uma função chamada estatisticas_album e mantenha o código organizado.
```


### 📸 Resultado

#### Resultado da requisição
<img src="../imagens/Print do resultado da requisição (desafio 3).png" alt="Print da requisição" width="80%">


---

> [!NOTE]
> Os prompts apresentados neste README foram utilizados para gerar as implementações dos desafios. Os códigos resultantes foram mantidos na pasta [projeto](../projeto), onde é possível visualizar a versão final da aplicação.
