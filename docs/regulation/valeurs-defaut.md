---
title: "Valeurs par défaut et courbes de chauffe (SystaComfort)"
description: "Tableau complet des valeurs par défaut, courbe de chauffe, données techniques du régulateur."
sources: [THF1777 p. 39-41]
---

# Valeurs par défaut et courbes de chauffe (SystaComfort)

## 11. Valeurs par défaut

Le tableau suivant donne les valeurs par défaut réglées en usine. Notez-y toutes les valeurs réglées lors de la première mise en service et remettez la documentation complète à l'utilisateur. Les chapitres 11.1 à 11.3 contiennent des instructions pour régler les valeurs du circuit de chauffage selon le type de chauffage. Tous les réglages ne sont pas disponibles pour toutes les installations.

| Sous-menu | Paramètre | Valeur par défaut | Réglé | Modifié |
|---|---|---|---|---|
| Données de l'installation pour le circuit de chauffage | Point de base | 35 °C | | |
| | Courbe chauffe | 1,3 K/K | | |
| | Régulation selon | la temp. extérieure | | |
| | Temp max départ | 70 °C | | |
| | Temp. limite chauffage | 20 °C | | |
| | Temp. Limite réduite | 10 °C | | |
| | Temp ext. antigel | 2 °C | | |
| | Constante Échauff | 120 min | | |
| | Temp. ambiante | 0 K/K | | |
| | Optimisation courbe. | Non | | |
| | Surchauffe Chaudière | 0 K | | |
| | Ecart Cir. chauf. | 20 K | | |
| | Régime min. pompe PHK | 100 % | | |
| | Durée mélangeur | 2 min | | |
| | Réglage proportionnel | 5 K | | |
| | Durée post-chauffage | 30 min | | |
| | Eau chaude Prioritaire | Non | | |
| | Température int. | 0 K | | |
| Données de l'installation pour le 2e circuit de chauffage | Point de base | 35 °C | | |
| | Courbe chauffe | 1,3 K/K | | |
| | Régulation selon | la temp. extérieure | | |
| | Temp max départ | 70 °C | | |
| | Temp. limite chauffage | 20 °C | | |
| | Temp. Limite réduite | 10 °C | | |
| | Temp ext. antigel | 2 °C | | |
| | Constante Échauff | 120 min | | |
| | Temp. ambiante | 0 K/K | | |
| | Optimisation courbe. | Non | | |
| | Surchauffe Chaudière | 0 K | | |
| | Ecart Cir. chauf. | 20 K | | |
| | Régime min. pompe PHK | 100 % | | |
| | Durée mélangeur | 2 min | | |
| | Réglage proportionnel | 5 K | | |
| | Durée post-chauffage | 30 min | | |
| | Eau chaude Prioritaire | Non | | |
| | Température int. | 0 K | | |
| Données de l'installation Tampon/Chaudière | Retour pompes PK / LP | 1 min | | |
| | Max. tampon | 90 | | |
| | Min. tampon | 0 | | |
| | Type de tampon OPTIMA/EXPRESSO | Oui | | |
| | Temp. max. eau chaude | 85 °C | | |
| | Diff. commutation Chaudière | 5 K | | |
| | Durée min. chaudière | 5 min | | |
| | Arrêt TA chaudière | 40 °C | | |
| | Régime min. pompe PK | 25 % | | |
| Données de l'installation Circulation | Durée de Retour PZI | 3 min | | |
| | Durée blocage Des touche | 15 min | | |
| | Diff. commutation pompe PZI | 5 K | | |
| | Date | | | |
| | Signature | | | |

<small>Source : THF1777 p. 39</small>

### 11.1 Réglage de la courbe de chauffe

Facteur de raideur (K/K) selon la zone climatique :

| Système de chauffage (conception) | Pied de la courbe (°C) | −16 °C | −14 °C | −12 °C | −10 °C | −8 °C |
|---|---|---|---|---|---|---|
| 40/30 | 20 | 0,6 | 0,7 | 0,8 | 0,8 | 0,9 |
| 40/30 | 25 | 0,4 | 0,5 | 0,6 | 0,6 | 0,7 |
| 50/35 | 20 | 0,9 | 1,0 | 1,1 | 1,2 | 1,3 |
| 50/35 | 25 | 0,7 | 0,8 | 0,9 | 1,0 | 1,1 |
| 70/50 | 30 | 1,3 | 1,4 | 1,5 | 1,6 | 1,7 |
| 70/50 | 35 | 1,1 | 1,2 | 1,3 | 1,4 | 1,5 |
| 90/70 | 30 | 2,0 | 2,1 | 2,2 | 2,3 | 2,4 |
| 90/70 | 35 | 1,9 | 2,0 | 2,1 | 2,2 | 2,3 |

Exemple : système 70/50, zone climatique −10 °C :

- pied de la courbe = 30 °C et facteur de raideur = 1,6 K/K, ou
- pied de la courbe = 35 °C et facteur de raideur = 1,4 K/K.

<small>Source : THF1777 p. 40</small>

### 11.2 Correction de la courbe de chauffe

| Température extérieure le jour | Température ambiante trop basse | Température ambiante trop élevée |
|---|---|---|
| +5 °C à +15 °C | Facteur de raideur inférieur de 0,2 K/K et pied de la courbe augmenté de 5 K | Facteur de raideur supérieur de 0,2 K/K et pied de la courbe réduit de 5 K |
| −20 °C à +5 °C | Facteur de raideur supérieur de 0,2 K/K | Facteur de raideur inférieur de 0,2 K/K |

<small>Source : THF1777 p. 40</small>

### 11.3 Réglage des paramètres du circuit de chauffage

| Réglage | Radiateurs | Chauffage par le plancher | Chauffage mural |
|---|---|---|---|
| Température de départ max. | 70 °C | 50 °C | 50 °C |
| Constante de temps | 120 min | 210 min | 180 min |
| Temp. ambiante (1) | 6 K/K | 3 K/K | 3 K/K |
| Ecart Circuit de chauffage | 20 K | 10 K | 10 K |
| Régime min. pompe PHK (2) | 25 % | 100 % | 100 % |

(1) Uniquement lorsque la commande est montée dans une pièce d'habitation appropriée ; sinon, régler l'influence de la pièce sur 0 !
(2) Avec les pompes électroniques des circuits de chauffage, réglez toujours la vitesse sur 100 %.

<small>Source : THF1777 p. 40</small>

## 12. Données techniques

| Caractéristique | Valeur |
|---|---|
| Tension d'alimentation | 230 V ±10 %, 50 Hz |
| Consommation | 8 VA max. |
| Température ambiante | 0 °C … 50 °C |
| Type de protection du régulateur dans le coffret mural | IP65 selon EN 60529-1 |
| Classe de protection dans le coffret mural | II selon EN 60730-1 |
| Type de protection du régulateur dans la chaudière | Voir les données techniques de la chaudière |
| Classe de protection du régulateur dans la chaudière | Voir les données techniques de la chaudière |
| Contrôle | Conforme à la norme CE |
| Puissance de commutation du relais (B1, mélangeur, ULV/LP, PZI) | 230 V, 1 A, 50 Hz |
| Puissance de commutation du relais électronique (PHK, PHK2, PK) | 230 V, 1 A, 50 Hz |
| Longueur du câble du bus de liaison aux commandes et au régulateur solaire | Longueur totale 30 m max., 2 × 0,75 mm² |
| Fusible pour le régulateur et les sorties | Fusible miniature 3,15 AT, 250 V |
| Sauvegarde de l'heure | 10 ans |

<small>Source : THF1777 p. 41</small>
