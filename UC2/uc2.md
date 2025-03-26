# AULA 02
- Os elementos (marcações) do html são conhecidos como tags.
- As tags podem possuir somente abertura ou abertura/encerramento.

1. Principais tags

- `<h1></h1>` Até a `<h6></h6>` prioridde é na ordem do h1 até o h6.
- `<p></p>` -> Parágrafo
- `<a></a>` -> Tag de link
- `<img>` -> Tag responsável por apresentar uma imagem.
- `<strong></strong>` -> Tag semântica. Indica uma força na palavra/frase.
- `<em></em>` -> Tag semântica. Indica uma ênfase na palavra/frase.
- `<b></b>` -> Coloca uma frase/palavra em negrito.
- `<i></i>` -> Coloca uma frase/palavra em itálico.
- `<br>` -> Realiza uma quebra de linha.
- `<hr>` -> Cria uma linha na horizontal.
- `<div></div>` -> Cria um bloco contendo outras tags.

2. Realizando a comunicação do css com o html

- `CSS interno` -> Fica no arquivo html e é separado pela tag `<style></style>`
- `CSS externo` -> É um arquivo separado ao arquivo do html. Possui a extensão .css e é a forma mais recomendada.
- `CSS inline` -> É utilizada exatamente na tag no html. Deve ser usado com cautela.

3. Estilizações básicas no CSS
- `color:` -> Irá colocar uma cor no texto.
- `background:` -> Irá colocar uma cor de pressnchimento no fundo do elemento.
- `font-size:` -> Altera o tamanho da fonte.

<br>

# AULA 03
## SELETORES NO CSS

É a forma como você irá chamar um determinado elemento do `html` no `css`.

- `tag` - Basicamente, você chama a tag em sí para realizar a estilização
  - Quando você chama diretamente a tag, cuidado para não estilizar todos os elementos que possuem aquela tag.
- `#id` - Você cria um identificador único na tag do elemento `html` e chama esse identificador no css.
- `.class` - Você cria um `apelido` na tag do elemento e esse `apelido` pode ser utilizado quantas vezes necessário, inclusive em outras tags diferentes.

<br>

## SISTEMA DE CORES
- `nome da cor` - Especifica o valor da cor através do nome dela em inglês.
- `hexadecimal` - Especifica o valor da cor através de uma sequência alfa-numérica.
- `rgb` - Especifica a cor através da intensidade do red(`vermelho`), green(`verde`) e blue(`azul`).
- `rgba` - São os mesmos valores do rgb, porém com o valor do alpha(`opacidade`)

# AULA 04
- `<img>` - Tag responsável por inserir uma imagem interna ou externa.
  - `src` -> é onde é inserido o caminho da imagem;
  - `alt` - é o texto alternativo que será exibido caso a imagem "quebre" e por questôes de acessibilidade.
    - ex: `<img src="caminho_da_imagem" alt="logo da Bikecraft">`

### listas
- `<ul></ul>` - Informa que existirá itens e a posição desses itens não importa. `Lista não ordenada`.
- `<ol></ol>` - Informa que existirá itens e a posição desses itens importa. `Lista ordenada`.
- `<li></li>` - É cada item da lista.

### tag de link
- `<a></a>` - É utilizada para gerar um texto clicável. `Link`
  - `href` - é uma propriedade onde você irá informar qual o caminho que o link irá enviar o usuário.
    - Ex: `<a href="caminho_do_link">Sobre</a>`

## css
- `font-family: Arial, Helvetica, sans-serif;` - Propriedade que altera o tipo de fonte utilizado no elemento.
- `padding` - É o espaçamento interno de um conteúdo até a borda.
- `margin` - É o espaçamento 
- `border` -

# AULA 05
### POSICIONAMENTO(GRID)

- `GRID` - É uma das texnolofias mais utilizadas nos sistemas web e sites. A lógica utilizada é separar a tela em olunas e linhas que podem ser de diferentes tamanhos.

### UTILIZANDO O GRID
Utilizamos a propriedade display com o valor de grid.

Ex: `display: grid;`

### PRINCIPAIS PROPRIEDADES DO GRID
- `grid-template-columns:` Propriedade utilizada para informar ao css quantas colunas e quais os tamanhos você irá usar.
- `grid-template-rows:` Propriedade utilizada para informar quantas linhas serão geradas e o tamanho delas.
  - Métricas utilizadas:
    - `%, e px` - evitar.
    - `fr` - Fração referente a página toda.
    - `auto` - tamanho de forma atutomática.

<br>

- `grid-row:` Define em qual linha o elemento irá se posicionar.
- `grid-column:` Define em qual coluna o elemento irá se posicionar.