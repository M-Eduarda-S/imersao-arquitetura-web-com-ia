# Alura Album - Copa do Mundo Tech

Este projeto é um **Álbum de Figurinhas Interativo** desenvolvido para homenagear grandes personalidades e pioneiros da tecnologia. O álbum conta com páginas folheáveis (com efeito físico de virada de página), efeitos sonoros de papel gerados dinamicamente via código e integração com uma API backend para carregar as imagens das figurinhas.

---

## 🎯 Objetivo do Projeto

O objetivo principal deste projeto é criar uma experiência interativa e imersiva para colecionar e visualizar figurinhas de gigantes da tecnologia. O álbum é dividido em categorias temáticas:
1. **Pioneiros da Inteligência Artificial (IA)** (Pág. 1)
2. **Arquitetos da Simplicidade (Python)** (Pág. 2)
3. **Arquitetos de Bancos de Dados (Database)** (Pág. 3)
4. **Arquitetos da Computação Moderna (Sistemas Operacionais)** (Pág. 4)
5. **Celebridades Tech do Brasil** (Pág. 5 e 6)

O projeto se destaca por combinar animações fluidas de folheamento de páginas, navegação responsiva por teclado, clique ou arraste, geração de som de papel realista diretamente no navegador (sem necessidade de arquivos de áudio externos) e carregamento dinâmico de dados e imagens a partir de uma API FastAPI externa.

---

## 📂 Arquivos do Projeto e suas Funcionalidades

O projeto é composto por três arquivos principais no frontend:

### 1. 📄 [index.html](./projeto/frontend/index.html)
Responsável por estruturar o esqueleto e o conteúdo do álbum.
* **Estrutura do Livro (`.flip-book`)**: Define a capa (`.page-cover`), as páginas internas (`.page-left` e `.page-right`) com suas respectivas grades de figurinhas (`.stickers-grid`), e a contracapa (`.page-cover-back`).
* **Slots de Figurinhas (`.sticker-slot`)**: Cada figurinha possui um slot demarcado com número, nome e cargo/função correspondente.
* **Controles Interativos**: Inclui botões de navegação lateral (anterior/próximo), botão de controle de áudio (mutar/desmutar) e o botão **🌓 Trocar tema** para a alternância de cores da aplicação.
* **Dependências Externas**: Carrega fontes personalizadas do Google Fonts (`Inter` e `Outfit`) e a biblioteca **PageFlip** via CDN (para o efeito físico de virada de páginas).

### 2. 🎨 [style.css](./projeto/frontend/style.css)
Responsável por toda a estilização, design responsivo e efeitos visuais premium.
* **Paleta de Cores & Temas (CSS Variables)**: Configurada usando variáveis semânticas. O tema escuro (padrão) utiliza tons de azul profundo, preto e azul neon. O tema claro, ativado pela classe `.light-theme` no `<body>`, redefine essas variáveis semânticas para cores suaves como cinza-claro, azul-celeste e branco, mantendo as cores e variáveis originais intactas.
* **Efeito de Páginas e Lombada**: Estiliza o livro com sombras realistas (`box-shadow`), gradientes para simular a dobra da lombada central do álbum (`.page-content::after`) e cursores de mão apropriados para agarrar e arrastar (`grab`/`grabbing`).
* **Visual Premium e Animações**: Contém estilos específicos para destaque de slots especiais, emblemas de categorias coloridos (`.tech-badge`), efeito de brilho e esfera 3D na capa, texto com efeito *glitch* estilizado, estilo glassmorphic dos botões de controle e responsividade para diferentes tamanhos de tela.

### 3. ⚡ [app.js](./projeto/frontend/app.js)
Contém toda a lógica e interatividade em JavaScript do aplicativo.
* **Integração com a API (`preencherFigurinhas`)**: Faz uma requisição assíncrona (`fetch`) para a API backend (`http://localhost:8000/figurinhas`) para carregar a lista de figurinhas e inserir dinamicamente as imagens nos slots correspondentes baseado no ID do slot (`#01`, `#02`, etc.).
* **Controle de Temas (Claro / Escuro)**: Alterna a classe `.light-theme` no `<body>` ao clicar no botão correspondente e salva o estado de preferência do usuário no `localStorage`, aplicando-o automaticamente na inicialização para evitar flashes visuais indesejados.
* **Inicialização do `PageFlip`**: Configura e inicializa a biblioteca com parâmetros de tamanho, limites de responsividade, desativação de cliques acidentais e ajustes de tempo de transição (800ms).
* **Controle de Arraste Avançado**: Sobrescreve e melhora os gestos de arrastar padrão da biblioteca para dispositivos móveis e desktop, garantindo que o folheamento só ocorra quando o usuário de fato arrastar além de uma distância limite (threshold).
* **Efeito Sonoro Dinâmico (`playPaperTurnSound`)**: Utiliza a **Web Audio API** para gerar de forma sintética (via código, sem carregar arquivos de áudio externos) o som realista de papel virando. Ele cria ruído branco dinâmico com envelopes de volume e filtros passa-banda/passa-biuxa para simular a fricção física.
* **Controles e Navegação**: Associa as teclas de setas do teclado (`ArrowLeft` e `ArrowRight`) e cliques nos botões laterais para folhear o álbum, além de gerenciar a exibição inteligente das setas (oculta a seta esquerda na capa e a direita na contracapa) e o controle de mudo do som.

---

## 🚀 Como Executar o Projeto

1. **Backend (API)**:
   * Certifique-se de que o backend esteja ativo para fornecer os dados e as imagens das figurinhas.
   * Se o backend estiver configurado na pasta apropriada, inicie-o usando:
     ```bash
     cd backend/dia-3
     uvicorn main:app --reload
     ```
   * A API deve rodar em `http://localhost:8000`.

2. **Frontend**:
   * Basta abrir o arquivo [index.html](file:///c:/Users/Usuário/Downloads/projeto/index.html) em qualquer navegador moderno.
   * Para testar a integração da API sem erros de CORS, recomenda-se rodar o frontend por meio de um servidor local (ex: extensão Live Server do VS Code, ou `python -m http.server 8080` no terminal).

---

## 📝 Sobre este README

Este README.md foi criado como parte da Imersão Arquitetura Web com IA. Seguindo as instruções, foi utilizado o Google Antigravity para gerar uma primeira versão a partir do seguinte prompt:

"Crie um README.md do projeto que explique o seu objetivo e as funcionalidades dos arquivos envolvidos."

O conteúdo foi posteriormente revisado e adaptado conforme necessário.

---

Desenvolvido durante a **Imersão Julho 2026** da Alura.