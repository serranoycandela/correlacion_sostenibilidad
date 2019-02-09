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
