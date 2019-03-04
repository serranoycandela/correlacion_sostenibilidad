from value_functions import discrete_factor as f
matrix_list = [
    [None,     f('+++'), f('++'),  f('+'),   f('+++'), f('+++'), f('+'),   f('++'),  f('+++'), f('+'),   f('+++'), f('+'),   f(0),     f(0),     f(0),     f('+'),   f('+'),   f('+'),   f('+++'), None,     None    ],
    [f('++'),  None,     f(0),     f('+'),   f(0),     f('+++'), f('+'),   f('+'),   f('+'),   f('++'),  f('+'),   f('+++'), f(0),     f(0),     f('+'),   f(0),     f(0),     f('+'),   f('++'),  f('+'),   f('++') ],
    [f('+'),   f('++'),  None,     f('++'),  f('++'),  f('+++'), f(0),     f(0),     f('++'),  f('+++'), f(0),     f('++'),  f('+'),   f(0),     f('+'),   f('+'),   f(0),     f('++'),  f('+++'), f('+'),   f('++') ],
    [f('+'),   f('+'),   f('+++'), None,     f('+'),   f('+++'), f('+'),   f('+'),   f('+++'), f('+++'), f('+'),   f('+'),   f('+'),   f(0),     f('+'),   f(0),     f(0),     f(0),     f('++'),  f('+'),   f('+')  ],
    [f('+++'), f(0),     f(0),     f('+'),   None,     f('+++'), f('+'),   f('+'),   f('+++'), f('+++'), f('+'),   f('++'),  f(0),     f(0),     f('+'),   f('+'),   f(0),     f('+'),   f('++'),  f('++'),  f('+++')],
    [f('+'),   f('+++'), f('+++'), f('+++'), f('+++'), None,     f('+'),   f(0),     f('+++'), f('++'),  f('+'),   f(0),     f(0),     f(0),     f('+'),   f(0),     f(0),     f(0),     f('--'),  f('++'),  f('+++')],
    [f('++'),  f('+'),   f(0),     f('+'),   f(0),     f(0),     None,     f('+++'), f(0),     f(0),     f('+++'), f('+'),   f(0),     f(0),     f('+'),   f('+'),   f(0),     f('+'),   f('+'),   f('+++'), f('+')  ],
    [f('++'),  f('+'),   f(0),     f(0),     f(0),     f(0),     f(0),     None,     f('++'),  f(0),     f('+++'), f('+'),   f(0),     f(0),     f('+'),   f('+'),   f(0),     f('+'),   f('++'),  f('+++'), f('+')  ],
    [f(0),     f(0),     f(0),     f(0),     f(0),     f('+++'), f(0),     f(0),     None,     f(0),     f(0),     f('+++'), f(0),     f(0),     f('+'),   f(0),     f(0),     f('+'),   f('+'),   f('+++'), f('++') ],
    [f(0),     f('++'),  f('+++'), f('+++'), f(0),     f('+'),   f(0),     f('+'),   f('+'),   None,     f('++'),  f('+'),   f(0),     f(0),     f('+'),   f(0),     f(0),     f('+'),   f('++'),  f('+'),   f('+++')],
    [f('++'),  f('++'),  f(0),     f('+'),   f(0),     f(0),     f('+'),   f('++'),  f(0),     f('+'),   None,     f('++'),  f('+'),   f(0),     f('++'),  f('+++'), f('+'),   f('+++'), f('+++'), f('+++'), f('+++')],
    [f(0),     f('++'),  f('+'),   f('+'),   f('+'),   f('+++'), f('+'),   f('+'),   f(0),     f(0),     f('+++'), None,     f(0),     f(0),     f('+'),   f('+++'), f(0),     f('+'),   f('+++'), f('+'),   f(0)    ],
    [f('+++'), f('+++'), f('+++'), f('+++'), f('+++'), f('+++'), f('+++'), f('+++'), f('+++'), f('+++'), f('+++'), f('++'),  None,     f(0),     f('+++'), f(0),     f(0),     f('+++'), f('+++'), f('+++'), f('+++')],
    [f('+'),   f('+++'), f('+'),   f('++'),  f('+++'), f('+++'), f('+++'), f('+++'), f('+++'), f('+++'), f('+++'), f('+'),   f('+'),   None,     f('+++'), f('+'),   f(0),     f('+++'), f('++'),  f('+++'), f('+')  ],
    [None,     f(0),     f(0),     f(0),     f(0),     f(0),     f('+'),   f('+'),   f(0),     f(0),     f('+'),   f('+++'), f('+'),   f(0),     None,     f('+++'), f('+'),   f('+'),   f('+++'), f('+++'), f('++') ],  # aguas! dudas aqui
    [f('+'),   f(0),     f(0),     f(0),     f(0),     f(0),     f(0),     f(0),     f(0),     f(0),     f('+++'), f('+'),   f('+'),   f('++'),  f('+++'), None,     f('+++'), f('++'),  f('+++'), f('++'),  f(0)    ],
    [f('++'),  f(0),     f(0),     f('+'),   f(0),     f(0),     f(0),     f(0),     f(0),     f(0),     f('+'),   f('++'),  f('++'),  f('+'),   f(0),     f('+'),   None,     f(0),     f('++'),  f('+++'), f(0)    ],
    [f('++'),  f('++'),  f('++'),  f('++'),  f('++'),  f('++'),  f('++'),  f('+'),   f(0),     f('++'),  f('+++'), f('+++'), f(0),     f('+'),   f('+++'), f('+++'), f(0),     None,     f('+++'), f('+++'), f(0)    ],
    [f('+++'), f('++'),  f('+'),   f('+'),   f('++'),  f('--'),  f('++'),  f('+++'), f(0),     f('++'),  f('+++'), f('++'),  f(0),     f(0),     f('+'),   f('+'),   f(0),     f('+'),   None,     f('++'),  f(0)    ],
    [f('+++'), f(0),     f('+++'), f('+'),   f('++'),  f('+++'), f('+++'), f('+++'), f('+++'), f(0),     f('+++'), f('++'),  f('+++'), f('+++'), f('+++'), f('+++'), f('+++'), f('+++'), f('+++'), None,     f(0)    ],
    [f(0),     f(0),     f(0),     f(0),     f(0),     f(0),     f(0),     f(0),     f(0),     f(0),     f(0),     f('+++'), f(0),     f(0),     f('+'),   f('++'),  f(0),     f('+'),   f('+++'), f(0),     None    ]
]

