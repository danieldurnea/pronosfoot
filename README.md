[![Build Status](https://travis-ci.org/dmartin35/pronosfoot.svg?branch=master)](https://travis-ci.org/dmartin35/pronosfoot)

# pronosfoot
Site web perso de pronos entre amis pour la Ligue 1


Présentation
------------
Ce site est un "vieux" projet né 2010, pour remplacer les fichiers excel envoyés par mails entre copains,
avec mise à jour auto des calendrier & resultats issus du site officiel de la LFP.

Il fonctionne toujours en production sous django 1.0.2 & python 2.5.
Je démarre une tentative de rajeunir ce projet et surtout mettre à jour les dépendances utilisées.
Le code est maintenant porté sur django 1.10 & python 3.4+.
Nouveau design utilisant material design.

Crons
-----
```bash
pronosfoot@ssh:~$ crontab -l
# m h  dom mon dow   command
30 23 * * * ~/pronosfoot/admin/cron_task_launcher.sh daily.py
0 12 * * * ~/pronosfoot/admin/cron_task_launcher.sh daily_remind.py
0 0 * * * ~/pronosfoot/admin/cron_task_launcher.sh maintenance.py
```

Notes
-----

- Remplacer maintenance.py par python manage.py clearsessions


