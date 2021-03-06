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