prenume=['Mihai' , 'George' , 'Ana' , 'Dan' , 'Ion' , 'Geta' , 'Vio']
varsta=[14 , 23 , 15 , 14 , 12 , 41 , 39]
prenume.extend(['Andreea' , 'Ion'])
varsta.extend([34 , 23])
print('Adăuga la final: (Andreea,Ioan)'  , prenume)
print('Adăuga la final: 34 și 23' , varsta)
prenume.pop(2)
varsta.pop(2)
print('Șterge Ana:' ,prenume)
print('Șterge varsta Anei:' ,varsta)
print('Afișa primele trei elemente din prenume:' ,prenume[0:3])
print('Afișa lista prenume de la dreapta la stânga:' ,prenume[::-1])
print('Afişa cu indicii 2 și 4:' ,prenume[2] , prenume[4])
print('Afişa de la 0 la 5:' , varsta[0:5])