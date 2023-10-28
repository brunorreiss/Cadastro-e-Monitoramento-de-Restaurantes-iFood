<h1 align="center"> Cadastro e Monitoramento de Restaurantes - iFood </h1>
<h4 align="center"> Vem ser Tech | Dados - <a href="https://www.linkedin.com/school/adatechbr">Ada Tech</a> (Primavera 2023) </h4>

<br>
</br>
<p align="center"> 
<a href="https://cdn.myportfolio.com/c8489c04-75f1-4bdc-b062-ae01d51f5d5a/2fd05462-bfe4-425f-a5c0-2bf47941914e_rwc_0x0x1244x1656x1244.gif?h=e226d8389a084ed355a8e3f7929c7357" target="_blank"><img src="https://cdn.myportfolio.com/c8489c04-75f1-4bdc-b062-ae01d51f5d5a/2fd05462-bfe4-425f-a5c0-2bf47941914e_rwc_0x0x1244x1656x1244.gif?h=e226d8389a084ed355a8e3f7929c7357" alt="image host" height="200px"/></a>
</p>

<h4> <p align="center"> <a href="#creditos">Créditos</a> | <a href="#contexto">Contexto e objetivo</a> | <a href="#especificacao">Especificação</a> | <a href="#tecnologias">Tecnologias</a> | <a href="#organizacao">Organização dos arquivos </a> | <a href="execucao">Execução</a> | <a href="#equipe">Equipe</a> </p>

<h2 id="creditos"> :scroll: CRÉDITOS</h2>

- Instituição: Let's Code <a href="https://www.linkedin.com/school/adatechbr/">(Ada Tech)</a>
- Curso: Vem ser Tech | Dados
- Disciplina: Lógica de Programação I
- Professores: Thiago

<a href="https://imgbox.com/3tZuCnVg" target="_blank"><img src="https://images2.imgbox.com/42/88/3tZuCnVg_o.png" alt="image host" height="5px" width="900px"/></a>

<h2 id="contexto"> 📊: CONTEXTO E OBJETIVO</h2>

O desenvolvimento do projeto dar-se-á conclusão do módulo I do curso Vem ser Tech | Dados, consistindo em um sistema simples de cadastro e monitoramentos de restaurantes.

<a href="https://imgbox.com/3tZuCnVg" target="_blank"><img src="https://images2.imgbox.com/42/88/3tZuCnVg_o.png" alt="image host" height="5px" width="900px"/></a>

<h2 id="especificacao"> :books: ESPECIFICAÇÃO</h2>

O seu grupo foi encarregado de fazer uma interface para cadastro e monitoramento de restaurantes no iFood. Desenvolvam um sistema com menu que tenha as seguintes características:
- Cadastro de um novo restaurante, da forma [nome_restaurante, [lat, lon], n_pedidos];
- Criar cardápio;
- Registrar histórico de vendas;
- Verificar restaurantes mais pertos de uma localidade;
- Além disso, crie também pelo menos três novas funcionalidades para essa interface. 

Obs:. Você terá em mãos algumas funções que implementam a manipulação de arquivos, para viabilizar o projeto. 

<a href="https://imgbox.com/3tZuCnVg" target="_blank"><img src="https://images2.imgbox.com/42/88/3tZuCnVg_o.png" alt="image host" height="5px" width="900px"/></a>

<h2 id="tecnologias"> 🛠️ TECNOLOGIAS UTILIZADAS </h2>

<ul>
  <li>Python</li>
  <p> A linguagem utilizada para o desenvolvimento fora <strong> Python</strong>, tanto por ser a ferramenta de aprendizado utilizada durante o curso, quanto por ser uma linguagem de alto nível, orientada a objetos, funcional e de tipagem dinâmica e forte. </p>
</ul> 
<ul>
  <li>JSON</li>
  <p> Sendo uma importante ferramenta utilizada para trocar informações entre um servidor e um cliente, além de seu formato de dados leve e de fácil leitura, o JSON, neste projeto, fora utilizado de forma que cada entrada representa um restaurante e é definida como um objeto detentor de várias propriedades, como uma matriz de objetos que descrevem os itens do cardápio ou vendas anteriores. </p>
</ul>

