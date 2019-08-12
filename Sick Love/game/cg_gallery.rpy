#CG Gallery
screen cg_gallery():
    
    tag menu
    use game_menu(_("Galeria de Personagens")):
        fixed:
            
            
            hbox:
                yalign 0.6
                xalign 0.5
                
                button:
                    action ShowMenu("sofia_gallery")

                    has vbox

                    add im.Scale(im.Crop(ImageReference("sofia standing"), (430, 100, 400, 600)), 250, 300) xalign 0.5

                    text "Sofia" xalign 0.5
                        
                button:
                    action ShowMenu("mariana_gallery")

                    has vbox

                    add im.Scale(im.Crop(ImageReference("mariana standing"), (20, 10, 400, 500)), 250, 300) xalign 0.5

                    text "Mariana" xalign 0.5
                        
                button:
                    action ShowMenu("rafaela_gallery")

                    has vbox

                    add im.Scale(im.Crop(ImageReference("rafaela standing"), (430, 100, 400, 600)), 250, 300) xalign 0.5

                    text "Rafaela" xalign 0.5