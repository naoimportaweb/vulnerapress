#!/usr/bin/env bash
# Runner de sincronização do Vulnerapress para agendamento (cron/systemd).
# Roda src/sync_all.py com trava anti-sobreposição e log com timestamp.
#
# Produção: NÃO exporte CRAUDIOWEBOT_DIRECT — os downloads passam pelo bot.
set -euo pipefail

REPO_ROOT="/home/user/desenv/vulnerapress"
PYTHON="${PYTHON:-/usr/bin/env python3}"
LOCK="/tmp/vulnerapress-sync.lock"
LOG_DIR="${REPO_ROOT}/logs"
LOG="${LOG_DIR}/sync.log"

mkdir -p "${LOG_DIR}"

# flock -n: se já houver um run em andamento, sai sem empilhar outro.
exec 9>"${LOCK}"
if ! flock -n 9; then
    echo "$(date -Is) [skip] já há uma sincronização em andamento" >>"${LOG}"
    exit 0
fi

cd "${REPO_ROOT}"
echo "$(date -Is) [start] sync_all" >>"${LOG}"
if ${PYTHON} src/sync_all.py >>"${LOG}" 2>&1; then
    echo "$(date -Is) [ok] sync_all concluído" >>"${LOG}"
else
    rc=$?
    echo "$(date -Is) [erro] sync_all saiu com código ${rc}" >>"${LOG}"
    exit ${rc}
fi
