## GitHub LTI Tool

Esta aplicação integra o GitHub a plataformas LMS (como Moodle ou Canvas) via LTI 1.1, permitindo o vínculo de repositórios e exibição de contribuições e commits diretamente no ambiente virtual.

### Funcionalidades
- Vinculação de repositórios GitHub por usuário e atividade.
- Exibição de contribuidores e commits recentes do repositório.
- Integração LTI 1.1 (compatível com Moodle, Canvas, etc).
- Configuração dinâmica via XML (`/lti-config.xml`).

### Instalação
1. Clone o repositório:
   ```bash
   git clone <seu-repo>
   cd <seu-repo>
   ```
2. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```
3. Configure as variáveis de ambiente (crie um arquivo `.env`):
   ```env
   FLASK_SECRET_KEY=uma_chave_secreta
   LTI_KEY=key
   LTI_SECRET=secret
   DB_PATH=github_lti.db
   GITHUB_TOKEN=seu_token_github
   ```
4. Execute a aplicação:
   ```bash
   python app.py
   ```

### Configuração LTI
- O campo `url` será `https://<seu-dominio>/launch`.

### Observações
- O banco de dados SQLite será criado automaticamente.
- O token do GitHub pode ser gerado em https://github.com/settings/tokens (apenas permissão pública é suficiente).
- Para produção, utilize HTTPS e configure variáveis de ambiente seguras.

