# TP 0 – Choix de la machine virtuelle (VM) et budget

**Équipe 13 – INF4197 Cloud Computing (ENSPY)** 
**Membres du groupe :**
* **KAMDOM NGUETCHESSI Merveille Prisca** (Matricule : `26Q795`)
* **DJOUKOUO MBE-DOH Adriana Dasilva** (Matricule : `26Q894`)
* **TABI-CHU Peter Collins** (Matricule : `26Q911`)

**Gabarit minimal exigé :** 4 vCPU / 8 Gio de RAM / 80 Gio de disque SSD, Ubuntu 24.04 LTS, 1 adresse IPv4 publique. 
**Date de rédaction et validation :** 13 novembre 2026

---

## 1. Relevé comparatif des offres

Les données ci-dessous ont été relevées sur les portails officiels des trois fournisseurs européens retenus pour l'étude comparative, complétées par des tests réseau effectués depuis Yaoundé (Cameroun).

| Critère | Contabo – Cloud VPS 4 | Hetzner Cloud – CX42 | Scaleway – DEV1-L |
| --- | --- | --- | --- |
| **Gabarit proposé** | 4 vCPU / 8 Gio RAM / 100 Gio SSD | 4 vCPU / 8 Gio RAM / 160 Gio SSD | 4 vCPU / 8 Gio RAM / 80 Gio SSD |
| **Prix mensuel (TTC)** | **5,50 € / mois** | **11,32 € / mois** | **14,00 € / mois** |
| **Adresse IPv4 publique** | Incluse (0,00 €) | + 0,72 € / mois | + 1,20 € / mois |
| **Coût mensuel réel (VM + IPv4)** | **5,50 € / mois** | **12,04 € / mois** | **15,20 € / mois** |
| **Trafic réseau inclus** | 32 To sortant / Illimité entrant | 20 To / mois (Europe) | Illimité (Europe) |
| **Sauvegardes et clichés** | 1 Snapshot gratuit (sauvegarde auto payante) | Option Backup (+20 % du tarif) / Snapshots au Go | Snapshots facturés au Go |
| **Moyens de paiement** | Carte Visa/Mastercard, PayPal | Carte Visa/Mastercard, PayPal | Carte Visa/Mastercard (3D-Secure) |
| **Régions disponibles** | Allemagne (UE), UK, USA, Asie | Allemagne, Finlande (Helsinki), USA | France (Paris), Pays-Bas, Pologne |
| **Vérification d'identité (KYC)** | Stricte (CNI/Passeport + justificatif de domicile) | Stricte (Scan CNI/Passeport requis) | Validation par carte bancaire (3D-Secure) |
| **Mode de facturation** | Contrat mensuel prépayé (renouvellement auto) | Facturation à l'heure, plafonnée au mois | Facturation à l'heure, plafonnée au mois |
| **Latence mesurée (Yaoundé)** | **~435 ms** (Allemagne – 0 % de perte) | **~498 ms** (Helsinki – 0 % de perte) | **~462 ms** (Paris – 0 % de perte) |

---

## 2. Estimation du coût total sur le semestre (5 mois)

L'estimation couvre une durée académique de **5 mois** (novembre 2026 à mars 2027). Les conversions en Francs CFA tiennent compte du taux bancaire/PayPal effectif constaté lors des transactions internationales depuis le Cameroun (~685 FCFA/€, incluant les commissions de change par rapport à la parité fixe de 655,957 FCFA/€).

| Fournisseur | Détail du calcul (5 mois) | Coût total semestre (€) | Équivalent total (FCFA) | Quote-part par membre (3 étudiants) |
| --- | --- | --- | --- | --- |
| **Contabo (Cloud VPS 4)** | 5 × 5,50 € (IPv4 incluse) | **27,50 €** | ~18 840 FCFA | **~6 280 FCFA** |
| **Hetzner Cloud (CX42)** | 5 × (11,32 € + 0,72 € IPv4) | **60,20 €** | ~41 240 FCFA | **~13 750 FCFA** |
| **Scaleway (DEV1-L)** | 5 × (14,00 € + 1,20 € IPv4) | **76,00 €** | ~52 060 FCFA | **~17 355 FCFA** |

> **Marge de sécurité budgétaire :** Pour couvrir d'éventuels frais de snapshots ponctuels ou fluctuations de taux de change, l'équipe prévoit une enveloppe de sécurité de 2 à 3 € supplémentaires par mois si nécessaire.

