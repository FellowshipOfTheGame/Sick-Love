# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.


# The game starts here.

label rafaelathirddate:

    $ nDatesRafaela+=1

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene black with Fade(0.7,0.2,0.7)

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    # These display lines of dialogue.
    
    scene bg room with Fade(0.7,0.2,0.7)
    
    "Caramba, desde aquele dia no estádio eu fico pensando o que eu quero da vida... Eu até já vi a Rafa algumas vezes pela universidade depois disso, mas a gente agiu normalmente e não tocou no assunto."
    
    "Eu achei que ia ficar mais {i}de boa{/i} sobre isso e deixar rolar, sem pensar muito. Mas eu não consigo tirar isso da minha cabeça."
    
    "Pensei bastante no tempo que a gente passou junto. E naquele beijo. E acho que realmente, no final das contas, eu gosto dela."
    
    p "AAAAAAAH Por que a vida é tão complicada?"
    
    "Ok. Hora de tomar uma decisão. Vou tentar ver se ela quer sair essa semana, e tento conversar sobre isso com ela pessoalmente. Falar o que sinto e ver se ela aceita algo mais sério comigo."
    
    show rafaela cell at celltransform
    
    p "Hey, Rafa, tudo bem? Então, eu queria saber se você não quer fazer alguma coisa esse final de semana. A gente acabou não tendo muito tempo de conversar desde o jogo..."
    
    r "Oi, gato! {i}Bora{/i}! Não sei se tu curte, mas vai ter uma rave {i}topíssima{/i} esse final de semana. Com um DJ dos bons. O que acha?"
    
    p "Nunca fui numa rave, mas seu último rolê \"aleatório\" comigo foi extremamente divertido pra mim. Então acho que vou arriscar de novo e confiar no seu bom gosto."
    
    r "Fico feliz pela confiança. Vou te passar os detalhes então."
    
    "-{i}Alguns detalhes e bate-papo depois...{/i}-"
    
    r "Te vejo no {i}rolê{/i}, então. {i}Bjs{/i}."
    
    p "{i}Bjs{/i}."
    
    hide rafaela cell
    
    "Aparentemente eu vou ter que arrumar uma brecha pra conversar sobre isso depois de \"fritar\" na rave dançando."
    
    p "Bem... eu dou um jeito. Não quero perder a oportunidade e ficar arrastando isso também."
    
    scene black with Fade(0.7,0.2,0.7)

    "-{i}Na rave...{/i}-"
    
    scene bg rave
    with Fade(0.7,0.2,0.7)
    
    p "Hey, Rafa, a música {i}tá{/i} muito boa, né?"
    
    show rafaela happy at noghost
    
    r "QUÊ?"
    
    p "A MÚSICA {i}TÁ{/i} MUITO BOA!"
    
    r "MÚSICA? VOCÊ {i}TÁ{/i} GOSTANDO?"
    
    "Ok... não vai dar para ter nenhuma conversa agora. Eu mal consigo escutar uma palavra... Bem, vou aproveitar a rave mesmo e na saída a gente tenta conversar..."
    
    "Respondi para ela com sinal de positivo e continuamos a dançar."
    
    "É uma experiência singular a de uma rave. As luzes e a batida da música parecem entrar na sua alma e tomar conta dos seus movimentos. E assim foi-se a noite."
    
    hide rafaela
    
    scene black with Fade(0.7,0.2,0.7)

    "-{i}Ao fim da rave...{/i}-"
    
    scene bg rave
    with Fade(0.7,0.2,0.7)
    
    "Ok, foi bem proveitoso no final das contas. Dançamos muito. Nos beijamos muito..."
     
    "Não consigo parar de ouvir um zunido no meu ouvido e tenho a impressão de que vou viver o resto da minha vida me movimentando em torno daquela batida..."
    
    "Mas eu ainda estava com meu objetivo original em mente."
    
    show rafaela happy at noghost
    
    r "E aí, curtiu bastante? Aliás, um dia esse zumbido vai passar, antes que você fique preocupado."
    
    p "Obrigado por avisar. Eu realmente estava me questionando isso. Acho que você lê meus pensamentos... Talvez seja algum efeito colateral das luzes e do som que fez você desenvolver novos poderes..."
    
    r "*risos* mas é um piadista mesmo."
    
    p "Mas eu curti sim. A rave foi muito legal e também foi muito bom poder curtir ela com você. Sempre que eu estou com você, não importa o quão alternativo pra mim seja o {i}rolê{/i}, ele sempre é inesquecível."
    
    show rafaela shy at noghost
    
    r "Ai, que fofo. Ele consegue sair da rave intacto e ainda falar essas coisas bonitinhas..." 
    
    r "Sabe, eu também gosto bastante da sua companhia. Fico muito feliz que você venha nesses {i}rolês{/i} comigo. Especialmente porque sei que não é algo que você está acostumado."
    
    "Ok. Essa é a hora. Eu preciso tomar coragem e falar. Não sei se é o energético ou a ansiedade, mas sinto meu coração disparado. Seguro a mão dela e olho nos olhos dela."
    
    p "Que bom que o sentimento é mútuo. Eu realmente gosto muito de você, Rafa. E nesses últimos dias eu pensei muito sobre a gente estar ficando e sobre a nossa conversa de não saber direito os sentimentos..."
    
    p "E depois de pensar muito sobre isso, eu acho que pelo menos a minha resposta eu tenho. Eu sei que não estamos juntos à muito tempo, e que talvez estejamos de novo sob efeito da adrenalina do momento... E talvez de energéticos e um pouco de álcool..."
    
    p "Mas eu posso dizer que eu realmente gosto de você. Você é uma pessoa que me fascinou tanto pela sua beleza quanto sua personalidade sempre divertida e descontraída." 
    
    p "E eu cheguei à conclusão que ficaria muito feliz de ser sua companhia fixa para qualquer rolê alternativo que você quiser ir... Pera, deixa eu recolocar isso de um jeito mais claro:"
    
    p "Rafa, eu vou entender se você achar que ainda é muito cedo pra aceitar, mas eu queria saber se você também gostaria de levar nosso relacionamento para um nível mais sério e ser minha namorada."
    
    "Ok, eu consegui falar. Foi difícil, falei mais rápido do que queria (com certeza os energéticos só pioraram meu nervosismo). Mas finalmente eu falei. Meu coração está explodindo. Nível máximo de ansiedade enquanto aguardo uma resposta..."
    
    r "Você é realmente um fofo! Eu também andei pensando sobre a gente esses tempos. Eu curto muito sua {i}vibe{/i}, adoro quando você vem nos {i}rolês{\i} que eu chamo." 
    
    r "E eu percebi também que recentemente, toda vez que eu pensava em sair para algum lugar, na hora vinha o pensamento de: \"caramba, eu preciso chamar o [povname]\". Tanto que eu fiquei muito feliz quando você me chamou para sair essa semana."
    
    r "Então... Sim, eu percebi que eu também estou gostando de você e eu ficaria feliz de ter você comigo em todos os {i}rolês{/i}." 
       
    show rafaela happy at noghost   
    
    r "Vou te dar a honra de ser meu namorado."
    
    "E então, nos beijamos. Não que nós não tenhamos feito isso várias vezes antes. Mas dessa vez foi diferente. Foi um beijo com gosto de romance. E a minha vida romântica estava apenas começando."
    
    hide rafaela
    
    scene black with Fade(0.7,0.2,0.7)
    
    "Porém, nem tudo em um romance envolve felicidade, {i}rolês{/i} e amor, como eu viria a descobrir depois... Mas isso é algo para um futuro próximo."
    
    scene bg room
    with Fade(0.7,0.2,0.7)
    
    "Por agora, eu só preciso de silêncio e uma noite de sono. Agora que a adrenalina passou e estou em casa, eu não consigo não prestar atenção nesse zumbido."
    
    # This ends the game.
    
    return