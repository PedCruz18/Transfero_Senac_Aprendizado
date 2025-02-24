# AULA 02
- Os elementos (marcações) do html são conhecidos como tags.
- As tags podem possuir somente abertura ou abertura/encerramento.

1. Principais tags
<h1></h1> até a <h6></h6> -> Títulos.
<p></p> -> Parágrafos.
<a></a> -> Tag de link.
<img> -> Tag responsável por apresentar uma imagem.
<strong></strong> -> Tag semântica. Indica uma força na palavra/frase.
<em></em> -> Tag semântica. Indica uma ênfase na palavra/frase.
<b></b> -> Coloca uma frase/palavra em negrito.
<i></i> -> Coloca uma frase/palavra em itálico.
<br> -> Realiza um quebra de linha.
<hr> -> Cria uma linha na horizontal.
<div></div> -> Cria um bloco contendo outras tags.

2. Realizando a comunicação do css com o html.
- `CSS interno` -> Fica no arquivo html e é separado pela tag <style></style>.
- `CSS Externo` -> É um arquivo separado ao arquivo do html. Possui a extensão .css e é a forma mais recomendada.
- `CSS Inline` -> É utilizado exatamente na tag no html. Deve ser usado com cautela.

3. Estilizações básicas no css
`color:` -> Irá colocar uma cor no texto.
`background:` -> Irá colocar uma cor de preenchimento no fundo do elemento.
`font-size:` -> Altera o tamanho da fonte.

# AULA 03
## SELETORES NO CSS
=> É a forma como você irá chamar um determinado elemento do `html` no `css`.
1. tag => Basicamente, você chama a tag em sí para realizar a estilização.
* Quando você chama diretamente a tag, cuidado para não estilizar todos os elementos que possuem aquela tag.

2. #id => Você cria um identificador único na tag do elemento [html] e chama esse identificador no css.

3. .class => Você cria um "apelido" na tag do elemento e esse "apelido" pode ser utilizado quantas vezes necessário, inclusive em outras tags diferentes.

## SISTEMA DE CORES
1. `nome da cor` => Especifica o valor da cor através do nome dela em inglês.
2. `hexadecimal` => Especifica o valor da cor através de uma sequência alfa-numérica.
3. rgb => Especifica a cor através da intensidade do red[vermelho], green[verde] e blue[azul].
4. rgba => São os mesmos valores do rgb, porém com o valor do alpha[opacidade].

# AULA 04
1. <img> => Tag responsável por inserir uma imagem interna ou externa.
- src -> é onde é inserido o caminho da imagem; 
- alt -> é o texto alternativo que será exibido caso a imagem "quebre" e por questões de acessibilidade.
ex: <img src="caminho_da_imagem" alt="Descrição da imagem">

2. Listas
<ul></ul> -> Informa que existirá itens e a posição desses itens não importa. Lista não ordenada.
<ol></ol> -> Informa que existirá itens e a posição desses itens importa. Lista ordenada.
<li></li> -> é cada item da lista.

3. Tag de link
<a></a> -> é utilizada para gerar um texto clicável. link
- href -> é uma propriedade onde você irá informar qual o caminho que o link irá enviar o usuário.
ex: <a href="caminho_do_link">Sobre</a>

## CSS
1. `font-family: Arial, Helvetica, sans-serif;` -> Propriedade que altera o tipo de fonte utilizado no elemento.
2. `padding` -> é o espaçamento interno de um conteúdo até a borda.
3. `margin` -> é o espaçamento externo da borda em relação a outro elemento.
4. `border` -> é a borda do elemento.

# AULA 05
1. POSICIONAMENTO (GRID)
'GRID' -> 