matrix_dict = {
    "Ordenamiento y planeación territorial sustentable (uso mixto del suelo, densificación acorde a la capacidad de carga del territorio)":
    [None,     f('+++'), f('++'),  f('+'),   f('+++'), f('+++'), f('+'),   f('++'),  f('+++'), f('+'),   f('+++'), f('+'),   f(0),     f(0),     f(0),     f('+'),   f('+'),   f('+'),   f('+++'), None,     None    ],
    "Edificaciones sustentables (Ecotecnias, diseño y materiales sustentables)":
    [f('++'),  None,     f(0),     f('+'),   f(0),     f('+++'), f('+'),   f('+'),   f('+'),   f('++'),  f('+'),   f('+++'), f(0),     f(0),     f('+'),   f(0),     f(0),     f('+'),   f('++'),  f('+'),   f('++') ],
    "Fomento de la economía circular (enfoque de ciclo de vida) y de mercados locales-regionales (proporción de actividades económicas y empleos “verdes”)":
    [f('+'),   f('++'),  None,     f('++'),  f('++'),  f('+++'), f(0),     f(0),     f('++'),  f('+++'), f(0),     f('++'),  f('+'),   f(0),     f('+'),   f('+'),   f(0),     f('++'),  f('+++'), f('+'),   f('++') ],
    "Acciones para una industria limpia (producción y circulación sustentable y responsabilidad extendida)":
    [f('+'),   f('+'),   f('+++'), None,     f('+'),   f('+++'), f('+'),   f('+'),   f('+++'), f('+++'), f('+'),   f('+'),   f('+'),   f(0),     f('+'),   f(0),     f(0),     f(0),     f('++'),  f('+'),   f('+')  ],
    "Movilidad sustentable (masiva, pública y crecientemente no motorizada, además de la regulación del transporte de carga)":
    [f('+++'), f(0),     f(0),     f('+'),   None,     f('+++'), f('+'),   f('+'),   f('+++'), f('+++'), f('+'),   f('++'),  f(0),     f(0),     f('+'),   f('+'),   f(0),     f('+'),   f('++'),  f('++'),  f('+++')],
    "Eficiencia energética y fomento a las energías renovables ":
    [f('+'),   f('+++'), f('+++'), f('+++'), f('+++'), None,     f('+'),   f(0),     f('+++'), f('++'),  f('+'),   f(0),     f(0),     f(0),     f('+'),   f(0),     f(0),     f(0),     f('--'),  f('++'),  f('+++')],
    "Infraestructura verde-azul para la adaptación al cambio climático":
    [f('++'),  f('+'),   f(0),     f('+'),   f(0),     f(0),     None,     f('+++'), f(0),     f(0),     f('+++'), f('+'),   f(0),     f(0),     f('+'),   f('+'),   f(0),     f('+'),   f('+'),   f('+++'), f('+')  ],
    "Bienes ambientales - áreas verdes / adaptación urbana basada en ecosistemas":
    [f('++'),  f('+'),   f(0),     f(0),     f(0),     f(0),     f(0),     None,     f('++'),  f(0),     f('+++'), f('+'),   f(0),     f(0),     f('+'),   f('+'),   f(0),     f('+'),   f('++'),  f('+++'), f('+')  ],
    "Mitigación de la emisión de contaminantes atmosféricos / mejora de la calidad del aire (acciones para..)":
    [f(0),     f(0),     f(0),     f(0),     f(0),     f('+++'), f(0),     f(0),     None,     f(0),     f(0),     f('+++'), f(0),     f(0),     f('+'),   f(0),     f(0),     f('+'),   f('+'),   f('+++'), f('++') ],
    "Gestión sustentable de residuos (RSU, especiales y peligrosos; incluye la cogeneración de energía)":
    [f(0),     f('++'),  f('+++'), f('+++'), f(0),     f('+'),   f(0),     f('+'),   f('+'),   None,     f('++'),  f('+'),   f(0),     f(0),     f('+'),   f(0),     f(0),     f('+'),   f('++'),  f('+'),   f('+++')],
    "Gestión de riesgo de desastres y reducción de la vulnerabilidad al cambio climático":
    [f('++'),  f('++'),  f(0),     f('+'),   f(0),     f(0),     f('+'),   f('++'),  f(0),     f('+'),   None,     f('++'),  f('+'),   f(0),     f('++'),  f('+++'), f('+'),   f('+++'), f('+++'), f('+++'), f('+++')],
    "Reducción de la pobreza y mejora de la calidad de vida (acciones para…)":
    [f(0),     f('++'),  f('+'),   f('+'),   f('+'),   f('+++'), f('+'),   f('+'),   f(0),     f(0),     f('+++'), None,     f(0),     f(0),     f('+'),   f('+++'), f(0),     f('+'),   f('+++'), f('+'),   f(0)    ],
    "Financiamiento para acciones y proyectos en sustentabilidad urbana (local, estatal, nacional e internacional)":
    [f('+++'), f('+++'), f('+++'), f('+++'), f('+++'), f('+++'), f('+++'), f('+++'), f('+++'), f('+++'), f('+++'), f('++'),  None,     f(0),     f('+++'), f(0),     f(0),     f('+++'), f('+++'), f('+++'), f('+++')],
    "Existencia de un presupuesto climático y seguros contra riesgos hidro-meteorológicos":
    [f('+'),   f('+++'), f('+'),   f('++'),  f('+++'), f('+++'), f('+++'), f('+++'), f('+++'), f('+++'), f('+++'), f('+'),   f('+'),   None,     f('+++'), f('+'),   f(0),     f('+++'), f('++'),  f('+++'), f('+')  ],
    "Acciones de educación para el cambio climático y difusión para la sustentabilidad":
    [None,     f(0),     f(0),     f(0),     f(0),     f(0),     f('+'),   f('+'),   f(0),     f(0),     f('+'),   f('+++'), f('+'),   f(0),     None,     f('+++'), f('+'),   f('+'),   f('+++'), f('+++'), f('++') ],  # aguas! dudas, en duda
    "Aumento en la participación social en el avance hacia la sustentabilidad, incluyente y justa":
    [f('+'),   f(0),     f(0),     f(0),     f(0),     f(0),     f(0),     f(0),     f(0),     f(0),     f('+++'), f('+'),   f('+'),   f('++'),  f('+++'), None,     f('+++'), f('++'),  f('+++'), f('++'),  f(0)    ],
    "Combate a la corrupción / aumento de la rendición de cuentas":
    [f('++'),  f(0),     f(0),     f('+'),   f(0),     f(0),     f(0),     f(0),     f(0),     f(0),     f('+'),   f('++'),  f('++'),  f('+'),   f(0),     f('+'),   None,     f(0),     f('++'),  f('+++'), f(0)    ],
    "Construcción de capacidades para la sustentabilidad urbana con perspectiva de género (incluye capacidades institucionales, empresariales y sociales)":
    [f('++'),  f('++'),  f('++'),  f('++'),  f('++'),  f('++'),  f('++'),  f('+'),   f(0),     f('++'),  f('+++'), f('+++'), f(0),     f('+'),   f('+++'), f('+++'), f(0),     None,     f('+++'), f('+++'), f(0)    ],
    "Mejora de la resiliencia urbana (biofísica y social del espacio urbano)":
    [f('+++'), f('++'),  f('+'),   f('+'),   f('++'),  f('--'),  f('++'),  f('+++'), f(0),     f('++'),  f('+++'), f('++'),  f(0),     f(0),     f('+'),   f('+'),   f(0),     f('+'),   None,     f('++'),  f(0)    ],
    "Fortalecimiento de la gobernanza del cambio climático":
    [f('+++'), f(0),     f('+++'), f('+'),   f('++'),  f('+++'), f('+++'), f('+++'), f('+++'), f(0),     f('+++'), f('++'),  f('+++'), f('+++'), f('+++'), f('+++'), f('+++'), f('+++'), f('+++'), None,     f(0)    ],
    "Salud":
    [f(0),     f(0),     f(0),     f(0),     f(0),     f(0),     f(0),     f(0),     f(0),     f(0),     f(0),     f('+++'), f(0),     f(0),     f('+'),   f('++'),  f(0),     f('+'),   f('+++'), f(0),     None    ]
}

