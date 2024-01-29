# Exercises slide 57
# given a unary function f and a sequence S, return the list 
# of the application of f to the element of S

def appl_unary(S,f):
    return [f(s) for s in S]

# Given two sequences s1 and s2 return the list of the
# elements present both in s1 and s2 (without caring about multiplicity)
def both_present(S1,S2):
    return [s1 for s1 in S1 if s1 in S2]
# def both_present(S1,S2):
#     return [s2 for s2 in S2 if s2 in S1]

def pythagorean_triples(k):
    # pythagorean triples (a,b,c) such that a^2+b^2 + c^2 <= k
    return [(a,b,c) for a in range(1,k) for b in range(1,k) for c in range(1,k) if a**2 + b**2 - c**2 == 0 if a**2+b**2+c**2 <= k]

def Floyd(d):
    # prints a floid triangle of order n, i.e. with n rows
    start = 1  # first number at the beggining of a row
    for i in range(1,d+1):
        end = start + i
        for k in range(start, end):
            print(k,end=' ')
        print('')
        start = end


# Write a function add_n_print(L,obj,pos,replace) that takes  4 parameters:
# L: a list
# obj: any object to be added to the list
# pos: the position in the list where to add the object
# replace: a boolean value (True|False) indicating if the object replaces the previous one at index pos
# Ideally, the function returns L with obj added at index pos.
# In some cases, the function returns an error message.

# Consider that:
# if L is not a list, the function returns the string "not a list".
# if pos is not a valid index of the list, the function returns "invalid pos"; note that, if pos==len(L) (i.e., the first position after the last valid index) the object is added after the last one.
# if replace is False, the (possible) objects after pos shift right by one.

# def add_n_print(L,obj,pos,replace):
#  # L: a list
#  # obj: any object to be added to the list
#  # pos: the position in the list where to add the object
#  # replace: a boolean value (True|False) indicating if the object replaces the previous one at index pos   
#     if type(L) != list:
#         return "not a list"
#     elif pos < -1 or pos > len(L): # not a valid index
#         return "invalid pos"
#     elif 
#     # if here we have a list with a valid index
#     if replace: # inserting in place of the old one
#         return L[:pos] + L[pos+1:]
#     else: # simply insert/append to the list
#         return L[:pos-1] + [obj] + L[pos:]
    
# solution
def add_n_print(L,obj,pos,replace):
     # L: a list
 # obj: any object to be added to the list
 # pos: the position in the list where to add the object
 # replace: a boolean value (True|False) indicating if the object replaces the previous one at index pos   
    if type(L)!=list:
        return 'not a list'
    if pos<0 or pos>len(L):
        return 'invalid pos'
    if pos < len(L):
        if replace: # more convenient than 'if replace==True:'
            L[pos] = obj
        else:
            L.insert(pos,obj)
    else:
        L.append(obj)
    return L


# Write a function str_to_list(s) that takes as parameter a string s and returns a list with some of the characters of the input string.

# If all the characters in s are alphabetic, the result list contains only the consonants, in the same order they appear in the string. Whether the consonants in s are lower or upper case letters, they are put in the list capitalized.
# If all the characters in s are digits, the result list contains only the odd digits, but in reverse order.
# NB: The result list contains unique characters: if a character (consonant or odd digit) appears in s more than once, only the first occurrence is considered.

# Special cases:
# If s is not a string, the function returns 'not a string'.
# If s does not contain only alphabetic characters, or only digits, the function returns 'alphanumeric'.
# If s is empty, the function returns the empty list

# this can be a solution if duplicates are removed from resul list in isalpha() == True case
def str_to_list(s):
    if type(s) != str:
        return 'not a string'
    result = ''
    if s.isalpha(): #contains just letters
        result = [char.capitalize() for char in s if char.capitalize() not in 'AEIOU']
        return result
    if s.isdigit(): # is a number
        result = [num for num in s if int(num) %2 != 0]
        result = list(set(result))
        result.sort(reverse=True)
        return result
    if len(s) == 0:
        return []
    else:  # contains both digits and letters
        return 'alphanumeric'
    

