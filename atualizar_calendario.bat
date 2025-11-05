@echo off
chcp 65001 > nul
:: Script de atalho para atualizar o calendário Kindle no Windows
:: Autor: Sistema de Calendário Kindle

echo.
echo ════════════════════════════════════════════════════════════
echo      📅  ATUALIZADOR DE CALENDÁRIO KINDLE  📅
echo ════════════════════════════════════════════════════════════
echo.

:: Navega para o diretório do script
cd /d "%~dp0"

echo [*] Iniciando atualização do calendário...
echo.

:: Executa o script Python
python atualizar_calendario.py

:: Verifica se houve erro
if %ERRORLEVEL% NEQ 0 (
    echo.
    echo ═══════════════════════════════════════════════════════════
    echo ❌ ERRO: O script Python encontrou um problema!
    echo ═══════════════════════════════════════════════════════════
    echo.
    echo Possíveis causas:
    echo   - Python não está instalado ou não está no PATH
    echo   - Dependências não foram instaladas (execute: pip install -r requirements.txt^)
    echo   - Arquivo credentials.json não foi configurado
    echo.
    echo Consulte o README.md para instruções detalhadas.
    echo.
    pause
    exit /b %ERRORLEVEL%
)

echo.
echo ════════════════════════════════════════════════════════════
echo ✅ Script finalizado!
echo ════════════════════════════════════════════════════════════
echo.
echo 📱 Próximos passos:
echo    1. Conecte o Kindle ao computador via USB
echo    2. Copie o arquivo 'calendario.html' para a pasta 'documents' do Kindle
echo    3. Ejete o Kindle com segurança
echo    4. Abra o arquivo no navegador do Kindle
echo.

:: Aguarda 5 segundos antes de fechar
echo [*] Esta janela fechará em 5 segundos...
timeout /t 5 /nobreak > nul
