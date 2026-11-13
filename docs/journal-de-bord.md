# Journal de bord – Équipe 13

**Cours :** INF4197 – Cloud Computing (ENSPY) 
**Membres de l'équipe :**
* **KAMDOM NGUETCHESSI Merveille Prisca** (Matricule : `26Q795`) – Compte VM : `prisca`
* **DJOUKOUO MBE-DOH Adriana Dasilva** (Matricule : `26Q894`) – Compte VM : `adriana`
* **TABI-CHU Peter Collins** (Matricule : `26Q911`) – Compte VM : `collins`

> *Ce journal retrace chronologiquement les actions menées par chaque membre, les choix techniques validés collectivement, ainsi que les blocages rencontrés et leurs résolutions.*

---

## TP 0 – Choix de la VM, déploiement et configuration Git

### Séance 1 – 11/11/2026 : Étude comparative des offres Cloud
* **Répartition de la veille tarifaire et technique entre les membres :**
  * **Prisca (`prisca`) :** Analyse de l'offre **Hetzner Cloud** (gabarit CX42, régions Allemagne/Finlande, politique KYC et latence).
  * **Adriana (`adriana`) :** Analyse de l'offre **Scaleway** (gabarit DEV1-L, coûts additionnels du disque et de l'IPv4).
  * **Collins (`collins`) :** Analyse de l'offre **Contabo** (gabarit Cloud VPS 4, modalités de paiement PayPal et inclusion de l'IPv4).
* **Constats principaux :**
  * Chez Scaleway, le tarif de base affiché pour l'instance `DEV1-L` n'inclut ni le stockage disque ni l'adresse IPv4 publique, ce qui alourdit sensiblement la facture mensuelle.
  * Le choix d'un fournisseur acceptant PayPal sans blocage bancaire depuis le Cameroun s'impose comme un critère déterminant pour le groupe.

---

### Séance 2 – 13/11/2026 : Commande, sécurisation de la VM et mise en place Git
*(Séance réalisée en visioconférence collective, avec exécution principale de l'administration initiale par **Collins**, puis configuration individuelle des espaces utilisateurs par **Prisca** et **Adriana**).*

#### 1. Provisionnement et accès initial (Collins)
* **Décision finale :** Validation de l'offre **Contabo – Cloud VPS 4** (4 vCPU, 8 Gio RAM, 100 Gio SSD NVMe, région Union européenne / Allemagne). Un projet préliminaire ouvert chez Hetzner a été abandonné sans création d'instance.
* **Règlement :** Paiement initial effectué par PayPal à hauteur de **7,50 €** (soit **5 152 FCFA**, incluant les frais de mise en service) pour un contrat mensuel reconductible à **5,50 € / mois**.
* **Authentification SSH :** Génération d'une paire de clés Ed25519 dédiée au cours (`~/.ssh/inf4197_ed25519`) et vérification de l'empreinte cryptographique du serveur lors de la première connexion : 
  `SHA256:uuoULx2HRaZEM4D03Tjx2uz/D546GQn9CaBQ5pt96eI`.

#### 2. Durcissement réseau et système (Collins)
* **Configuration du pare-feu Contabo :** Ouverture stricte du port **TCP 22** (SSH) et du protocole **ICMP** (Ping) ; blocage par défaut de tout autre trafic entrant.
* **Gestion des utilisateurs :** Création des trois comptes nominatifs (`collins`, `prisca`, `adriana`), ajout au groupe `sudo`, déploiement de leurs clés publiques respectives et validation des accès individuels.
* **Sécurisation SSH :** Désactivation complète de l'authentification par mot de passe dans `/etc/ssh/sshd_config.d/00-inf4197.conf`.
* **Préparation de l'environnement :** Mise à jour complète du système (`apt full-upgrade`), configuration du nom d'hôte (`inf4197-e13`) et du fuseau horaire (`Africa/Douala`), installation des outils requis (`git`, `curl`, `jq`, `htop`, `tree`, `unzip`, `python3-venv`, `apache2-utils`), suivie d'un redémarrage propre.
* **Inventaire matériel et réseau :** Relevé complet des caractéristiques système et mesures de latence consignés dans `docs/architecture.md`.

#### 3. Configuration GitHub et travail collaboratif sur la VM (Équipe complète)
* **Initialisation du dépôt :** Création du dépôt privé `inf4197-equipe-13` structuré selon le modèle du polycopié, avec ajout des collaborateurs.
* **Configuration individuelle sur la VM :** Génération d'une clé SSH Ed25519 propre à chaque membre directement sous sa session utilisateur sur la VM (`~/.ssh/id_ed25519`), liaison aux comptes GitHub personnels, clonage du dépôt dans chaque espace personnel (`~/inf4197-equipe-13`) et création de branches dédiées (`tp0-prisca`, etc.) pour isoler les contributions avant fusion (*Pull Request*) vers `main`.

---

### Écarts constatés par rapport à l'énoncé

| Écart identifié | Cause technique / organisationnelle | Mesure corrective appliquée |
| --- | --- | --- |
| **VM provisionnée avec mot de passe `root`** | Le formulaire de commande Contabo impose la définition d'un mot de passe `root` et ne permet pas l'injection directe d'une clé SSH à la création. | Injection immédiate de la clé publique via `ssh-copy-id`, suivie de la désactivation stricte de l'authentification par mot de passe dans `sshd_config`. |
| **Absence d'alerte automatique de budget** | L'espace client Contabo ne dispose pas de mécanisme natif de seuil d'alerte financière. | Choix d'un contrat à tarif mensuel fixe sans dépassement (5,50 €) et programmation d'un rappel calendrier avant la fin du 5ᵉ mois. |
| **Dépôt modèle de l'enseignant inaccessible** | Le lien vers le dépôt modèle (*template*) n'était pas encore disponible au moment du démarrage du TP. | Création manuelle de l'arborescence complète (`README.md`, `docs/`) conformément aux spécifications du polycopié et notification envoyée à l'enseignant. |

---

### Journal des incidents et résolutions

| Problème rencontré | Diagnostic / Cause | Solution mise en œuvre |
| --- | --- | --- |
| **Erreur `Could not resolve hostname inf4197-root`** | Le bloc d'alias SSH avait été rédigé dans `~/.ssh/config` sans être sauvegardé correctement. | Réécriture propre du bloc de configuration via `cat >> ~/.ssh/config` et validation immédiate avec la commande `ssh -G inf4197-root`. |
| **Absence de réponse au `ping` vers la VM** | Le pare-feu réseau bloquait les requêtes ICMP par défaut et n'avait pas encore été rattaché à l'instance nouvellement créée. | Association explicite du profil de pare-feu à la VM dans le panneau Contabo et ajout d'une règle entrante autorisant le trafic **ICMP / Ping**. |
| **Confusion et échecs lors du clonage GitHub sur la VM** | Confusion initiale entre les clés SSH de connexion à la VM (générées sur les PC locaux) et les clés SSH d'authentification vers GitHub (à générer depuis chaque compte personnel sur la VM), entraînant des refus de permission lors du clonage et des `push`. | Génération d'une clé SSH dédiée (`ssh-keygen -t ed25519`) sous chaque session utilisateur de la VM (`prisca`, `collins`, `adriana`), ajout de la clé publique dans *GitHub > Settings > SSH keys*, test via `ssh -T git@github.com`, puis clonage du dépôt dans le répertoire personnel (`~/inf4197-equipe-13`). |
| **Déconnexions SSH brutales (`Broken pipe`) en cours d'édition** | Micro-coupures de la connexion Internet locale interrompant le tunnel SSH entre le poste client et le serveur distant. 
