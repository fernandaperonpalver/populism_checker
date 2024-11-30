import pandas as pd

brazilian_dictionary = [
    "a elite",
    "sistema corrupto",
    "a grande mídia",
    "os poderosos",
    "eles contra o povo",
    "instituições falidas",
    "corte suprema",
    "STF",
    "o povo de bem",
    "a voz do povo",
    "a verdadeira maioria",
    "o trabalhador",
    "o Brasil acima de tudo",
    "defender a pátria",
    "brasileiros de verdade",
    "nossa cultura está em perigo",
    "socialistas",
    "comunistas",
    "globalistas",
    "traidores da pátria",
    "mamadores do dinheiro público",
    "falsos líderes",
    "moral e bons costumes",
    "família tradicional",
    "contra a ideologia de gênero",
    "corrupção generalizada",
    "defender nossas fronteiras",
    "recuperar o Brasil",
    "interferência externa",
    "petralhas",
    "comunismo fantasma",
    "esquerdopatas",
    "cidadão de bem",
    "povo",
    "trabalhadores",
    "sistema",
    "arrogante",
    "às custas da coletividade",
    "às custas dos trabalhadores",
    "às custas dos cidadãos",
    "banqueiros",
    "políticos de carreira",
    "população esclarecida",
    "patrões",
    "desconectado do cidadão",
    "os cidadãos estão fartos",
    "os cidadãos exigem",
    "vontade popular",
    "burocratas",
    "desastre",
    "tradição brasileira",
    "diktat (imposição autoritária)",
    "diletantismo",
    "democracia direta",
    "audacioso",
    "cidadãos médios",
    "simples cidadão",
    "torre de marfim",
    "elites",
    "indignação popular",
    "establishment",
    "partido estabelecido",
    "burocrata europeu",
    "corrupção (filz)",
    "financiadores",
    "audácia",
    "dominação estrangeira",
    "dirigentes sem poder real",
    "para o nosso povo",
    "pela maioria",
    "pelas pessoas comuns",
    "tutela",
    "contra o povo brasileiro",
    "povo comum",
    "ganância",
    "globalistas",
    "cidadãos decentes",
    "pessoas decentes",
    "pessoas razoáveis",
    "favoritismo",
    "cidadãos estão cansados",
    "arrogância",
    "insanidade",
    "mafia",
    "manipulação",
    "corrupção",
    "dominação do sistema",
    "partido do sistema",
    "plebiscitário",
    "povo soberano",
    "vontade popular",
    "falhas políticas",
    "propaganda",
    "pseudo-partidos",
    "distante da realidade",
    "classes altas",
    "povo honesto",
    "cidadãos comuns",
    "maioria silenciosa",
    "traição ao povo",
    "sem espinha dorsal",
    "sistema falho",
]


brazilian_dictionary.extend(
    [
        "cidadãos decentes",
        "pessoas decentes",
        "ganância",
        "manipulação",
        "massa silenciosa",
        "elite global",
        "classes dominantes",
        "traição ao povo",
        "sistemas falidos",
        "partido do sistema",
        "povo soberano",
        "democracia plebiscitária",
        "políticos corruptos",
        "fraqueza moral",
    ]
)


brazilian_dictionary.extend(
    [
        "povo soberano",
        "sistema falho",
        "manipulação",
        "elite global",
        "nós",
        "ganância",
        "corrupção",
        "políticos corruptos",
        "vontade popular",
        "dominação do sistema",
        "massa silenciosa",
        "partido do sistema",
        "democracia plebiscitária",
        "fraude eleitoral",
        "sistema injusto",
    ]
)

brazilian_dictionary.extend(
    [
        "povo de Deus",
        "esquerdistas",
        "comunistas",
        "nós contra eles",
        "família tradicional",
        "valores judaico-cristãos",
        "guerra do bem contra o mal",
        "ideologia de gênero",
        "Deus acima de todos",
        "Brasil acima de tudo",
        "inimigos da pátria",
    ]
)


brazilian_dictionary.extend(
    [
        "populismo",
        "povo",
        "elite",
        "dualidade",
        "revolução",
        "libertação",
        "nacionalismo",
        "liderança carismática",
        "antissistema",
        "retórica maniqueísta",
        "soberania",
        "democracia",
        "desigualdade",
        "justiça",
        "massa",
        "movimento",
        "resistência",
        "hegemonia",
        "discurso moral",
        "redistribuição de renda",
        "oposição",
        "establishment",
        "valores compartilhados",
        "mobilização popular",
        "consenso",
        "aliança",
        "confronto",
        "latifundiário",
        "mercado interno",
        "política de identidade",
    ]
)

brazilian_dictionary = set(brazilian_dictionary)