# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## O que é

Espelho local de plugins e temas do repositório oficial do wordpress.org. Um sync
baixa cada componente do catálogo e o arquiva, versionado, num "cofre" fora do
repositório git. Sem dependências externas: só a biblioteca padrão do Python 3.

O código, os docstrings e as mensagens de log estão em português — mantenha.

## Comandos

```bash
python3 src/sync_all.py                 # sincroniza todos os 233 componentes
python3 src/sync_all.py akismet yoast   # só os slugs passados (filtro por slug)
python3 src/components/akismet/download.py   # um componente, via seu wrapper
python3 src/downloader.py <slug> <plugin|theme> [nome]   # ad-hoc, sem catálogo

scripts/sync_cron.sh                    # runner agendado: flock + log em logs/sync.log
```

Não há testes, linter nem build. `logs/` e `.env` são ignorados pelo git.

## Configuração

`.env` na raiz (veja `.env.template`), carregado por `load_env()` com
`os.environ.setdefault` — variáveis de ambiente já definidas vencem o arquivo.

- `PATH_COFRE` — raiz do cofre; `~` é expandido. Sem ele, `vault_root()` levanta erro.
- `FETCH_BACKEND` — `http` (atual) ou `craudiowebot` (legado).

## Arquitetura

**Fonte da verdade: `data/components.json`** — `{"plugins": [...], "themes": [...]}`,
cada item com `name` + `slug` canônico do wordpress.org. O `slug` é o que importa:
`sync_all.slug()` só deriva um do nome como fallback, e nomes de exibição quase nunca
batem com o slug real do repositório (ex.: "Solid Security" → `better-wp-security`).
Slug errado ⇒ o lookup na API devolve `None` e o componente é pulado com `[?]`.

**Três camadas, uma implementação:**

- `src/downloader.py` — todo o comportamento vive aqui: escolha de backend, lookup na
  API, layout do cofre, dedup, escrita.
- `src/sync_all.py` — itera o catálogo e chama `sync_component()`. Uma exceção num
  componente não derruba o lote (loga `[x]` e segue com `rc=1`).
- `src/components/<slug>/download.py` — 233 wrappers de ~10 linhas, cada um com um dict
  `COMPONENT` literal, fazendo `sys.path.insert` até `src/` e chamando `sync_component()`.
  São gerados a partir do catálogo, mas **o gerador não está no repositório**: ao mudar
  `components.json`, os wrappers ficam dessincronizados até serem reescritos à mão.

**Fluxo de um sync** (`sync_component()` em `src/downloader.py`):
consulta a API do wordpress.org (`/plugins/info/1.0/<slug>.json` ou
`/themes/info/1.1/?action=theme_information`) → grava em
`PATH_COFRE/<slug>/downloads/<slug>-<versão>.zip` + um sidecar `<arquivo>.zip.json`
com sha1, md5, tamanho, `source_url` e timestamp UTC. Se o zip da versão já existe, o
sha1 é conferido contra o sidecar: bate ⇒ pula (`[=]`); difere ⇒ rebaixa (`[!]`).
O sidecar é o único índice — não há banco de dados.

**Backends de fetch** (`make_fetcher()`): `HttpFetcher` busca direto por urllib e é o
padrão de produção hoje. `Craudiowebot` fala com um serviço HTTP local (porta 11015)
cujo contrato real nunca foi confirmado — todos os `CRAUDIOWEBOT_*` são suposições
configuráveis. `CRAUDIOWEBOT_DIRECT=1` é compat legado e força o `HttpFetcher`.

**Componentes premium** (Divi, WP Rocket, Avada…) não estão no repositório livre:
o lookup devolve `None` e `sync_component()` sai com 0 sem baixar nada, por design.

## Agendamento

`scripts/sync_cron.sh` roda diariamente às 03:00 via `vulnerapress-sync.timer`
(`Type=oneshot`, `Persistent=true`). O script serializa runs com `flock -n` em
`/tmp/vulnerapress-sync.lock` — se um sync já está rodando, o novo sai limpo.
`REPO_ROOT` está **hardcoded** em `scripts/sync_cron.sh` e nos dois units.

## Pegadinhas

- Um wrapper novo em `src/components/<slug>/` só funciona se o `slug` do diretório
  bater com o do dict `COMPONENT` e com o do catálogo — nada valida isso.
