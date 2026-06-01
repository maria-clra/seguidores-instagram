# 🧹 Instagram Followers Cleaner

Projeto em Python que utiliza automação com **Playwright** para identificar e remover automaticamente contas que não seguem de volta no Instagram.

⚠️ **Atenção:** Este projeto é apenas para fins educacionais. O uso de automação em redes sociais pode violar os termos de uso da plataforma.

---

## 🚀 Funcionalidades

* Leitura de seguidores a partir de arquivos JSON exportados do Instagram
* Comparação entre seguidores e contas seguidas
* Identificação de contas que não seguem de volta
* Automação de remoção no Instagram com Playwright
* Controle de limite de execuções para segurança
* Intervalos aleatórios para simular comportamento humano

---

## 🧠 Como funciona

O programa:

1. Lê os arquivos:

   * `followers_1.json`
   * `following.json`

2. Constrói listas de:

   * Seguidores
   * Seguindo

3. Calcula:

```python
seguindo - seguidores
```

4. Abre o Instagram automaticamente com Playwright

5. Remove os perfis encontrados (até o limite definido)

---

## 🛠️ Tecnologias utilizadas

* Python 🐍
* Playwright
* JSON
* Random
* Automação de navegador (Chromium)

---

## 📂 Estrutura esperada

```
followers_1.json
following.json
script.py
```

---

## ⚙️ Configuração

Antes de rodar, edite:

```python
USUARIO_INSTAGRAM = "SEU_USUARIO"
LIMITE = 50
```

---

## ▶️ Como executar

1. Instale dependências:

```bash
pip install playwright
playwright install
```

2. Execute o script:

```bash
python script.py
```

---

## 📌 Observações

* É necessário estar logado no Instagram no navegador automatizado
* Os arquivos JSON devem ser exportados do Instagram
* O script usa interface gráfica (headless=False)

---

