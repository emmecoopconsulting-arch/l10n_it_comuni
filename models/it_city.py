from odoo import fields, models

class ItCity(models.Model):
    _name = "it.city"
    _description = "Comune italiano"
    _rec_name = "name"
    _order = "name"

    name = fields.Char(required=True, index=True)
    istat_code = fields.Char(string="Codice ISTAT", required=True, size=6, index=True)
    region_name = fields.Char(string="Regione", index=True)
    province_name = fields.Char(string="Provincia", index=True)
    province_code = fields.Char(string="Sigla", size=2, index=True)
    cadastral_code = fields.Char(string="Codice catastale", size=4, index=True)
    cap = fields.Char(string="CAP", help="CAP multipli separati da virgola")
    population = fields.Integer(string="Popolazione")

    _sql_constraints = [
        ("istat_code_unique", "unique(istat_code)", "Il codice ISTAT deve essere unico."),
    ]