# solution 
# def str_to_list(s):
#     if type(s) != str:
#         return 'not a string'
#     R = []
#     if len(s) == 0:
#         return R
#     if s.isalpha():
#         R = []
#         s = s.upper()
#         for c in s:
#             if c not in R and c not in 'AEIOU':
#                 R.append(c)
#         return R 
#     if s.isdigit():
#         R = []
#         for d in s:
#             if d not in R and int(d)%2 == 1:
#                 R.insert(0,d)
#         return R
#     return 'alphanumeric'
    

###----------------------------------------------------###
# Collatz algorithm

# Collatz conjecture is based on the following algorithm:
# Take a positive integer number m.
# If m=1 the algorithm terminates.
# If m is even, divide it by 2 (integer division); if m is odd, multiply it by 3 and sum 1.
# Start again with the new m updated as above.
# The conjecture, yet unproven, states this algorithm always terminates.

# Write a function collatz(m) that returns a list containing all the numbers of the Collatz sequence from m to 1.
    
# def collatz_step(m):
#     if m == 1 :
#         return
#     if m % 2 == 0:
#         return m //2
#     else:
#         return (m*3 +1)
    
# recursive
# def collatz(m):
#     if m == 1 :
#         return 'finished'
#     if m % 2 == 0:
#         return collatz(m //2)
#     else:
#         return collatz(m*3 +1)

def collatz(m):
    L = []
    if m < 1:
        return []
    while m > 1:
        L.append(m)
        if m % 2 == 0:
            m //= 2
        else:
            m *= 3
            m+=1
    return L + [1,]

# ciao mi chiamo Giulia, il mio ragazzo Niccolo [ [[ e molto intelligente, lo amo un saccoooooooooooo]]]

# Write a function increasing(L) that checks if a list L is sorted in ascending order (<=).

# Suppose that L is a list and contains objects that can be ordered, without checkin).

# Then, write a function join_ordered(L1, L2) which takes as parameters two lists ordered in ascending order (check it using the increasing function), creates and returns a third one, also ordered, from the union of the two.

# If at least one of the two lists is not in ascending order, return None.

# Do not use the sort function (or analogous, e.g. sorted) - for us to check this, you are not allowed in this test to use any words (even in comments) containing the substring sort.

def increasing(L):
    for i in range(1,len(L)):
        if L[i] < L[i-1]:
            return False
    return True

def join_ordered(L1,L2):
    if not increasing(L1) or not increasing(L2):
        return None
    i = 0
    j = 0
    R = []
    while i < len(L1) and j < len(L2):
        if L1[i] <= L2[j]:
            R.append(L1[i])
            i += 1
        else:
            R.append(L2[j])
            j += 1
    # let's determine which lists was completely scanned
    if i == len(L1):
        R.extend(L2[j:])
    else: # j == len(L2)
        R.extend(L1[i:])
    return R

# Write a function contiguous(L) that takes a list L as a parameter and creates and returns a new 
# list with values taken from L - in which a series of equal contiguous values is replaced by one 
# single entry of the value followed by the number of occurrences of the equal contiguous values in L.

def check_cont(start_i,L):
#return num of contiguous occurences of an element of the list
    occur = 1
    for i in range(start_i+1,len(L)):
        if L[i] == L[i-1]:
            occur +=1
        else:
            return occur
    return occur # reached when the list is scanned all the way down to its length

def contiguous(L):
    R = []
    i = 0
    occur = 1
    while i < len(L):
        occur = check_cont(i,L)
        if occur == 1:
            R.append(L[i])
            i  += 1
        else:
            R.append(L[i])
            R.append(occur)
            i  += occur
    return R

# TODO Write a function contiguous_inplace(L) that (analougosly to the previous exercise) takes a list L as a parameter and modifies the list L such that a series of equal contiguous values is replaced by one single entry of the value followed by the number of occurrences of the equal contiguous values in A.

# The function does not return anything. It modifies L without modyfing the id and without using auxiliary structures like other lists or tuples.

# def contiguous_inplace(L):
    