subcats = ["Ordenamiento y planeación territorial sustentable (uso mixto del suelo, densificación acorde a la capacidad de carga del territorio)",
"Edificaciones sustentables (Ecotecnias, diseño y materiales sustentables)",
"Fomento de la economía circular (enfoque de ciclo de vida) y de mercados locales-regionales (proporción de actividades económicas y empleos “verdes”)",
"Acciones para una industria limpia (producción y circulación sustentable y responsabilidad extendida)",
"Movilidad sustentable (masiva, pública y crecientemente no motorizada, además de la regulación del transporte de carga)",
"Eficiencia energética y fomento a las energías renovables ",
"Infraestructura verde-azul para la adaptación al cambio climático",
"Bienes ambientales - áreas verdes / adaptación urbana basada en ecosistemas",
"Mitigación de la emisión de contaminantes atmosféricos / mejora de la calidad del aire (acciones para..)",
"Gestión sustentable de residuos (RSU, especiales y peligrosos; incluye la cogeneración de energía)",
"Gestión de riesgo de desastres y reducción de la vulnerabilidad al cambio climático",
"Reducción de la pobreza y mejora de la calidad de vida (acciones para…)",
"Financiamiento para acciones y proyectos en sustentabilidad urbana (local, estatal, nacional e internacional)",
"Existencia de un presupuesto climático y seguros contra riesgos hidro-meteorológicos",
"Acciones de educación para el cambio climático y difusión para la sustentabilidad",
"Aumento en la participación social en el avance hacia la sustentabilidad, incluyente y justa",
"Combate a la corrupción / aumento de la rendición de cuentas",
"Construcción de capacidades para la sustentabilidad urbana con perspectiva de género (incluye capacidades institucionales, empresariales y sociales)",
"Mejora de la resiliencia urbana (biofísica y social del espacio urbano)",
"Fortalecimiento de la gobernanza del cambio climático",
"Salud"]

