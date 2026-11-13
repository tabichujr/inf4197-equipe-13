# Journal de bord – Équipe 13

À compléter à chaque séance : ce qui a été fait, par qui, ce qui a échoué et pourquoi.

## TP 0 – VM et budget

### 11/11/2026 – Étude des offres

- Répartition des fournisseurs à étudier : Hetzner, Scaleway, Contabo (un membre chacun). [préciser qui]
- Relevé des prix Scaleway sur les pages officielles : l'instance DEV1-L n'inclut ni le disque ni l'IPv4 (+34 % sur le prix affiché).

### 13/11/2026 – Choix, commande et création de la VM (Collins, avec l'équipe en visioconférence)

- Décision : Contabo, Cloud VPS 4 (voir `choix-vm-et-budget.md`). Un projet avait d'abord été ouvert chez Hetzner, puis abandonné sans aucune ressource créée.
- Commande payée par PayPal : 7,50 € (5 152 FCFA), contrat mensuel ; prix mensuel ensuite 5,50 €.
- Création d'une clé SSH dédiée au cours (`~/.ssh/inf4197_ed25519`) sur le poste de Collins, sans toucher aux clés existantes.
- Empreinte du serveur vérifiée à la première connexion : `SHA256:uuoULx2HRaZEM4D03Tjx2uz/D546GQn9CaBQ5pt96eI`.
- Pare-feu Contabo : TCP 22 accepté, ICMP (ping) accepté, tout le reste bloqué.
- Comptes personnels créés : `collins`, `prisca`, `adriana`, membres du groupe `sudo`, connexion par clé testée pour chacun.
- Authentification SSH par mot de passe désactivée (`/etc/ssh/sshd_config.d/00-inf4197.conf`).
- Mise à jour complète, nom d'hôte `inf4197-e13`, fuseau `Africa/Douala`, outils installés, redémarrage.
- Inventaire de la VM réalisé (voir `architecture.md`).

### Écarts par rapport à l'énoncé

| Écart | Cause | Mesure prise |
| --- | --- | --- |
| VM créée avec un mot de passe root | Le formulaire de commande Contabo impose un mot de passe et ne permet pas de coller une clé | Clé ajoutée avec `ssh-copy-id`, puis authentification par mot de passe désactivée |
| Pas d'alerte de budget | Contabo n'en propose pas | Prix mensuel fixe (5,50 €), date de renouvellement notée |
| Dépôt modèle de l'enseignant indisponible | Lien non communiqué | Dépôt créé par l'équipe selon la structure du polycopié ; demande envoyée à l'enseignant par e-mail |

### Problèmes rencontrés

| Problème | Cause | Solution |
| --- | --- | --- |
| `Could not resolve hostname inf4197-root` | Bloc ajouté dans `~/.ssh/config` mais non enregistré | Ajout du bloc avec `cat >> ~/.ssh/config` puis vérification avec `ssh -G` |
| Ping vers la VM sans réponse | Le pare-feu bloquait l'ICMP ; il n'était d'abord affecté à aucune VM | Affectation du pare-feu à la VM et ajout d'une règle « Ping / ICMP » |
