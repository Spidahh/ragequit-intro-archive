import subprocess,sys
text="ma quel cazzo di arciere che spara lentissimo nel nulla la freccia a che cazzo serve ? poorcodio , è ancora una merda, dio porcoio, ma s come cvfazzo sdi fa un viudeo ? è lento!! non ce azione, non succede nulla, porcodio sei una merda inutile fa isempre le solite cazzate di merda, ti avvevo chiesto un video professionaloe e sai realizzare siolo questa merda è assurdo porcodio, ti avevo detto di usare programmi esterni anche ee skil e altro, porcodio perchè fai questa merda ?"
subprocess.run([sys.executable,'tools/direttive.py','parole',text],check=True)
