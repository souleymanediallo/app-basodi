COLOR_CHOICES = [
    ('NE', 'Noir'),
    ('NS', 'Marron'),
    ('TE', 'Beige'),
    ('BE', 'Gris'),
    ('ST', 'Blanc'),
    ('ST', 'Bleu'),
    ('ST', 'Bleu pétrole'),
    ('ST', 'Turquoise'),
    ('ST', 'Vert'),
    ('ST', 'Vert olive'),
    ('ST', 'Jaune'),
    ('ST', 'Orange'),
    ('ST', 'Rouge'),
    ('ST', 'Rose'),
    ('ST', 'Violet'),
    ('ST', 'Doré'),
    ('ST', 'Argenté'),
    ('ST', 'Multicolore')
]

CONDITION_CHOICES = [
    ('NE', 'Neuf avec étiquettes'),
    ('NS', 'Neuf sans étiquettes'),
    ('TE', 'Très bon état'),
    ('BE', 'Bon état'),
    ('ST', 'Satisfaisant'),
]

CATEGORY_CHOICES = [
    ('Mariage', (
        ('VEF', 'Femmes'),
        ('CHF', 'Hommes'),
        ('CHF', 'Mariés'),
        ('SAF', 'Ensembles'),
        ('BEF', 'Enfants'),
        ('BEF', 'Accessoires'),
    )
     ),
    ('Femmes', (
        ('VEF', 'Vêtements'),
        ('CHF', 'Chaussures'),
        ('SAF', 'Sacs'),
        ('BEF', 'Beauté'),
    )
     ),
    ('Hommes', (
        ('VEH', 'Vêtements'),
        ('CHH', 'Chaussures'),
        ('SAH', 'Sacs'),
        ('SOH', 'Soins'),
    )
     ),
    ('Enfants', (
        ('FI', 'Filles'),
        ('GA', 'Garçons'),
        ('JE', 'Jeux et Jouets'),
        ('SO', 'Soins bébé'),
        ('AC', 'Accessoires'),
    )
     ),
    ('Maison', (
        ('AR', 'Arts'),
        ('DE', 'Décorations'),
        ('LI', 'Livres'),
        ('AC', 'Accessoires'),
    )
     ),
]