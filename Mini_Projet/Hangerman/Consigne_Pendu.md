# Pendu - Jeu à Deux Joueurs

## Objectif
Un joueur pense à un mot. L'autre joueur doit le deviner en proposant des lettres.

## Comment Jouer

### Joueur 1 (Créateur du Mot)
- Pense à un mot
- Écris le nombre de lettres du mot
- Valide chaque lettre proposée par le Joueur 2

### Joueur 2 (Devineur)
- Propose une lettre à la fois
- Essaie de deviner le mot avant 6 erreurs
- Observe les lettres trouvées pour deviner

## Règles

1. Le mot doit avoir au minimum 4 lettres
2. Le Joueur 2 a le droit à 6 erreurs maximum
3. Chaque mauvaise lettre = 1 erreur
4. Les bonnes lettres ne comptent pas comme erreur
5. Pas de majuscules/minuscules (traiter pareil)
6. Pas de tirets ou accents dans les mots

## Déroulement

- Joueur 1 annonce le nombre de lettres: "Mon mot a 6 lettres"
- Joueur 2 propose une lettre: "E?"
- Joueur 1 dit oui ou non et affiche le mot avec les lettres trouvées
- On continue jusqu'à victoire ou 6 erreurs

## Victoire / Défaite

**Joueur 2 gagne** si le mot est trouvé avant 6 erreurs.

**Joueur 1 gagne** si Joueur 2 atteint 6 erreurs sans trouver le mot.

## Exemple

```
Joueur 1: "Mon mot a 5 lettres"
Affichage: _ _ _ _ _

Joueur 2: "E?"
Joueur 1: "Oui!" → _ _ _ E _

Joueur 2: "A?"
Joueur 1: "Non" (1 erreur)

Joueur 2: "O?"
Joueur 1: "Oui!" → _ O _ E _

... et ainsi de suite
```

Amusez-vous bien! 🎮