# Architecture et inventaire

## Vue d'ensemble

```
Postes des membres (Yaoundé)
  collins / prisca / adriana
        │  SSH (TCP 22), clé personnelle, ~170 ms
        ▼
Pare-feu Contabo : TCP 22 et ICMP acceptés, reste bloqué
        │
        ▼
VM inf4197-e13 – Contabo Cloud VPS 4 – UE (Allemagne)
Ubuntu 24.04.5 LTS – 4 vCPU / 7,8 Gi / 100 Go SSD – KVM
```

## Inventaire de la VM (TP 0 – étape 6)

Relevé du 13/11/2026, VM `inf4197-e13`.

| Élément | Commandé | Constaté | Commentaire |
| --- | --- | --- | --- |
| Système | Ubuntu 24.04 | Ubuntu 24.04.5 LTS (Noble Numbat) | conforme |
| vCPU | 4 | 4 × AMD EPYC Processor | vCPU partagés sur un serveur physique AMD EPYC |
| Hyperviseur | – | KVM, virtualisation complète (`systemd-detect-virt` : kvm) | |
| Mémoire | 8 Go | 7,8 Gi | le noyau réserve une petite partie |
| Swap | – | aucun (0 B) | sans gêne pour Kubernetes (TP 4) |
| Disque | 100 Go SSD | 100 G (`sda`), 96 G utilisables sur `/` | ROTA = 0 : disque non rotatif ; « QEMU HARDDISK » = disque virtuel |
| Autre périphérique | – | `sr0` 4 M (DVD-ROM QEMU) | lecteur virtuel de configuration initiale (cloud-init) |
| Réseau | 1 IPv4 | 1 IPv4 (/17) et 1 IPv6 (/64) | IPv6 fournie en plus |
| Temps volé (`st`) | – | 0 % sur 5 mesures | aucune contention au moment du relevé |

## Latence

| Mesure | Min | Moyenne | Max |
| --- | --- | --- | --- |
| Yaoundé → VM (ping, 13/11/2026) | 146 ms | 172 ms | 232 ms |
| VM → 8.8.8.8 (10 paquets) | 2,95 ms | 3,67 ms | 6,14 ms |

La latence perçue depuis Yaoundé vient de la distance et du routage international. Depuis la VM, l'accès à Internet est très rapide, car le centre de données européen est directement connecté aux grands réseaux.

## Réponses aux questions du TP 0

1. **Gabarit livré et hyperviseur.** Le gabarit livré correspond au gabarit acheté (4 vCPU, 7,8 Gi utilisables sur 8 Go, 100 Go SSD). L'hyperviseur est KVM.
2. **Latence.** Environ 172 ms depuis Yaoundé contre 3,7 ms depuis la VM vers 8.8.8.8 : la distance et le routage international pèsent sur l'accès depuis le Cameroun, pas sur la connectivité de la VM.
3. **Comptes personnels.** Ils assurent la traçabilité (qui a fait quoi, journaux par utilisateur) et permettent de retirer l'accès d'une seule personne sans toucher aux autres.
4. **Facturation.** Chez Contabo, arrêter la VM ne réduit pas la facture : le contrat mensuel est prépayé et renouvelé automatiquement. Pour ne plus payer, il faut résilier le contrat avant la fin de la période en cours.
