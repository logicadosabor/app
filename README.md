# Sistema de Monitoramento de Boas Práticas na Higienização de Vegetais

Este repositório contém o código-fonte e a documentação completa do Sistema de Monitoramento de Boas Práticas na Higienização de Vegetais desenvolvido para o Restaurante Lógica do Sabor.

## Estrutura do Projeto

```
projeto_restaurante/
├── docs/                           # Documentação completa
│   ├── estrutura_site.md           # Definição da estrutura e funcionalidades
│   ├── exigencias_sanitarias.md    # Exigências da vigilância sanitária
│   ├── implantacao_e_uso.md        # Instruções de implantação e uso
│   ├── layout_design.md            # Planejamento de layout e design visual
│   ├── plano_testes_usabilidade.md # Plano de testes de usabilidade
│   ├── selecao_template.md         # Seleção de templates e tecnologias
│   └── validacao_conformidade.md   # Validação de conformidade com normas
│
├── pesquisa/                       # Pesquisas e referências
│   └── vigilancia_sanitaria/       # Pesquisas sobre vigilância sanitária
│       ├── cartilha_boas_praticas.pdf  # Cartilha da ANVISA
│       ├── cartilha_boas_praticas.txt  # Versão texto da cartilha
│       └── exigencias_sanitarias.md    # Consolidação das exigências
│
├── src/                            # Código-fonte do sistema
│   ├── backend/                    # Backend em FastAPI
│   │   ├── src/
│   │   │   ├── models/             # Modelos de dados
│   │   │   ├── routes/             # Rotas da API
│   │   │   ├── schemas/            # Esquemas Pydantic
│   │   │   ├── utils/              # Utilitários
│   │   │   ├── api.py              # Configuração da API
│   │   │   ├── database.py         # Configuração do banco de dados
│   │   │   └── main.py             # Ponto de entrada
│   │   ├── requirements.txt        # Dependências do backend
│   │   └── venv/                   # Ambiente virtual Python
│   │
│   └── frontend/                   # Frontend em React
│       ├── public/                 # Arquivos públicos
│       ├── src/                    # Código-fonte React
│       ├── package.json            # Dependências do frontend
│       └── README.md               # Instruções específicas do frontend
```

## Documentação

### Documentação de Análise e Planejamento
- [Exigências da Vigilância Sanitária](docs/exigencias_sanitarias.md) - Consolidação das exigências sanitárias aplicáveis
- [Estrutura e Funcionalidades](docs/estrutura_site.md) - Definição da estrutura e funcionalidades do sistema
- [Layout e Design Visual](docs/layout_design.md) - Planejamento do layout e design visual
- [Seleção de Templates](docs/selecao_template.md) - Seleção de templates e tecnologias

### Documentação Técnica
- [Validação de Conformidade](docs/validacao_conformidade.md) - Validação de conformidade com normas sanitárias
- [Plano de Testes de Usabilidade](docs/plano_testes_usabilidade.md) - Plano detalhado para testes de usabilidade

### Documentação para Usuário Final
- [Implantação e Uso](docs/implantacao_e_uso.md) - Instruções detalhadas para implantação e uso do sistema

## Tecnologias Utilizadas

### Backend
- FastAPI - Framework web de alta performance
- SQLAlchemy - ORM para interação com banco de dados
- Pydantic - Validação de dados
- JWT - Autenticação e autorização
- MySQL - Banco de dados relacional

### Frontend
- React - Biblioteca JavaScript para interfaces
- TypeScript - Superset tipado de JavaScript
- Tailwind CSS - Framework CSS utilitário
- Recharts - Biblioteca de visualização de dados
- shadcn/ui - Componentes de interface

## Requisitos de Sistema

### Servidor
- Sistema operacional: Linux (Ubuntu 20.04 LTS ou superior recomendado)
- Python 3.11 ou superior
- Node.js 20.x ou superior
- MySQL 8.0 ou superior
- Servidor web (Nginx recomendado)

### Clientes (Dispositivos de Acesso)
- Navegadores modernos (Chrome, Firefox, Safari, Edge - últimas versões)
- Resolução mínima recomendada: 1280x720
- Suporte a dispositivos móveis (tablets e smartphones)

## Instalação Rápida

Consulte o documento [Implantação e Uso](docs/implantacao_e_uso.md) para instruções detalhadas de instalação e configuração.

## Conformidade

Este sistema foi desenvolvido em conformidade com a RDC 216/2004 da ANVISA e outras normas aplicáveis à segurança alimentar em restaurantes no Brasil. A documentação completa de conformidade está disponível em [Validação de Conformidade](docs/validacao_conformidade.md).

## Suporte

Para suporte técnico ou dúvidas sobre o sistema, entre em contato:
- Email: suporte@logicadosabor.com.br
- Telefone: (XX) XXXX-XXXX
- Horário de atendimento: Segunda a Sexta, 8h às 18h
