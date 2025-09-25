# 🇮🇹 Comuni d'Italia per Odoo

Questo modulo aggiunge in Odoo un modello `it.city` con l'elenco di tutti i **comuni italiani**, 
facilmente riutilizzabile in altri moduli tramite un campo `Many2one`.

## ✨ Funzionalità
- Elenco completo dei comuni italiani con: nome, codice ISTAT, provincia, regione, codice catastale, CAP e popolazione.
- Import automatico da una fonte esterna (`comuni.json`) ospitata su GitHub.
- Aggiornamento programmato tramite `cron` (settimanale di default).
- Fallback a un file locale se la connessione fallisce.

## 🔗 Fonte dati
Il file JSON dei comuni è mantenuto da [@matteocontrini](https://github.com/matteocontrini):  
➡️ [matteocontrini/comuni-json](https://github.com/matteocontrini/comuni-json)

I dati dichiarano come riferimento la situazione al **01/01/2020**.

## ⚙️ Installazione
1. Copiare la cartella `l10n_it_comuni/` nel percorso addons della propria istanza Odoo.
2. Installare la dipendenza Python `requests`:
   ```bash
   pip3 install requests