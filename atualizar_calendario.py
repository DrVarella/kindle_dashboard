#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script para atualizar o calendário HTML com eventos do Google Calendar
Autor: Sistema de Calendário Kindle
Data: 2025
"""

import os
import json
import re
from datetime import datetime, timedelta
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# Escopos necessários para acessar o Google Calendar (apenas leitura)
SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']

# Arquivos de credenciais
CREDENTIALS_FILE = 'credentials.json'
TOKEN_FILE = 'token.json'
HTML_FILE = 'calendario.html'


def exibir_banner():
    """Exibe banner ASCII art do programa"""
    banner = """
    ╔═══════════════════════════════════════════════════════════╗
    ║                                                           ║
    ║        📅  ATUALIZADOR DE CALENDÁRIO KINDLE  📅          ║
    ║                                                           ║
    ║          Sincronização com Google Calendar               ║
    ║                                                           ║
    ╚═══════════════════════════════════════════════════════════╝
    """
    print(banner)


def autenticar_google_calendar():
    """
    Autentica com o Google Calendar API usando OAuth 2.0

    Returns:
        service: Objeto de serviço do Google Calendar API
        None: Se houver erro na autenticação
    """
    print("\n[1/3] Autenticando com Google Calendar...")

    creds = None

    # Verifica se o arquivo credentials.json existe
    if not os.path.exists(CREDENTIALS_FILE):
        print(f"\n❌ ERRO: Arquivo '{CREDENTIALS_FILE}' não encontrado!")
        print("\n📋 INSTRUÇÕES PARA CRIAR O ARQUIVO:")
        print("   1. Acesse: https://console.cloud.google.com/")
        print("   2. Crie um novo projeto ou selecione um existente")
        print("   3. Ative a Google Calendar API")
        print("   4. Crie credenciais OAuth 2.0 (Aplicativo de Desktop)")
        print("   5. Baixe o arquivo JSON e renomeie para 'credentials.json'")
        print("   6. Coloque o arquivo na mesma pasta deste script\n")
        print("📖 Consulte o README.md para instruções detalhadas!\n")
        return None

    # Verifica se já existe um token salvo
    if os.path.exists(TOKEN_FILE):
        creds = Credentials.from_authorized_user_file(TOKEN_FILE, SCOPES)

    # Se não há credenciais válidas, faz o login
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            print("   → Atualizando token de autenticação...")
            creds.refresh(Request())
        else:
            print("   → Iniciando processo de autenticação OAuth...")
            print("   → Uma janela do navegador será aberta")
            print("   → Faça login com sua conta Google e autorize o acesso\n")

            try:
                flow = InstalledAppFlow.from_client_secrets_file(
                    CREDENTIALS_FILE, SCOPES)
                creds = flow.run_local_server(port=0)
            except Exception as e:
                print(f"\n❌ ERRO durante autenticação: {e}")
                return None

        # Salva as credenciais para a próxima execução
        with open(TOKEN_FILE, 'w') as token:
            token.write(creds.to_json())
        print("   ✅ Token salvo com sucesso!")
    else:
        print("   ✅ Autenticação válida encontrada!")

    try:
        service = build('calendar', 'v3', credentials=creds)
        print("   ✅ Conectado ao Google Calendar API\n")
        return service
    except HttpError as error:
        print(f'\n❌ Erro ao conectar com a API: {error}\n')
        return None


def buscar_eventos(service, dias=7):
    """
    Busca eventos do Google Calendar

    Args:
        service: Objeto de serviço do Google Calendar API
        dias: Número de dias futuros para buscar eventos

    Returns:
        dict: Dicionário com eventos organizados por data
              Formato: {"YYYY-MM-DD": [{"titulo": "...", "inicio": "HH:MM", "fim": "HH:MM"}]}
    """
    print(f"[2/3] Buscando eventos dos próximos {dias} dias...")

    # Define período de busca
    agora = datetime.utcnow()
    data_inicio = agora.isoformat() + 'Z'  # 'Z' indica UTC
    data_fim = (agora + timedelta(days=dias)).isoformat() + 'Z'

    eventos_por_data = {}
    total_eventos = 0

    try:
        # Busca eventos do calendário principal
        print("   → Consultando Google Calendar API...")
        eventos_result = service.events().list(
            calendarId='primary',
            timeMin=data_inicio,
            timeMax=data_fim,
            maxResults=100,
            singleEvents=True,
            orderBy='startTime'
        ).execute()

        eventos = eventos_result.get('items', [])

        if not eventos:
            print("   ⚠️  Nenhum evento encontrado no período\n")
            return eventos_por_data

        print(f"   ✅ {len(eventos)} evento(s) encontrado(s)")
        print("   → Processando eventos...\n")

        # Processa cada evento
        for evento in eventos:
            titulo = evento.get('summary', 'Sem título')

            # Pega data/hora de início
            inicio = evento['start'].get('dateTime', evento['start'].get('date'))
            fim = evento['end'].get('dateTime', evento['end'].get('date'))

            # Se for evento de dia inteiro (sem hora específica)
            if 'T' not in inicio:
                data_str = inicio
                hora_inicio = "00:00"
                hora_fim = "23:59"
                titulo = f"⭐ {titulo}"  # Marca eventos de dia inteiro
            else:
                # Converte para o fuso horário local
                dt_inicio = datetime.fromisoformat(inicio.replace('Z', '+00:00'))
                dt_fim = datetime.fromisoformat(fim.replace('Z', '+00:00'))

                data_str = dt_inicio.strftime('%Y-%m-%d')
                hora_inicio = dt_inicio.strftime('%H:%M')
                hora_fim = dt_fim.strftime('%H:%M')

            # Adiciona evento ao dicionário
            if data_str not in eventos_por_data:
                eventos_por_data[data_str] = []

            eventos_por_data[data_str].append({
                'titulo': titulo,
                'inicio': hora_inicio,
                'fim': hora_fim
            })

            total_eventos += 1
            print(f"      • {data_str} | {hora_inicio}-{hora_fim} | {titulo}")

        print(f"\n   ✅ Total: {total_eventos} eventos em {len(eventos_por_data)} dia(s)\n")

    except HttpError as error:
        print(f'\n❌ Erro ao buscar eventos: {error}\n')
        return {}

    return eventos_por_data


def atualizar_html(eventos_por_data, html_file=HTML_FILE):
    """
    Atualiza o arquivo HTML com os novos eventos

    Args:
        eventos_por_data: Dicionário com eventos organizados por data
        html_file: Caminho do arquivo HTML

    Returns:
        bool: True se atualizado com sucesso, False caso contrário
    """
    print(f"[3/3] Atualizando arquivo {html_file}...")

    # Verifica se o arquivo HTML existe
    if not os.path.exists(html_file):
        print(f"\n❌ ERRO: Arquivo '{html_file}' não encontrado!")
        print("   Certifique-se de que o arquivo HTML está na mesma pasta.\n")
        return False

    try:
        # Lê o arquivo HTML
        print("   → Lendo arquivo HTML...")
        with open(html_file, 'r', encoding='utf-8') as f:
            conteudo_html = f.read()

        # Converte eventos para formato JSON
        eventos_json = json.dumps(eventos_por_data, ensure_ascii=False, indent=12)

        # Padrão regex para encontrar o objeto eventosData
        # Procura por: const eventosData = {...};
        padrao = r'const eventosData = \{[^}]*(?:\{[^}]*\}[^}]*)*\};'

        # Substitui o objeto eventosData pelos novos dados
        novo_codigo = f'const eventosData = {eventos_json};'

        conteudo_atualizado = re.sub(
            padrao,
            novo_codigo,
            conteudo_html,
            flags=re.DOTALL
        )

        # Verifica se a substituição foi feita
        if conteudo_atualizado == conteudo_html:
            print("\n⚠️  AVISO: Não foi possível localizar 'const eventosData' no HTML")
            print("   O arquivo pode estar em formato diferente do esperado.\n")
            return False

        # Salva o arquivo atualizado
        print("   → Salvando arquivo atualizado...")
        with open(html_file, 'w', encoding='utf-8') as f:
            f.write(conteudo_atualizado)

        print("   ✅ Arquivo HTML atualizado com sucesso!\n")

        # Exibe estatísticas
        print("   📊 ESTATÍSTICAS:")
        print(f"      • Total de dias com eventos: {len(eventos_por_data)}")
        for data, eventos in sorted(eventos_por_data.items()):
            data_formatada = datetime.strptime(data, '%Y-%m-%d').strftime('%d/%m/%Y')
            print(f"      • {data_formatada}: {len(eventos)} evento(s)")
        print()

        return True

    except Exception as e:
        print(f"\n❌ ERRO ao atualizar HTML: {e}\n")
        return False


def main():
    """Função principal que orquestra todo o processo"""
    exibir_banner()

    # Passo 1: Autenticar
    service = autenticar_google_calendar()
    if not service:
        print("❌ Falha na autenticação. Encerrando.\n")
        return

    # Passo 2: Buscar eventos (próximos 7 dias - pode ser alterado)
    DIAS_FUTUROS = 7  # Altere aqui para buscar mais ou menos dias
    eventos = buscar_eventos(service, dias=DIAS_FUTUROS)

    if not eventos:
        print("⚠️  Nenhum evento para atualizar.\n")
        # Mesmo sem eventos, pode querer limpar eventos antigos
        resposta = input("Deseja atualizar o HTML mesmo sem eventos? (s/n): ")
        if resposta.lower() != 's':
            print("\nOperação cancelada.\n")
            return

    # Passo 3: Atualizar HTML
    sucesso = atualizar_html(eventos)

    if sucesso:
        print("═" * 60)
        print("✅ PROCESSO CONCLUÍDO COM SUCESSO!")
        print("═" * 60)
        print(f"\n📱 O arquivo '{HTML_FILE}' está pronto para ser usado no Kindle!")
        print("   Copie-o para o seu dispositivo e abra no navegador.\n")
    else:
        print("═" * 60)
        print("❌ PROCESSO CONCLUÍDO COM ERROS")
        print("═" * 60)
        print("\n📖 Verifique as mensagens acima e consulte o README.md\n")


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n⚠️  Operação cancelada pelo usuário.\n")
    except Exception as e:
        print(f"\n\n❌ ERRO INESPERADO: {e}\n")
        print("📖 Consulte o README.md ou verifique os logs acima.\n")
