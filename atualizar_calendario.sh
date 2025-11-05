#!/bin/bash
# Script de atalho para atualizar o calendário Kindle em Linux/Mac
# Autor: Sistema de Calendário Kindle

echo ""
echo "════════════════════════════════════════════════════════════"
echo "     📅  ATUALIZADOR DE CALENDÁRIO KINDLE  📅"
echo "════════════════════════════════════════════════════════════"
echo ""

# Navega para o diretório do script
cd "$(dirname "$0")"

echo "[*] Iniciando atualização do calendário..."
echo ""

# Tenta usar python3, se não existir tenta python
if command -v python3 &> /dev/null; then
    PYTHON_CMD="python3"
elif command -v python &> /dev/null; then
    PYTHON_CMD="python"
else
    echo "════════════════════════════════════════════════════════════"
    echo "❌ ERRO: Python não está instalado!"
    echo "════════════════════════════════════════════════════════════"
    echo ""
    echo "Por favor, instale o Python:"
    echo "  - Ubuntu/Debian: sudo apt install python3"
    echo "  - macOS: brew install python3"
    echo "  - Ou visite: https://www.python.org/downloads/"
    echo ""
    exit 1
fi

# Executa o script Python
$PYTHON_CMD atualizar_calendario.py

# Verifica se houve erro
if [ $? -ne 0 ]; then
    echo ""
    echo "════════════════════════════════════════════════════════════"
    echo "❌ ERRO: O script Python encontrou um problema!"
    echo "════════════════════════════════════════════════════════════"
    echo ""
    echo "Possíveis causas:"
    echo "  - Dependências não foram instaladas"
    echo "    Execute: pip3 install -r requirements.txt"
    echo "  - Arquivo credentials.json não foi configurado"
    echo "  - Problemas de permissão"
    echo ""
    echo "Consulte o README.md para instruções detalhadas."
    echo ""
    exit 1
fi

echo ""
echo "════════════════════════════════════════════════════════════"
echo "✅ Script finalizado!"
echo "════════════════════════════════════════════════════════════"
echo ""
echo "📱 Próximos passos:"
echo "   1. Conecte o Kindle ao computador via USB"
echo "   2. Copie o arquivo 'calendario.html' para a pasta 'documents' do Kindle"
echo "   3. Ejete o Kindle com segurança"
echo "   4. Abra o arquivo no navegador do Kindle"
echo ""

# ========================================
# AUTOMAÇÃO COM CRONTAB (Opcional)
# ========================================
# Descomente as linhas abaixo para adicionar este script ao crontab automaticamente
# Isso fará o calendário atualizar todos os dias às 6h da manhã

# SCRIPT_PATH="$(cd "$(dirname "$0")" && pwd)/$(basename "$0")"
# CRON_JOB="0 6 * * * $SCRIPT_PATH"
#
# # Verifica se o cron job já existe
# if ! crontab -l 2>/dev/null | grep -q "$SCRIPT_PATH"; then
#     echo "════════════════════════════════════════════════════════════"
#     echo "⏰ CONFIGURAR ATUALIZAÇÃO AUTOMÁTICA"
#     echo "════════════════════════════════════════════════════════════"
#     echo ""
#     echo "Deseja adicionar este script para executar automaticamente"
#     echo "todos os dias às 6h da manhã?"
#     echo ""
#     read -p "Adicionar ao crontab? (s/n): " -n 1 -r
#     echo ""
#
#     if [[ $REPLY =~ ^[SsYy]$ ]]; then
#         (crontab -l 2>/dev/null; echo "$CRON_JOB") | crontab -
#         echo "✅ Atualização automática configurada!"
#         echo "   O calendário será atualizado todos os dias às 6h."
#         echo ""
#         echo "Para remover: crontab -e (e delete a linha com este script)"
#         echo ""
#     else
#         echo "⏭️  Pulando configuração automática."
#         echo "   Você pode configurar manualmente editando este script."
#         echo ""
#     fi
# fi

exit 0
