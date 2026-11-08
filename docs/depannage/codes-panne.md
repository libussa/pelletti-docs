---
title: "Codes de panne de la chaudière"
description: "Déblocage, historique des pannes, tableau des codes de panne PFA II avec causes et remèdes détaillés, pannes sans affichage."
sources: [THF1849 p. 51-53, THF1751 p. 14-23]
---

# Codes de panne de la chaudière

!!! note "Notation des touches"
    Le manuel représente les touches du module de commande par des pictogrammes. Notation utilisée ici : **OK** = niveau de menu inférieur, **ESC** = niveau de menu supérieur, **▼ / ▲** = se déplacer dans un menu, **− / +** = modifier les valeurs.

## 18. Programme de contrôle

### 18.1 Réglage du mode de fonctionnement

Dans le programme de contrôle, il est possible d'activer et de désactiver
manuellement tous les consommateurs électriques à des fins de test. En outre,
ce menu permet de mettre à l'arrêt la chaudière à granulés de bois pendant
les mois d'été.

1. Passez de l'affichage par défaut au menu principal à l'aide de la touche
   **OK**.
2. Sélectionnez ensuite le menu principal `Prog contrôle` avec la touche
   **▼**, puis **OK**.
3. La touche **+** permet de passer au mode de fonctionnement suivant.

| Mode de fonction | Description |
|---|---|
| Auto | Fonctionnement normal. |
| Test | Les fonctions de régulation de la chaudière sont désactivées. Ce mode permet de commuter les sorties électriques manuellement. |
| Manuel | La chaudière se régule automatiquement sur la température de consigne réglée. |
| Arrêt | Toutes les fonctions de régulation de la chaudière sont désactivées. Par exemple pendant les mois d'été, lorsque l'approvisionnement en eau chaude doit provenir exclusivement d'une installation solaire. |
| Entretien | Affichage d'entretien supplémentaire : apparaît uniquement si la fonction d'entretien a été activée auparavant. Vous pouvez désactiver ce mode avec les touches − ou +. |

<small>Source : THF1849 p. 50</small>

### 18.2 Contrôle des sorties