subcats2 = ["Ordenamiento y planeación territorial sustentable (uso mixto del suelo, densificación acorde a la capacidad de carga del territorio)",
"Edificaciones sustentables (Ecotecnias, diseño y materiales sustentables)",
"Acciones para una industria limpia (producción y circulación sustentable y responsabilidad extendida)",
"Movilidad sustentable (masiva, pública y crecientemente no motorizada, además de la regulación del transporte de carga)",
"Eficiencia energética y fomento a las energías renovables ",
"Infraestructura verde-azul para la adaptación al cambio climático",
"Bienes ambientales - áreas verdes / adaptación urbana basada en ecosistemas",
"Mitigación de la emisión de contaminantes atmosféricos / mejora de la calidad del aire (acciones para..)",
"Gestión sustentable de residuos (RSU, especiales y peligrosos; incluye la cogeneración de energía)",
"Mejora de la resiliencia urbana (biofísica y social del espacio urbano)",
"Fomento de la economía circular (enfoque de ciclo de vida) y de mercados locales-regionales (proporción de actividades económicas y empleos “verdes”)",
"Reducción de la pobreza y mejora de la calidad de vida (acciones para…)",
"Financiamiento para acciones y proyectos en sustentabilidad urbana (local, estatal, nacional e internacional)",
"Acciones de educación para el cambio climático y difusión para la sustentabilidad",
"Aumento en la participación social en el avance hacia la sustentabilidad, incluyente y justa",
"Salud",
"Gestión de riesgo de desastres y reducción de la vulnerabilidad al cambio climático",
"Existencia de un presupuesto climático y seguros contra riesgos hidro-meteorológicos",
"Combate a la corrupción / aumento de la rendición de cuentas",
"Construcción de capacidades para la sustentabilidad urbana con perspectiva de género (incluye capacidades institucionales, empresariales y sociales)",
"Fortalecimiento de la gobernanza del cambio climático"
]
# orden = [0, 1, 3, 4, 5, 6, 7, 8, 9, 18, 2, 11, 12, 14, 17, 20, 10, 13, 16, 17, 19]

