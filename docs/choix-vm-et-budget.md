# TP 0 – Choix de la VM et budget

Gabarit demandé : 4 vCPU / 8 Gio de RAM / 80 Gio de disque, Ubuntu 24.04, IPv4 publique.
Prix relevés sur les pages officielles des fournisseurs aux dates indiquées.

> Les valeurs marquées « à vérifier » ou « à mesurer » doivent être complétées par le membre responsable de chaque fournisseur avant la fusion.

## 1. Relevé des offres

| Critère | Contabo – Cloud VPS 4 | Hetzner – CX33 | Scaleway – DEV1-L |
| --- | --- | --- | --- |
| Responsable du relevé | [membre] | [membre] | [membre] |
| Date du relevé | 13/11/2026 | à compléter | 11/11/2026 |
| Gabarit | 4 vCPU, 8 Go, 100 Go SSD | 4 vCPU, 8 Go, 80 Go SSD | 4 vCPU, 8 Go, 400 Mbps (disque en sus) |
| Prix mensuel | 5,50 € / mois (contrat 1 mois) | ~6,50–7 € / mois (à vérifier) | 31,27 € / mois (0,04284 €/h) |
| Frais d'installation | ~2 € (une fois) | aucun | aucun |
| Disque 80 Go | inclus (100 Go) | inclus | 7,59 € / mois (Block Storage 5K, 0,000130 €/Go/h) |
| IPv4 publique | incluse | ~0,50 € / mois (à vérifier) | ~2,92 € / mois (à vérifier) |
| Trafic inclus | illimité, port 200 Mbit/s | 20 To / mois (UE) | sortant non facturé, 400 Mbps |
| Sauvegardes | Auto Backup payant ; 1 snapshot inclus | backups +20 % du prix ; snapshots payants | snapshots payants au Go |
| Pare-feu réseau | gratuit | gratuit | groupes de sécurité |
| Moyens de paiement | carte, PayPal | carte, PayPal (vérification stricte) | carte bancaire |
| Régions | UE (Allemagne), UK, USA, Asie… | Allemagne, Finlande, USA, Singapour | Paris, Amsterdam, Varsovie, Milan |
| Vérification d'identité | aucune demandée lors de notre commande | souvent pièce d'identité ; refus fréquents hors Europe | carte obligatoire, pièce parfois demandée |
| Facturation | contrat prépayé, renouvellement automatique | à l'heure, plafonnée au mois | à l'heure |
| Latence depuis Yaoundé | min 146 / moy 172 / max 232 ms (VM, 13/11) | à mesurer (`fsn1-speed.hetzner.com`) | à mesurer (`ping.online.net`) |

## 2. Coût total sur le semestre (~5 mois)

| Fournisseur | Calcul | Total | Par membre |
| --- | --- | --- | --- |
| Contabo | 7,50 € (1er mois, frais inclus) + 4 × 5,50 € | **29,50 €** (~19 350 FCFA) | ~6 450 FCFA |
| Hetzner | 5 × ~7,50 € (VM + IPv4) | ~37,50 € (à vérifier) | ~8 200 FCFA |
| Scaleway | 5 × (31,27 + 7,59 + 2,92) € | ~209 € | ~45 700 FCFA |

Premier paiement Contabo réel : 7,50 € le 13/11/2026 par PayPal, soit 5 152 FCFA. Le taux appliqué (≈ 687 FCFA/€) dépasse la parité fixe (655,957 FCFA/€) : la conversion PayPal coûte environ 4 à 5 %.

## 3. Grille pondérée

Poids fixés par l'équipe avant la notation (total 100). Notes de 0 à 5.
Score = Σ (note × poids) / (5 × Σ poids) × 100.

| Critère | Poids | Contabo | Hetzner | Scaleway | Justification |
| --- | --- | --- | --- | --- | --- |
| Coût total sur le semestre | 30 | 5 | 4 | 1 | 29,50 € / ~37,50 € / ~209 € |
| Moyens de paiement / ouverture du compte | 20 | 5 | 3 | 2 | PayPal accepté et commande réussie / vérification stricte / carte obligatoire |
| Latence depuis Yaoundé | 15 | 3 | 3 | 3 | ~170 ms vers l'Allemagne ; à confirmer par les mesures |
| Sauvegardes | 10 | 2 | 3 | 3 | option payante, 1 snapshot / backups automatiques +20 % / snapshots au Go |
| Documentation et support | 10 | 3 | 5 | 4 | |
| Réversibilité | 10 | 2 | 5 | 5 | contrat prépayé à résilier / facturation à l'heure |
| Localisation / conformité | 5 | 3 | 3 | 4 | UE (RGPD) pour les trois |
| **Score** | **100** | **76,0** | **74,0** | **51,0** | |

> Notes proposées à valider en équipe.

## 4. Analyse de sensibilité (poids du coût ± 10)

| Poids du coût | Contabo | Hetzner | Scaleway |
| --- | --- | --- | --- |
| 20 | 73,3 | 73,3 | 54,4 |
| 30 (retenu) | 76,0 | 74,0 | 51,0 |
| 40 | 78,2 | 74,5 | 48,2 |

Contabo reste premier dès que le coût pèse au moins 30 %. À 20 %, Contabo et Hetzner sont à égalité : le choix est donc sensible au poids du coût. Ce qui départage alors les deux offres est le critère « paiement / ouverture du compte », décisif pour une équipe d'étudiants au Cameroun. Scaleway est dernier dans tous les cas.

## 5. Décision

**Fournisseur retenu : Contabo, Cloud VPS 4, région UE (Allemagne), contrat mensuel, paiement PayPal.**

Justification : coût le plus bas sur le semestre, paiement PayPal accepté sans blocage, gabarit supérieur au minimum (100 Go). Limites assumées : contrat prépayé à résilier avant la fin du semestre, sauvegardes payantes, performances potentiellement moins régulières (surveillance de la colonne `st` de `vmstat`).

Hypothèses : budget ≈ 30 € pour le semestre partagé entre 3 membres ; résiliation du contrat prévue en fin de semestre.
