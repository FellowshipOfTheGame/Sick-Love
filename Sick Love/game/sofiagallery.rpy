#Sofia Gallery


init python:
    #Galleries settings - start
    #list the CG gallery images here:
    gallery_sofia_items = ["sofia standing", "sofia happy", "sofia sad", "sofia angry", "sofia crying", "sofia evasive", 
        "sofia upset", "sofia shy", "sofia standing2", "sofia happy2", "sofia sad2", "sofia angry2", "sofia crying2", 
        "sofia evasive2", "sofia upset2", "sofia shy2", "sofia standing3", "sofia happy3", "sofia sad3", "sofia angry3", 
        "sofia crying3", "sofia evasive3", "sofia upset3", "sofia shy3"]
    #how many rows and columns in the gallery screens?
    gal_rows = 3
    gal_cols = 3
    #thumbnail size in pixels:
    thumbnail_x = 182
    thumbnail_y = 136
    #the setting above will work well with 4:3 screen ratio. Make sure to adjust it, if your are using 16:9 (such as 267x150) or something else.
    #Galleries settings - end
    
    gal_cells = gal_rows * gal_cols    
    g_sofia = Gallery()
    for gal_item in gallery_sofia_items:
        g_sofia.button(gal_item + " butt")
        g_sofia.unlock_image(gal_item)
    g_sofia.transition = fade
    sofia_page=0
    
init +1 python:
    #Here we create the thumbnails. We use a special "locked" image for CGs to prevent spoilers.
    for gal_item in gallery_sofia_items:
        renpy.image (gal_item + " butt", im.Scale(ImageReference(gal_item), thumbnail_x, thumbnail_y))
        
screen sofia_gallery():
    tag menu
    use game_menu(_("Galeria da Sofia"), scroll="viewport"):
        vbox:
            grid gal_cols gal_rows:
                spacing 35
                xpos 80
                $ i = 0
                $ next_sofia_page = sofia_page + 1
                $ previous_sofia_page = sofia_page - 1
                if next_sofia_page > int(len(gallery_sofia_items)/gal_cells):
                    $ next_sofia_page = 0
                if previous_sofia_page < 0:
                    $ previous_sofia_page = int(len(gallery_sofia_items)/gal_cells)
                for gal_item in gallery_sofia_items:
                    $ i += 1
                    if i <= (sofia_page+1)*gal_cells and i>sofia_page*gal_cells:
                        add g_sofia.make_button(gal_item + " butt", gal_item + " butt", im.Scale("gui/gallocked.png", thumbnail_x, thumbnail_y), xalign=0.5, yalign=0.5, idle_border=None, background=None, bottom_margin=0)
                for j in range(i, (sofia_page+1)*gal_cells): #we need this to fully fill the grid
                    null
            
            null height 50
            
            hbox:
                spacing 200
                if len(gallery_sofia_items)>gal_cells:
                    textbutton _("Anterior") action [SetVariable('sofia_page', previous_sofia_page), ShowMenu("sofia_gallery")]
                textbutton _("Voltar") action ShowMenu("cg_gallery")
                if len(gallery_sofia_items)>gal_cells:
                    textbutton _("Próxima") action [SetVariable('sofia_page', next_sofia_page), ShowMenu("sofia_gallery")]
            