<a href="https://imgbox.com/3tZuCnVg" target="_blank"><img src="https://images2.imgbox.com/42/88/3tZuCnVg_o.png" alt="image host" height="5px" width="900px"/></a>

<h2 id="organizacao"> 📂 ORGANIZAÇÃO DOS ARQUIVOS </h2>

<p>Este projeto inclui arquivos executáveis e de destino, além de acesso ao diretório fonte (repositório), como a seguir:</p>
<h4>➔ Arquivos executáveis:</h4>
<ul>
  <li><a href="https://github.com/brunorreiss/Cadastro-e-Monitoramento-de-Restaurantes-iFood/blob/main/src/main.py"><b>main.py</b></a> - Contém o código-fonte responsável pelos menus disponíveis para o restaurante parceiro e para o cliente (incluindo procedimentos de cadastro, validação de pedidos através da disponibilidade do produto em estoque, mensagens de erro para entradas inválidas etc.). </li>
   <li><a href="https://github.com/brunorreiss/Cadastro-e-Monitoramento-de-Restaurantes-iFood/blob/main/src/json_manipulation.py"><b>json_manipulation.py</b></a> - Define um conjunto de funções para lidar com a criação, leitura, validação, gravação e manipulação dos dados em formato JSON no arquivo importado no cabeçalho do código. </li>
    <li><a href="https://github.com/brunorreiss/Cadastro-e-Monitoramento-de-Restaurantes-iFood/blob/main/src/restaurante.py"><b>restaurante.py</b></a> - As funcionalidades deste código reduzem o estoque do item quando este é confirmado, incrementam o contador de pedidos do restaurante, criam um dicionário representando a solicitação e adicionam o pedido ao histórico de vendas do restaurante. </li>
</ul>
<h4>➔ Bibliotecas utilizadas:</h4> 
<ul>
  » No arquivo <a href="https://github.com/brunorreiss/Cadastro-e-Monitoramento-de-Restaurantes-iFood/blob/main/src/main.py"><b>main.py</b>:</a>
  <li>import os: fornece funcionalidades para interagir com o sistema operacional, como manipular arquivos, pastas e variáveis de ambiente. </li>
  <li>import platform: permite ao programa obter informações sobre a plataforma na qual ele está sendo executado, como o sistema operacional e a arquitetura do sistema.. </li>
</ul>
<ul>
  » No arquivo <a href="https://github.com/brunorreiss/Cadastro-e-Monitoramento-de-Restaurantes-iFood/blob/main/src/json_manipulation.py"><b>json_manipulation.py</b>:</a>
  <li>from uuid import uuid4: sendo uma importação específica do módulo uuid, permite a geração de chaves primárias. </li>
 </ul> 
 <ul>
  » No arquivo <a href="https://github.com/brunorreiss/Cadastro-e-Monitoramento-de-Restaurantes-iFood/blob/main/src/restaurante.py"><b>restaurante.py</b>:</a>
  <li>import math: sendo a principal biblioteca por fornecer várias funções e constantes matemáticas, neste código, ela é responsável calcular a proximidade entre um conjunto de restaurantes e as coordenadas geográficas do usuário através da fórmula de Haversine. </li>
</ul>
<h4>➔ Módulos internos:</h4> 
<ul>
  » No arquivo <a href="https://github.com/ligianogueira1/Bot_Discord_IFPB/blob/main/main.py"><b>main.py</b>:</a> </li>
  <li>from src.restaurante import *: esta linha importa todas as funções, classes e variáveis definidas no módulo "restaurante", localizado no diretório "src." Isso significa que o código pode utilizar todas as definições deste módulo em todo o programa. </li>
  <li>from src.json_manipulation import *: importa todas as funções, classes e variáveis definidas no módulo "json_manipulation" localizado no diretório "src." </li>
</ul>
<h4>➔ Arquivos de destino:</h4> 
<ul>
  <li><a href="https://github.com/brunorreiss/Cadastro-e-Monitoramento-de-Restaurantes-iFood/blob/main/database/json_db.json"><b>json_db.json</b>:</a>Contém informações fictícias sobre usuários e restaurantes, sendo utilizado como um pequeno banco de dados para o projeto. </li>