Le mode de fonctionnement Test permet au technicien spécialisé de contrôler
les sorties. Ainsi, l'état des sorties peut être vérifié grâce à ce mode. Les
fonctions de régulation sont hors service. Depuis l'affichage `Mode de
fonction Test`, accédez au programme de contrôle à l'aide de la touche
**OK**.

!!! note "Remarque"
    Le mode Test ne peut être démarré que lorsque la chaudière est en mode
    PAUSE ou lorsque la phase de combustion est terminée.

!!! note "Remarque"
    L'état sélectionné des sorties reste généralement conservé lors de la
    sélection de l'option de menu suivante. Un test parallèle de plusieurs
    sorties est ainsi possible.

Les options se suivent avec **▼** ; les touches **−** et **+** activent et
désactivent la sortie (ou modifient la vitesse). Contrôlez à chaque fois que
l'élément est actionné.

| Option | Sortie contrôlée | Action − / + |
|---|---|---|
| Alarme externe | Sortie Alarme externe | Marche / Arrêt |
| Régu.ext AEF | Décharge de démarrage de la régulation externe | Marche / Arrêt |
| Ventilat Vent RGV | Ventilateur de gaz de fumée | Marche / Arrêt |
| Pompe KP | Pompe de la chaudière | Modifie la vitesse (%) |
| Moteur RM | Moteur de nettoyage | Marche / Arrêt |
| Coup.feu BSK | Clapet coupe-feu | Marche / Arrêt |
| Allumage Z | Allumage | Marche / Arrêt |
| Moteur ESM | Moteur d'injection | Marche / Arrêt |
| Ventilat BG | Ventilateur du brûleur | Modifie la vitesse (%) |
| Moteur RA | Moteur d'extraction | Marche / Arrêt |
| Turbine ST | Turbine d'aspiration ; en parallèle, la sortie du moteur intermédiaire (ZW) est actionnée. Dans les systèmes de vis sans fin, seule la sortie du moteur intermédiaire est actionnée. | Marche / Arrêt |
| Fumée EX | Aspirateur de fumées (Extract Fumée) | Marche / Arrêt |
| Version PPUI | Affiche la version de programme du module de commande et la date de création du logiciel (ex. V 1.00, 20.01.05) | — |
| Version PFAII | Affiche la version de programme de la commande automatique du brûleur et la date de création du logiciel (ex. V 2.00, 20.01.05) | — |

!!! note "Remarque"
    Système d'aspiration : si lors du test de la sortie RA le clapet
    coupe-feu est ouvert, la sortie RA n'est pas actionnée.

!!! warning "Attention"
    Danger de blocage de la vis sans fin en cas de réservoir à granulés de
    bois rempli. Déclenchez le moteur d'extraction pour le test de la vis
    sans fin.

!!! note "Remarque"
    Si lors du test de la sortie ST le clapet coupe-feu est ouvert, la sortie
    ST n'est pas actionnée.

<small>Source : THF1849 p. 51-52</small>

## 19. Affichage des pannes

Si la chaudière à granulés de bois Pelletti rencontre une panne (affichage
`Pelletti` / `Alarme`), vous pouvez consulter le code de panne et les
paramètres de l'installation correspondants dans le menu principal `Panne`.

1. Passez de l'affichage par défaut au menu principal à l'aide de la touche
   **OK**.
2. Sélectionnez ensuite le menu principal `Panne` avec la touche **▼**.
3. Appuyez sur la touche **OK** pour accéder au sous-menu. `Panne actuelle` :
   si une panne est actuellement présente, elle s'affiche ici (sinon
   « --- »).

<small>Source : THF1849 p. 53</small>

### 19.1 Déblocage de la chaudière

1. Appuyez sur la touche **OK** pour accéder au sous-menu. Le code de panne
   actuelle est affiché (ex. 18). Le code de panne donne une indication
   importante relative à un composant spécifique ou un mode de
   fonctionnement.
2. Passez à l'option suivante, `Déverrouil`, avec la touche **▼**. Vous
   pouvez débloquer la chaudière avec la touche **+**. Le code de panne
   actuel est effacé dans l'affichage précédent.

<small>Source : THF1849 p. 53</small>

### 19.2 Affichage des pannes

Passez à l'option suivante, `Panne chaud.`, avec la touche **▼**. Les touches
**−** et **+** permettent de passer d'une panne enregistrée en mémoire à une
autre. Il est possible d'enregistrer un maximum de dix pannes.

!!! note "Remarque"
    Si aucune panne n'est enregistrée ou ne s'est produite, cet affichage
    n'est pas disponible.

Pour chaque panne, la touche **▼** fait défiler :

| Affichage | Exemple | Contenu |
|---|---|---|
| Code panne | 18 | Code de panne sélectionné |
| Heure panne | 13:23 | Heure à laquelle la panne s'est produite |
| Date panne | 07.02.05 | Date de la panne |
| Moment panne | Allumage | Mode de fonctionnement ayant rencontré la panne |
| TK panne | 34.5 °C | Température de la chaudière au moment de la panne |
| TRG panne | 174 °C | Température des gaz de fumée au moment de la panne |

<small>Source : THF1849 p. 53</small>

### 19.3 Effacement des pannes de la mémoire

Passez à l'option de menu suivante, `Effacer mémoire`, avec la touche **▼**.
La touche **+** permet d'effacer de la mémoire toutes les pannes enregistrées
ainsi que les informations correspondantes.

!!! warning "Attention"
    Seul le technicien spécialisé est autorisé à effacer les pannes
    enregistrées.

<small>Source : THF1849 p. 53</small>

### 19.4 Tableau des messages de panne

| Panne | Signification | Arrêt de la chaudière | Affichage de l'alarme | Cause / Dépannage |
|---|---|---|---|---|
| 0 | STB s'est déclenché | Oui | Oui | Tube capillaire éventuellement défectueux, remplacer STB, augmenter le temps de poursuite de la pompe chaudière. |
| 2 | Absence de flammes | Oui | Oui | Vérifier l'approvisionnement/alimentation en combustible, la cartouche d'allumage, le ventilateur du brûleur. |
| 12 | Panne PFA, pas de communication | Oui | Oui | Couper brièvement la tension de réseau (réinitialisation). Problème électromagnétique éventuel – séparer les câbles sous tension des câbles de sondes. |
| 18 | Température de la chaudière trop élevée | Non | Non | Vérifier la sonde de la chaudière, vérifier le débit hydraulique et volumétrique, éventuellement augmenter le temps de poursuite de la pompe chaudière. |
| 19 | Température de retour trop élevée | Non | Non | Vérifier la sonde de retour, vérifier le débit hydraulique et volumétrique. |
| 28 | Le ventilateur du brûleur ne fonctionne pas | Oui | Oui | Vérifier le fonctionnement du ventilateur du brûleur. |
| 29 | Le ventilateur du brûleur ne s'arrête pas | Oui | Oui | Vérifier le fonctionnement du ventilateur du brûleur, informer le service client. |
| 31 | Court-circuit de la sonde de la chaudière | Oui | Oui | Vérifier la sonde de la chaudière et la fiche de raccordement. En cas de défaut constaté, les remplacer. |
| 32 | Court-circuit de la sonde de retour | Oui | Oui | Vérifier la sonde de retour et la fiche de raccordement. En cas de défaut constaté, les remplacer. |
| 35 | Court-circuit de la sonde de gaz de fumée | Oui | Oui | Vérifier la sonde de gaz de fumée et la fiche de raccordement. En cas de défaut constaté, les remplacer. |
| 36 | Déconnexion de la sonde de la chaudière | Oui | Oui | Vérifier la sonde de la chaudière et la fiche de raccordement. En cas de défaut constaté, les remplacer. |
| 40 | Déconnexion de la sonde de gaz de fumée | Oui | Oui | Vérifier la sonde de gaz de fumée et la fiche de raccordement. En cas de défaut constaté, les remplacer. |
| 43 | Température des gaz de fumée trop élevée | Oui | Oui | Vérifier la sonde de gaz de fumée et la fiche de raccordement. Chaudière fortement encrassée, procéder à l'entretien. |
| 44 | Température des gaz de fumée trop basse en fonctionnement normal | Oui | Oui | Approvisionnement en combustible insuffisant, vérifier le système d'alimentation et le réservoir des granulés. |
| 50 | Le clapet coupe-feu ne se ferme pas | Oui | Oui | Vérifier la position et le fonctionnement du clapet coupe-feu (fermé, corps étranger), vérifier l'interrupteur de fin de course. |
| 51 | Le clapet coupe-feu ne s'ouvre pas | Oui | Oui | Vérifier la position et le fonctionnement du clapet coupe-feu, vérifier l'interrupteur de fin de course. Informer le service client. |
| 52 | Le convoyeur de remplissage ne se met pas en marche | Oui | Oui | Vérifier le fonctionnement du moteur d'injection. |
| 53 | Le convoyeur de remplissage ne se met pas à l'arrêt | Oui | Oui | Vérifier le fonctionnement du moteur d'injection, informer le service client. |
| 54 | L'allumage ne s'active pas | Oui | Oui | Vérifier le fonctionnement de l'allumage. |
| 55 | L'allumage ne se désactive pas | Oui | Oui | Vérifier le fonctionnement de l'allumage, informer le service client. |
| 56 | Surchauffe des moteurs | Oui | Oui | Moteur d'injection ou d'extraction bloqué. Vérifier le réservoir à granulés et le système d'alimentation. |
| 57 | Surveillance de l'interrupteur thermostatique | Oui | Oui | Surchauffe dans la vis sans fin, informer le service client. |
| 59 | Nombre max. de tentatives de remplissage dépassé (système d'aspiration) | Non | Oui | Vérifier l'approvisionnement en combustible, vérifier et ajuster la sonde de capacité, vérifier le fonctionnement de la turbine d'aspiration. |
| 60 | Erreur de l'interrupteur de fin de course du clapet coupe-feu | Oui | Oui | Vérifier l'affectation des plots de connexion de l'interrupteur de fin de course, informer le service client. |

!!! note "Remarque"
    Pour le contrôle ou le test des sorties électriques et des éléments de
    puissance électriques qui y sont raccordés, vous pouvez activer et
    désactiver ces derniers dans le programme de contrôle (voir
    chapitre 18).

<small>Source : THF1849 p. 54</small>

## Diagnostic détaillé (instructions d'entretien THF1751)

### 6.1 Déblocage de la chaudière

Si la chaudière à granulés de bois Pelletti rencontre une panne
(affichage `Pelletti` / `Alarme`), vous pouvez consulter le code de
panne et les paramètres de l'installation correspondants dans le menu
principal Panne.

(Le manuel représente les touches par des pictogrammes : « touche Menu »
et « touche flèche » désignent respectivement la touche de menu et la
touche de défilement vers le bas.)

1. Passez de l'affichage par défaut au menu principal à l'aide de la
   touche Menu.
2. Sélectionnez ensuite le menu principal **Panne** avec la touche
   flèche (affichage `Prog contrôle` / `▶Panne`).
3. Appuyez sur la touche Menu pour accéder au sous-menu. Affichage
   `Panne actuelle` : si une panne est actuellement présente, elle
   s'affiche ici (sinon `---`).

<small>Source : THF1751 p. 13</small>

#### 6.1.1 Déblocage de la chaudière

Appuyez sur la touche Menu pour accéder au sous-menu. Le code de panne
actuel est affiché (`Panne actuelle`, par ex. `18`). Le code de panne
donne une indication importante relative à un composant spécifique ou à
un mode de fonctionnement.

Passez à l'option suivante avec la touche flèche (`Déverrouil` /
`▶Non`). Vous pouvez débloquer la chaudière avec la touche **+**. Le code
de panne actuel est effacé dans l'affichage précédent. La chaudière à
granulés de bois revient à l'état de fonctionnement actuel.

#### 6.1.2 Affichage des pannes

Passez à l'option suivante avec la touche flèche (`Panne chaud.`, n° 1).
Les touches **−** et **+** permettent de passer d'une panne enregistrée
en mémoire à une autre. Il est possible d'enregistrer un maximum de dix
pannes.

!!! note "Remarque"
    Si aucune panne n'est enregistrée ou ne s'est produite, cet affichage
    n'est pas disponible.

**Exemple d'affichage** (passage d'un écran au suivant avec la touche
flèche) :

| Affichage | Exemple | Contenu |
|---|---|---|
| `Code panne` | 18 | Le code de panne sélectionné. |
| `Heure panne` | 13:23 | L'heure à laquelle la panne s'est produite. |
| `Date panne` | 07.02.05 | La date de la panne. |
| `Moment panne` | Allumage | Le mode de fonctionnement ayant rencontré une panne. |
| `TK panne` | 34.5 °C | La température de la chaudière au moment de la panne. |
| `TRG panne` | 174 °C | La température des gaz de fumée au moment de la panne. |

#### 6.1.3 Effacement des pannes de la mémoire

Passez à l'option de menu suivante avec la touche flèche (`Effacer
mémoire` / `▶Non`). La touche **+** permet d'effacer de la mémoire toutes
les pannes enregistrées ainsi que les informations correspondantes.

(Le manuel numérote ce paragraphe « 16.1.3 » par erreur.)

<small>Source : THF1751 p. 13</small>

### 6.2 Code de panne

Vue d'ensemble :

| Code | Description des erreurs |
|---|---|
| 0 | Le limiteur de température de sécurité (STB) s'est déclenché |
| 2 | Absence de flammes |
| 12 | Panne de communication (bus LON) entre la commande automatique du brûleur PFA II et le module de commande PPUI |
| 18 | Température maximale de la chaudière TK dépassée |
| 19 | Température de retour de la chaudière TKR trop élevée |
| 28 | Le ventilateur du brûleur BG ne tourne pas |
| 29 | Le ventilateur du brûleur BG ne s'éteint pas |
| 31 | Court-circuit de la sonde de la chaudière TK |
| 32 | Court-circuit de la sonde de retour TKR |
| 35 | Court-circuit de la sonde de gaz de fumée TRG |
| 36 | Déconnexion de la sonde de la chaudière TK |
| 40 | Déconnexion de la sonde de gaz de fumée TRG |
| 43 | Température des gaz de fumée trop élevée |
| 44 | Température des gaz de fumée trop basse en fonctionnement normal |
| 50 | Le clapet coupe-feu ne se ferme pas |
| 51 | Le clapet coupe-feu ne s'ouvre pas |
| 52 | Le convoyeur de remplissage ne se met pas en marche |
| 53 | Le convoyeur de remplissage ne se met pas à l'arrêt |
| 54 | L'allumage Z ne s'active pas |
| 55 | L'allumage Z ne se désactive pas |
| 56 | Surchauffe des moteurs |
| 57 | Surveillance de température |
| 59 | Nombre max. de tentatives de remplissage dépassé (système d'aspiration) |
| 60 | Erreur de l'interrupteur de fin de course du clapet coupe-feu BSK |

#### Code 0 — Le limiteur de température de sécurité (STB) s'est déclenché

**Cause(s) :**

- La température de la chaudière a dépassé 110 °C.
- Le limiteur de température de sécurité STB est défectueux.

**Dépannage :**

- Retirez le bouchon de protection noir du limiteur de température de
  sécurité STB sur la tôle de commande et appuyez sur le bouton de
  déblocage.
- Vérifiez si une tension de 230 VAC est présente au niveau des deux
  contacts de la borne X8.
- Vérifiez les raccordements par câble du limiteur de température de
  sécurité STB (chapitre 7.2).
- Vérifiez que le tube capillaire n'est pas défectueux (par ex. plié).
  Remplacez le STB.
- Augmentez le temps de poursuite de la pompe (KP).

#### Code 2 — Absence de flammes

**Cause(s) :**

- La température minimale des gaz de fumée de 60 °C n'a pas été atteinte
  en 10 minutes même après activation de la cartouche d'allumage.
- Trois tentatives d'allumage dépassées.
- Absence de combustible sur le plateau de combustion ou alimentation en
  combustible interrompue.
- Entraînement de l'alimentation en combustible défectueux.
- Cartouche d'allumage défectueuse.
- La cartouche d'allumage n'est pas traversée par de l'air de
  combustion.
- Fusible F5 défectueux (p. 14) / Fusible F1 défectueux (p. 15).
- Fusible F3 défectueux.

**Dépannage :**

- Vérifiez si les granulés de bois ont été injectés. Il doit y avoir des
  granulés de bois sur le plateau de combustion jusqu'à l'ouverture au
  niveau de la cartouche d'allumage.

Si tel n'est pas le cas :

*Dans les systèmes de vis sans fin :*

- Vérifiez le niveau du réservoir à granulés.
- Contrôlez le fonctionnement du moteur d'extraction RA, par ex.
  déclenchez-le à titre d'essai de la vis sans fin et commandez-le
  manuellement dans le programme de contrôle (mode Test) (le clapet
  coupe-feu BSK doit être ouvert). En cas de défaut constaté,
  remplacez-le.
- Vérifiez la présence d'une tension 230 VAC au niveau de la sortie RA
  (X24).
- Vérifiez le fusible F5 (3,15 A/T).
- Si la sortie RA (X24) est défectueuse, remplacez la commande
  automatique du brûleur PFA II.
- Lorsque la vis sans fin est bloquée (par ex. obstruction), installez
  l'adaptateur pour le mode manuel (Réf. 05-2018) et débloquez la vis
  sans fin par des rotations gauche/droite.
- Vérifiez le fonctionnement du moteur d'injection ESM, par ex.
  commandez-le manuellement dans le programme de contrôle (mode Test)
  (le clapet coupe-feu BSK doit être ouvert). En cas de défaut constaté,
  remplacez-le.
- Vérifiez la présence d'une tension 230 VAC au niveau de la sortie ESM
  (X27).
- Vérifiez le fusible F3 (1,6 A/T).
- Si la sortie ESM (X27) est défectueuse, remplacez la commande
  automatique du brûleur PFA II.

*Dans les systèmes d'aspiration :*

- Y a-t-il du combustible dans le récipient de stockage ?
- Vérifiez le fonctionnement du moteur d'injection ESM, par ex.
  commandez-le manuellement dans le programme de contrôle (mode Test)
  (le clapet coupe-feu BSK doit pour cela être ouvert). En cas de défaut
  constaté, remplacez-le.
- Vérifiez la présence d'une tension 230 VAC au niveau de la sortie ESM
  (X27).
- Vérifiez le fusible F3 (1,6 A/T).
- Si la sortie ESM (X27) est défectueuse, remplacez la commande
  automatique du brûleur PFA II.

*Suite (tous systèmes) :*

- Vérifiez la présence d'encrassements au niveau du plateau de
  combustion et nettoyez-le si nécessaire.
- Vérifiez la sonde des gaz de fumée TRG (valeurs de sonde PT 1000 : voir
  le tableau au chapitre 6.4). En cas d'écarts, remplacez la sonde.
- Vérifiez l'ouverture à la pointe de la cartouche d'allumage pour vous
  assurer qu'elle est dégagée (pas d'encrassement). Si nécessaire,
  démontez-la et nettoyez-la.
- Vérifiez le fonctionnement de la cartouche d'allumage Z, par ex.
  commandez-la manuellement dans le programme de contrôle (mode Test).
  En cas de défaut constaté, remplacez-la.
- Vérifiez le fonctionnement du ventilateur du brûleur BG, par ex.
  commandez-le manuellement dans le programme de contrôle (mode Test).
  En cas de défaut constaté, remplacez-le.
- Vérifiez la présence d'une tension 230 VAC au niveau de la sortie Z
  (X26) pendant le processus d'allumage.
    - Vérifiez le fusible F1 (10 A/T).
    - Si la sortie Z (X26) est défectueuse, remplacez la commande
      automatique du brûleur PFA II.
- Vérifiez la présence d'une tension 230 VAC au niveau de la sortie BG
  (X25).
    - Vérifiez le fusible F3 (1,6 A/T).
    - Si la sortie RA (X24) est défectueuse, remplacez la commande
      automatique du brûleur PFA II. (sic : le manuel indique RA (X24)
      à cet endroit)
- Vérifiez les fiches (X16, X24, X25, X26, X27) du raccordement par
  câble pour vous assurer de l'absence de mauvais contact. Pour ce
  faire, débranchez les câbles, puis rebranchez-les.

#### Code 12 — Panne de communication (bus LON) entre la commande automatique du brûleur PFA II et le module de commande PPUI

**Cause(s) :**

- La fiche de raccordement entre le module de commande et la commande
  automatique du brûleur est déconnectée.
- Mauvais contact dans les fiches.
- La commande PFA II et le module de commande ne sont pas reliés.
- Problème CEM.

**Dépannage :**

- Débranchez le raccordement par câble (X38) entre la commande
  automatique du brûleur et le module de commande, puis rebranchez-le.
  Assurez-vous de brancher correctement la fiche du module de commande.
- Vérifiez la fiche (X38) du raccordement par câble pour vous assurer
  de l'absence de mauvais contact. Pour ce faire, débranchez le câble,
  puis rebranchez-le.
- Reliez la commande PFA II et le module PPUI.
- Recherchez la source de perturbations électromagnétiques et
  éliminez-la.

#### Code 18 — Température maximale de la chaudière TK dépassée

**Cause(s) :**

- La température maximale de 100 °C a été dépassée au niveau de la sonde
  de la chaudière TK.
- Sonde de la chaudière défectueuse.
- Absence de prise de chaleur :
    - Pompe(s) du circuit de chauffage défectueuse(s)
    - Erreur du système hydraulique
    - Absence de débit
    - Air dans la/les pompe(s) du circuit de chauffage ou le système
      hydraulique
- Avec un ballon tampon :
    - La pompe de la chaudière ne convoie pas
    - Absence de poursuite de la pompe de la chaudière
- Fusible F2 défectueux.

**Dépannage :**

- Vérifiez la sonde de la chaudière TK (valeurs de sonde NTC : voir le
  tableau au chapitre 6.4). En cas d'écarts, remplacez la sonde.
- Assurez-vous qu'une tension 230 VAC est bien présente au niveau de
  la/des pompe(s) du circuit de chauffage.
- Purgez la/les pompe(s) du circuit de chauffage.
- En cas de défaut, remplacez la/les pompe(s) du circuit de chauffage.
- **Avec un ballon tampon :**
    - Vérifiez le fonctionnement de la pompe de la chaudière KP, par ex.
      commandez-la manuellement dans le programme de contrôle (mode
      Test). En cas de défaut constaté, remplacez-la.
    - Vérifiez la présence d'une tension 230 VAC au niveau de la sortie
      KP (X6).
    - Vérifiez le fusible F2 (630 mA/T).
    - Si la sortie KP (X6) est défectueuse, remplacez la commande
      automatique du brûleur PFA II.
    - Vérifiez la fiche (X6) du raccordement par câble pour vous assurer
      de l'absence de mauvais contact. Pour ce faire, débranchez le
      câble, puis rebranchez-le.

#### Code 19 — Température de retour de la chaudière TKR trop élevée

**Cause(s) :**

- La température de retour maximale de la chaudière de 100 °C a été
  dépassée.
- Sonde de retour de la chaudière TKR défectueuse.

**Dépannage :**

- Vérifiez la sonde de la chaudière TKR (valeurs de sonde NTC : voir le
  tableau au chapitre 6.4). En cas d'écarts, remplacez la sonde.
- Vérifiez la fiche (X16) du raccordement par câble pour vous assurer
  de l'absence de mauvais contact. Pour ce faire, débranchez le câble,
  puis rebranchez-le.

#### Code 28 — Le ventilateur du brûleur BG ne tourne pas

**Cause(s) :**

- Sortie BG (X25) défectueuse.
- Ventilateur du brûleur BG défectueux.
- Fusible F3 défectueux.

**Dépannage :**

- Vérifiez le fonctionnement du ventilateur du brûleur BG, par ex.
  commandez-le manuellement dans le programme de contrôle (mode Test).
  En cas de défaut constaté, remplacez-le.
- Vérifiez la présence d'une tension 230 VAC au niveau de la sortie BG
  (X25).
    - Vérifiez le fusible F3 (1,6 A/T).
    - Si la sortie BG (X25) est défectueuse, remplacez la commande
      automatique du brûleur PFA II.
- Vérifiez la fiche (X25) du raccordement par câble pour vous assurer
  de l'absence de mauvais contact. Pour ce faire, débranchez le câble,
  puis rebranchez-le.

#### Code 29 — Le ventilateur du brûleur BG ne s'éteint pas

**Cause(s) :**

- Sortie BG (X25) défectueuse.

**Dépannage :**

- Vérifiez le fonctionnement du ventilateur du brûleur BG, par ex.
  commandez-le manuellement dans le programme de contrôle (mode Test).
  Si le ventilateur du brûleur est impossible à arrêter, remplacez la
  commande automatique du brûleur PFA II.

#### Code 31 — Court-circuit de la sonde de la chaudière TK

**Cause(s) :**

- Sonde de la chaudière TK défectueuse.
- Entrée TK (X15) défectueuse.

**Dépannage :**

- Vérifiez la sonde de la chaudière TK (valeurs de sonde NTC : voir le
  tableau au chapitre 6.4). En cas d'écarts, remplacez la sonde.
- Vérifiez la fiche (X15) du raccordement par câble pour vous assurer
  de l'absence de court-circuit. Pour ce faire, débranchez le câble,
  puis rebranchez-le.
- Vérifiez l'entrée X15 avec la sonde de remplacement (NTC). S'il n'y a
  pas de défaut au niveau de la sonde de la chaudière TK, remplacez la
  commande automatique du brûleur PFA II.

#### Code 32 — Court-circuit de la sonde de retour TKR

**Cause(s) :**

- Sonde de retour TKR défectueuse.
- Entrée TKR (X16) défectueuse.

**Dépannage :**

- Vérifiez la sonde de retour de la chaudière TKR (valeurs de sonde
  NTC : voir le tableau au chapitre 6.4). En cas d'écarts, remplacez la
  sonde.
- Vérifiez la fiche (X16) du raccordement par câble pour vous assurer
  de l'absence de court-circuit. Pour ce faire, débranchez le câble,
  puis rebranchez-le.
- Vérifiez l'entrée X16 avec la sonde de remplacement (NTC). S'il n'y a
  pas de défaut au niveau de la sonde de retour de la chaudière TKR,
  remplacez la commande automatique du brûleur PFA II.

#### Code 35 — Court-circuit de la sonde de gaz de fumée TRG

**Cause(s) :**

- Sonde de gaz de fumée TRG défectueuse.
- Entrée TRG (X17) défectueuse.

**Dépannage :**

- Vérifiez la sonde de gaz de fumée TRG (valeurs de sonde PT 1000 :
  voir le tableau au chapitre 6.4). En cas d'écarts, remplacez la sonde.
- Vérifiez la fiche (X17) du raccordement par câble pour vous assurer
  de l'absence de court-circuit. Pour ce faire, débranchez le câble,
  puis rebranchez-le.
- Vérifiez l'entrée X17 avec la sonde de remplacement (PT 1000). S'il
  n'y a pas de défaut au niveau de la sonde de gaz de fumée TRG,
  remplacez la commande automatique du brûleur PFA II.

#### Code 36 — Déconnexion de la sonde de la chaudière TK

**Cause(s) :**

- Sonde de la chaudière TK défectueuse.
- Entrée TK (X15) défectueuse.

**Dépannage :**

- Vérifiez la sonde de la chaudière TK (valeurs de sonde NTC : voir le
  tableau au chapitre 6.4). En cas d'écarts, remplacez la sonde.
- Vérifiez la fiche (X15) du raccordement par câble pour vous assurer
  de l'absence de mauvais contact. Pour ce faire, débranchez le câble,
  puis rebranchez-le.
- Vérifiez l'entrée X15 avec la sonde de remplacement (NTC). S'il n'y a
  pas de défaut au niveau de la sonde de la chaudière TK, remplacez la
  commande automatique du brûleur PFA II.

#### Code 40 — Déconnexion de la sonde de gaz de fumée TRG

**Cause(s) :**

- Sonde de gaz de fumée TRG défectueuse.
- Entrée TRG (X17) défectueuse.

**Dépannage :**

- Vérifiez la sonde de gaz de fumée TRG (valeurs de sonde PT 1000 :
  voir le tableau au chapitre 6.4). En cas d'écarts, remplacez la sonde.
- Vérifiez la fiche (X17) du raccordement par câble pour vous assurer
  de l'absence de mauvais contact. Pour ce faire, débranchez le câble,
  puis rebranchez-le.
- Vérifiez l'entrée X17 avec la sonde de remplacement (NTC — sic, la
  sonde TRG est une PT 1000). S'il n'y a pas de défaut au niveau de la
  sonde de gaz de fumée TRG, remplacez la commande automatique du
  brûleur PFA II.

#### Code 43 — Température des gaz de fumée trop élevée

**Cause(s) :**

- La température maximale des gaz de fumée de 350 °C a été dépassée.
- Entrée TRG (X17) défectueuse.
- Sonde de gaz de fumée TRG défectueuse.
- Chaudière fortement encrassée.
- Mélange combustible/air mal harmonisé.
- Feu de cheminée dans la chaudière ou le tube de raccordement.
- Entrée TRG (X17) défectueuse.

**Dépannage :**

- Vérifiez la sonde de gaz de fumée TRG (valeurs de sonde PT 1000 :
  voir le tableau au chapitre 6.4). En cas d'écarts, remplacez la sonde.
- Vérifiez la fiche (X17) du raccordement par câble pour vous assurer
  de l'absence de mauvais contact. Pour ce faire, débranchez le câble,
  puis rebranchez-le.
- Nettoyez la chaudière et le tube de raccordement vers la cheminée ou
  procédez à l'entretien.
- Harmonisez le mélange combustible/air (voir chapitre 4.2 Réglage de
  la qualité de combustion — sic, il s'agit du chapitre 4.3).
- Vérifiez l'entrée X17 avec la sonde de remplacement (PT 1000). S'il
  n'y a pas de défaut au niveau de la sonde de gaz de fumée TRG,
  remplacez la commande automatique du brûleur PFA II.

#### Code 44 — Température des gaz de fumée trop basse en fonctionnement normal

**Cause(s) :**

- Absence de combustible sur le plateau de combustion ou alimentation en
  combustible interrompue.
- La température des gaz de fumée est passée sous la valeur minimale de
  60 °C pendant le mode de fonctionnement réglé (mode Normal).
- Sonde de gaz de fumée TRG défectueuse.
- Entrée TRG (X17) défectueuse.

En plus, avec les systèmes d'aspiration :

- Absence de combustible dans le récipient de stockage.
- Récipient de stockage rempli, pourtant formation de ponts au niveau
  de la vis de dosage.
- L'interrupteur de niveau de la turbine d'aspiration SST (X32)
  s'arrête trop tôt.
- Interrupteur de niveau de la turbine d'aspiration SST (X32)
  défectueux.

**Dépannage :**

- Contrôlez le niveau du réservoir à granulés.
- Vérifiez la sonde de retour de la chaudière TRG (valeurs de sonde
  PT 1000 : voir le tableau au chapitre 6.4). En cas d'écarts,
  remplacez la sonde.
- Vérifiez la fiche (X17) du raccordement par câble pour vous assurer
  de l'absence de mauvais contact. Pour ce faire, débranchez le câble,
  puis rebranchez-le.
- Remédiez à l'insuffisance de l'approvisionnement en combustible. Pour
  ce faire, procédez comme décrit pour le code de panne 2 (Absence de
  flammes).
- Vérifiez l'entrée X17 avec la sonde de remplacement (PT 1000). S'il
  n'y a pas de défaut au niveau de la sonde de gaz de fumée TRG,
  remplacez la commande automatique du brûleur PFA II.

En plus, avec les systèmes d'aspiration :

- Contrôlez le remplissage du récipient de stockage. Pour ce faire,
  déclenchez le remplissage forcé dans le menu des paramètres de
  l'installation.
- Videz le récipient de stockage et aspirez les éléments fins au niveau
  de la vis de dosage.
- Ajustez l'interrupteur de niveau de la turbine d'aspiration SST (X32)
  conformément aux instructions de montage (chapitre Mise en service).
- Remplacez l'interrupteur de niveau de la turbine d'aspiration SST
  (X32).

#### Code 50 — Le clapet coupe-feu ne se ferme pas

**Cause(s) :**

- Echec de l'information en retour de la position Clapet coupe-feu
  fermé BSK/g (X34).
- Corps étrangers dans le clapet coupe-feu.
- Le clapet coupe-feu (robinet à tournant sphérique) fonctionne
  difficilement.
- Ressort de rappel du moteur de commande défectueux.

**Dépannage :**

- Vérifiez le fonctionnement du moteur de commande du clapet coupe-feu
  BSK, par ex. commandez-le manuellement dans le programme de contrôle
  (mode Test). Contrôle visuel pour vous assurer que le clapet
  coupe-feu (robinet à tournant sphérique) s'ouvre et se ferme
  entièrement.
- Vérifiez le signal de l'information en retour de la position au
  niveau de la fiche X34. En cas de clapet coupe-feu fermé, +12 VDC
  entre les bornes blanche2 (BSK/g) et blanche1/4 (GND). En cas de
  défaut constaté, remplacez le moteur de commande.
- Vérifiez la fiche du raccordement par câble pour vous assurer de
  l'absence de mauvais contact. Pour ce faire, débranchez le câble,
  puis rebranchez-le.
- Assurez-vous de l'absence de corps étrangers dans le clapet coupe-feu
  (robinet à tournant sphérique). Pour ce faire dans les systèmes à
  aspiration, retirez le récipient de stockage.
- Remplacez le coupe-feu (robinet à tournant sphérique) s'il fonctionne
  difficilement.

#### Code 51 — Le clapet coupe-feu ne s'ouvre pas

**Cause(s) :**

- Echec de l'information en retour de la position Clapet coupe-feu
  ouvert BSK/o (X34).
- Le clapet coupe-feu (robinet à tournant sphérique) fonctionne
  difficilement.
- Moteur de commande du clapet coupe-feu défectueux.
- Fusible F1 défectueux.

**Dépannage :**

- Vérifiez le fonctionnement du moteur de commande du clapet coupe-feu
  BSK, par ex. commandez-le manuellement dans le programme de contrôle
  (mode Test). Contrôle visuel pour vous assurer que le clapet
  coupe-feu (robinet à tournant sphérique) s'ouvre et se ferme
  entièrement.
- Vérifiez la présence d'une tension 230 VAC au niveau de la sortie BSK
  (X9).
    - Vérifiez le fusible F1 (10 A/T).
    - Si la sortie BSK (X9) est défectueuse, remplacez la commande
      automatique du brûleur PFA II.
- Vérifiez le signal de l'information en retour de la position au
  niveau de la fiche X34. En cas de clapet coupe-feu ouvert, +12 VDC
  entre les bornes blanche (BSK/g) et blanche 1/4 (GND). En cas de
  défaut constaté, remplacez le moteur de commande.
- Vérifiez les fiches (X9 et X34) du raccordement par câble pour vous
  assurer de l'absence de mauvais contact. Pour ce faire, débranchez
  les câbles, puis rebranchez-les.
- Remplacez le coupe-feu (robinet à tournant sphérique) s'il fonctionne
  difficilement.

#### Code 52 — Le convoyeur de remplissage ne se met pas en marche

**Cause(s) :**

- Moteur d'injection ESM défectueux.
- Fusible F3 défectueux.
- Sortie ESM (X27) défectueuse.

**Dépannage :**

- Vérifiez le fonctionnement du moteur d'injection ESM, par ex.
  commandez-le manuellement dans le programme de contrôle (mode Test).
  En cas de défaut constaté, remplacez-le.
- Vérifiez la présence d'une tension 230 VAC au niveau de la sortie ESM
  (X27).
    - Vérifiez le fusible F3 (1,6 A/T).
    - Si la sortie ESM (X27) est défectueuse, remplacez la commande
      automatique du brûleur PFA II.

#### Code 53 — Le convoyeur de remplissage ne se met pas à l'arrêt

**Cause(s) :**

- Sortie ESM (X27) défectueuse.

**Dépannage :**

- Vérifiez le fonctionnement du moteur d'injection ESM, par ex.
  commandez-le manuellement dans le programme de contrôle (mode Test).
  Si le moteur d'injection est impossible à arrêter, remplacez la
  commande automatique du brûleur PFA II.

#### Code 54 — L'allumage Z ne s'active pas

**Cause(s) :**

- Cartouche d'allumage Z défectueuse.
- Fusible F1 défectueux.
- Sortie Z (X26) défectueuse.

**Dépannage :**

- Vérifiez la cartouche d'allumage (chapitre 3.5).
- Vérifiez le fonctionnement de la cartouche d'allumage Z, par ex.
  commandez-la manuellement dans le programme de contrôle (mode Test).
  En cas de défaut constaté, remplacez-la.
- Vérifiez la présence d'une tension 230 VAC au niveau de la sortie Z
  (X26).
    - Vérifiez le fusible F1 (10 A/T).
    - Si la sortie Z (X26) est défectueuse, remplacez la commande
      automatique du brûleur PFA II.

#### Code 55 — L'allumage Z ne se désactive pas

**Cause(s) :**

- Sortie Z (X26) défectueuse.

**Dépannage :**

- Vérifiez le fonctionnement de l'allumage Z, par ex. commandez-la
  manuellement dans le programme de contrôle (mode Test). Si l'allumage
  est impossible à désactiver, remplacez la commande automatique du
  brûleur PFA II.

#### Code 56 — Surchauffe des moteurs

**Cause(s) :**

- Le moteur d'injection ESM (X27) s'est arrêté en raison d'une
  surchauffe ou d'un blocage (protection thermique).
- Le moteur d'extraction RA (X24) s'est arrêté en raison d'une
  surchauffe ou d'un blocage (protection thermique).
- Protection thermique ESM ou RA défectueuse.
- La jonction de câbles n'a pas été raccordée à la protection du moteur
  intermédiaire MZW (X41).
- La jonction de câbles n'a pas été raccordée à la protection du moteur
  de la turbine d'aspiration MST (X42), jonction de câbles dans le
  connecteur correspondant.
- Le câble du moteur d'extraction (X24) (associé au dispositif de
  séparation d'aspiration dans le silo tissé Pelleton/Pelleton
  Maulwurf ou entraînement de réservoirs de stockage enterrés) n'est
  pas raccordé.
- Le relais enfichable de la turbine d'aspiration ne s'active pas ou le
  relais enfichable est défectueux.
- Système d'aspiration associé à la vis sans fin de réservoir de
  stockage souterrain :
    - Turbine d'aspiration défectueuse
    - Pas de puissance d'aspiration

**Dépannage :**

- Vérifiez les jonctions de câbles (X41, X42) pour vous assurer de
  l'absence de mauvais contact. Pour ce faire, débranchez les jonctions
  de câbles, puis rebranchez-les.
- Vérifiez les fiches (X39, X40) du raccordement par câble pour vous
  assurer de l'absence de mauvais contact. Pour ce faire, débranchez
  les câbles, puis rebranchez-les.

*Dans les systèmes de vis sans fin :*

- Lorsque la vis sans fin est bloquée (par ex. obstruction), installez
  l'adaptateur pour le mode manuel (Réf. 05-2018) et débloquez la vis
  sans fin par des rotations gauche/droite.
- Vérifiez la protection thermique du moteur d'extraction MRA (X39).
    - Résistance proche de l'infini, la protection thermique s'est
      déclenchée.
    - Résistance faible, la protection thermique ne s'est pas
      déclenchée.
- Remplacez le moteur d'extraction RA, lorsque la résistance de la
  protection thermique ESM reste proche de l'infini après le
  refroidissement.

*Dans les systèmes d'aspiration :*

- Vérifiez le fonctionnement de la turbine d'aspiration ST, par ex.
  commandez-la manuellement dans le programme de contrôle (mode Test).
  En cas de défaut constaté, remplacez-la.
- Vérifiez la présence d'une tension 230 VAC au niveau de la sortie ST
  (X29).
    - Vérifiez le fusible F4 (10 A/T).
    - Vérifiez le relais enfichable de la turbine d'aspiration.
    - Si le relais enfichable est défectueux, remplacez-le.
- Vérifiez les fiches (X29, X24) du raccordement par câble pour vous
  assurer de l'absence de mauvais contact. Pour ce faire, débranchez
  les câbles, puis rebranchez-les.
- Contrôlez la présence de fuites au niveau de la conduite d'aspiration
  des granulés et de l'air de retour et remédiez-y le cas échéant.
- Système d'aspiration associé à la vis sans fin de réservoir de
  stockage souterrain :
    - Lorsque la vis sans fin est bloquée (par ex. obstruction),
      installez l'adaptateur pour le mode manuel (Réf. 05-2018) et
      débloquez la vis sans fin par des rotations gauche/droite.
- Vérifiez la protection thermique du moteur d'extraction MRA (X39).
    - Résistance proche de l'infini, la protection thermique s'est
      déclenchée.
    - Résistance faible, la protection thermique ne s'est pas
      déclenchée.
    - Remplacez le moteur d'extraction RA, lorsque la résistance de la
      protection thermique ESM reste proche de l'infini après le
      refroidissement.
- Système d'aspiration associé à un dispositif de séparation
  d'aspiration avec silo tissé (même pour les réservoirs de stockage
  enterrés et les Sonnen-Pellet Maulwurf®) :
    - Vérifiez la jonction de câbles dans la fiche correspondante (X24)
      pour vous assurer de l'absence de mauvais contact. Pour ce faire,
      débranchez les jonctions de câbles, puis rebranchez-les.

#### Code 57 — Surveillance de température

**Cause(s) :**

- La chaudière à granulés de bois n'a pas été éteinte pendant le
  remplissage du réservoir à granulés ; il est possible que des gaz de
  fumée chauds aient été aspirés dans le convoyeur de remplissage.
- L'interrupteur thermostatique de sécurité dans le convoyeur de
  remplissage a dépassé 60 °C et a mis la chaudière à granulés de bois à
  l'arrêt.
- Panne/erreur dans la commande du clapet coupe-feu BSK (X9, X34).
- Des gaz de fumée chauds ont été aspirés par la turbine d'aspiration ST
  dans le récipient de stockage.
- Relais enfichable de la turbine d'aspiration ST (X29) défectueux.
- Surpression dans la chambre de combustion :
    - Voies des gaz de fumée dans la chaudière ou le système de gaz
      d'échappement fortement encrassé ou obstrué
    - Mauvais tirage de cheminée
    - Système de gaz d'échappement sousdimensionné

**Dépannage :**

- Débloquez la chaudière à granulés de bois après la livraison des
  granulés ou le remplissage du réservoir à granulés.
- Assurez-vous que l'interrupteur thermostatique de sécurité est
  redescendu à une température inférieure à 60 °C.
- Vérifiez le fonctionnement de l'entrée de la surveillance de
  température TÜB (X35) :
    - A titre d'essai, remplacez l'interrupteur thermostatique de
      sécurité par une jonction de câbles.
    - Débloquez la chaudière. Une fois la panne éliminée, remplacez
      l'interrupteur thermostatique de sécurité.
- Vérifiez la fiche (X35) du raccordement par câble pour vous assurer
  de l'absence de mauvais contact. Pour ce faire, débranchez le câble,
  puis rebranchez-le.
- Vérifiez le fonctionnement du clapet coupe-feu BSK (X9, X34). Pour le
  contrôle et le dépannage, reportez-vous aux codes de pannes 50 et 51.
- Vérifiez la position du clapet coupe-feu BSK (le clapet coupe-feu BSK
  **doit** se fermer complètement, procédez à un contrôle visuel).
- Remplacez le relais enfichable de la turbine d'aspiration ST (X29).
- Nettoyez les voies des gaz de fumées et assurez-vous qu'elles sont
  dégagées.
- Vérifiez les demandes minimales au niveau du besoin en tirage (tirage
  de cheminée) ou mesurez le tirage (pour connaître le besoin en tirage
  des Pelletti II, reportez-vous aux données techniques). Eliminez les
  éventuelles sources d'air parasite (limiteur de tirage non étanche,
  fentes et ouvertures dans la conduite de raccordement à la cheminée).

#### Code 59 — Nombre max. de tentatives de remplissage dépassé (système d'aspiration)

**Cause(s)** (dans les systèmes d'aspiration) :

- Absence de combustible dans le réservoir à granulés.
- Absence de combustible dans le réservoir de stockage.
- L'interrupteur de niveau de la turbine d'aspiration SST (X32)
  s'arrête trop tôt.
- Relais enfichable de la turbine d'aspiration défectueux.
- Turbine d'aspiration défectueuse.
- Pas de puissance d'aspiration.

**Dépannage** (dans les systèmes d'aspiration) :

- Contrôlez le niveau du réservoir à granulés.
- Contrôlez le remplissage du récipient de stockage. Pour ce faire,
  déclenchez le remplissage forcé dans le menu des paramètres de
  l'installation.
- Réduisez l'intervalle d'activation de l'interrupteur de niveau de la
  turbine d'aspiration SST (X32) ou réglez-le/ajustez-le conformément
  aux instructions de montage (chapitre Mise en service).
- Vérifiez la fiche (X32) du raccordement par câble pour vous assurer
  de l'absence de mauvais contact. Pour ce faire, débranchez le câble,
  puis rebranchez-le.
- Vérifiez le fonctionnement de la turbine d'aspiration ST, par ex.
  commandez-la manuellement dans le programme de contrôle (mode Test).
  En cas de défaut constaté, remplacez-la.
- Remplacez le relais enfichable de la turbine d'aspiration ST (X29).
  En cas de défaut constaté, remplacez-le.
- Contrôlez la présence de fuites au niveau de la conduite d'aspiration
  des granulés et de l'air de retour et remédiez-y le cas échéant.
- Contrôlez l'éventuelle présence de fuites dans le récipient de
  stockage et les raccords de flexibles en général.

#### Code 60 — Erreur de l'interrupteur de fin de course du clapet coupe-feu BSK

**Cause(s) :**

- L'information en retour de la position du clapet coupe-feu BSKo/g
  (X34) est erronée.
- Moteur de commande du clapet coupe-feu défectueux.

**Dépannage :**

- Vérifiez le signal de l'information en retour de la position au
  niveau de la fiche X34. En cas de clapet coupe-feu fermé, +12 VDC
  entre les bornes blanche2 (BSK/g) et blanche1/4 (GND). En cas de
  défaut constaté, remplacez le moteur de commande.
- Vérifiez le signal de l'information en retour de la position au
  niveau de la fiche X34. En cas de clapet coupe-feu ouvert, +12 VDC
  entre les bornes blanche6 (BSK/g) et blanche1/4 (GND). En cas de
  défaut constaté, remplacez le moteur de commande.
- Vérifiez la fiche (X34) du raccordement par câble pour vous assurer
  de l'absence de mauvais contact. Pour ce faire, débranchez le câble,
  puis rebranchez-le.

<small>Source : THF1751 p. 14–21</small>

### 6.3 Pannes sans affichage

#### Le module de commande n'affiche rien / Le module de commande ne réagit pas aux entrées

**Cause(s) :**

- L'interrupteur d'arrêt d'urgence du chauffage est désactivé.
- La chaudière n'est pas sous tension.
- Fusible F1 défectueux.
- Absence de raccordement par câble au module de commande PPUI (X14) ou
  fiche débranchée.

**Dépannage :**

- Activez l'interrupteur d'arrêt d'urgence du chauffage.
- Vérifiez la présence d'une tension 230 VAC au niveau de la sortie
  réseau (X2).
- Vérifiez le coupe-circuit automatique (mis à disposition par le maître
  d'œuvre) pour la chaudière à granulés.
- Vérifiez le fusible F1 (10 A/T).
- Vérifiez la fiche (X38) du raccordement par câble vers le module de
  commande pour vous assurer de l'absence de mauvais contact. Pour ce
  faire, débranchez le câble, puis rebranchez-le.

#### Impossible de commander les sorties en mode « Test » / L'affichage revient sur « Arrêt »

**Cause(s) :**

- Le mode Test ne peut être démarré que lorsque la chaudière est en mode
  « Pause » ou lorsque la phase de combustion est terminée.
- Une demande de chaleur est présente.

**Dépannage :**

- Retirez la demande de chaleur, par ex. positionnez le régulateur de
  chauffage sur « Arrêt » ou passez en mode « Arrêt » dans le programme
  de contrôle.
- Attendez la phase de combustion jusqu'à ce que la chaudière soit
  passée automatiquement en mode « Pause ». Passez dans le programme de
  contrôle en mode « Test » et commandez les sorties selon vos besoins.

#### La chaudière produit d'importants cristaux de suie ou est pleine de goudron

**Cause(s) :**

- Mises en marche / à l'arrêt fréquentes de la chaudière ou demandes de
  chaleur brèves mais très fréquentes.
- Manque d'air pendant la combustion.
- Entrée d'air parasite par la porte du foyer (problèmes d'étanchéité).
- Tirage de cheminée trop faible.
- Granulés non brûlés dans le récipient de cendres.
- Trop de granulés sont amenés.
- Clapet coupe-feu BSK non étanche, granulés se consumant à petit feu
  dans le convoyeur de remplissage. Possible également avec le code de
  panne 2 « Absence de flammes ».

!!! note "Remarque"
    Une formation de cristaux de suie dans la chaudière à granulés est
    due à une combustion incomplète (gaz de distillation à basse
    température, manque d'air). Les conséquences d'une combustion
    incomplète sont une plus grande formation de fumée, des rejets plus
    importants de monoxyde de carbone et d'hydrocarbures, tels que la
    suie et le goudron.

**Dépannage :**

- Avec le client, regroupez par blocs les programmes horaires pour la
  production d'eau chaude (évitez si possible l'activation de la
  production d'eau chaude sur toute la journée).
- Assurez une combustion propre. Pour cela, procédez à une analyse des
  gaz d'échappement et réglez la qualité de combustion (voir
  chapitre 4.3).
- Evitez l'air parasite. Assurez la fermeture étanche de la porte du
  foyer. Ajustez si nécessaire la porte de foyer au niveau de la poignée
  (voir chapitre 4.3).
- Assurez un tirage de cheminée suffisant :
    - Isolez le tube de raccordement vers la cheminée contre les pertes
      de chaleur.
    - Réglez la température des gaz d'échappement sur 140-170 °C (voir
      chapitre 4.4).
- Retirez les granulés non consumés du récipient de cendres. Nettoyez le
  plateau de combustion (chapitre 3.4). Si nécessaire, réduisez
  légèrement la quantité de combustible. Procédez à une analyse des gaz
  d'échappement (voir chapitre 4.3).
- Vérifiez l'étanchéité du clapet coupe-feu :
    - *Dans les systèmes d'aspiration :* retirez le récipient de
      stockage.
    - *Dans les systèmes de vis sans fin :* retirez le tuyau flexible.
      Procédez à un contrôle visuel du clapet coupe-feu BSK. Pour cela,
      désactivez la chaudière. La sphère dans le clapet coupe-feu doit
      complètement fermer la section libre à l'état hors tension (pas
      d'écart admissible). Si un écart est visible, réglez le clapet
      coupe-feu (robinet à tournant sphérique). Pour cela, retirez le
      moteur BSK et tournez le robinet jusqu'à ce que la section
      complète soit fermée. Poussez de nouveau le moteur BSK.
- Remplacez le clapet coupe-feu BSK s'il existe une tolérance (du jeu)
  entre l'axe du clapet coupe-feu et le manchon d'entraînement du moteur
  BSK.
- Pour le nettoyage de la chaudière, utilisez un produit spécial suie et
  goudron pour le nettoyage des chaudières à combustible solide que vous
  trouverez chez un spécialiste (par ex. Fauch 300).

<small>Source : THF1751 p. 22</small>
