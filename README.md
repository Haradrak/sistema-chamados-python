# sistema-chamados-python
Sistema de Chamados com Python e SQLite

Este projeto simula um sistema básico de Service Desk, permitindo o gerenciamento de chamados com persistência de dados.

Funcionalidades

Criação de chamados
Listagem de chamados
Filtro de chamados abertos
Fechamento de chamados
Definição de prioridade (Baixa, Média, Alta)
Registro de data e hora

Tecnologias utilizadas
Python 3
SQLite (banco de dados local)

Como executar
1. Certifique-se de ter o Python instalado
2. Execute o script: python chamados.py

O banco de dados será criado automaticamente na primeira execução.

Como funciona
O sistema utiliza SQLite para armazenar os chamados em um banco local (chamados.db).

Cada chamado possui:
ID (gerado automaticamente)
Título
Status (aberto/fechado)
Prioridade
Data de criação

O usuário interage via terminal através de um menu com opções para:
Criar novos chamados
Visualizar registros
Filtrar chamados abertos
Atualizar status para fechado

Objetivo do projeto

Demonstrar conceitos de:
Persistência de dados
Operações CRUD (Create, Read, Update)
Estruturação de lógica de sistemas
Simulação de fluxo de atendimento técnico

Estrutura do banco

Tabela: chamados

| Campo        | Tipo    | Descrição              |
| ------------ | ------- | ---------------------- |
| id           | INTEGER | Identificador único    |
| titulo       | TEXT    | Descrição do chamado   |
| status       | TEXT    | Aberto ou fechado      |
| prioridade   | TEXT    | Baixa, Média ou Alta   |
| data_criacao | TEXT    | Data e hora de criação |

Possíveis melhorias
Interface gráfica (GUI)
API para integração com outros sistemas
Sistema de autenticação de usuários
Dashboard de métricas
