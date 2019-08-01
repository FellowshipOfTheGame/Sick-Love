init python:

    # Step 1. Create a MusicRoom instance.
    mr = MusicRoom(fadeout=1.0)

    # Step 2. Add music files.
    mr.add("sounds/song1.wav", always_unlocked=True)
    mr.add("sounds/song2.wav")
    mr.add("sounds/song3.wav")
    mr.add("sounds/song3remix.wav")


# Step 3. Create the music room screen.
screen music_room:

    tag menu
    use game_menu(_("Galeria de Músicas")):
        fixed:
            vbox:
                spacing 10
                null height 50

                text "Escolha a música que quer ouvir!" size 30 color gui.accent_color xalign 0.5
                
                null height 100
                
                # The buttons that play each track.
                textbutton "Main Theme" action mr.Play("sounds/song1.wav") xalign 0.5
                textbutton "Second Part Theme" action mr.Play("sounds/song2.wav") xalign 0.5
                textbutton "Party Theme" action mr.Play("sounds/song3.wav") xalign 0.5
                textbutton "Party Theme Remix" action mr.Play("sounds/song3remix.wav") xalign 0.5

                null height 50
                # Buttons that let us advance tracks.
                hbox:
                    spacing 400
                    textbutton _("Anterior") action mr.Previous() 
                    textbutton _("Próxima") action mr.Next()
                    

    # Start the music playing on entry to the music room.
    on "replace" action mr.Play()

    # Restore the main menu music upon leaving.
    on "replaced" action Play("music", "sounds/song1.wav")