# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.


# The game starts here.

label sofiaseconddate:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room
    with Fade(0.7,0.2,0.7)

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    # These display lines of dialogue.

    "Terminei! Esse também foi intenso! Caramba, nunca pensei que fosse possível sentir medo lendo um livro."
    
    "Desde minha primeira visita na biblioteca eu virei fã de contos de terror, e agora eu terminei o último conto de Lovecraft que faltava, \"A Sombra Vinda do Tempo\"."
    
    "Foi um dos melhores dele. Acho que não senti tantos calafrios enquanto lia em nenhum outro."
    
    "Eu preciso agradecer a Sofia pelas recomendações. Nunca achei que eu ia gostar tanto de livros de Horror."
    
    "Já tá meio tarde. Será que eu mando mensagem agora? Será que ela deixa as coisas no silencioso antes de dormir?"
    
    "Eu sempre coloco porque o <i>spam</i> é real nos grupos, mas e se eu acordar ela? Huuum, melhor esperar amanhã. Não quero que ela me odeie pro resto da vida."
    
    "É. Acho que vou dormir. Não é como se eu estivesse levemente apreensivo por ler um livro sobre criaturas de outra dimensão que podem te deixar louco só de pensar nelas."
    
    "Com certeza não. Quem ficaria com medo de um livro. Que absurdo..."
    
    # TODO: Tela preta - barulho de energia apagando
    
    p "Mas que diabos! Acabou a luz? BEM AGORA? SÉRIO!?"
    
    p "Só me faltava essa. Tem curso de engenharia elétrica na universidade e ninguém tem a capacidade de fazer manutenção na rede elétrica e não sobrecarregar o transformador."
    
    p "Não vou nem começar a falar do <i>wifi</i>..."
    
    # TODO: Som de vento creepy
    
    "... Ok... Eu acho que vou mandar uma mensagem pra Sofia. Não por estar com medo. Com certeza não. É pra passar o tempo..."
    
    "Pior que vou ter que usar o 3G. Triste a vida."

    p "Opa! Ela respondeu."
    
    "<i>- Algumas mensagens depois -</i>"
    
    p "Esse final de semana você vai estar livre? Eu estava pensando em ir pra algum lugar e a gente pode trocar uma ideia sobre livros, a vida, o universo e tudo mais."

    s "*risos* Gostei da referência. Eu estava querendo ir ver uma exposição temática de terror no museu. Disseram que está muito boa. Quer ir?"

    p "Claro! Não costumo ir em museus, mas depois das suas ótimas recomendações de livro, vou arriscar. Vai ver descubro mais uma coisa que eu gosto e nunca iria imaginar."
    
    p "E no pior dos casos, vai ter você pra conversar, então está ótimo!"
    
    s "Perfeito! Só não vale me culpar depois se você se apaixonar por esculturas grotescas."
    
    p "*risos* Pode deixar."

    "<i>- Algumas despedidas depois e a conversa chega ao fim -</i>"

    "Ok, eu acho que estou mais calmo agora. Vou conseguir dormir tranquilo..."
    
    p "<i>PERA!</i>"
    
    p "Eu acabei de marcar um encontro com uma garota?" 
    
    "Será que isso é um encontro? Eu não pensei direito porque eu <i>tava</i> nervoso com a falta de luz e o livro..."
    
    "Caramba. Será que ela acha que eu gosto dela? Será que ela acha que é um encontro?"
    
    "Aliás... Eu gosto dela? Digo, ela é bonita e inteligente. E gosta de ler também..."
    
    "Ah, pronto. Agora sim que eu não vou dormir. Por que eu fui pensar nisso agora?"
    
    "<i>- No fim de semana -</i>"
    
    #TODO mudar pro cenário do museu (ou do ponto de encontro)
    
    

    # This ends the game.

    return
