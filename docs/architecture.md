# Architecture et inventaire technique – Équipe 13

**Cours :** INF4197 – Cloud Computing (ENSPY) 
**Membres de l'équipe :**
* **KAMDOM NGUETCHESSI Merveille Prisca** (Matricule : `26Q795`) – Compte VM : `prisca`
* **DJOUKOUO MBE-DOH Adriana Dasilva** (Matricule : `26Q894`) – Compte VM : `adriana`
* **TABI-CHU Peter Collins** (Matricule : `26Q911`) – Compte VM : `collins`

**Hôte :** `inf4197-e13` (Contabo Cloud VPS 4 – Union européenne / Allemagne) 
**Date du relevé :** 13 novembre 2026

---

## 1. Vue d'ensemble de l'architecture réseau et accès

L'infrastructure repose sur une machine virtuelle unique hébergée en Allemagne chez Contabo, protégée par un pare-feu réseau restrictif et administrée à distance via SSH par clés asymétriques Ed25519 nominatives.

```text
Postes clients des membres (Yaoundé, Cameroun)
   ├── collins  (clé SSH dédiée)
   ├── prisca   (clé SSH dédiée)
   └── adriana  (clé SSH dédiée)
          │
          │  Tunnel SSH chiffré (TCP 22) – Latence moyenne : ~172 ms
          ▼
┌─────────────────────────────────────────────────────────────┐
│  Pare-feu réseau Contabo                                    │
│  • Entrant autorisé : TCP 22 (SSH), ICMP (Ping)             │
│  • Entrant bloqué   : Tout autre trafic (politique DROP)    │
└─────────────────────────────────────────────────────────────┘
          │
          ▼
┌─────────────────────────────────────────────────────────────┐
│  VM : inf4197-e13 (Contabo Cloud VPS 4 – UE / Allemagne)    │
│  • OS          : Ubuntu 24.04.5 LTS (Noble Numbat)          │
│  • Ressources  : 4 vCPU AMD EPYC / 7,8 Gio RAM / 100 Gio SSD│
│  • Hyperviseur : KVM (virtualisation matérielle complète)   │
│  • Réseau      : IPv4 publique (/17) + IPv6 (/64) sur eth0  │
└─────────────────────────────────────────────────────────────┘
```

---

## 2. Inventaire matériel et système (TP 0 – Étape 6)

Le tableau ci-dessous confronte les spécifications souscrites lors de la commande avec les valeurs réelles extraites directement depuis le système d'exploitation de la VM (`inf4197-e13`).

| Composant | Gabarit commandé | Valeur constatée sur la VM | Commande de vérification | Analyse et observation technique |
| --- | --- | --- | --- | --- |
| **Système d'exploitation** | Ubuntu 24.04 | **Ubuntu 24.04.5 LTS** *(Noble Numbat)* | `cat /etc/os-release` | Version LTS à jour et strictement conforme au cahier des charges. |
| **Processeur (vCPU)** | 4 vCPU | **4 × AMD EPYC Processor** *(with IBPB)* | `lscpu` | Cœurs virtuels alloués sur une architecture serveur AMD EPYC avec protection matérielle *IBPB*. |
| **Hyperviseur** | – | **KVM** *(virtualisation complète)* | `systemd-detect-virt` | Virtualisation matérielle complète (`full`) assurée par l'hyperviseur Linux KVM. |
| **Mémoire vive (RAM)** | 8 Gio | **7,8 Gio** total *(7,4 Gio disponibles)* | `free -h` | Conforme : l'écart de ~200 Mio correspond à l'empreinte réservée par le noyau Linux au démarrage. |
| **Mémoire d'échange (Swap)** | – | **0 B** *(aucun espace swap configuré)* | `free -h` | Configuration optimale en vue du déploiement de Kubernetes (TP 4), qui exige la désactivation du swap. |
| **Stockage principal** | 100 Gio SSD | **100 Gio** (`sda`) / **96 Gio** utiles (`/`) | `lsblk` / `df -h /` | `ROTA=0` confirme un support non rotatif (SSD) ; modèle virtuel `QEMU HARDDISK` (3 % utilisés). |
| **Périphérique secondaire** | – | **4 Mio** (`sr0` – `QEMU DVD-ROM`) | `lsblk` | Lecteur optique virtuel (`ROTA=1`) utilisé par Contabo pour l'initialisation via *cloud-init*. |
| **Interfaces réseau** | 1 IPv4 publique | **IPv4** `169.58.252.3/17` + **IPv6** `/64` | `ip -br address` | Interface `eth0` active avec connectivité double pile (IPv4 publique et bloc IPv6 `2a02:c207:...`). |
| **Contention CPU (`st`)** | – | **0 %** sur 5 échantillons consécutifs | `vmstat 2 5` | Aucun temps processeur volé (*steal time* nul) : l'hôte physique n'était pas saturé lors du test. |