# To check that the modified list is actually the same as the one passed as a parameter, the test will check that the id (of the two lists) match, and that list L has been modified correctly. However, you will not see any results in the automatic tests. A possible test to do in Thonny is the following:

# A = ['a','b','b','z','o','o','b','b','b','b','k']
# AR = ['a', 'b', 2, 'z', 'o', 2, 'b', 4, 'k']
# id_before = id(A)
# contiguous_inplace(A)
# print((id_before == id(A)) and (A == AR))

# -------------------------------------------------------------------------
# Write a Python program (not a function!) that asks the user for non-negative integers that represent measurements of the daily amount of rain.

# When the user enters the value 99999, the program prints the average of the numbers received before that value.
# If the user enters negative numbers, they are ignored.

# The system will automatically input some values (shown, one at a time) to test your program

# To make the automatic system work:

# The input descriptive string should be exactly R: (with no black spaces: hence you should use input("R:"))
# The output should be the print of float, mandatory rounded using function round to two decimal digits, without any other characters
# If there is no valid input, the program does not print anything.
# In this exercise only you are allowed, and required, to use print.

def ex2_5_prompt():
    
    L= []
    el= input("R:")
    
    while el != '9999':
        if int(el) >= 0:
            L.append(int(el))
        el= input("R:")
    
    average = sum(L) / len(L)
    print(round(average,2))

# The tuple voc, already defined in the global environment, contains in alphabetical order the 1160 most common words in the Italian language, in the form of strings.

# Write a bin_search(word) function that takes as parameter a word string (suppose it is a string without checking) and returns a tuple of two elements that contains, in order:

# the position of the string word in the tuple voc (i.e. the first element'a' has position 0, the last 'zone' has position 1159), or -1 if word is not present in voc
# the number of attempts the algorithm has made to find the location of word
# Using the binary search algorithm
    
#name voc is bound to a tuple containing
#the 1160 most common italian words, in alphabetical order

import math as mth

