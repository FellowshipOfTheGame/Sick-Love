
define t = Character("Professor", color = "#36F3AE", what_color = "#2BD798",what_prefix='"', what_suffix='"')

label intro:

scene bg room

"Ufa, acho que consegui chegar a tempo, a lousa ainda está vazia."

t "Então estejam preparados, a faculdade pode compor os melhores ou os piores anos de suas vidas, tudo depende de vocês..."

"Nossa, isso foi desnecessariamente dramático."

"Bem, ao menos ninguém parece estar levando ele muito a sério nesse quesito."

t "Ver todas essas carinhas novas fazem-me lembrar de quando eu entrei na universidade"

t "Tudo era tão diferente..."

t "Eu me lembro que..."

"E lá vai ele..."

"Mesmo querendo pagar de sério esse professor deve ser bem tranquilo, não acho que devo me preocupar muito."

"Ainda não boto fé que deu pra chegar na sala sem perder muita coisa."

"Não acredito que caí no papo do meu pai de chegar no dia da primeira aula."

"Por sorte dentro do campus dá pra se guiar só pelas placas, se não fossem por elas até agora estaria rodando sem sair do lugar."

"Consegui ainda passar no dormitório pra deixar minhas malas."

"O quarto é bem espaçoso, mesmo eu tendo que dividir não acho que vá ser um problema."

t "Acho que até hoje os professores devem se perguntar quem fez aquilo, se ainda estiverem vivos HAHAHAHAHA"

"{i}*Silêncio...*{/i}"

"Incrível como a aula nem começou de verdade e eu já quero ir embora."

"Nossa... não conheço ninguém aqui..."

"Achei que mais pessoas do meu colégio tivessem prestado pra cá, mas aparentemente eu estava errado."

t"""
Nunca vou esquecer a cara que ele fez HAHAHA.

Desculpem as histórias e devaneios, eu sempre fui o piadista do grupo.

Mas bem, já que hoje foi apenas uma aula introdutória, vamos parar aqui por hoje.

Vejo que alguns de você parecem estar um pouco deslocados, mas não se esqueçam:

Alguns amigos feitos na faculdade ficam pra vida toda, então não fiquem sozinhos!

Ouvi dizer que nosso time de handball está com tudo, então quem tiver interessado dê uma passadinha no ginásio.

Claro que caso você goste de outro esporte você também deve ir pro ginásio, lá os outros alunos poderão melhor te guiar.

Por último, só queria lembrar que a biblioteca da nossa universidade é invejável.

Se forem lá aposto que não se arrependerão.
"""
scene bg room
with Fade(0.7,0.2,0.7)

"""
Bem, eu acho que posso chamar isso de uma primeira aula

Vários alunos já sairam, mas tem um grupo que acabou ficando pra bater papo.
"""

menu:
    "O que devo fazer agora?"

    "Ir para a biblioteca":

        jump sofiafirstdate

    "Ficar e conversar com o grupo na sala":

        "testeb"

    "Ir ao ginásio":

        "teste"
