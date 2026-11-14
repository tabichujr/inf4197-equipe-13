# INF4197 – Cloud Computing · Équipe 13

Dépôt officiel de l'Équipe 13 pour les travaux pratiques du cours **INF4197 – Cloud Computing** (M1-SI, ENSPY, Année académique 2026–2027).

---

##  Membres de l'équipe

| Membre | Matricule | Identifiant sur la VM | 
| :--- | :---: | :---: |
| **TABI-CHU Peter Collins** | `26Q911` | `collins` | 
| **KAMDOM NGUETCHESSI Merveille Prisca** | `26Q795` | `prisca` | 
| **DJOUKOUO MBE-DOH Adriana Dasilva** | `26Q894` | `adriana` | 
---

##  Infrastructure retenue

| Élément technique | Spécification / Valeur |
| :--- | :--- |
| **Fournisseur Cloud** | Contabo |
| **Offre souscrite** | Cloud VPS 4 (4 vCPU AMD EPYC, 8 Gio RAM, 100 Gio SSD NVMe) |
| **Région / Datacenter** | Union européenne (Allemagne) |
| **Système d'exploitation** | Ubuntu Server 24.04.5 LTS (Noble Numbat) |
| **Nom d'hôte de la VM** | `inf4197-e13` (IP publique : `169.58.252.3`) |
| **Politique d'accès** | Authentification SSH par clés Ed25519 nominatives uniquement ; aucun accès par mot de passe ni par le compte `root`. |

> **Sécurité :** L'adresse IP publique, les mots de passe et les paires de clés cryptographiques privées ne sont jamais versionnés dans ce dépôt.

---

##  Organisation du dépôt

```text
.
├── README.md
├── .gitignore
└── docs/
    ├── choix-vm-et-budget.md    # TP 0 : étude comparative, grille pondérée et budget semestriel
    ├── journal-de-bord.md       # Suivi chronologique : actions, responsabilités et résolutions
    └── architecture.md          # Inventaire matériel, hyperviseur KVM, latences et schémas
```

---

##  Règles de travail collaboratif

1. **Sécurité des données :** Aucun secret, mot de passe ou clé privée ne doit être commité (vérification via `.gitignore`).
2. **Isolation des contributions :** Utilisation systématique d'une branche dédiée par TP (ex. `tp0-prisca`, `tp1-securite-docker`, …). Toute modification fait l'objet d'une *Pull Request* (demande de fusion) relue et validée par un autre membre de l'équipe.
3. **Traçabilité :** Le journal de bord et les rapports d'architecture sont mis à jour et validés à chaque étape clé.

---

## État d'avancement des Travaux Pratiques

| Travail Pratique | Branche associée | État d'avancement |
| :--- | :---: | :---: |
| **TP 0 – Choix de la VM, budget & architecture** | `tp0-vm` / `tp0-prisca` | **Terminé et fusionné [ OK ]** |
| **TP 1 – Durcissement SSH, pare-feu & Docker** | `tp1-securite-docker` | **En cours** |
