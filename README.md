# servidores-distribuidos

Universidade do Estado de Santa Catarina - UDESC

Curso: Tecnologia em Análise e Desenvolvimento de Sistemas - TADS

Disciplina: Sistemas Distribuídos

## Serviço de Echo Tolerante a Falha

Este serviço será responsável por ecoar (espelhar) mensagem enviada por cliente. Contudo será um serviço tolerante a falha, ou seja, caso um servidor não possa atender (responder a mensagem enviada pelo cliente), o cliente deverá enviar a requisição (mensagem) à outro servidor de eco idêntico, que deverá responder ao cliente.

### Requisitos

* Python versão 2.7.15

### Configuração

Antes de executar o cliente é necessário configurar os servidores disponíveis. Para isso há o arquivo **servers.txt** que armazenará todos os servidores conhecidos. Cada linha do arquivo corresponde às informação de um servidor. 
A linha é estruturada da seguinte ordem: *Nome, Endereço, Porta*

### Execução

Comando para executar o servidor:

    python server.py
* Após a execução será solicitado a porta do socket do servidor.

Comando para executar o cliente:

    python cliente.py

## Autores

* [Helena Dalmazo](https://github.com/nefasta)
* [Matheus Queiroz](https://github.com/Matheusqz)
