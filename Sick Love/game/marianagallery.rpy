#mariana Gallery


init python:
    #Galleries settings - start
    #list the CG gallery images here:
    gallery_mariana_items = ["mariana standing", "mariana happy", "mariana sad", "mariana mad", "mariana evasive", 
        "mariana excited", "mariana blushed", "mariana standing2", "mariana happy2", "mariana sad2", "mariana mad2", "mariana evasive2", 
        "mariana blushed2", "mariana standing3", "mariana happy3", "mariana evasive3", "mariana excited3", "mariana blushed3"]
    #how many rows and columns in the gallery screens?
    gal_rows = 3
    gal_cols = 3
    #thumbnail size in pixels:
    thumbnail_x = 182
    thumbnail_y = 136
    #the setting above will work well with 4:3 screen ratio. Make sure to adjust it, if your are using 16:9 (such as 267x150) or something else.
    #Galleries settings - end
    
    gal_cells = gal_rows * gal_cols    
    g_mariana = Gallery()
    for gal_item in gallery_mariana_items:
        g_mariana.button(gal_item + " butt")
        g_mariana.unlock_image(gal_item)
    g_mariana.transition = fade
    mariana_page=0
    
init +1 python:
    #Here we create the thumbnails. We use a special "locked" image for CGs to prevent spoilers.
    for gal_item in gallery_mariana_items:
        renpy.image (gal_item + " butt", im.Scale(ImageReference(gal_item), thumbnail_x, thumbnail_y))
        
screen mariana_gallery():
    tag menu
    use game_menu(_("Galeria da mariana"), scroll="viewport"):
        vbox:
            grid gal_cols gal_rows:
                xpos 80
                spacing 35
                $ i = 0
                $ next_mariana_page = mariana_page + 1
                $ previous_mariana_page = mariana_page - 1
                if next_mariana_page > int(len(gallery_mariana_items)/gal_cells):
                    $ next_mariana_page = 0
                if previous_mariana_page < 0:
                    $ previous_mariana_page = int(len(gallery_mariana_items)/gal_cells)
                for gal_item in gallery_mariana_items:
                    $ i += 1
                    if i <= (mariana_page+1)*gal_cells and i>mariana_page*gal_cells:
                        add g_mariana.make_button(gal_item + " butt", gal_item + " butt", im.Scale("gui/gallocked.png", thumbnail_x, thumbnail_y), xalign=0.5, yalign=0.5, idle_border=None, background=None, bottom_margin=0)
                for j in range(i, (mariana_page+1)*gal_cells): #we need this to fully fill the grid
                    null
            null height 50
            
            hbox:
                spacing 200
                if len(gallery_mariana_items)>gal_cells:
                    textbutton _("Anterior") action [SetVariable('mariana_page', previous_mariana_page), ShowMenu("mariana_gallery")]
                textbutton _("Voltar") action ShowMenu("cg_gallery")
                if len(gallery_mariana_items)>gal_cells:
                    textbutton _("Próxima") action [SetVariable('mariana_page', next_mariana_page), ShowMenu("mariana_gallery")]
                
                
                
                
                