# 📅 Sistema de Calendário Interativo para Kindle

Sistema completo de calendário HTML otimizado para dispositivos Kindle com integração ao Google Calendar. Mostra seus eventos de forma elegante em uma tela e-ink com alto contraste e interface intuitiva.

---

## 🌟 Funcionalidades do Calendário HTML

### Interface Adaptável
- **Modo Paisagem**: Relógio à esquerda, eventos à direita (lado a lado)
- **Modo Retrato**: Relógio em cima, eventos embaixo (empilhados)
- Alternância entre modos com salvamento automático da preferência

### Relógio Digital
- Display grande com formato HH:MM
- Data por extenso em português (ex: "5 de Novembro")
- Dia da semana completo
- Atualização automática a cada minuto
- Tamanho ajustável (60px a 200px)

### Gerenciamento de Eventos
- **Eventos Passados**: Aparência esmaecida (40% opacidade)
- **Evento Atual**: Destaque com fundo amarelo e negrito
- **Próximos Eventos**: Fundo claro com borda cinza
- Scroll vertical para muitos eventos
- Visualização clara de título e horário (início - fim)

### Painel de Controles (⚙️)
- **Slider de Tamanho**: Ajuste o tamanho do relógio
- **Navegação Rápida**: Botões Ontem | Hoje | Amanhã
- **Seletor de Data**: Escolha qualquer dia específico
- **Modo de Layout**: Alterne entre paisagem e retrato
- Preferências salvas no navegador

### Otimizações para E-ink
- Alto contraste preto e branco
- Sem animações complexas
- Design minimalista
- Atualização suave a cada minuto

---

## 🔄 Funcionalidades do Script Python

O script `atualizar_calendario.py` automatiza a sincronização com o Google Calendar:

- ✅ Autenticação OAuth 2.0 segura
- ✅ Token salvo para execuções futuras (não precisa autenticar toda vez)
- ✅ Busca eventos dos próximos 7 dias (configurável)
- ✅ Suporta eventos com horário específico e eventos de dia inteiro
- ✅ Atualiza automaticamente o arquivo HTML
- ✅ Mensagens claras de progresso e estatísticas
- ✅ Tratamento robusto de erros
- ✅ Banner ASCII art elegante

---

## 🚀 Configuração Inicial

### 1. Instalar Dependências Python

Primeiro, instale as bibliotecas necessárias:

```bash
pip install -r requirements.txt
```

Ou manualmente:

```bash
pip install google-auth-oauthlib google-auth-httplib2 google-api-python-client
```

### 2. Criar Projeto no Google Cloud Console

