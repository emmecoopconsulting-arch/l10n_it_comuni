import json, logging
from odoo import api, SUPERUSER_ID
from odoo.modules.module import get_resource_path

_logger = logging.getLogger(__name__)

DEFAULT_URL = "https://raw.githubusercontent.com/matteocontrini/comuni-json/refs/heads/master/comuni.json"

def _download_json(env):
    import requests  # external_dependencies
    url = env["ir.config_parameter"].sudo().get_param("l10n_it_comuni.source_url", DEFAULT_URL)
    r = requests.get(url, timeout=30)
    r.raise_for_status()
    return r.json()

def _load_rows(env, rows):
    City = env["it.city"]
    existing = {c.istat_code: c.id for c in City.search([])}
    to_create, to_update = [], []
    for row in rows:
        istat = row.get("codice")
        vals = {
            "name": row.get("nome"),
            "istat_code": istat,
            "region_name": (row.get("regione") or {}).get("nome"),
            "province_name": (row.get("provincia") or {}).get("nome"),
            "province_code": row.get("sigla"),
            "cadastral_code": row.get("codiceCatastale"),
            "cap": ",".join(row.get("cap") or []),
            "population": row.get("popolazione"),
        }
        if istat in existing:
            to_update.append((existing[istat], vals))
        else:
            to_create.append(vals)
    if to_create:
        City.create(to_create)
    for rec_id, vals in to_update:
        City.browse(rec_id).write(vals)

def load_comuni_from_source(cr, registry):
    env = api.Environment(cr, SUPERUSER_ID, {})
    try:
        data = _download_json(env)
        _load_rows(env, data)
        _logger.info("l10n_it_comuni: import da URL completato (%s record).", len(data))
    except Exception as e:
        _logger.warning("l10n_it_comuni: download fallito, uso fallback locale: %s", e)
        path = get_resource_path("l10n_it_comuni", "data", "comuni.json")
        if path:
            with open(path, "r", encoding="utf-8") as fp:
                data = json.load(fp)
            _load_rows(env, data)
            _logger.info("l10n_it_comuni: import da fallback locale completato (%s record).", len(data))
        else:
            _logger.error("l10n_it_comuni: nessuna fonte disponibile.")