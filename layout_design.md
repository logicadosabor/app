# Layout e Design Visual do Sistema

Este documento detalha o planejamento do layout e design visual do Sistema de Monitoramento de Boas Práticas na Higienização de Vegetais para o Restaurante Lógica do Sabor.

## 1. Princípios de Design

### 1.1 Identidade Visual
- **Paleta de Cores**: 
  - **Primária**: Verde (#2E7D32) - Representa frescor e alimentos saudáveis
  - **Secundária**: Azul (#1565C0) - Representa limpeza e higiene
  - **Terciária**: Laranja (#F57C00) - Representa energia e atenção
  - **Neutras**: Cinza claro (#F5F5F5), Cinza médio (#9E9E9E), Cinza escuro (#424242)
  - **Alertas**: Vermelho (#D32F2F), Amarelo (#FFC107), Verde claro (#4CAF50)

- **Tipografia**:
  - **Títulos**: Inter (sans-serif), peso 600-700
  - **Corpo de texto**: Inter (sans-serif), peso 400-500
  - **Dados e métricas**: Roboto Mono (monospace) para melhor alinhamento de números

- **Iconografia**:
  - Conjunto consistente de ícones Lucide
  - Ícones simples e reconhecíveis para funções principais
  - Uso de ícones específicos para cada tipo de vegetal e solução

### 1.2 Princípios de Usabilidade
- **Clareza**: Informações apresentadas de forma direta e compreensível
- **Consistência**: Padrões visuais e interativos mantidos em todo o sistema
- **Feedback**: Respostas visuais claras para todas as ações do usuário
- **Eficiência**: Tarefas comuns realizáveis com o mínimo de cliques
- **Acessibilidade**: Contraste adequado, tamanhos de fonte ajustáveis, suporte a leitores de tela

## 2. Layout das Páginas Principais

### 2.1 Estrutura Geral
- **Cabeçalho**: Logo, título do sistema, menu de navegação principal, perfil do usuário
- **Barra Lateral**: Navegação contextual, filtros rápidos, acesso a funções frequentes
- **Área de Conteúdo**: Conteúdo principal da página atual
- **Rodapé**: Informações de copyright, links úteis, versão do sistema

### 2.2 Página de Login
- Layout centralizado e minimalista
- Logo do restaurante em destaque
- Campos para usuário e senha com validação visual
- Opção "Esqueci minha senha"
- Mensagens de erro claras e específicas

### 2.3 Dashboard Principal
- **Cabeçalho**: Título da página, filtros globais (período, vegetal, solução, responsável)
- **Resumo**: Cards com KPIs principais (total de processos, conformidade, vegetais processados)
- **Gráficos Principais**: 2-3 gráficos mais relevantes em destaque
- **Navegação para Gráficos**: Acesso rápido aos 12 gráficos específicos
- **Atividade Recente**: Lista dos últimos processos registrados

### 2.4 Formulário de Registro de Processo
- Layout em etapas para facilitar o preenchimento
- Campos agrupados logicamente:
  - Informações básicas (data, responsável)
  - Seleção de vegetais (com imagens para identificação rápida)
  - Detalhes da higienização (solução, concentração, tempo)
  - Observações e evidências
- Validação em tempo real com feedback visual
- Botões de ação claros (Salvar, Cancelar, Rascunho)

### 2.5 Visualização de Gráficos
- Layout flexível para acomodar diferentes tipos de gráficos
- Área de filtros específicos para cada gráfico
- Legendas claras e informativas
- Opções de exportação (PNG, PDF, dados brutos)
- Tooltips detalhados ao passar o mouse sobre elementos do gráfico

### 2.6 Tabela de Dados
- Layout de tabela responsiva com paginação
- Cabeçalhos fixos durante rolagem
- Opções de ordenação por coluna
- Filtros avançados com opções de busca textual
- Ações contextuais por linha (visualizar detalhes, editar, etc.)

### 2.7 Documentação (Manual e POPs)
- Layout de documento com índice lateral fixo
- Conteúdo bem estruturado com títulos hierárquicos
- Destaques para informações importantes
- Ilustrações e diagramas explicativos
- Opção de impressão formatada

## 3. Componentes de Interface

### 3.1 Componentes de Navegação
- **Menu Principal**: Horizontal no topo, com ícones e texto
- **Menu Lateral**: Expansível/retrátil, com categorias e subcategorias
- **Breadcrumbs**: Indicação clara da localização atual na hierarquia do site
- **Tabs**: Para alternar entre visualizações relacionadas
- **Paginação**: Para navegar entre páginas de resultados

### 3.2 Componentes de Entrada de Dados
- **Campos de Texto**: Com validação visual e mensagens de erro
- **Seletores**: Dropdowns, radio buttons, checkboxes conforme apropriado
- **Datepickers**: Para seleção de datas e períodos
- **Sliders**: Para valores numéricos em intervalos
- **Upload de Arquivos**: Para evidências fotográficas

### 3.3 Componentes de Visualização
- **Cards**: Para informações resumidas e KPIs
- **Tabelas**: Para dados tabulares com ordenação e filtragem
- **Gráficos**: Diversos tipos conforme especificado (barras, linhas, KDE, etc.)
- **Badges**: Para indicadores de status (conformidade, pendências)
- **Tooltips**: Para informações contextuais adicionais

### 3.4 Componentes de Feedback
- **Toasts**: Notificações temporárias para ações concluídas
- **Modais**: Para confirmações e ações importantes
- **Spinners**: Indicadores de carregamento
- **Mensagens de Erro/Sucesso**: Formatadas de forma consistente
- **Indicadores de Progresso**: Para processos multi-etapas

## 4. Responsividade e Adaptação

### 4.1 Breakpoints
- **Mobile**: 320px - 480px
- **Tablet**: 481px - 768px
- **Desktop pequeno**: 769px - 1024px
- **Desktop médio**: 1025px - 1200px
- **Desktop grande**: 1201px+

### 4.2 Adaptações por Dispositivo
- **Mobile**:
  - Menu principal convertido em menu hambúrguer
  - Gráficos simplificados e empilhados verticalmente
  - Tabelas com scroll horizontal ou visualização alternativa
  - Formulários com campos em tela cheia

- **Tablet**:
  - Layout híbrido com elementos reorganizados
  - Gráficos redimensionados para melhor visualização
  - Menus laterais retráteis

- **Desktop**:
  - Layout completo com múltiplas colunas
  - Visualização lado a lado de informações relacionadas
  - Uso completo do espaço disponível para gráficos e tabelas

## 5. Protótipos de Telas Principais

### 5.1 Wireframes de Baixa Fidelidade
Serão desenvolvidos wireframes para as seguintes telas:
- Login
- Dashboard principal
- Formulário de registro de processo
- Visualização de gráficos específicos
- Tabela de dados com filtros
- Documentação (Manual e POPs)

### 5.2 Mockups de Alta Fidelidade
Após aprovação dos wireframes, serão desenvolvidos mockups detalhados para:
- Todas as telas principais
- Estados de componentes (hover, active, disabled)
- Versões responsivas (mobile, tablet, desktop)
- Fluxos de interação completos

## 6. Guia de Estilo e Componentes

### 6.1 Documentação de Componentes
- Biblioteca de componentes reutilizáveis
- Especificações de espaçamento e alinhamento
- Variações de componentes para diferentes contextos
- Estados e comportamentos interativos

### 6.2 Diretrizes de Implementação
- Uso consistente de classes CSS
- Nomenclatura padronizada
- Hierarquia de estilos
- Acessibilidade (WCAG 2.1 AA)

## 7. Considerações Específicas para o Contexto

### 7.1 Ambiente de Cozinha
- Interface resistente a toques com mãos úmidas (botões maiores)
- Alto contraste para visualização em ambientes com iluminação variável
- Opção de modo simplificado para registro rápido durante períodos de movimento intenso
- Compatibilidade com tablets resistentes à água

### 7.2 Visualização de Dados para Gerência
- Dashboards impressos automaticamente formatados
- Exportação de relatórios em formatos padrão (PDF, Excel)
- Visualizações comparativas para análise de tendências
- Alertas visuais para desvios significativos

### 7.3 Conformidade com Vigilância Sanitária
- Destaque visual para campos obrigatórios por lei
- Indicadores claros de conformidade/não-conformidade
- Acesso rápido à documentação regulatória
- Formatação de relatórios conforme exigências legais
