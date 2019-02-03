
matrix_list = [
    [None, '+++', '++', '+', '+++', '+++', '+', '++', '+++', '+', '+++', '+', 0, 0, 0, '+', '+', '+', '+++', None, None,],
    ['++', None, 0, '+', 0, '+++', '+', '+', '+', '++', '+', '+++', 0, 0, '+', 0, 0, '+', '++', '+', '++',],
    ['+', '++', None, '++', '++', '+++', 0, 0, '++', '+++', 0, '++', '+', 0, '+', '+', 0, '++', '+++', '+', '++',],
    ['+', '+', '+++', None, '+', '+++', '+', '+', '+++', '+++', '+', '+', '+', 0, '+', 0, 0, 0, '++', '+', '+',],
    ['+++', 0, 0, '+', None, '+++', '+', '+', '+++', '+++', '+', '++', 0, 0, '+', '+', 0, '+', '++', '++', '+++',],
    ['+', '+++', '+++', '+++', '+++', None, '+', 0, '+++', '++', '+', 0, 0, 0, '+', 0, 0, 0, '--', '++', '+++',],
    ['++', '+', 0, '+', 0, 0, None, '+++', 0, 0, '+++', '+', 0, 0, '+', '+', 0, '+', '+', '+++', '+',],
    ['++', '+', 0, 0, 0, 0, 0, None, '++', 0, '+++', '+', 0, 0, '+', '+', 0, '+', '++', '+++', '+',],
    [0, 0, 0, 0, 0, '+++', 0, 0, None, 0, 0, '+++', 0, 0, '+', 0, 0, '+', '+', '+++', '++',],
    [0, '++', '+++', '+++', 0, '+', 0, '+', '+', None, '++', '+', 0, 0, '+', 0, 0, '+', '++', '+', '+++',],
    ['++', '++', 0, '+', 0, 0, '+', '++', 0, '+', None, '++', '+', 0, '++', '+++', '+', '+++', '+++', '+++', '+++',],
    [0, '++', '+', '+', '+', '+++', '+', '+', 0, 0, '+++', None, 0, 0, '+', '+++', 0, '+', '+++', '+', 0,],
    ['+++', '+++', '+++', '+++', '+++', '+++', '+++', '+++', '+++', '+++', '+++', '++', None, 0, '+++', 0, 0, '+++', '+++', '+++', '+++',],
    ['+', '+++', '+', '++', '+++', '+++', '+++', '+++', '+++', '+++', '+++', '+', '+', None, '+++', '+', 0, '+++', '++', '+++', '+',],
    [None, 0, 0, 0, 0, 0, '+', '+', 0, 0, '+', '+++', '+', 0, 0, None, '+++', '+', '+', '+++', '+++', '++']
    ['+', 0, 0, 0, 0, 0, 0, 0, 0, 0, '+++', '+', '+', '++', '+++', None, '+++', '++', '+++', '++', 0,],
    ['++', 0, 0, '+', 0, 0, 0, 0, 0, 0, '+', '++', '++', '+', 0, '+', None, 0, '++', '+++', 0,],
    ['++', '++', '++', '++', '++', '++', '++', '+', 0, '++', '+++', '+++', 0, '+', '+++', '+++', 0, None, '+++', '+++', 0,],
    ['+++', '++', '+', '+', '++', '--', '++', '+++', 0, '++', '+++', '++', 0, 0, '+', '+', 0, '+', None, '++', 0,],
    ['+++', 0, '+++', '+', '++', '+++', '+++', '+++', '+++', 0, '+++', '++', '+++', '+++', '+++', '+++', '+++', '+++', '+++', None, 0,],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '+++', 0, 0, '+', '++', 0, '+', '+++', 0,]
]

