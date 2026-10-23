import subprocess,sys
messages=["porcodio ma perchè continui a fare le stesse cazzate dimerda ?pèorocdio è una merda sto ideeo vuoi capirlo pezzo di emrda, è fdatot male è sbagliatyo , hai mai vbisot una scena di combattimento vera o di un film o un amime ? non èquello che hai realizzato procoideo hai fatot una merda è un frame che scorre non è un cazoz di video pezoz dimerda ma che cazo combini ? ma la smetit di f<re queste cazzate di merdA ?","cime cazoz lavori pezzo di merdA ?","come cazzo faccio a farti fare una cosa decente, porcodio unaaaaaaa nella tua vita di merda"]
for message in messages:
    subprocess.run([sys.executable,'tools/direttive.py','parole',message],check=True)
subprocess.run([sys.executable,'tools/direttive.py','bocciato','--tema','immagini','--testo','Autore boccia ragequit-duello.mp4: realizzazione sbagliata, percepita come un frame che scorre anziche un combattimento credibile di film o anime. Chiede di smettere con questi rifacimenti ripetuti e contesta il metodo. Non proporre di nuovo questa produzione come riuscita.','--parole',messages[0]],check=True)
subprocess.run([sys.executable,'tools/direttive.py','export'],check=True)