# matrix_list_fake = [
#     [None,     "f('+++')", "f('++')",  "f('+')",   "f('+++')", "f('+++')", "f('+')",   "f('++')",  "f('+++')", "f('+')",   "f('+++')", "f('+')",   "f(0)",     "f(0)",     "f(0)",     "f('+')",   "f('+')",   "f('+')",   "f('+++')", None,     None    ],
#     ["f('++')",  None,     "f(0)",     "f('+')",   "f(0)",     "f('+++')", "f('+')",   "f('+')",   "f('+')",   "f('++')",  "f('+')",   "f('+++')", "f(0)",     "f(0)",     "f('+')",   "f(0)",     "f(0)",     "f('+')",   "f('++')",  "f('+')",   "f('++')" ],
#     ["f('+')",   "f('++')",  None,     "f('++')",  "f('++')",  "f('+++')", "f(0)",     "f(0)",     "f('++')",  "f('+++')", "f(0)",     "f('++')",  "f('+')",   "f(0)",     "f('+')",   "f('+')",   "f(0)",     "f('++')",  "f('+++')", "f('+')",   "f('++')" ],
#     ["f('+')",   "f('+')",   "f('+++')", None,     "f('+')",   "f('+++')", "f('+')",   "f('+')",   "f('+++')", "f('+++')", "f('+')",   "f('+')",   "f('+')",   "f(0)",     "f('+')",   "f(0)",     "f(0)",     "f(0)",     "f('++')",  "f('+')",   "f('+')"  ],
#     ["f('+++')", "f(0)",     "f(0)",     "f('+')",   None,     "f('+++')", "f('+')",   "f('+')",   "f('+++')", "f('+++')", "f('+')",   "f('++')",  "f(0)",     "f(0)",     "f('+')",   "f('+')",   "f(0)",     "f('+')",   "f('++')",  "f('++')",  "f('+++')"],
#     ["f('+')",   "f('+++')", "f('+++')", "f('+++')", "f('+++')", None,     "f('+')",   "f(0)",     "f('+++')", "f('++')",  "f('+')",   "f(0)",     "f(0)",     "f(0)",     "f('+')",   "f(0)",     "f(0)",     "f(0)",     "f('--')",  "f('++')",  "f('+++')"],
#     ["f('++')",  "f('+')",   "f(0)",     "f('+')",   "f(0)",     "f(0)",     None,     "f('+++')", "f(0)",     "f(0)",     "f('+++')", "f('+')",   "f(0)",     "f(0)",     "f('+')",   "f('+')",   "f(0)",     "f('+')",   "f('+')",   "f('+++')", "f('+')"  ],
#     ["f('++')",  "f('+')",   "f(0)",     "f(0)",     "f(0)",     "f(0)",     "f(0)",     None,     "f('++')",  "f(0)",     "f('+++')", "f('+')",   "f(0)",     "f(0)",     "f('+')",   "f('+')",   "f(0)",     "f('+')",   "f('++')",  "f('+++')", "f('+')"  ],
#     ["f(0)",     "f(0)",     "f(0)",     "f(0)",     "f(0)",     "f('+++')", "f(0)",     "f(0)",     None,     "f(0)",     "f(0)",     "f('+++')", "f(0)",     "f(0)",     "f('+')",   "f(0)",     "f(0)",     "f('+')",   "f('+')",   "f('+++')", "f('++')" ],
#     ["f(0)",     "f('++')",  "f('+++')", "f('+++')", "f(0)",     "f('+')",   "f(0)",     "f('+')",   "f('+')",   None,     "f('++')",  "f('+')",   "f(0)",     "f(0)",     "f('+')",   "f(0)",     "f(0)",     "f('+')",   "f('++')",  "f('+')",   "f('+++')"],
#     ["f('++')",  "f('++')",  "f(0)",     "f('+')",   "f(0)",     "f(0)",     "f('+')",   "f('++')",  "f(0)",     "f('+')",   None,     "f('++')",  "f('+')",   "f(0)",     "f('++')",  "f('+++')", "f('+')",   "f('+++')", "f('+++')", "f('+++')", "f('+++')"],
#     ["f(0)",     "f('++')",  "f('+')",   "f('+')",   "f('+')",   "f('+++')", "f('+')",   "f('+')",   "f(0)",     "f(0)",     "f('+++')", None,     "f(0)",     "f(0)",     "f('+')",   "f('+++')", "f(0)",     "f('+')",   "f('+++')", "f('+')",   "f(0)"    ],
#     ["f('+++')", "f('+++')", "f('+++')", "f('+++')", "f('+++')", "f('+++')", "f('+++')", "f('+++')", "f('+++')", "f('+++')", "f('+++')", "f('++')",  None,     "f(0)",     "f('+++')", "f(0)",     "f(0)",     "f('+++')", "f('+++')", "f('+++')", "f('+++')"],
#     ["f('+')",   "f('+++')", "f('+')",   "f('++')",  "f('+++')", "f('+++')", "f('+++')", "f('+++')", "f('+++')", "f('+++')", "f('+++')", "f('+')",   "f('+')",   None,     "f('+++')", "f('+')",   "f(0)",     "f('+++')", "f('++')",  "f('+++')", "f('+')"  ],
#     [None,     "f(0)",     "f(0)",     "f(0)",     "f(0)",     "f(0)",     "f('+')",   "f('+')",   "f(0)",     "f(0)",     "f('+')",   "f('+++')", "f('+')",   "f(0)",     None,     "f('+++')", "f('+')",   "f('+')",   "f('+++')", "f('+++')", "f('++')" ],  # aguas! dudas aqui
#     ["f('+')",   "f(0)",     "f(0)",     "f(0)",     "f(0)",     "f(0)",     "f(0)",     "f(0)",     "f(0)",     "f(0)",     "f('+++')", "f('+')",   "f('+')",   "f('++')",  "f('+++')", None,     "f('+++')", "f('++')",  "f('+++')", "f('++')",  "f(0)"    ],
#     ["f('++')",  "f(0)",     "f(0)",     "f('+')",   "f(0)",     "f(0)",     "f(0)",     "f(0)",     "f(0)",     "f(0)",     "f('+')",   "f('++')",  "f('++')",  "f('+')",   "f(0)",     "f('+')",   None,     "f(0)",     "f('++')",  "f('+++')", "f(0)"    ],
#     ["f('++')",  "f('++')",  "f('++')",  "f('++')",  "f('++')",  "f('++')",  "f('++')",  "f('+')",   "f(0)",     "f('++')",  "f('+++')", "f('+++')", "f(0)",     "f('+')",   "f('+++')", "f('+++')", "f(0)",     None,     "f('+++')", "f('+++')", "f(0)"    ],
#     ["f('+++')", "f('++')",  "f('+')",   "f('+')",   "f('++')",  "f('--')",  "f('++')",  "f('+++')", "f(0)",     "f('++')",  "f('+++')", "f('++')",  "f(0)",     "f(0)",     "f('+')",   "f('+')",   "f(0)",     "f('+')",   None,     "f('++')",  "f(0)"    ],
#     ["f('+++')", "f(0)",     "f('+++')", "f('+')",   "f('++')",  "f('+++')", "f('+++')", "f('+++')", "f('+++')", "f(0)",     "f('+++')", "f('++')",  "f('+++')", "f('+++')", "f('+++')", "f('+++')", "f('+++')", "f('+++')", "f('+++')", None,     "f(0)"    ],
#     ["f(0)",     "f(0)",     "f(0)",     "f(0)",     "f(0)",     "f(0)",     "f(0)",     "f(0)",     "f(0)",     "f(0)",     "f(0)",     "f('+++')", "f(0)",     "f(0)",     "f('+')",   "f('++')",  "f(0)",     "f('+')",   "f('+++')", "f(0)",     None    ]
# ]