matrix_dict = {
    "Ordenamiento y planeación territorial sustentable (uso mixto del suelo, densificación acorde a la capacidad de carga del territorio)":
    [None, '+++', '++', '+', '+++', '+++', '+', '++', '+++', '+', '+++', '+', 0, 0, 0, '+', '+', '+', '+++', None, None,],
    "Edificaciones sustentables (Ecotecnias, diseño y materiales sustentables)":
    ['++', None, 0, '+', 0, '+++', '+', '+', '+', '++', '+', '+++', 0, 0, '+', 0, 0, '+', '++', '+', '++',],
    "Fomento de la economía circular (enfoque de ciclo de vida) y de mercados locales-regionales (proporción de actividades económicas y empleos “verdes”)":
    ['+', '++', None, '++', '++', '+++', 0, 0, '++', '+++', 0, '++', '+', 0, '+', '+', 0, '++', '+++', '+', '++',],
    "Acciones para una industria limpia (producción y circulación sustentable y responsabilidad extendida)":
    ['+', '+', '+++', None, '+', '+++', '+', '+', '+++', '+++', '+', '+', '+', 0, '+', 0, 0, 0, '++', '+', '+',],
    "Movilidad sustentable (masiva, pública y crecientemente no motorizada, además de la regulación del transporte de carga)":
    ['+++', 0, 0, '+', None, '+++', '+', '+', '+++', '+++', '+', '++', 0, 0, '+', '+', 0, '+', '++', '++', '+++',],
    "Eficiencia energética y fomento a las energías renovables ":
    ['+', '+++', '+++', '+++', '+++', None, '+', 0, '+++', '++', '+', 0, 0, 0, '+', 0, 0, 0, '--', '++', '+++',],
    "Infraestructura verde-azul para la adaptación al cambio climático":
    ['++', '+', 0, '+', 0, 0, None, '+++', 0, 0, '+++', '+', 0, 0, '+', '+', 0, '+', '+', '+++', '+',],
    "Bienes ambientales - áreas verdes / adaptación urbana basada en ecosistemas":
    ['++', '+', 0, 0, 0, 0, 0, None, '++', 0, '+++', '+', 0, 0, '+', '+', 0, '+', '++', '+++', '+',],
    "Mitigación de la emisión de contaminantes atmosféricos / mejora de la calidad del aire (acciones para..)":
    [0, 0, 0, 0, 0, '+++', 0, 0, None, 0, 0, '+++', 0, 0, '+', 0, 0, '+', '+', '+++', '++',],
    "Gestión sustentable de residuos (RSU, especiales y peligrosos; incluye la cogeneración de energía)":
    [0, '++', '+++', '+++', 0, '+', 0, '+', '+', None, '++', '+', 0, 0, '+', 0, 0, '+', '++', '+', '+++',],
    "Gestión de riesgo de desastres y reducción de la vulnerabilidad al cambio climático":
    ['++', '++', 0, '+', 0, 0, '+', '++', 0, '+', None, '++', '+', 0, '++', '+++', '+', '+++', '+++', '+++', '+++',],
    "Reducción de la pobreza y mejora de la calidad de vida (acciones para…)":
    [0, '++', '+', '+', '+', '+++', '+', '+', 0, 0, '+++', None, 0, 0, '+', '+++', 0, '+', '+++', '+', 0,],
    "Financiamiento para acciones y proyectos en sustentabilidad urbana (local, estatal, nacional e internacional)":
    ['+++', '+++', '+++', '+++', '+++', '+++', '+++', '+++', '+++', '+++', '+++', '++', None, 0, '+++', 0, 0, '+++', '+++', '+++', '+++',],
    "Existencia de un presupuesto climático y seguros contra riesgos hidro-meteorológicos":
    ['+', '+++', '+', '++', '+++', '+++', '+++', '+++', '+++', '+++', '+++', '+', '+', None, '+++', '+', 0, '+++', '++', '+++', '+',],
    "Acciones de educación para el cambio climático y difusión para la sustentabilidad":
    [None, 0, 0, 0, 0, 0, '+', '+', 0, 0, '+', '+++', '+', 0, 0, None, '+++', '+', '+', '+++', '+++',
     '++'] # aguas, son 21!
    "Aumento en la participación social en el avance hacia la sustentabilidad, incluyente y justa":
    ['+', 0, 0, 0, 0, 0, 0, 0, 0, 0, '+++', '+', '+', '++', '+++', None, '+++', '++', '+++', '++', 0,],
    "Combate a la corrupción / aumento de la rendición de cuentas":
    ['++', 0, 0, '+', 0, 0, 0, 0, 0, 0, '+', '++', '++', '+', 0, '+', None, 0, '++', '+++', 0,],
    "Construcción de capacidades para la sustentabilidad urbana con perspectiva de género (incluye capacidades institucionales, empresariales y sociales)":
    ['++', '++', '++', '++', '++', '++', '++', '+', 0, '++', '+++', '+++', 0, '+', '+++', '+++', 0, None, '+++', '+++', 0,],
    "Mejora de la resiliencia urbana (biofísica y social del espacio urbano)":
    ['+++', '++', '+', '+', '++', '--', '++', '+++', 0, '++', '+++', '++', 0, 0, '+', '+', 0, '+', None, '++', 0,],
    "Fortalecimiento de la gobernanza del cambio climático":
    ['+++', 0, '+++', '+', '++', '+++', '+++', '+++', '+++', 0, '+++', '++', '+++', '+++', '+++', '+++', '+++', '+++', '+++', None, 0,],
    "Salud":
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '+++', 0, 0, '+', '++', 0, '+', '+++', 0,]
}



def test_update:
    v = CriteriaVector([.1,.3,.....],
                       matrix)
    v.update(criterion=1, delta=3)
    assert v.criteria == []

