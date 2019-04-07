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
#
subcats3 = ["A1. Ordenamiento territorial y planeación urbana sustentable",
"A2. Edificaciones sustentables",
"A3. Industria limpia",
"A4. Movilidad urbana sustentable",
"A5. Eficiencia energética y renovables",
"A6. Infraestructura verde",
"A7. Conservación ambiental e hídrica y AbE",
"A8. Mitigación de GEI y calidad del aire",
"A9. Gestión integral de los residuos",
"A10. Resiliencia urbana",
"E1. Economía circular",
"E2. Reducción de la pobreza  y de la vulnerabilidad al cambio climático",
"E3. Financiamiento para la sustentabilidad urbana",
"S1. Educación para el cambio climático",
"S2. Participación social",
"S3. Mejoramiento de la salud pública",
"G1. Gestión integral del riesgo de desastres",
"G2. Presupuesto climático y  seguros contra riesgos hidro-meteorológicos",
"G3. Combate a la corrupción y rendición de cuentas",
"G4. Construcción de capacidades para sustentabilidad urbana con perspectiva de género",
"G5. Fortalecimiento de la gobernanza del cambio climático"]

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


tooltip = {"A1":"<html><head/><body><font size='5'><p><b>A1. Ordenamiento territorial y planeación urbana sustentable</p></b><p>El ordenamiento y la planeación urbana sustentable permiten delinear el tipo de espacio construido, las características y funciones de las edificaciones e infraestructura, así como las dinámicas urbanas en general. Son esenciales para reducir el riesgo de desastres, mejorar la calidad de vida, la inclusión social y en sí, fortalecer la adaptación al cambio climático y construir una resiliencia urbana cada vez más robusta.</p></font></body></html>",
"A2":"<html><head/><body><font size='5'><p><b>A2. Edificaciones sustentables</p></b><p>Las edificaciones de buena calidad, asequibles y bien localizadas proporcionan una base sólida para la adaptación al cambio climático en toda la ciudad y al mismo tiempo minimizan la exposición al riesgo y las pérdidas. La seguridad humana en cierta medida depende de buenas viviendas. Las políticas de vivienda sustentable pueden ser el espacio para los cobeneficios entre mitigación y adaptación.</p></font></body></html>",
"A3":"<html><head/><body><font size='5'><p><b>A3. Industria limpia</p></b><p>La calidad del aire en las ciudades y las emisiones de GEI dependen, en un buen porcentaje, de la actividad industrial. Una industria limpia contribuye a la reducciónde los GEI y por ende a la mitigación del cambio climático. Además, la innovación tecnológica para la adaptación es muy importante y proviene del sector industrial y de servicios. Diferentes acciones y medidas de gestióin sustentable de residuos dependen de la industria limpia.</p></font></body></html>",
"A4":"<html><head/><body><font size='5'><p><b>A4. Movilidad urbana sustentable</p></b><p>La movilidad sustentable trae importantes cobeneficios tanto en la capacidad que tiene una ciudad para hacer una buena gestión de riesgo de desastres y una eficiente respuesta a emergencias como para reducir el consumo de energía de vehículos motorizados y abatir las emisiones de GEI. La redistribución de la riqueza puede hacerse a través de esquemas de movilidad como el del metrobus de la ciudad de México.</p></font></body></html>",
"A5":"<html><head/><body><font size='5'><p><b>A5. Eficiencia energética y energías renovables.</p></b><p>La seguridad energética de una ciudad es central para su sustentabilidad y resiliencia. La seguridad energética puede estar amenazada por la reducción de la capacidad nacional de generación. Las emisiones de GEI pueden sustancialmente reducirse mediante el fomento al uso de energías renovables y a su amplia distribución en grupos de bajos ingresos. Esto a su vez provee condiciones para la reducción de la pobreza energética.</p></font></body></html>",
"A6":"<html><head/><body><font size='5'><p><b>A6. Infraestructura verde</p></b><p>La infraestructura verde es central en la adaptación al cambio climático al modular la temperatura y la escorrentía superficial. Esta infraestructura proporciona espacios para hacer una gestión de riesgo de inundaciones eficiente y con dividendos en grupos vulnerables. Asimismo, es un componente central para un ordenamiento ecológico del territorio y la adaptación basada en ecosistemas.</p></font></body></html>",
"A7":"<html><head/><body><font size='5'><p><b>A7. Conservación ambiental e hídrica y adaptación basada en ecosistemas</p></b><p>La adaptación urbana basada en ecosistemas, como una estrategia de adaptación al cambio climático, se enfoca no en árboles de calles y parques sino en el rol que los ecosistemas, sus servicios y la biodiversidad pueden tener en la reducción de la vulnerabilidad de la gente. La restauración ecosistémica contribuye a la sustentabilidad urbana al garantizar la recarga de acuíferos, tratamiento de aguas y captura de CO2.</p></font></body></html>",
"A8":"<html><head/><body><font size='5'><p><b>A8. Mitigación de GEI y calidad del aire</p></b><p>La eficiencia energética y el uso de energias renovables trae cobeneficios de mitigación del cambio climático al reducir GEI. La reducción de contaminantes atmosféricos no solo mejora la calidad del aire sino también se convierte en una estrategia de adaptación a largo plazo ya que puede contribuir a reducir los déficits de adaptación, el riesgo climático y amplía opciones.</p></font></body></html>",
"A9":"<html><head/><body><font size='5'><p><b>A9. Gestión integral de residuos</p></b><p>La gestión integral y sustentable de residuos, además de limitar la exportación de “males” ambientales a otros espacios territoriales y de disminuir las emisiones asociadas de GEI, puede ayudar también en la adaptación y resiliencia urbana al, por ejemplo, mantener limpios los sistemas de desagüe, mejorar la transformación de residuos en composta o materiales reutilizables o reciclables, y mejorar la calidad ambiental de los ecosistemas urbanos (lo que se vincula a la variable S.3). Para que tal gestión además abone en la reducción de la pobreza (variable E.2), debe dar cuenta tanto de los circuitos formales como informales de la gestión de los residuos para, desde ahí, plantear alianzas y construir espacios de colaboración con la población que vive de la gestión informal de los residuos (lo que pasa por avanzar en las variables G.4 y G.5).</p></font></body></html>",
"A10":"<html><head/><body><font size='5'><p><b>A10. Resiliencia urbana</p></b><p>La adaptación basada en ecosistemas ha probado ser clave en la construcción de la resiliencia urbana. Las soluciones basadas en la participación comunitaria pueden construir capital social y por ende mejorar la resiliencia urbana. Una adecuada gestión de riesgo de desastres donde participe las comunidades es una estrategia de resiliencia urbana.</p></font></body></html>",
"E1":"<html><head/><body><font size='5'><p><b>E1. Economía circular</p></b><p></p>La economía circular parte de reconocer que el modelo lineal de flujos de energía y materiales que caracterizan los procesos económicos contemporáneos ha llegado a su límite debido a los impactos acumulados que ha generado en la biósfera. Desde tal perspectiva, una economía circular urbana supone, además de mayores eficiencias en el uso de la energía y materiales, el “cierre” de flujos de materiales, ello a partir de la reducción, el rediseño y extensión de la vida útil de los productos, el reúso y el reciclaje (variable A.9). El avance de acciones para la conformación de una economía circular, estimula la creatividad, la innovación tecnológica y la conformación de toda una nueva economía que si es bien canalizada puede particularmente contribuir al avance de la variable E.2.</p></font></body></html>",
"E2":"<html><head/><body><font size='5'><p><b>E2. Reducción de la pobreza y vulnerabilidad al cambio climático</p></b><p>Esta variable proporciona diversos co-beneficios ambientales y de gobernanza. La reducción de la pobreza contribuye a la reducción de la vulnerabilidad y por ende del riesgo de desastres de origen hidrometeorológico y climático. Una ciudad incluyente que fomenta la participación democrática permite ser sensible a las demandas de los grupos de escasos recursos y es visible a las opiniones y visiones de los grupos marginados.</p></font></body></html>",
"E3":"<html><head/><body><font size='5'><p><b>E3. Financiamiento para la sustentabilidad urbana</p></b><p>Esta variable económica trae co-beneficios a 17 de 21 otras variables, de ahí su importancia. El financiamiento climático se ha convertido en una palanca que impulsa proyectos y acciones de mitigación y adaptación al cambio climático en las ciudades y trae cobeneficios en la construcción de la resiliencia.</p></font></body></html>",
"S1":"<html><head/><body><font size='5'><p><b>S1. Educación para el cambio climático</p></b><p>La educación y comunicación para la sustentabilidad urbana tiene como a uno de sus ejes centrales el combate al cambio climático a través de acciones concretas de mitigación y adaptación. Los individuos pueden participar de manera directa en la construcción de capacidades colectivas, en la transparencia y rendición de cuentas; es decir, para una buena gobernanza climática.</p></font></body></html>",
"S2":"<html><head/><body><font size='5'><p><b>S2. Participación social</p></b><p>El cambio de comportamiento colectivo implica no solo un cambio en la percepción del riesgo climático sino también en los  mecanismos y formas de participación social para garantizar la justicia climática de los habitantes de la ciudad. Esto puede proveer co-beneficios en el combate a la corrupción, en la rendición de cuentas y también en la reducción del riesgo climático.</p></font></body></html>",
"S3":"<html><head/><body><font size='5'><p><b>S3. Mejoramiento de la salud pública</p></b><p>Las medidas de la categoría “A”, pero también de la categoría “E”, impactan positivamente en la preservación y mejora de las funciones ecosistémicas y, consecuentemente en el mejoramiento de la salud pública. Otras medidas, como la movilidad no-motorizada de la mano de una planeación ad hoc urbana, fomentan un cambio en la vida sedentaria urbana lo que tiene importantes beneficios a la salud. La reducción de emisiones de GEI evita un costo asociado conocido como “costo social del carbono” el cual debe ser considerado en la toma de decisiones a escala local.</p></font></body></html>",
"G1":"<html><head/><body><font size='5'><p><b>G1. Gestión integral de riesgo de desastres.</p></b><p>Esta es una variable clave para la adaptación de la ciudad al cambio climático y proporciona diversos co-beneficios tanto ambientales como económicos. La gestión de riesgo de desastres es una base muy sólida para reducir la vulnerabilidad. La reducción de la pobreza y la participación social son condiciones sobre las cuales se puede constituir una eficiente gestión de riesgo de desastres.</p></font></body></html>",
"G2":"<html><head/><body><font size='5'><p><b>G2. Presupuesto climático y seguros contra riesgos hidro-meteorológicos.</p></b><p>Múltiples co-benficios pueden proporcionar los esquemas de aseguramiento contra riesgos hidrometeorológicos. La ciudades son muy atractivas para las empresas privadas e inversión. Las empresas privadas favorecen a aquellas ciudades que cuentan con infraestructura que funciona y con una amplia gama de servicios. El aseguramiento juega un papel central en garantizar la sustentabilidad tanto de las firmas como de la infraestructura urbana.</p></font></body></html>",
"G3":"<html><head/><body><font size='5'><p><b>G3. Combate a la corrupción y rendición de cuentas</p></b><p>El combate a la corrupción y la rendición de cuentas es central para avanzar hacia una gobernanza climática robusta en la que la actuación de los diversos actores de gobierno, económicos y de sociedad civil organizada sea efectivamente transparente, cumpla con el marco regulatorio establecido y haga un uso eficiente de los recursos. Dicho ejercicio puede además contribuir a identificar espacios de oportunidad para hacer rendir los recursos limitados con los que suelen operar los gobiernos locales. Esta variable se vincula especialmente con las variables G.3, G.4 y G.5, pero también con las S.1 y S.2.</p></font></body></html>",
"G4":"<html><head/><body><font size='5'><p><b>G4. Construcción de capacidades para la sustentabilidad urbana con perspectiva de género</p></b><p>Esta variable proporciona cobeneficios de diversa índole sobre todo cuando se trata de reducir las disparidades socio-económicas, las vulnerabilidades diferenciales y la construcción de capacidades locales frente al cambio climático. También se ha reconocido a nivel mundial que el diseño de políticas sensibles a las diferencias de género puede crear condiciones de mayor justicia climática.</p></font></body></html>",
"G5":"<html><head/><body><font size='5'><p><b>G5. Fortalecimiento de la gobernanza del cambio climático.</p></b><p>Las ciudades están compuestas por sistemas complejos e inter-dependientes que pueden potenciarse para contribuir a la adaptación al cambio climático a través de una gobernanza multinivel. La buena gobernanza facilita la mediación de políticas y decisiones entre todos los diferentes actores, esferas de influencia, fuentes de información y recursos, co-producción de conocimiento y aprendizaje a lo largo del tiempo (Revi et al 2014).</p></body></html>"}