# matrix2 = []
# r = -1
# for row in orden:
#     r += 1
#     c = -1
#     matrix2.append([])
#     for column in orden:
#         c += 1
#         matrix2[r].append(matrix_list_fake[row][column])
#     print(matrix2[r])

matrix_list2 = [[None, f('+++'), f('+'), f('+++'), f('+++'), f('+'), f('++'), f('+++'), f('+'), f('+++'), f('++'), f('+'), f(0), f(0), f('+'), None, f('+++'), f(0), f('+'), f('+'), None],
[f('++'), None, f('+'), f(0), f('+++'), f('+'), f('+'), f('+'), f('++'), f('++'), f(0), f('+++'), f(0), f('+'), f('+'), f('++'), f('+'), f(0), f(0), f('+'), f('+')],
[f('+'), f('+'), None, f('+'), f('+++'), f('+'), f('+'), f('+++'), f('+++'), f('++'), f('+++'), f('+'), f('+'), f('+'), f(0), f('+'), f('+'), f(0), f(0), f(0), f('+')],
[f('+++'), f(0), f('+'), None, f('+++'), f('+'), f('+'), f('+++'), f('+++'), f('++'), f(0), f('++'), f(0), f('+'), f('+'), f('+++'), f('+'), f(0), f(0), f('+'), f('++')],
[f('+'), f('+++'), f('+++'), f('+++'), None, f('+'), f(0), f('+++'), f('++'), f('--'), f('+++'), f(0), f(0), f('+'), f(0), f('+++'), f('+'), f(0), f(0), f(0), f('++')],
[f('++'), f('+'), f('+'), f(0), f(0), None, f('+++'), f(0), f(0), f('+'), f(0), f('+'), f(0), f('+'), f('+'), f('+'), f('+++'), f(0), f(0), f('+'), f('+++')],
[f('++'), f('+'), f(0), f(0), f(0), f(0), None, f('++'), f(0), f('++'), f(0), f('+'), f(0), f('+'), f('+'), f('+'), f('+++'), f(0), f(0), f('+'), f('+++')],
[f(0), f(0), f(0), f(0), f('+++'), f(0), f(0), None, f(0), f('+'), f(0), f('+++'), f(0), f('+'), f('+'), f('++'), f(0), f(0), f(0), f('+'), f('+++')],
[f(0), f('++'), f('+++'), f(0), f('+'), f(0), f('+'), f('+'), None, f('++'), f('+++'), f('+'), f(0), f('+'), f('+'), f('+++'), f('++'), f(0), f(0), f('+'), f('+')],
[f('+++'), f('++'), f('+'), f('++'), f('--'), f('++'), f('+++'), f(0), f('++'), None, f('+'), f('++'), f(0), f('+'), f('+'), f(0), f('+++'), f(0), f(0), f('+'), f('++')],
[f('+'), f('++'), f('++'), f('++'), f('+++'), f(0), f(0), f('++'), f('+++'), f('+++'), None, f('++'), f('+'), f('+'), f('++'), f('++'), f(0), f(0), f(0), f('++'), f('+')],
[f(0), f('++'), f('+'), f('+'), f('+++'), f('+'), f('+'), f(0), f(0), f('+++'), f('+'), None, f(0), f('+'), f('+'), f(0), f('+++'), f(0), f(0), f('+'), f('+')],
[f('+++'), f('+++'), f('+++'), f('+++'), f('+++'), f('+++'), f('+++'), f('+++'), f('+++'), f('+++'), f('+++'), f('++'), None, f('+++'), f('+++'), f('+++'), f('+++'), f(0), f(0), f('+++'), f('+++')],
[None, f(0), f(0), f(0), f(0), f('+'), f('+'), f(0), f(0), f('+++'), f(0), f('+++'), f('+'), None, f('+'), f('++'), f('+'), f(0), f('+'), f('+'), f('+++')],
[f('++'), f('++'), f('++'), f('++'), f('++'), f('++'), f('+'), f(0), f('++'), f('+++'), f('++'), f('+++'), f(0), f('+++'), None, f(0), f('+++'), f('+'), f(0), None, f('+++')],
[f(0), f(0), f(0), f(0), f(0), f(0), f(0), f(0), f(0), f('+++'), f(0), f('+++'), f(0), f('+'), f('+'), None, f(0), f(0), f(0), f('+'), f(0)],
[f('++'), f('++'), f('+'), f(0), f(0), f('+'), f('++'), f(0), f('+'), f('+++'), f(0), f('++'), f('+'), f('++'), f('+++'), f('+++'), None, f(0), f('+'), f('+++'), f('+++')],
[f('+'), f('+++'), f('++'), f('+++'), f('+++'), f('+++'), f('+++'), f('+++'), f('+++'), f('++'), f('+'), f('+'), f('+'), f('+++'), f('+++'), f('+'), f('+++'), None, f(0), f('+++'), f('+++')],
[f('++'), f(0), f('+'), f(0), f(0), f(0), f(0), f(0), f(0), f('++'), f(0), f('++'), f('++'), f(0), f(0), f(0), f('+'), f('+'), None, f(0), f('+++')],
[f('++'), f('++'), f('++'), f('++'), f('++'), f('++'), f('+'), f(0), f('++'), f('+++'), f('++'), f('+++'), f(0), f('+++'), None, f(0), f('+++'), f('+'), f(0), None, f('+++')],
[f('+++'), f(0), f('+'), f('++'), f('+++'), f('+++'), f('+++'), f('+++'), f(0), f('+++'), f('+++'), f('++'), f('+++'), f('+++'), f('+++'), f(0), f('+++'), f('+++'), f('+++'), f('+++'), None]]

