label part2:

    #scene black with Fade(0.7,0.2,0.7)

    #"O futuro é incerto. Tudo pode acontecer quando os desejos, sonhos e ambições de duas pessoas são colocados à prova em nome da convivência íntima e intensa que o amor traz."

    #"O que acontecerá na vida deste novo casal? Como a vida deles seguirá? Como eles viverão seus momentos felizes? Como eles resolverão seus conflitos? Como eles lidarão com as diferenças?"

    #"Essa história fica para outro dia. Um dia não muito distante. Mas ainda não é a hora certa para contar a vocês."
    
    
    #Load all stuff as Sofia's
    if nDatesSofia == 3:
        python:
            g = s
            girltransform = noghost
            renpy.copy_images("sofia", "girlfriend")
        
    
    #Load all stuff as Mariana's
    elif nDatesMariana == 3:
        python:
            g = m
            girltransform = arantesnoghost
            renpy.copy_images("mariana", "girlfriend")
        
    #Load all stuff as Rafaela's
    else:
        python:
            g = r
            girltransform = noghost
            renpy.copy_images("rafaela", "girlfriend")
    
    jump part2firstevent
    
    return