</ul>
<h4>➔ Diretório fonte:</h4>
<ul>
  <li><a href="https://github.com/brunorreiss/Cadastro-e-Monitoramento-de-Restaurantes-iFood"><b>Cadastro-e-Monitoramento-de-Restaurantes-iFood</b>:</a>Inclui todos os arquivos listados acima. </li>
</ul>
  

<a href="https://imgbox.com/3tZuCnVg" target="_blank"><img src="https://images2.imgbox.com/42/88/3tZuCnVg_o.png" alt="image host" height="5px" width="900px"/></a>

<h2 id="execucao"> 🖥️ INSTRUÇÕES DE EXECUÇÃO</h2>

Como a proposta do projeto foi a utilização de técnicas e tecnologias vistas em aula, não fez-se necessário a utilização de pacotes externos.

<p>A ordem a seguir, de possível execução dos arquivos do programa, deve ser seguida após realizar o dowload do arquivo ZIP do <a href="https://github.com/brunorreiss/Cadastro-e-Monitoramento-de-Restaurantes-iFood"><b>diretório fonte</b></a>:</p>

<p><b>Passo 1) Manipulação do JASON</b>:</p>
<p>É necessário que o arquivo <a href="https://github.com/brunorreiss/Cadastro-e-Monitoramento-de-Restaurantes-iFood/blob/main/src/json_manipulation.py"><b>json_manipulation.py</b></a> seja carregado e executado antes de todos os outros do repositório, visto que, em termos de dependência, é o responsável por criar o diretório e o arquivo JSON de banco de dados, caso eles não existam. Após, carrega os dados do arquivo, salva-os na ferramenta JSON e adiciona um novo restaurante ao data-base.</p>

<p><b>Passo 2) Banco de dados </b>:</p>
<p>Diferentemente do arquivo JSON de manipulação, supracitado, este <a href="https://github.com/brunorreiss/Cadastro-e-Monitoramento-de-Restaurantes-iFood/blob/main/database/json_db.json"><b>banco</b></a> armazena os dados dos restaurantes, cardápios e histórico de vendas.</p>
  
<p><b>Passo 3) Menu principal</b>:</a></p>
<p> O arquivo <a href="https://github.com/ligianogueira1/Bot_Discord_IFPB/blob/main/main.py"><b>main.py</b></a> exerce a base do projeto quando possui funções as quais exibem o menu principal do programa, permitindo que o usuário escolha entre acessar como 1. parceiro ou 2. usuário. Na opção 1, há o menu de operações disponíveis para um parceiro, como cadastrar um novo restaurante, criar cardápio, ver histórico de vendas, listar restaurantes, remover restaurante, atualizar estoque ou sair. A opção 2, por sua vez, permite que o usuário encontre restaurantes próximos e realize pedidos.</p>

<p><b>Passo 4) Funções para o restaurante</b>:</a></p>
<p> No arquivo <a href="https://github.com/brunorreiss/Cadastro-e-Monitoramento-de-Restaurantes-iFood/blob/main/src/restaurante.py"><b>restaurante.py</b></a>, há funções relacionadas à manipulação de restaurantes, cardápio, atualização de estoque, cálculo de proximidade e realização de pedidos.</p>

<p><b>Passo 5) O ambiente</b>:</a></p>
<p> Um arquivo de ambiente <a href="https://github.com/brunorreiss/Cadastro-e-Monitoramento-de-Restaurantes-iFood/blob/main/utils/environment.yml"><b>Conda</b></a> é indispensável para especificar as dependências necessárias para executar o projeto.</p>
  
<a href="https://imgbox.com/3tZuCnVg" target="_blank"><img src="https://images2.imgbox.com/42/88/3tZuCnVg_o.png" alt="image host" height="5px" width="900px"/></a>

<h2 id="equipe"> :brain: EQUIPE</h2>

Projeto desenvolvido pelos Devs:

- [Anna Lígia Nogueira](https://github.com/ligianogueira1)
- [Bruno Reis](https://github.com/brunorreiss)
- [Gabriel Victor](https://github.com/gabrielvmdvital)
- [Guilherme Pereira](https://github.com/Guilhermepsilva003)
- [Matheus Miranda Brandão](https://github.com/MatBrands)