voc = ('a', 'abbandonare', 'abbastanza', 'abitare', 'abito', 'accadere', 'accanto', 'accendere', 'accettare', 'accogliere', 'accompagnare', 'accordo', 'accorgersi', 'acqua', 'addirittura', 'addosso', 'adesso', 'affare', 'affatto', 'affermare', 'affrontare', 'aggiungere', 'ah', 'aiutare', 'aiuto', 'albergo', 'albero', 'alcuno', 'allontanare', 'allora', 'almeno', 'alto', 'altro', 'alzare', 'amare', 'ambiente', 'americano', 'amico', 'ammazzare', 'ammettere', 'amore', 'ampio', 'anche', 'ancora', 'andare', 'angolo', 'anima', 'animale', 'animo', 'anno', 'annunciare', 'antico', 'anzi', 'apparire', 'appartenere', 'appena', 'appoggiare', 'appunto', 'aprire', 'argomento', 'aria', 'arma', 'armare', 'arrestare', 'arrivare', 'arte', 'articolo', 'ascoltare', 'aspettare', 'aspetto', 'assai', 'assicurare', 'assistere', 'assoluto', 'assumere', 'attaccare', 'atteggiamento', 'attendere', 'attento', 'attenzione', 'attesa', 'attimo', 'attività', 'atto', 'attore', 'attorno', 'attraversare', 'attuale', 'aumentare', 'automobile', 'autore', 'autorità', 'avanti', 'avanzare', 'avere', 'avvenire', 'avvertire', 'avvicinare', 'avvocato', 'azione', 'azzurro', 'baciare', 'badare', 'bagno', 'bambina', 'bambino', 'base', 'basso', 'bastare', 'battaglia', 'battere', 'bellezza', 'bello', 'bene', 'bere', 'bestia', 'bianco', 'biondo', 'bisognare', 'bisogno', 'bocca', 'bosco', 'braccio', 'bravo', 'breve', 'bruciare', 'brutto', 'buio', 'buono', 'buttare', 'cadere', 'caffè', 'calcio', 'caldo', 'cambiare', 'camera', 'camminare', 'campagna', 'campo', 'cane', 'cantare', 'capace', 'capello', 'capire', 'capitare', 'capo', 'carattere', 'caratteristico', 'carne', 'caro', 'carta', 'casa', 'caso', 'cattivo', 'cattolico', 'causa', 'cavallo', 'celebrare', 'centrale', 'centro', 'cercare', 'certamente', 'certo', 'che', 'chi', 'chiamare', 'chiaro', 'chiave', 'chiedere', 'chiesa', 'chilometro', 'chissà', 'chiudere', 'ci', 'ciascuno', 'cielo', 'cioè', 'circa', 'cittadino', 'città', 'civile', 'civiltà', 'ciò', 'classe', 'collina', 'collo', 'colore', 'coloro', 'colpa', 'colpire', 'colpo', 'come', 'cominciare', 'commercio', 'commissione', 'comodo', 'compagnia', 'compagno', 'compiere', 'completamente', 'comporre', 'comprare', 'comprendere', 'comune', 'comunicazione', 'comunque', 'con', 'concedere', 'concetto', 'concludere', 'condizione', 'condurre', 'confessare', 'confronto', 'congresso', 'conoscenza', 'conoscere', 'conseguenza', 'consentire', 'conservare', 'considerare', 'consiglio', 'contadino', 'contare', 'contatto', 'contenere', 'contento', 'continuare', 'continuo', 'conto', 'contrario', 'contro', 'controllo', 'convincere', 'coprire', 'coraggio', 'corpo', 'corrente', 'correre', 'corsa', 'corso', 'cortile', 'cosa', 'coscienza', 'costa', 'costituire', 'costringere', 'costruire', 'costruzione', 'creare', 'credere', 'crescere', 'crisi', 'cristiano', 'croce', 'cucina', 'cui', 'cultura', 'cuore', 'cura', 'da', 'dare', 'davanti', 'davvero', 'decidere', 'decisione', 'dedicare', 'denaro', 'dente', 'dentro', 'descrivere', 'desiderare', 'desiderio', 'destino', 'destro', 'determinare', 'di', 'dichiarare', 'dietro', 'difendere', 'difesa', 'differenza', 'difficile', 'difficoltà', 'diffondere', 'dimenticare', 'dimostrare', 'dinanzi', 'dio', 'dipendere', 'dire', 'diretto', 'direttore', 'direzione', 'dirigere', 'diritto', 'discorso', 'discutere', 'disporre', 'disposizione', 'distanza', 'distinguere', 'distruggere', 'dito', 'divenire', 'diventare', 'diverso', 'divertire', 'dividere', 'dolce', 'dolore', 'domanda', 'domandare', 'domani', 'domenica', 'don', 'donna', 'dopo', 'dormire', 'dottore', 'dove', 'dovere', 'dubbio', 'dunque', 'durante', 'durare', 'duro', 'e', 'eccellenza', 'eccetera', 'ecco', 'economico', 'effetto', 'egli', 'eh', 'elemento', 'elettrico', 'elevare', 'energia', 'enorme', 'entrare', 'entro', 'epoca', 'eppure', 'erba', 'errore', 'esame', 'escludere', 'esempio', 'esercito', 'esistere', 'esperienza', 'esporre', 'espressione', 'esprimere', 'essa', 'essere', 'esso', 'estate', 'estendere', 'estero', 'estremo', 'età', 'europeo', 'evitare', 'fabbrica', 'faccia', 'facile', 'fame', 'famiglia', 'famoso', 'fantasia', 'fatica', 'fatto', 'favore', 'fede', 'felice', 'fenomeno', 'ferire', 'fermare', 'fermo', 'ferro', 'festa', 'fianco', 'fiducia', 'figlia', 'figlio', 'figura', 'figurare', 'film', 'filo', 'finalmente', 'finché', 'fine', 'finestra', 'finire', 'fino', 'fiore', 'fissare', 'fiume', 'foglia', 'folla', 'fondare', 'fondo', 'forma', 'formare', 'fornire', 'forse', 'forte', 'fortuna', 'forza', 'fra', 'francese', 'frase', 'fratello', 'freddo', 'fresco', 'fretta', 'fronte', 'frutto', 'fuggire', 'fumare', 'funzione', 'fuoco', 'fuori', 'futuro', 'gamba', 'gatto', 'generale', 'genere', 'gente', 'gesto', 'gettare', 'giallo', 'giardino', 'giocare', 'gioco', 'gioia', 'giornale', 'giornata', 'giorno', 'giovane', 'giovanotto', 'girare', 'giro', 'giudicare', 'giudizio', 'giugno', 'giungere', 'giustizia', 'giusto', 'già', 'giù', 'godere', 'governo', 'grado', 'grande', 'grave', 'grazia', 'grazie', 'greco', 'gridare', 'grigio', 'grosso', 'gruppo', 'guardare', 'guardia', 'guerra', 'guidare', 'gusto', 'idea', 'ieri', 'il', 'immaginare', 'immagine', 'imparare', 'impedire', 'imporre', 'importante', 'importanza', 'importare', 'impossibile', 'impressione', 'improvviso', 'in', 'incontrare', 'indicare', 'indietro', 'industria', 'industriale', 'infatti', 'infine', 'inglese', 'iniziare', 'inizio', 'innamorare', 'inoltre', 'insegnare', 'insieme', 'insistere', 'insomma', 'intanto', 'intendere', 'intenzione', 'interessante', 'interessare', 'interesse', 'internazionale', 'interno', 'intero', 'intorno', 'inutile', 'invece', 'inverno', 'invitare', 'io', 'isola', 'istante', 'istituto', 'italiano', 'labbro', 'lago', 'lanciare', 'largo', 'lasciare', 'latino', 'lato', 'latte', 'lavorare', 'lavoro', 'legare', 'legge', 'leggere', 'leggero', 'lei', 'lettera', 'letto', 'levare', 'li', 'liberare', 'libero', 'libertà', 'libro', 'limitare', 'limite', 'linea', 'lingua', 'lira', 'lo', 'lontano', 'loro', 'lotta', 'luce', 'lui', 'luna', 'lungo', 'luogo', 'là', 'lì', 'ma', 'macchina', 'madre', 'maestro', 'magari', 'maggio', 'maggiore', 'malattia', 'male', 'mamma', 'mancare', 'mandare', 'mangiare', 'maniera', 'mano', 'mantenere', 'mare', 'marito', 'massa', 'massimo', 'materia', 'matrimonio', 'mattina', 'mattino', 'medesimo', 'medico', 'medio', 'meglio', 'memoria', 'meno', 'mente', 'mentre', 'mercato', 'meritare', 'merito', 'mese', 'messa', 'mestiere', 'metro', 'mettere', 'metà', 'mezzo', 'mi', 'migliore', 'milione', 'militare', 'minimo', 'ministro', 'minore', 'minuto', 'mio', 'misura', 'moderno', 'modo', 'moglie', 'molto', 'momento', 'mondo', 'montagna', 'monte', 'morale', 'morire', 'morte', 'mostrare', 'motivo', 'movimento', 'muovere', 'muro', 'musica', 'nascere', 'nascondere', 'natura', 'naturale', 'naturalmente', 'nave', 'nazionale', 'nazione', 'ne', 'neanche', 'necessario', 'necessità', 'nemico', 'nemmeno', 'neppure', 'nero', 'nessuno', 'niente', 'no', 'nobile', 'noi', 'nome', 'non', 'nord', 'normale', 'nostro', 'notare', 'notevole', 'notizia', 'noto', 'notte', 'nudo', 'nulla', 'numero', 'numeroso', 'nuovo', 'né', 'o', 'occasione', 'occhio', 'occorrere', 'odore', 'offendere', 'offrire', 'oggetto', 'oggi', 'ogni', 'ognuno', 'oh', 'oltre', 'ombra', 'onore', 'opera', 'operaio', 'operazione', 'opinione', 'opporre', 'oppure', 'ora', 'oramai', 'ordinare', 'ordine', 'orecchio', 'organizzare', 'origine', 'oro', 'ospedale', 'osservare', 'ottenere', 'pace', 'padre', 'padrone', 'paese', 'pagare', 'pagina', 'palazzo', 'pane', 'papà', 'parecchio', 'parere', 'parete', 'parlare', 'parola', 'parte', 'partecipare', 'particolare', 'partire', 'partito', 'passare', 'passato', 'passione', 'passo', 'patria', 'paura', 'pazzo', 'peccato', 'peggio', 'pelle', 'pena', 'pensare', 'pensiero', 'per', 'perché', 'perciò', 'perdere', 'perfetto', 'perfino', 'pericolo', 'pericoloso', 'periodo', 'permettere', 'persona', 'personaggio', 'personale', 'però', 'pesare', 'peso', 'pezzo', 'piacere', 'piangere', 'piano', 'pianta', 'piantare', 'pianura', 'piazza', 'piccolo', 'piede', 'pieno', 'pietra', 'pietà', 'piuttosto', 'più', 'poco', 'poesia', 'poeta', 'poiché', 'politica', 'politico', 'polizia', 'pomeriggio', 'ponte', 'popolazione', 'popolo', 'porre', 'porta', 'portare', 'porto', 'posare', 'posizione', 'possedere', 'possibile', 'possibilità', 'posto', 'potenza', 'potere', 'povero', 'pranzo', 'prato', 'preciso', 'preferire', 'pregare', 'prendere', 'preoccupare', 'preparare', 'presentare', 'presente', 'presenza', 'presidente', 'presso', 'presto', 'prevedere', 'prezzo', 'prima', 'primo', 'principale', 'principe', 'principio', 'privato', 'probabilmente', 'problema', 'procedere', 'processo', 'prodotto', 'produrre', 'produzione', 'professore', 'profondo', 'programma', 'promettere', 'pronto', 'proporre', 'proposito', 'proposta', 'proprio', 'prossimo', 'prova', 'provare', 'provincia', 'provocare', 'provvedere', 'pubblicare', 'pubblico', 'punta', 'punto', 'pure', 'puro', 'qua', 'quadro', 'qualche', 'qualcosa', 'qualcuno', 'quale', 'qualità', 'qualsiasi', 'qualunque', 'quanto', 'quarto', 'quasi', 'quello', 'questione', 'questo', 'qui', 'quindi', 'raccogliere', 'raccontare', 'ragazza', 'ragazzo', 'raggiungere', 'ragione', 'rapido', 'rapporto', 'rappresentare', 'reale', 'realtà', 'recare', 'recente', 'regione', 'regno', 'relazione', 'religioso', 'rendere', 'repubblica', 'resistere', 'restare', 'resto', 'ricchezza', 'ricco', 'ricerca', 'ricevere', 'richiedere', 'riconoscere', 'ricordare', 'ricordo', 'ridere', 'ridurre', 'riempire', 'rientrare', 'riferire', 'rifiutare', 'riguardare', 'rimanere', 'rimettere', 'ringraziare', 'ripetere', 'riportare', 'riprendere', 'risolvere', 'rispetto', 'rispondere', 'risposta', 'risultare', 'risultato', 'ritenere', 'ritornare', 'ritorno', 'ritrovare', 'riunire', 'riuscire', 'riva', 'rivedere', 'rivelare', 'rivolgere', 'rivoluzione', 'roba', 'romano', 'rompere', 'rosso', 'russo', 'sacrificio', 'sacro', 'sala', 'salire', 'saltare', 'salutare', 'salvare', 'sangue', 'sapere', 'sbagliare', 'scala', 'scappare', 'scegliere', 'scena', 'scendere', 'scherzare', 'scienza', 'scomparire', 'scopo', 'scoppiare', 'scoprire', 'scorrere', 'scrittore', 'scrivere', 'scuola', 'scusare', 'se', 'secolo', 'secondo', 'sede', 'sedere', 'segnare', 'segno', 'segretario', 'segreto', 'seguire', 'seguito', 'sembrare', 'semplice', 'senso', 'sentimento', 'sentire', 'senza', 'sera', 'sereno', 'serie', 'serio', 'servire', 'servizio', 'settimana', 'sforzo', 'sguardo', 'si', 'sicurezza', 'sicuro', 'significare', 'signora', 'signore', 'signorina', 'silenzio', 'simile', 'sinistro', 'sino', 'sistema', 'situazione', 'smettere', 'sociale', 'società', 'soffrire', 'sognare', 'sogno', 'soldato', 'sole', 'solito', 'solo', 'soltanto', 'soluzione', 'sonno', 'sopra', 'soprattutto', 'sorella', 'sorgere', 'sorprendere', 'sorridere', 'sorriso', 'sostenere', 'sottile', 'sotto', 'spalla', 'spazio', 'speciale', 'specie', 'spegnere', 'speranza', 'sperare', 'spesa', 'spesso', 'spettacolo', 'spiegare', 'spingere', 'spirito', 'sposare', 'stabilire', 'staccare', 'stagione', 'stamattina', 'stampa', 'stanco', 'stanza', 'stare', 'stasera', 'stato', 'stazione', 'stella', 'stesso', 'storia', 'storico', 'strada', 'straniero', 'strano', 'straordinario', 'stringere', 'strumento', 'studiare', 'studio', 'stupido', 'su', 'subito', 'succedere', 'successo', 'sud', 'suo', 'suonare', 'superare', 'superiore', 'svegliare', 'sviluppo', 'svolgere', 'sì', 'tacere', 'tagliare', 'tale', 'tanto', 'tardi', 'tavola', 'tavolo', 'teatro', 'tecnico', 'tedesco', 'temere', 'tempo', 'tendere', 'tenere', 'tentare', 'termine', 'terreno', 'territorio', 'terzo', 'testa', 'tipo', 'tirare', 'titolo', 'toccare', 'togliere', 'tono', 'tornare', 'tra', 'tranquillo', 'trarre', 'trascinare', 'trasformare', 'trattare', 'tratto', 'treno', 'triste', 'troppo', 'trovare', 'tu', 'tuo', 'tuttavia', 'tutto', 'uccidere', 'udire', 'ufficiale', 'ufficio', 'uguale', 'ultimo', 'umano', 'un', 'unico', 'unire', 'università', 'uno', 'uomo', 'usare', 'uscire', 'uso', 'utile', 'valere', 'valle', 'valore', 'vario', 'vasto', 'vecchio', 'vedere', 'vendere', 'venire', 'vento', 'veramente', 'verde', 'verità', 'vero', 'verso', 'vestire', 'vestito', 'vi', 'via', 'viaggio', 'vicino', 'villa', 'vincere', 'vino', 'visita', 'viso', 'vista', 'vita', 'vivere', 'vivo', 'voce', 'voglia', 'voi', 'volare', 'volere', 'volgere', 'volontà', 'volta', 'voltare', 'volto', 'vostro', 'vuoto', 'zia', 'zio', 'zitto', 'zona')

# def bin_search(word):
#     L = 0
#     R = len(voc) - 1
    
#     i = 1  # keeps track of algorithm steps
#     while L <= R:
#         m = mth.floor((L+R)/2)
#         elem = voc[m]
#         if word < elem:
#             R = m - 1  # search the first half
#             i += 1 
#         elif word > elem: 
#             L = m + 1
#             i += 1
#         else:
#             return (m,i) # (index, n. steps)
#      # L > R 
#     return (-1,i)

# solution

def bin_search(word):
    high = len(voc)
    low = 0
    n = 0 #numero di tentativi    
    while low < high:
        n = n+1
        med = (high+low)//2
        if voc[med] == word:
            return med, n
        if word < voc[med]:
            high = med
        else:
            low = med+1
    return -1, n


'''print(bin_search('a'))
print(bin_search('casa'))
print(bin_search('voluttuoso'))
print(bin_search('Michael'))
print(bin_search('bello'))
print(bin_search('zona'))
print(bin_search('vero'))
print(bin_search('medico'))
print(bin_search(''))'''


