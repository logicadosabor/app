# Documentação de Implantação e Uso

Este documento fornece instruções detalhadas para implantação e uso do Sistema de Monitoramento de Boas Práticas na Higienização de Vegetais do Restaurante Lógica do Sabor.

## 1. Requisitos de Sistema

### 1.1 Servidor
- Sistema operacional: Linux (Ubuntu 20.04 LTS ou superior recomendado)
- Python 3.11 ou superior
- Node.js 20.x ou superior
- MySQL 8.0 ou superior
- Servidor web (Nginx recomendado)

### 1.2 Clientes (Dispositivos de Acesso)
- Navegadores modernos (Chrome, Firefox, Safari, Edge - últimas versões)
- Resolução mínima recomendada: 1280x720
- Suporte a dispositivos móveis (tablets e smartphones)

## 2. Instruções de Implantação

### 2.1 Configuração do Banco de Dados
1. Criar banco de dados MySQL:
```sql
CREATE DATABASE logica_do_sabor CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
CREATE USER 'logica_user'@'localhost' IDENTIFIED BY 'senha_segura';
GRANT ALL PRIVILEGES ON logica_do_sabor.* TO 'logica_user'@'localhost';
FLUSH PRIVILEGES;
```

2. Configurar variáveis de ambiente para conexão:
```bash
export DB_USERNAME=logica_user
export DB_PASSWORD=senha_segura
export DB_HOST=localhost
export DB_PORT=3306
export DB_NAME=logica_do_sabor
```

### 2.2 Implantação do Backend
1. Clonar o repositório:
```bash
git clone https://github.com/logica-do-sabor/sistema-higienizacao.git
cd sistema-higienizacao/backend
```

2. Criar e ativar ambiente virtual:
```bash
python -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate
```

3. Instalar dependências:
```bash
pip install -r requirements.txt
```

4. Configurar variáveis de ambiente adicionais:
```bash
export SECRET_KEY="chave_secreta_gerada_aleatoriamente"
export ACCESS_TOKEN_EXPIRE_MINUTES=30
```

5. Iniciar o servidor:
```bash
cd src
uvicorn main:app --host 0.0.0.0 --port 8000
```

6. Para produção, configurar com Gunicorn:
```bash
gunicorn -w 4 -k uvicorn.workers.UvicornWorker main:app
```

### 2.3 Implantação do Frontend
1. Navegar para o diretório do frontend:
```bash
cd ../frontend
```

2. Instalar dependências:
```bash
npm install
```

3. Configurar variável de ambiente para API:
```bash
echo "REACT_APP_API_URL=http://seu-servidor:8000" > .env
```

4. Construir para produção:
```bash
npm run build
```

5. Configurar Nginx para servir os arquivos estáticos:
```nginx
server {
    listen 80;
    server_name seu-dominio.com;

    location / {
        root /caminho/para/frontend/build;
        try_files $uri /index.html;
    }

    location /api {
        proxy_pass http://localhost:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }
}
```

### 2.4 Configuração Inicial do Sistema
1. Criar usuário administrador inicial:
```bash
cd ../backend
source venv/bin/activate
python scripts/create_admin.py
```

2. Importar dados iniciais (opcional):
```bash
python scripts/import_initial_data.py
```

## 3. Instruções de Uso

### 3.1 Acesso ao Sistema
1. Acessar o sistema pelo navegador: `http://seu-dominio.com`
2. Fazer login com as credenciais fornecidas

### 3.2 Perfil Gerente
#### 3.2.1 Gerenciamento de Usuários
1. Acessar menu "Usuários"
2. Cadastrar novos usuários com perfil adequado (Cozinheiro ou Gerente)
3. Gerenciar usuários existentes (editar, ativar/desativar)

#### 3.2.2 Gerenciamento de Vegetais
1. Acessar menu "Vegetais"
2. Cadastrar novos vegetais a serem monitorados
3. Gerenciar vegetais existentes (editar, ativar/desativar)

#### 3.2.3 Gerenciamento de Soluções
1. Acessar menu "Soluções de Higienização"
2. Cadastrar novas soluções com parâmetros padrão
3. Gerenciar soluções existentes (editar, ativar/desativar)

#### 3.2.4 Visualização de Dashboards
1. Acessar menu "Dashboard"
2. Aplicar filtros conforme necessidade (período, vegetal, solução)
3. Analisar gráficos e indicadores de conformidade
4. Exportar relatórios quando necessário

### 3.3 Perfil Cozinheiro
#### 3.3.1 Registro de Processos
1. Acessar menu "Novo Processo"
2. Preencher formulário com dados do processo de higienização:
   - Selecionar vegetal
   - Informar quantidade/peso
   - Selecionar solução utilizada
   - Registrar detalhes da aplicação (concentração, tempo)
   - Adicionar observações se necessário
3. Enviar formulário e verificar feedback de conformidade

#### 3.3.2 Upload de Evidências
1. Após registrar processo, acessar detalhes do processo
2. Clicar em "Adicionar Evidência"
3. Selecionar foto da evidência
4. Enviar arquivo

#### 3.3.3 Consulta de Processos
1. Acessar menu "Histórico de Processos"
2. Aplicar filtros conforme necessidade
3. Visualizar detalhes de processos específicos

## 4. Manutenção do Sistema

### 4.1 Backup de Dados
1. Configurar backup automático do banco de dados:
```bash
# Adicionar ao crontab
0 2 * * * mysqldump -u logica_user -p'senha_segura' logica_do_sabor > /caminho/para/backups/backup_$(date +\%Y\%m\%d).sql
```

2. Configurar backup de evidências fotográficas:
```bash
# Adicionar ao crontab
0 3 * * * rsync -av /caminho/para/backend/static/evidencias/ /caminho/para/backups/evidencias/
```

### 4.2 Atualização do Sistema
1. Atualizar o código-fonte:
```bash
cd /caminho/para/repositorio
git pull
```

2. Atualizar dependências do backend:
```bash
cd backend
source venv/bin/activate
pip install -r requirements.txt
```

3. Atualizar dependências do frontend:
```bash
cd ../frontend
npm install
npm run build
```

4. Reiniciar serviços:
```bash
sudo systemctl restart logica-api
sudo systemctl restart nginx
```

### 4.3 Monitoramento
1. Verificar logs do backend:
```bash
tail -f /var/log/logica-api.log
```

2. Verificar logs do nginx:
```bash
tail -f /var/log/nginx/access.log
tail -f /var/log/nginx/error.log
```

## 5. Solução de Problemas Comuns

### 5.1 Problemas de Conexão com Banco de Dados
- Verificar se o serviço MySQL está em execução: `systemctl status mysql`
- Verificar configurações de conexão nas variáveis de ambiente
- Verificar permissões do usuário do banco de dados

### 5.2 Problemas de Upload de Evidências
- Verificar permissões do diretório de evidências: `chmod -R 755 /caminho/para/backend/static/evidencias`
- Verificar limites de tamanho de arquivo no nginx e na configuração do FastAPI

### 5.3 Problemas de Autenticação
- Verificar se o token JWT está sendo gerado corretamente
- Verificar se a chave secreta está configurada corretamente
- Limpar cookies e cache do navegador

## 6. Suporte e Contato

Para suporte técnico ou dúvidas sobre o sistema, entre em contato:
- Email: suporte@logicadosabor.com.br
- Telefone: (XX) XXXX-XXXX
- Horário de atendimento: Segunda a Sexta, 8h às 18h