1. Acesse: [Google Cloud Console](https://console.cloud.google.com/)
2. Clique em "Selecionar projeto" → "Novo Projeto"
3. Dê um nome ao projeto (ex: "Calendário Kindle")
4. Clique em "Criar"

### 3. Ativar a Google Calendar API

1. No menu lateral, vá em **APIs e Serviços** → **Biblioteca**
2. Busque por "Google Calendar API"
3. Clique em "Google Calendar API"
4. Clique no botão **"Ativar"**

### 4. Criar Credenciais OAuth 2.0

1. Vá em **APIs e Serviços** → **Credenciais**
2. Clique em **"+ Criar Credenciais"** → **"ID do cliente OAuth"**
3. Se for a primeira vez:
   - Clique em "Configurar tela de consentimento"
   - Escolha **"Externo"** → Clique em "Criar"
   - Preencha apenas os campos obrigatórios:
     - Nome do app: "Calendário Kindle"
     - E-mail de suporte: seu e-mail
     - E-mail do desenvolvedor: seu e-mail
   - Clique em "Salvar e continuar" até finalizar
   - Em "Usuários de teste", adicione seu e-mail do Google
4. Volte para **Credenciais** → **"+ Criar Credenciais"** → **"ID do cliente OAuth"**
5. Tipo de aplicativo: **"App para computador"**
6. Nome: "Calendário Kindle Desktop"
7. Clique em **"Criar"**

### 5. Baixar Credenciais

1. Na lista de IDs do cliente OAuth 2.0, localize o que você criou
2. Clique no ícone de **download** (seta para baixo) à direita
3. Salve o arquivo JSON baixado
4. **Renomeie o arquivo para `credentials.json`**
5. **Coloque na mesma pasta dos scripts** (`/home/pedro/kindle/`)

---

## 🎯 Primeira Execução

### Executar o Script

**Linux/Mac:**
```bash
python3 atualizar_calendario.py
```

**Windows:**
```bash
python atualizar_calendario.py
```

Ou simplesmente execute o script de atalho:
- **Windows**: Clique duas vezes em `atualizar_calendario.bat`
- **Linux/Mac**: Execute `./atualizar_calendario.sh`

### Processo de Autenticação (Primeira Vez)

1. Uma janela do navegador será aberta automaticamente
2. Faça login com sua conta Google
3. Você verá um aviso "Este app não foi verificado pelo Google"
   - Clique em **"Avançado"**
   - Clique em **"Ir para Calendário Kindle (não seguro)"**
4. Autorize o acesso ao calendário (apenas leitura)
5. Você verá "A autenticação foi bem-sucedida"
6. Feche a janela do navegador
7. O script continuará automaticamente

### O que Acontece

- O script cria um arquivo `token.json` com suas credenciais
- Busca eventos dos próximos 7 dias do seu Google Calendar
- Atualiza o arquivo `calendario.html` com os eventos
- Mostra estatísticas de quantos eventos foram adicionados

**Nas próximas execuções**, o script usará o `token.json` salvo e não pedirá autenticação novamente!

---

## 📱 Usar no Kindle

### Transferir o Arquivo

1. Conecte seu Kindle ao computador via USB
2. Copie o arquivo `calendario.html` para a pasta `documents` do Kindle
3. Ejete o Kindle com segurança

### Abrir no Kindle

1. No Kindle, pressione o botão **Menu** ou toque nos três pontos
2. Vá em **"Navegador Web Experimental"** ou **"Web Browser"**
3. Digite na barra de endereços:
   ```
   file:///mnt/us/documents/calendario.html
   ```
   Ou navegue pelos favoritos se já tiver adicionado

4. Adicione aos favoritos para acesso rápido!

### Dica: Atalho Rápido

1. Abra o arquivo pela primeira vez usando o caminho acima
2. Toque no ícone de **estrela** ou **favoritos**
3. Salve com nome "📅 Calendário"
4. Nas próximas vezes, basta acessar pelos favoritos!

---

## ⚙️ Atualização dos Eventos

### Atualização Manual

Execute o script sempre que quiser atualizar os eventos:

**Linux/Mac:**
```bash
./atualizar_calendario.sh
```

**Windows:**
```
atualizar_calendario.bat
```

Depois, copie o arquivo `calendario.html` atualizado para o Kindle novamente.

### Atualização Automática

#### Linux/Mac (Crontab)

Para executar automaticamente todos os dias às 6h da manhã:

1. Edite o crontab:
   ```bash
   crontab -e
   ```

2. Adicione a linha (substitua o caminho pelo caminho completo do seu projeto):
   ```
   0 6 * * * cd /home/pedro/kindle && /usr/bin/python3 atualizar_calendario.py
   ```

3. Salve e feche

**Outros horários úteis:**
- `0 */4 * * *` - A cada 4 horas
- `0 8,20 * * *` - Às 8h e 20h
- `*/30 * * * *` - A cada 30 minutos

#### Windows (Agendador de Tarefas)

1. Pressione `Win + R`, digite `taskschd.msc` e pressione Enter
2. Clique em **"Criar Tarefa Básica"**
3. Nome: "Atualizar Calendário Kindle"
4. Gatilho: "Diariamente" → Escolha o horário (ex: 06:00)
5. Ação: "Iniciar um programa"
6. Programa/script: Navegue e selecione `atualizar_calendario.bat`
7. Inicie em: Pasta do projeto (`C:\Users\SeuUsuario\kindle\`)
8. Marque "Abrir a caixa de diálogo Propriedades..."
9. Em Propriedades, vá em "Configurações" e desmarque "Parar se execução durar mais de 3 dias"
10. Clique OK

---

## 🎮 Usando os Controles do Site

### Abrir Painel de Controles

- Toque no botão **⚙️** no canto superior esquerdo
- O painel se abrirá com todas as opções
- Toque fora do painel para fechá-lo

### Ajustar Tamanho do Relógio

- Arraste o slider de "Tamanho do Relógio"
- Veja o valor em tempo real (60px a 200px)
- O tamanho é salvo automaticamente

### Navegar Entre Dias

**Seleção Rápida:**
- Toque em **"Ontem"** para ver eventos de ontem
- Toque em **"Hoje"** para voltar ao dia atual
- Toque em **"Amanhã"** para ver eventos de amanhã

**Data Específica:**
- Toque no campo de data
- Escolha qualquer dia no calendário
- Os eventos daquele dia serão exibidos

### Alternar Modo de Layout

- Toque em **"Paisagem"** para layout lado a lado
- Toque em **"Retrato"** para layout empilhado
- A preferência é salva automaticamente

---

## 💡 Dicas para o Kindle

### Otimização da Tela E-ink

- A tela e-ink atualiza lentamente - seja paciente ao tocar nos botões
- Evite toques rápidos múltiplos
- O relógio atualiza automaticamente a cada minuto

### Economia de Bateria

- O calendário é estático (sem animações pesadas)
- Feche o navegador quando não estiver usando
- Considere atualizar eventos apenas uma vez por dia

### Melhor Experiência

- **Kindle com tela maior**: Use modo paisagem
- **Kindle com tela pequena**: Use modo retrato
- Ajuste o tamanho do relógio conforme preferência
- Mantenha o brilho da tela confortável

---

## 🔧 Personalizações Possíveis

### Alterar Período de Busca

Edite o arquivo `atualizar_calendario.py`:

```python
DIAS_FUTUROS = 7  # Altere para 14, 30, etc.
```

### Usar Calendário Específico

Por padrão, o script busca do calendário principal. Para usar outro:

1. Abra `atualizar_calendario.py`
2. Encontre a linha:
   ```python
   calendarId='primary',
   ```
3. Substitua `'primary'` pelo ID do calendário desejado
   - Você pode encontrar o ID em: Google Calendar → Configurações → [Seu Calendário] → "Integrar calendário"

### Personalizar Cores no HTML

Edite `calendario.html` na seção `<style>`:

```css
/* Exemplo: Mudar cor do evento atual */
.evento.atual {
    background: #e6f7ff;  /* Azul claro em vez de amarelo */
}
```

---

## 🐛 Troubleshooting

### Erro: "credentials.json não encontrado"

**Solução:** Siga a seção "Configuração Inicial" acima e crie as credenciais OAuth.

### Erro: "token.json inválido" ou "erro de autenticação"

**Solução:**
1. Delete o arquivo `token.json`
2. Execute o script novamente
3. Faça a autenticação no navegador

### Nenhum evento aparece

**Possíveis causas:**
- Seu calendário Google está vazio no período
- Você não autorizou o acesso corretamente
- O calendário correto não está selecionado

**Solução:**
1. Verifique se há eventos no Google Calendar web
2. Execute o script novamente e veja as mensagens
3. Verifique se autorizou o acesso na primeira execução

### HTML não abre no Kindle

**Solução:**
- Verifique se o arquivo está na pasta correta (`documents`)
- Tente o caminho completo: `file:///mnt/us/documents/calendario.html`
- Alguns modelos de Kindle mais antigos podem ter navegadores limitados

### Eventos não atualizam no Kindle

**Solução:**
- Execute o script para atualizar o `calendario.html`
- Copie o arquivo atualizado para o Kindle novamente
- No navegador do Kindle, recarregue a página (Menu → Reload/Atualizar)

### Script demora muito ou trava

**Solução:**
- Reduza o número de dias: `DIAS_FUTUROS = 3`
- Verifique sua conexão com a internet
- Verifique se o Google Calendar API está ativo

---

## 📁 Arquivos do Projeto

```
kindle/
├── calendario.html              # Página HTML interativa (arquivo principal)
├── atualizar_calendario.py      # Script Python para sincronização
├── atualizar_calendario.bat     # Atalho para Windows
├── atualizar_calendario.sh      # Atalho para Linux/Mac
├── requirements.txt             # Dependências Python
├── README.md                    # Este arquivo
├── credentials.json             # Credenciais OAuth (você cria)
└── token.json                   # Token salvo (gerado automaticamente)
```

**Arquivos que você cria:**
- `credentials.json` - Baixado do Google Cloud Console

**Arquivos gerados automaticamente:**
- `token.json` - Criado na primeira autenticação

---

## 📝 Notas Importantes

### Segurança

- **Nunca compartilhe** os arquivos `credentials.json` ou `token.json`
- Esses arquivos contêm acesso à sua conta Google
- Mantenha-os em local seguro
- Adicione ao `.gitignore` se usar controle de versão

### Privacidade

- O script acessa apenas seus eventos do calendário (leitura)
- Não modifica, deleta ou compartilha seus dados
- Funciona completamente offline após sincronização

### Limitações

- O Kindle não atualiza eventos automaticamente (requer execução manual do script e cópia do arquivo)
- A tela e-ink tem taxa de atualização limitada
- Navegadores de Kindle têm recursos limitados comparados a navegadores modernos

---

## 🎉 Pronto para Usar!

Agora você tem um calendário completo e funcional otimizado para Kindle com sincronização automática do Google Calendar!

**Fluxo de uso diário:**

1. **Uma vez por dia** (ou configure automação):
   - Execute `atualizar_calendario.py`
   - Copie `calendario.html` para o Kindle

2. **No Kindle**:
   - Abra o calendário pelos favoritos
   - Use os controles para navegar entre dias
   - Veja seus eventos atualizados em tempo real

**Dúvidas ou problemas?** Consulte a seção de Troubleshooting acima!

---

**Desenvolvido com ❤️ para produtividade no Kindle**
