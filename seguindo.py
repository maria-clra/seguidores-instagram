import json
import random
from playwright.sync_api import sync_playwright

ARQUIVO_SEGUIDORES = "followers_1.json"
ARQUIVO_SEGUINDO = "following.json"

USUARIO_INSTAGRAM = "SEU_USUARIO"
LIMITE = 50


# =========================
# CARREGAR SEGUIDORES
# =========================

def carregar_seguidores(arquivo):
    with open(arquivo, "r", encoding="utf-8") as f:
        dados = json.load(f)

    usuarios = []

    for item in dados:
        try:
            username = item["string_list_data"][0]["value"]
            usuarios.append(username)
        except:
            pass

    return usuarios


# =========================
# CARREGAR SEGUINDO
# =========================

def carregar_seguindo(arquivo):
    with open(arquivo, "r", encoding="utf-8") as f:
        dados = json.load(f)

    usuarios = []

    lista = dados["relationships_following"]

    for item in lista:
        try:
            username = item["title"]
            usuarios.append(username)
        except:
            pass

    return usuarios


seguidores = carregar_seguidores(ARQUIVO_SEGUIDORES)
seguindo = carregar_seguindo(ARQUIVO_SEGUINDO)

alvos = sorted(list(set(seguindo) - set(seguidores)))

print(f"\n{len(alvos)} pessoas encontradas:\n")

confirmar = input("\nRemover seguidores? (s/n): ")

if confirmar.lower() != "s":
    exit()

# =========================
# PLAYWRIGHT
# =========================

with sync_playwright() as p:

    context = p.chromium.launch_persistent_context(
        user_data_dir="perfil",
        headless=False
    )

    page = context.new_page()

    page.goto(
        f"https://www.instagram.com/maclaranb/",
        wait_until="domcontentloaded"
    )

    input(
        "\nFaça login se precisar e aperte ENTER 😎\n"
    )

    # Abrir seguidores
    seguidores_botao = page.get_by_text("seguindo")

    seguidores_botao.click()

    page.wait_for_timeout(4000)

    contador = 0

    for usuario in alvos:

        if contador >= LIMITE:
            print("\nLimite atingido.")
            break

        try:

            print(f"\nProcurando: {usuario}")

            # Campo de pesquisa
            pesquisa = page.locator("input").last

            pesquisa.fill(usuario)

            page.wait_for_timeout(
                random.randint(3000, 5000)
            )

            # Botão remover
            # Primeiro remover
            remover = page.get_by_role(
                "button",
                name="Seguindo"
            ).nth(0)

            remover.click(force=True)

            page.wait_for_timeout(2000)

            # Confirmação
            confirmar_remocao = page.get_by_text(
                "Deixar de seguir"
            ).last

            confirmar_remocao.click(force=True)

            print(f"FINALIZADO: {usuario}")

            contador += 1

            # limpar pesquisa
            pesquisa.fill("")

            espera = random.randint(5000, 10000)

            print(f"Aguardando {espera/1000:.1f}s")

            page.wait_for_timeout(espera)

        except Exception as e:

            print(f"\nErro com {usuario}")
            print(e)

    print("\nFinalizado.")

    context.close()