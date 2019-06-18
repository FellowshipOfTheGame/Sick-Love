label part1options:
    "o que será que devo fazer essa semana?"

    menu:
        "Ir para a biblioteca" if nDatesSofia == 0:
            jump sofiafirstdate

        "Conversar com a Sofia" if nDatesSofia == 1:
            jump sofiaseconddate

        "Marcar um encontro com a Sofia" if nDatesSofia == 2:
            jump sofiathirddate

        "Ficar e conversar com o grupo na sala" if nDatesMariana == 0:
            jump marianafirstdate

        "Conversar com a Mariana" if nDatesMariana == 1:
            jump marianaseconddate

        "Marcar um encontro com a Mariana" if nDatesMariana == 2:
            jump marianathirddate
            
        "Ir para o ginásio esportivo" if nDatesRafaela == 0:
            jump rafaelafirstdate
            
        "Conversar com a Rafaela" if nDatesRafaela == 1:
            jump sofiaseconddate

    return
