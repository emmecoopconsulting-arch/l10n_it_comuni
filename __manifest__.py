{
    "name": "Comuni d'Italia (base)",
    "version": "18.0.1.0.0",
    "summary": "Elenco comuni italiani con import da fonte esterna",
    "depends": ["base"],
    "data": [
        "security/ir.model.access.csv",
        "views/it_city_views.xml",
        "data/cron.xml",
    ],
    "post_init_hook": "load_comuni_from_source",
    "external_dependencies": {"python": ["requests"]},
    "license": "LGPL-3",
    "installable": True,
}