# Estrutura e Funcionalidades do Site

Este documento define a estrutura e as funcionalidades do site para o Sistema de Monitoramento de Boas Práticas na Higienização de Vegetais do Restaurante Lógica do Sabor, com base nas diretrizes do projeto e nas exigências da vigilância sanitária brasileira.

## 1. Visão Geral do Sistema

O sistema será uma aplicação web completa que permitirá o registro, acompanhamento e visualização de dados referentes aos processos de higienização de vegetais, demonstrando a aplicação de boas práticas na minoração de agrotóxicos e garantindo conformidade com as exigências da vigilância sanitária.

## 2. Arquitetura do Sistema

### 2.1 Frontend
- **Tecnologia**: React com Hooks e Context API para gerenciamento de estado
- **Bibliotecas de Gráficos**: Recharts para visualização de dados
- **Estilização**: Tailwind CSS para design responsivo
- **Componentes**: shadcn/ui para interface consistente
- **Ícones**: Lucide icons

### 2.2 Backend
- **Tecnologia**: FastAPI (Python)
- **Validação de Dados**: Pydantic
- **ORM**: SQLAlchemy
- **Migrações**: Alembic
- **Autenticação**: JWT (JSON Web Tokens)

### 2.3 Banco de Dados
- **Tecnologia**: PostgreSQL
- **Backup**: Estratégia de backup automático diário

## 3. Estrutura de Páginas e Módulos

### 3.1 Módulo de Autenticação
- **Página de Login**: Acesso seguro com autenticação de usuários
- **Recuperação de Senha**: Fluxo para redefinição de senha
- **Gerenciamento de Perfil**: Atualização de dados pessoais

### 3.2 Módulo de Administração
- **Gerenciamento de Usuários**: CRUD de usuários (Cozinheiros, Gerentes)
- **Gerenciamento de Vegetais**: CRUD de vegetais monitorados
- **Gerenciamento de Soluções de Higienização**: CRUD de soluções e parâmetros
- **Configurações Gerais**: Definição de unidades de medida e parâmetros do sistema

### 3.3 Módulo de Registro de Processos
- **Formulário de Registro**: Interface intuitiva para registrar processos de higienização
- **Histórico de Registros**: Visualização e filtro de registros anteriores
- **Validação de Dados**: Alertas visuais para valores fora do padrão

### 3.4 Módulo de Dashboard e Visualização
- **Dashboard Principal**: Visão geral com KPIs e acesso aos gráficos
- **Filtros Globais**: Período, tipo de vegetal, solução, responsável
- **12 Gráficos Específicos**:
  1. KDE/Violino 1: Distribuição dos tempos de imersão por tipo de vegetal
  2. KDE/Violino 2: Distribuição dos tempos de imersão por tipo de solução
  3. KDE/Violino 3: Distribuição da concentração da solução por tipo de vegetal
  4. Barras Empilhadas 1: Frequência de uso de cada solução por tipo de vegetal
  5. Barras Empilhadas 2: Processos por cozinheiro, empilhados por tipo de solução
  6. Barras Empilhadas 3: Conformidade de tempo de imersão por vegetal
  7. Histograma Empilhado 1: Distribuição de tempos de imersão, empilhados por vegetal
  8. Histograma Empilhado 2: Distribuição de tempos de imersão, empilhados por solução
  9. Histograma Empilhado 3: Processos por dia da semana, empilhados por cozinheiro
  10. Barras Empilhadas 4: Total de vegetais processados por mês
  11. KDE/Violino 4: Comparação de tempo de imersão entre cozinheiros
  12. Barras Empilhadas 5: Percentual de utilização de cada método ao longo do tempo
- **Tabela de Dados**: Exibição paginada com filtros e exportação

### 3.5 Módulo de Documentação
- **Manual de Boas Práticas**: Documentação completa conforme RDC 216/2004
- **POPs**: Procedimentos Operacionais Padronizados
- **Guia de Higienização**: Instruções detalhadas para higienização de vegetais
- **Legislação**: Acesso às normas e regulamentos aplicáveis