subcats3 = ["Ordenamiento territorial y planeación urbana sustentable A1",
"Edificaciones sustentables (Ecotecnias, diseño y materiales sustentables) A2",
"Industria limpia (produccion y circulacion sustentable) A3",
"Movilidad sustentable A4",
"Eficiencia energética y fomento a las energías renovables A5",
"Infraestructura verde-azul para la adaptacion al cambio climático A6",
"Conservación ambiental y adaptacion urbana basada en ecosistemas A7",
"Mitigacion de gases efecto invernadero y mejora de la calidad del aire A8",
"Gestión sustentable de residuos y cogeneración de energía A9",
"Fomento a la resiliencia urbana A10",
"Economía circular y mercados locales-regionales E1",
"Reducción de la pobreza y de la vulnerabilidad al cambio climático E2",
"Financiamiento para la sustentabilidad urbana E3",
"Acciones de educación para el cambio climático y difusión para la sustentabilidad S1",
"Participación social en el avance hacia la sustentabilidad, incluyente y justa S2",
"Mejoramiento de la salud pública S3",
"Gestión de riesgo de desastres y reducción de la vulnerabilidad al cambio climático G1",
"Presupuesto climático y seguros contra riesgos hidro-meteorológicos G2",
"Combate a la corrupción y rendición de cuentas G3",
"Construcción de capacidades para sustentabilidad urbana con perspectiva de género G4",
"Fortalecimiento de la gobernanza del cambio climático G5"]

abrevia3 = ["A1",
"A2",
"A3",
"A4",
"A5",
"A6",
"A7",
"A8",
"A9",
"A10",
"E1",
"E2",
"E3",
"S1",
"S2",
"S3",
"G1",
"G2",
"G3",
"G4",
"G5"]