---

## 3. Mesures de performance et latence réseau

Deux séries de tests ICMP ont été conduites le 13/11/2026 afin d'évaluer la réactivité de la machine virtuelle depuis le Cameroun ainsi que sa propre connectivité vers le réseau mondial.

| Trajet réseau testé | Paquets | Perte | Latence Min | Latence Moyenne | Latence Max | Écart-type (`mdev`) |
| --- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Yaoundé → VM (`inf4197-e13`)** | 10 | 0 % | **146,00 ms** | **172,00 ms** | **232,00 ms** | – |
| **VM (`inf4197-e13`) → `8.8.8.8` (Google DNS)** | 10 | 0 % | **2,95 ms** | **3,67 ms** | **6,14 ms** | **1,06 ms** |

**Interprétation :**
* La latence moyenne d'environ **172 ms** perçue depuis Yaoundé s'explique par la distance géographique intercontinentale et le routage des câbles sous-marins entre l'Afrique centrale et l'Europe. Cette latence reste tout à fait fluide pour une administration en ligne de commande via SSH.
* Depuis la VM vers Internet (`8.8.8.8`), la latence chute à **3,67 ms** sans aucune perte de paquet, démontrant l'excellente interconnexion du centre de données allemand aux dorsales Internet européennes.

---

## 4. Réponses aux questions d'analyse du TP 0

1. **Conformité du gabarit livré et nature de l'hyperviseur :** 
   Les ressources constatées correspondent exactement à l'offre souscrite : 4 vCPU AMD EPYC, 8 Gio de RAM nominaux (7,8 Gio visibles par l'espace utilisateur après réservation noyau) et un disque SSD de 100 Gio (96 Gio disponibles sur la partition racine `/` après formatage). L'environnement s'exécute au-dessus de l'hyperviseur **KVM** en mode de virtualisation complète (`full`).

2. **Analyse comparative des latences (Yaoundé vs VM) :** 
   L'écart entre les **~172 ms** depuis Yaoundé et les **3,67 ms** depuis la VM vers `8.8.8.8` montre que le goulot d'étranglement se situe uniquement sur le transit réseau international entre le Cameroun et l'Europe. La machine virtuelle elle-même dispose d'une connectivité réseau à très faible latence, idéale pour télécharger des paquets, des images de conteneurs ou héberger des services web.

3. **Intérêt des comptes nominatifs personnels (`collins`, `prisca`, `adriana`) :** 
   La création d'un compte individuel par membre (plutôt que le partage du compte `root`) garantit la **traçabilité et l'imputabilité** des actions via les journaux système (`/var/log/auth.log` et historique des commandes). Sur le plan de la sécurité, cette séparation permet également de révoquer instantanément la clé SSH d'un seul utilisateur en cas de compromission de son poste, sans perturber l'accès des autres membres de l'équipe.

4. **Impact de l'arrêt de la VM sur la facturation chez Contabo :** 
   Contrairement aux fournisseurs facturant à l'heure ou à la seconde sur les ressources actives, Contabo fonctionne sur un modèle de **forfait mensuel prépayé** avec renouvellement automatique. Éteindre la machine virtuelle (`shutdown` ou arrêt depuis le panneau client) libère les cycles CPU mais maintient la réservation de l'adresse IPv4 et du stockage SSD : **la facturation continue donc intégralement**. Pour interrompre les prélèvements à la fin du semestre, il est impératif de résilier explicitement le contrat depuis l'espace client avant la date d'échéance.
