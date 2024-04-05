# Prova Semana 9

### Luiz Fernando Leão

## 📜 Descrição

&emsp;Está é a prova da Semana 9. Para a questão prática da avaliação, você deve construir um sistema que permite ao usuário visualizar os logs de acesso a duas rotas. Cada vez que uma dessas rotas receber uma requisição, armazenar o horário do servidor e a requisição realizada em uma lista com essas informações. Além disso, construir uma página na rota '/dash', que permite visualizar o histórico das requisições realizadas. Esse dash deve ser construído utilizando o render_template() do Flask e HTMX para atualizar as informações sobre o log das informações. Para obter as informações para a construção da página, criar a rota '/info', que deve retornar mídia sobre os dados armazenados.

## 📁 Estrutura de pastas

&emsp;&emsp;Dentre os arquivos e pastas presentes na raiz do projeto, define-se:

- <b>static</b>: pasta com os códigos de css e tambem imagens estaticas
- <b>templates</b>: pasta com os códigos de html
- <b>.gitignore</b>: arquivo que ignora a importação de pastas desnessárias
- <b>app.py</b>: arquivo em python que faz o programa funcionar
- <b>echo.json</b>: arquivo que armazena as informações do banco de dados sobre o echo
- <b>ping.json</b>: arquivo que armazena as informações do banco de dados sobre o ping
- <b>readme.md</b>: arquivo de texto com informações sobre este repositório
- <b>requirements</b>: arquivo com as bibliotecas que precisam ser instaladas pro sistema funcionar

## 🔧 Instalação

&emsp;Para executar o projeto, instale o repositório no dispositivo. Abra o Prompt de Comando e digite ```python3 -m venv venv``` para criar o ambiente virtual e depois ```venv/bin/activate´´´ para ativar o venv
. Digite ```pip install -r requirements.txt``` para instalar todas dependências e aguarde enquanto a instalação é feita.
Para concluir, digite ```python app.py``` para iniciar o projeto, e aguarde até a página ser carregada.