matrix_list3 = [[None, f('+++'), f(0), f('+++'), f('+++'), f(0), f('++'), f('+++'), f(0), f('+++'), f('++'), f(0), f(0), f(0), f(0), None, f('+++'), f(0), f(0), f(0), None],
[f('++'), None, f(0), f(0), f('+++'), f(0), f(0), f(0), f('++'), f('++'), f(0), f('+++'), f(0), f(0), f(0), f('++'), f(0), f(0), f(0), f(0), f(0)],
[f(0), f(0), None, f(0), f('+++'), f(0), f(0), f('+++'), f('+++'), f('++'), f('+++'), f(0), f(0), f(0), f(0), f(0), f(0), f(0), f(0), f(0), f(0)],
[f('+++'), f(0), f(0), None, f('+++'), f(0), f(0), f('+++'), f('+++'), f('++'), f(0), f('++'), f(0), f(0), f(0), f('+++'), f(0), f(0), f(0), f(0), f('++')],
[f(0), f('+++'), f('+++'), f('+++'), None, f(0), f(0), f('+++'), f('++'), f('--'), f('+++'), f(0), f(0), f(0), f(0), f('+++'), f(0), f(0), f(0), f(0), f('++')],
[f('++'), f(0), f(0), f(0), f(0), None, f('+++'), f(0), f(0), f(0), f(0), f(0), f(0), f(0), f(0), f(0), f('+++'), f(0), f(0), f(0), f('+++')],
[f('++'), f(0), f(0), f(0), f(0), f(0), None, f('++'), f(0), f('++'), f(0), f(0), f(0), f(0), f(0), f(0), f('+++'), f(0), f(0), f(0), f('+++')],
[f(0), f(0), f(0), f(0), f('+++'), f(0), f(0), None, f(0), f(0), f(0), f('+++'), f(0), f(0), f(0), f('++'), f(0), f(0), f(0), f(0), f('+++')],
[f(0), f('++'), f('+++'), f(0), f(0), f(0), f(0), f(0), None, f('++'), f('+++'), f(0), f(0), f(0), f(0), f('+++'), f('++'), f(0), f(0), f(0), f(0)],
[f('+++'), f('++'), f(0), f('++'), f('--'), f('++'), f('+++'), f(0), f('++'), None, f(0), f('++'), f(0), f(0), f(0), f(0), f('+++'), f(0), f(0), f(0), f('++')],
[f(0), f('++'), f('++'), f('++'), f('+++'), f(0), f(0), f('++'), f('+++'), f('+++'), None, f('++'), f(0), f(0), f('++'), f('++'), f(0), f(0), f(0), f('++'), f(0)],
[f(0), f('++'), f(0), f(0), f('+++'), f(0), f(0), f(0), f(0), f('+++'), f(0), None, f(0), f(0), f(0), f(0), f('+++'), f(0), f(0), f(0), f(0)],
[f('+++'), f('+++'), f('+++'), f('+++'), f('+++'), f('+++'), f('+++'), f('+++'), f('+++'), f('+++'), f('+++'), f('++'), None, f('+++'), f('+++'), f('+++'), f('+++'), f(0), f(0), f('+++'), f('+++')],
[f(0), f(0), f(0), f(0), f(0), f(0), f(0), f(0), f(0), f('+++'), f(0), f('+++'), f(0), None, f(0), f('++'), f(0), f(0), f(0), f(0), f('+++')],
[f('++'), f('++'), f('++'), f('++'), f('++'), f('++'), f(0), f(0), f('++'), f('+++'), f('++'), f('+++'), f(0), f('+++'), None, f(0), f('+++'), f(0), f(0), f('++'), f('+++')],
[f(0), f(0), f(0), f(0), f(0), f(0), f(0), f(0), f(0), f('+++'), f(0), f('+++'), f(0), f(0), f(0), None, f(0), f(0), f(0), f(0), f(0)],
[f('++'), f('++'), f(0), f(0), f(0), f(0), f('++'), f(0), f(0), f('+++'), f(0), f('++'), f(0), f('++'), f('+++'), f('+++'), None, f(0), f(0), f('+++'), f('+++')],
[f(0), f('+++'), f('++'), f('+++'), f('+++'), f('+++'), f('+++'), f('+++'), f('+++'), f('++'), f(0), f(0), f(0), f('+++'), f('+++'), f(0), f('+++'), None, f(0), f('+++'), f('+++')],
[f('++'), f(0), f(0), f(0), f(0), f(0), f(0), f(0), f(0), f('++'), f(0), f('++'), f('++'), f(0), f(0), f(0), f(0), f(0), None, f(0), f('+++')],
[f('++'), f('++'), f('++'), f('++'), f('++'), f('++'), f(0), f(0), f('++'), f('+++'), f('++'), f('+++'), f(0), f('+++'), f('+++'), f(0), f('+++'), f(0), f(0), None, f('+++')],
[f('+++'), f(0), f(0), f('++'), f('+++'), f('+++'), f('+++'), f('+++'), f(0), f('+++'), f('+++'), f('++'), f('+++'), f('+++'), f('+++'), f(0), f('+++'), f('+++'), f('+++'), f('+++'), None]]
