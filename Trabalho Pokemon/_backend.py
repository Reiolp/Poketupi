pokemon = {
    "Ararazul": {
        "nome": "Ararazul",
        "tipo": ["Grass", "Flying"],
        "numero": 1,
        "stats": {"hp": 100, "def": 30, "speed": 70},
        "efetividade": [
            {"Fraqueza2x": {"Fire", "Flying", "Poison", "Rock"}, "Fraqueza4x": {"Ice"}},
            {"Resistencia2x": {"Fighting", "Water"}, "Resistencia4x": {"Grass"}},
            {"Imunidade": None}
        ],
        "moveset": [
            {"nome": "Leaf Blade", "dano": 60, "precisao": 95, "tipo": "Grass", "efeito": None},
            {"nome": "Air Slash", "dano": 50, "precisao": 95, "tipo": "Flying", "efeito": {"nome": "Flinch", "chance": 20}},
            {"nome": "Roost", "dano": 0, "precisao": 100, "tipo": "Flying", "efeito": {"nome": "Heal", "chance": 100}},
            {"nome": "Hurricane", "dano": 85, "precisao": 70, "tipo": "Flying", "efeito": None}
        ]
    },
    "Bojarro": {
        "nome": "Bojarro",
        "tipo": ["Ground", "Flying"],
        "numero": 2,
        "stats": {"hp": 100, "def": 30, "speed": 100},
        "efetividade": [
            {"Fraqueza2x": {"Water"}, "Fraqueza4x": {"Ice"}},
            {"Resistencia2x": {"Bug", "Fighting", "Poison"}, "Resistencia4x": {None}},
            {"Imunidade": {"Electric", "Ground"}}
        ],
        "moveset": [
            {"nome": "Earthquake", "dano": 60, "precisao": 100, "tipo": "Ground", "efeito": None},
            {"nome": "Aerial Ace", "dano": 40, "precisao": 100, "tipo": "Flying", "efeito": None},
            {"nome": "Stone Edge", "dano": 70, "precisao": 80, "tipo": "Rock", "efeito": None},
            {"nome": "U-turn", "dano": 50, "precisao": 100, "tipo": "Bug", "efeito": None}
        ]
    },
    "Cafasma": {
        "nome": "Cafasma",
        "tipo": ["Ghost", "Fire"],
        "numero": 3,
        "stats": {"hp": 100, "def": 25, "speed": 70},
        "efetividade": [
            {"Fraqueza2x": {"Water", "Rock", "Ghost"}, "Fraqueza4x": None},
            {"Resistencia2x": {"Fire", "Grass", "Ice", "Steel", "Fairy", "Poison"}, "Resistencia4x": None},
            {"Imunidade": {"Normal", "Fighting"}}
        ],
        "moveset": [
            {"nome": "Shadow Ball", "dano": 55, "precisao": 95, "tipo": "Ghost", "efeito": {"nome": "Lower Defense", "chance": 20}},
            {"nome": "Flamethrower", "dano": 60, "precisao": 90, "tipo": "Fire", "efeito": {"nome": "Burn", "chance": 10}},
            {"nome": "Will-O-Wisp", "dano": 0, "precisao": 85, "tipo": "Fire", "efeito": {"nome": "Burn", "chance": 100}},
            {"nome": "Hex", "dano": 50, "precisao": 100, "tipo": "Ghost", "efeito": None}
        ]
    },
    "Capilorde": {
        "nome": "Capilorde",
        "tipo": ["Water", "Rock"],
        "numero": 4,
        "stats": {"hp": 100, "def": 50, "speed": 110},
        "efetividade": [
            {"Fraqueza2x": {"Grass", "Electric", "Fighting", "Ground"}, "Fraqueza4x": None},
            {"Resistencia2x": {"Fire", "Ice", "Flying", "Normal", "Poison"}, "Resistencia4x": None},
            {"Imunidade": None}
        ],
        "moveset": [
            {"nome": "Surf", "dano": 60, "precisao": 95, "tipo": "Water", "efeito": None},
            {"nome": "Rock Slide", "dano": 50, "precisao": 90, "tipo": "Rock", "efeito": {"nome": "Flinch", "chance": 20}},
            {"nome": "Aqua Jet", "dano": 40, "precisao": 100, "tipo": "Water", "efeito": {"nome": "Priority Attack", "chance": 100}},
            {"nome": "Ice Beam", "dano": 55, "precisao": 90, "tipo": "Ice", "efeito": {"nome": "Freeze", "chance": 10}}
        ]
    },
    "Cobrata": {
        "nome": "Cobrata",
        "tipo": ["Fire", "Dark"],
        "numero": 5,
        "stats": {"hp": 100, "def": 45, "speed": 30},
        "efetividade": [
            {"Fraqueza2x": {"Fighting", "Ground", "Rock", "Water"}, "Fraqueza4x": None},
            {"Resistencia2x": {"Fire", "Grass", "Ice", "Dark", "Ghost", "Steel"}, "Resistencia4x": None},
            {"Imunidade": {"Psychic"}}
        ],
        "moveset": [
            {"nome": "Fire Fang", "dano": 50, "precisao": 95, "tipo": "Fire", "efeito": {"nome": "Burn", "chance": 10}},
            {"nome": "Crunch", "dano": 50, "precisao": 100, "tipo": "Dark", "efeito": {"nome": "Lower Defense", "chance": 20}},
            {"nome": "Flame Charge", "dano": 40, "precisao": 100, "tipo": "Fire", "efeito": None},
            {"nome": "Will-O-Wisp", "dano": 0, "precisao": 85, "tipo": "Fire", "efeito": {"nome": "Burn", "chance": 100}}
        ]
    },
    "Jacarevac": {
        "nome": "Jacarevac",
        "tipo": ["Water"],
        "numero": 6,
        "stats": {"hp": 100, "def": 30, "speed": 102},
        "efetividade": [
            {"Fraqueza2x": {"Electric", "Grass"}, "Fraqueza4x": None},
            {"Resistencia2x": {"Fire", "Water", "Ice", "Steel"}, "Resistencia4x": None},
            {"Imunidade": None}
        ],
        "moveset": [
            {"nome": "Waterfall", "dano": 50, "precisao": 95, "tipo": "Water", "efeito": {"nome": "Flinch", "chance": 20}},
            {"nome": "Aqua Jet", "dano": 40, "precisao": 100, "tipo": "Water", "efeito": {"nome": "Priority Attack", "chance": 100}},
            {"nome": "Crunch", "dano": 50, "precisao": 100, "tipo": "Dark", "efeito": {"nome": "Lower Defense", "chance": 20}},
            {"nome": "Ice Fang", "dano": 45, "precisao": 95, "tipo": "Ice", "efeito": {"nome": "Freeze", "chance": 10}}
        ]
    },
    "Lutandua": {
        "nome": "Lutandua",
        "tipo": ["Ground", "Fighting"],
        "numero": 7,
        "stats": {"hp": 100, "def": 35, "speed": 120},
        "efetividade": [
            {"Fraqueza2x": {"Water", "Flying", "Grass", "Psychic", "Ice", "Fairy"}, "Fraqueza4x": None},
            {"Resistencia2x": {"Bug", "Poison", "Rock"}, "Resistencia4x": None},
            {"Imunidade": {"Electric"}}
        ],
        "moveset": [
            {"nome": "Close Combat", "dano": 65, "precisao": 95, "tipo": "Fighting", "efeito": {"nome": "Self Lower Defense", "chance": 100}},
            {"nome": "Earthquake", "dano": 60, "precisao": 100, "tipo": "Ground", "efeito": None},
            {"nome": "Stone Edge", "dano": 70, "precisao": 80, "tipo": "Rock", "efeito": None},
            {"nome": "Bulk Up", "dano": 0, "precisao": 100, "tipo": "Fighting", "efeito": {"nome": "Buff", "chance": 100}}
        ]
    },
    "Douraleao": {
        "nome": "Douraleao",
        "tipo": ["Fire", "Steel"],
        "numero": 8,
        "stats": {"hp": 100, "def": 40, "speed": 55},
        "efetividade": [
            {"Fraqueza2x": {"Water", "Fighting"}, "Fraqueza4x": {"Ground"}},
            {"Resistencia2x": {"Normal", "Flying", "Psychic", "Bug", "Ice", "Dragon", "Steel", "Fairy"}, "Resistencia4x": {"Grass"}},
            {"Imunidade": {"Poison"}}
        ],
        "moveset": [
            {"nome": "Flash Cannon", "dano": 55, "precisao": 95, "tipo": "Steel", "efeito": {"nome": "Lower Defense", "chance": 10}},
            {"nome": "Flamethrower", "dano": 60, "precisao": 90, "tipo": "Fire", "efeito": {"nome": "Burn", "chance": 10}},
            {"nome": "Iron Defense", "dano": 0, "precisao": 100, "tipo": "Steel", "efeito": {"nome": "Buff", "chance": 100}},
            {"nome": "Lava Plume", "dano": 60, "precisao": 100, "tipo": "Fire", "efeito": {"nome": "Burn", "chance": 30}}
        ]
    },
    "Piropira": {
        "nome": "Piropira",
        "tipo": ["Grass", "Fire"],
        "numero": 9,
        "stats": {"hp": 100, "def": 35, "speed": 81},
        "efetividade": [
            {"Fraqueza2x": {"Flying", "Poison", "Rock"}, "Fraqueza4x": None},
            {"Resistencia2x": {"Electric", "Steel", "Fairy"}, "Resistencia4x": {"Grass"}},
            {"Imunidade": None}
        ],
        "moveset": [
            {"nome": "Energy Ball", "dano": 55, "precisao": 95, "tipo": "Grass", "efeito": None},
            {"nome": "Flame Charge", "dano": 40, "precisao": 100, "tipo": "Fire", "efeito": {"nome": "Raise Speed", "chance": 100}},
            {"nome": "Sunny Day", "dano": 0, "precisao": 100, "tipo": "Fire", "efeito": {"nome": "Buff", "chance": 100}},
            {"nome": "Solar Beam", "dano": 70, "precisao": 80, "tipo": "Grass", "efeito": None}
        ]
    },
    "Pistolin": {
        "nome": "Pistolin",
        "tipo": ["Fighting", "Flying"],
        "numero": 10,
        "stats": {"hp": 100, "def": 40, "speed": 80},
        "efetividade": [
            {"Fraqueza2x": {"Electric", "Flying", "Fairy", "Psychic", "Ice"}, "Fraqueza4x": None},
            {"Resistencia2x": {"Bug", "Fighting", "Grass"}, "Resistencia4x": None},
            {"Imunidade": {"Ground"}}
        ],
        "moveset": [
            {"nome": "Close Combat", "dano": 65, "precisao": 95, "tipo": "Fighting", "efeito": {"nome": "Self Lower Defense", "chance": 100}},
            {"nome": "Brave Bird", "dano": 70, "precisao": 100, "tipo": "Flying", "efeito": {"nome": "Recoil", "chance": 100}},
            {"nome": "Roost", "dano": 0, "precisao": 100, "tipo": "Flying", "efeito": {"nome": "Heal", "chance": 100}},
            {"nome": "Bulk Up", "dano": 0, "precisao": 100, "tipo": "Fighting", "efeito": {"nome": "Buff", "chance": 100}}
        ]
    },
    "Sacere": {
        "nome": "Sacere",
        "tipo": ["Flying", "Psychic"],
        "numero": 11,
        "stats": {"hp": 100, "def": 35, "speed": 70},
        "efetividade": [
            {"Fraqueza2x": {"Dark", "Ghost", "Electric", "Ice", "Rock"}, "Fraqueza4x": None},
            {"Resistencia2x": {"Fighting", "Grass", "Psychic"}, "Resistencia4x": None},
            {"Imunidade": {"Ground"}}
        ],
        "moveset": [
            {"nome": "Psychic", "dano": 60, "precisao": 95, "tipo": "Psychic", "efeito": {"nome": "Lower Defense", "chance": 10}},
            {"nome": "Air Slash", "dano": 50, "precisao": 95, "tipo": "Flying", "efeito": {"nome": "Flinch", "chance": 20}},
            {"nome": "Calm Mind", "dano": 0, "precisao": 100, "tipo": "Psychic", "efeito": {"nome": "Buff", "chance": 100}},
            {"nome": "Reflect", "dano": 0, "precisao": 100, "tipo": "Psychic", "efeito": {"nome": "Buff Defense", "chance": 100}}
        ]
    },
    "Viramelo": {
        "nome": "Viramelo",
        "tipo": ["Normal", "Psychic"],
        "numero": 12,
        "stats": {"hp": 100, "def": 40, "speed": 60},
        "efetividade": [
            {"Fraqueza2x": {"Bug", "Dark", "Ghost"}, "Fraqueza4x": None},
            {"Resistencia2x": {"Psychic"}, "Resistencia4x": None},
            {"Imunidade": {"Ghost"}}
        ],
        "moveset": [
            {"nome": "Hyper Voice", "dano": 60, "precisao": 100, "tipo": "Normal", "efeito": None},
            {"nome": "Psychic", "dano": 60, "precisao": 95, "tipo": "Psychic", "efeito": {"nome": "Lower Defense", "chance": 10}},
            {"nome": "Calm Mind", "dano": 0, "precisao": 100, "tipo": "Psychic", "efeito": {"nome": "Buff", "chance": 100}},
            {"nome": "Recover", "dano": 0, "precisao": 100, "tipo": "Normal", "efeito": {"nome": "Heal", "chance": 100}}
        ]
    }
}