### 3.6 Módulo de Alertas e Notificações
- **Alertas de Conformidade**: Notificações para processos fora dos padrões
- **Lembretes**: Avisos sobre tarefas pendentes ou periódicas

## 4. Fluxos Principais

### 4.1 Fluxo de Registro de Processo de Higienização
1. Cozinheiro acessa o sistema com suas credenciais
2. Navega até o formulário de registro de processo
3. Seleciona o(s) vegetal(is) a ser(em) higienizado(s)
4. Informa quantidade/peso aproximado
5. Seleciona solução de higienização utilizada
6. Registra detalhes da aplicação (concentração, tempo)
7. Adiciona observações e/ou evidências (opcional)
8. Sistema valida os dados e alerta sobre possíveis desvios
9. Cozinheiro confirma o registro
10. Sistema salva os dados e atualiza dashboards

### 4.2 Fluxo de Análise de Dados
1. Gerente acessa o sistema com suas credenciais
2. Navega até o dashboard principal
3. Aplica filtros conforme necessidade (período, vegetal, etc.)
4. Visualiza os gráficos e indicadores
5. Identifica padrões, tendências ou desvios
6. Acessa detalhes específicos se necessário
7. Exporta relatórios ou dados brutos para análise adicional

## 5. Modelos de Dados

### 5.1 User
- `id`: int, primary_key
- `username`: string, unique
- `hashed_password`: string
- `full_name`: string
- `role`: enum (COZINHEIRO, GERENTE)
- `is_active`: boolean

### 5.2 Vegetal
- `id`: int, primary_key
- `nome`: string, unique
- `descricao`: text, opcional
- `ativo`: boolean

### 5.3 SolucaoHigienizacao
- `id`: int, primary_key
- `nome`: string, unique
- `tipo_solucao`: enum (VINAGRE, BICARBONATO, HIPOCLORITO, AGUA, OUTRO)
- `descricao`: text, opcional
- `param_padrao_concentracao`: string
- `param_padrao_tempo_min`: int
- `param_padrao_tempo_max`: int
- `ativo`: boolean

### 5.4 ProcessoHigienizacao
- `id`: int, primary_key
- `data_hora_registro`: datetime, default now
- `user_id`: int, foreign_key to User
- `vegetal_id`: int, foreign_key to Vegetal
- `lote_identificador`: string, opcional
- `quantidade_vegetal`: float, opcional
- `unidade_quantidade`: string, opcional
- `solucao_higienizacao_id`: int, foreign_key to SolucaoHigienizacao
- `concentracao_aplicada_valor1`: float, opcional
- `concentracao_aplicada_unidade1`: string, opcional
- `concentracao_aplicada_valor2`: float, opcional
- `concentracao_aplicada_unidade2`: string, opcional
- `tempo_imersao_real_minutos`: int
- `houve_enxague_posterior`: boolean
- `observacoes`: text, opcional
- `foto_evidencia_path`: string, opcional
- `conformidade_tempo`: enum (DENTRO_PADRAO, ABAIXO_PADRAO, ACIMA_PADRAO, NAO_AVALIADO)
- `conformidade_concentracao`: enum (similar ao anterior)

## 6. Requisitos Não Funcionais

### 6.1 Usabilidade
- Interface intuitiva e fácil de usar
- Design responsivo para acesso em tablets na cozinha
- Feedback visual claro para ações do usuário
- Ajuda contextual e tooltips para orientação

### 6.2 Desempenho
- Carregamento rápido dos gráficos e listagens
- Otimização de consultas no backend
- Paginação para grandes volumes de dados

### 6.3 Segurança
- Autenticação segura com JWT
- Proteção contra XSS, CSRF e SQL Injection
- Senhas armazenadas com hash seguro
- Controle de acesso baseado em papéis

### 6.4 Manutenibilidade
- Código bem estruturado e comentado
- Documentação técnica completa
- Logs detalhados para troubleshooting

### 6.5 Escalabilidade
- Arquitetura que permita futuras expansões
- Separação clara entre frontend e backend

### 6.6 Conformidade
- Aderência total à RDC 216/2004 da ANVISA
- Suporte a todos os registros exigidos pela vigilância sanitária
