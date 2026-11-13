# INF4197 – Cloud Computing · Équipe 13

Dépôt de l'équipe 13 pour les TP du cours INF4197 (M1-SI, ENSPY, 2026–2027, Dr Adamou Hamza).

## Membres

| Membre | Identifiant sur la VM | Compte GitHub |
| --- | --- | --- |
| Collins TABI-CHU | `collins` | @À_COMPLÉTER |
| Prisca KAMDOM | `prisca` | @À_COMPLÉTER |
| Adriana DJOUKOU | `adriana` | @À_COMPLÉTER |

## Infrastructure

| Élément | Valeur |
| --- | --- |
| Fournisseur | Contabo |
| Offre | Cloud VPS 4 (4 vCPU, 8 Go RAM, 100 Go SSD) |
| Région | Union européenne (Allemagne) |
| Système | Ubuntu Server 24.04 LTS |
| Nom de la VM | `inf4197-e13` |
| Accès | SSH par clé uniquement, un compte personnel par membre |

L'adresse IP, les mots de passe et les clés privées ne sont jamais versionnés dans ce dépôt.

## Organisation du dépôt

```
.
├── README.md
├── .gitignore
└── docs/
    ├── choix-vm-et-budget.md   # TP 0 : comparaison des offres, grille pondérée, budget
    ├── journal-de-bord.md      # complété à chaque séance : quoi, qui, échecs et pourquoi
    └── architecture.md         # inventaire de la VM et schéma de l'infrastructure
```

## Règles de travail

1. Aucun secret n'est versionné (voir `.gitignore`).
2. Une branche par TP (`tp0-vm`, `tp1-securite`, `tp2-compose`, …), fusionnée par une demande de fusion relue par un autre membre.
3. Le journal de bord est complété à chaque séance.

## Avancement

| TP | Branche | État |
| --- | --- | --- |
| TP 0 – VM et budget | `tp0-vm` | en cours |