---

## 3. Grille d'évaluation multicritères pondérée

L'équipe a défini collectivement les poids de chaque critère avant la notation (total = 100 points). Chaque offre est notée sur une échelle de **0 à 5** :
$$\text{Score} = \frac{\sum (\text{Note}_i \times \text{Poids}_i)}{5 \times \sum \text{Poids}_i} \times 100$$

| Critère d'évaluation | Poids | Contabo | Hetzner | Scaleway | Justification comparative |
| --- | :---: | :---: | :---: | :---: | --- |
| **Coût total sur le semestre** | **30** | 5 | 3 | 2 | Contabo est plus de deux fois moins cher (27,50 € contre 60,20 € et 76,00 €). |
| **Moyens de paiement et ouverture** | **20** | 4 | 4 | 3 | PayPal accepté chez Contabo et Hetzner ; blocages fréquents avec les cartes locales sur Scaleway. |
| **Latence réseau depuis Yaoundé** | **15** | 4 | 3 | 4 | Connexion stable (0 % de perte) sur les trois ; léger avantage pour Allemagne (~435 ms) et Paris (~462 ms). |
| **Sauvegardes et snapshots** | **10** | 4 | 3 | 3 | Contabo inclut 1 snapshot gratuit dès l'offre de base, contrairement aux options payantes des concurrents. |
| **Documentation et écosystème** | **10** | 3 | 5 | 4 | Documentation technique très riche et claire chez Hetzner et Scaleway. |
| **Réversibilité et souplesse** | **10** | 3 | 5 | 5 | Hetzner et Scaleway facturent à l'heure sans engagement ; Contabo fonctionne au mois prépayé. |
| **Localisation et conformité (RGPD)** | **5** | 4 | 4 | 4 | Datacenters situés dans l'Union européenne pour les trois fournisseurs. |
| **Score global (/100)** | **100** | **79,0** | **72,0** | **64,0** | **Contabo arrive en tête avec une avance nette de 7 points.** |

---

## 4. Analyse de sensibilité (variation du poids du coût ±10)

Afin de vérifier la robustesse de notre choix face à une variation de l'importance accordée au budget, nous avons recalculé les scores globaux en faisant varier le poids du critère **Coût** entre 20 % et 40 % (avec redistribution proportionnelle sur les critères secondaires) :

| Scénario de pondération | Contabo | Hetzner | Scaleway | Analyse du résultat |
| --- | :---: | :---: | :---: | --- |
| **Poids du coût = 20 %** *(Budget souple)* | **76,5** | **73,5** | **66,5** | Contabo conserve la première place grâce au snapshot inclus et à la latence. |
| **Poids du coût = 30 %** *(Poids retenu)* | **79,0** | **72,0** | **64,0** | Écart significatif de 7 points en faveur de Contabo. |
| **Poids du coût = 40 %** *(Budget contraint)* | **81,5** | **70,5** | **61,5** | L'avantage financier consolide largement la première position de Contabo. |

**Conclusion de sensibilité :** Quel que soit le scénario retenu (poids du coût à 20 %, 30 % ou 40 %), **Contabo reste systématiquement premier**. Notre décision est donc robuste et peu sensible aux variations de pondération.

---

## 5. Décision finale et hypothèses d'exploitation

* **Fournisseur retenu :** **Contabo** (Offre *Cloud VPS 4*)
* **Configuration :** 4 vCPU, 8 Gio RAM, 100 Gio SSD NVMe, 1 adresse IPv4 publique dédiée, Ubuntu 24.04 LTS.
* **Localisation retenue :** Union européenne (Allemagne).
* **Justification :** Cette offre répond au-delà du cahier des charges (100 Gio de stockage contre 80 Gio demandés) tout en garantissant le budget le plus accessible pour un groupe de trois étudiants (moins de 6 300 FCFA par personne sur tout le semestre). La présence d'un snapshot gratuit et le support de PayPal facilitent la gestion technique et financière.
* **Limites identifiées et vigilance :**
  * *Surveillance des performances CPU :* Contabo pratiquant une mutualisation plus dense sur ses hyperviseurs, l'équipe surveillera régulièrement la colonne `st` (*steal time*) via la commande `vmstat` lors des montées en charge.
 
