PART_CHOICES = {
    ("INTER SPRINT", "INTER SPRINT"),
    ("FINAL PART", "FINAL PART"),
    ("PRE FOLLOW UP", "PRE FOLLOW UP"),
}

TEAM_CHOICES = {
    ("David", "David"),
    ("Hamid", "Hamid"),
    ("William", "William"),
    ("Florian", "Florian"),
    ("Rodolphe", "Rodolphe"),
    ("Guillaume", "Guillaume"),
}

FIELD_CHOICES = {
    ("SOFTWARE", "SOFTWARE"),
    ("HARDWARE", "HARDWARE"),
    ("FRONT END WEB", "FRONT END WEB"),
    ("BACK END WEB", "BACK END WEB"),
    ("IA", "IA"),
    ("MANAGEMENT", "MANAGEMENT"),
}

FOCUS_CHOICES = (
    ("All system", "ALL SYSTEM"),
    ("Hardware", "HARDWARE"),
    ("Software", "SOFTWARE"),
    ("Reagents", "REAGENTS"),
    ("Sensor", "SENSOR"),
)

MEASUREMENT_COMMENT_CHOICES = (
    ("None", "NONE"),
    ("Ok", "OK"),
    ("Nok", "NOK"),
)

PARAMETERS_CHOICES = (
    ("pH", "pH"),
    ("pCO2", "p02"),
    ("Hct", "Hct"),
    ("Na", "Na"),
    ("K", "K"),
    ("Ca++", "Ca++"),
    ("Cl", "Cl"),
    ("GLU", "GLU"),
    ("LAC", "LAC"),
    ("tHb", "tHb"),
    ("SO2", "SO2"),
    ("Bili", "Bili"),
    ("Hb", "Hb"),
)

SAMPLE_TYPE_CHOICES = {
    ("Capillary", "Capillary"),
    ("Syringe", "Syringe"),
}

SAMPLE_MATRIX_CHOICES = {
    ("Whole blood", "Whole blood"),
    ("Plasma", "Plasma"),
    ("Serum", "Serum"),
}

PROJECT_TYPE_CHOICES = {
    ("Method comparison", "Method comparison"),
    ("Precision", "Precision"),
    ("Linearity", "Linearity"),
    ("Software verification", "Software verification"),
    ("Interference", "Interference"),
    ("Throughput", "Throughput"),
}