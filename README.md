### Visão Geral:

Esse é um código responsável para criação de PDFs a partir de um template PDF.

O Template PDF pode ser gerado atráves de um HTML básico.

Para esse projeto, eu prototipei o template via Figma e usei um plugin do próprio FIGMA para converter para HTML.
Dentro do próprio Figma você pode colocar as variáveis no formato ${nome_variavel}, como no exemplo template.pdf.
(Você também pode fazer em HTML direto, não há problema)

Com o HTML em mãos, vamos imprimir e transformar em PDF com o nome "template.pdf"

O código python fará a leitura do template, substituirá as variáveis pelos valores fornecidos e gerará um "Output.pdf",
que basicamente é o "template.pdf" com as variáveis substituídas pelos valores atribuidos dentro do código.

### Sobre meu código:

Usei as infos como um dicioniário pois consigo visualizar melhor o que chega até mim e o que deve sair no resultado final.

Não necessariamente você precisa fazer isso para o seu caso, porém existem alguns ifs de formatação dependendo da varíavel.
Esse tratamento tem a ver com a formatação que sai no PDF, na qual sua versão padrão pode vir incorreta.
A função .insert_text faz a inserção do texto possibilitando ajustar a formatação conforme necessário.
