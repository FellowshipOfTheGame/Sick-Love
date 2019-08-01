#rafaela Gallery


init python:
    #Galleries settings - start
    #list the CG gallery images here:
    gallery_rafaela_items = ["rafaela standing", "rafaela happy", "rafaela sad", "rafaela evasive", "rafaela upset", "rafaela shy", 
        "rafaela standing2", "rafaela happy2", "rafaela sad2", "rafaela evasive2", "rafaela upset2", "rafaela shy2", "rafaela standing3", 
        "rafaela happy3", "rafaela sad3", "rafaela evasive3", "rafaela upset3", "rafaela shy3"]
    #how many rows and columns in the gallery screens?
    gal_rows = 3
    gal_cols = 3
    #thumbnail size in pixels:
    thumbnail_x = 182
    thumbnail_y = 136
    #the setting above will work well with 4:3 screen ratio. Make sure to adjust it, if your are using 16:9 (such as 267x150) or something else.
    #Galleries settings - end
    
    gal_cells = gal_rows * gal_cols    
    g_rafaela = Gallery()
    for gal_item in gallery_rafaela_items:
        g_rafaela.button(gal_item + " butt")
        g_rafaela.unlock_image(gal_item)
    g_rafaela.transition = fade
    rafaela_page=0
    
init +1 python:
    #Here we create the thumbnails. We use a special "locked" image for CGs to prevent spoilers.
    for gal_item in gallery_rafaela_items:
        renpy.image (gal_item + " butt", im.Scale(ImageReference(gal_item), thumbnail_x, thumbnail_y))
        
screen rafaela_gallery():
    tag menu
    use game_menu(_("Galeria da rafaela"), scroll="viewport"):
        hbox:
            grid gal_cols gal_rows:
                spacing 35
                $ i = 0
                $ next_rafaela_page = rafaela_page + 1
                $ previous_rafaela_page = rafaela_page - 1
                if next_rafaela_page > int((len(gallery_rafaela_items)-1)/gal_cells):
                    $ next_rafaela_page = 0
                if previous_rafaela_page < 0:
                    $ previous_rafaela_page = int((len(gallery_rafaela_items)-1)/gal_cells)
                for gal_item in gallery_rafaela_items:
                    $ i += 1
                    if i <= (rafaela_page+1)*gal_cells and i>rafaela_page*gal_cells:
                        add g_rafaela.make_button(gal_item + " butt", gal_item + " butt", im.Scale("gui/gallocked.png", thumbnail_x, thumbnail_y), xalign=0.5, yalign=0.5, idle_border=None, background=None, bottom_margin=0)
                for j in range(i, (rafaela_page+1)*gal_cells): #we need this to fully fill the grid
                    null
            frame:
                xpos -150
                ypos 555
                if len(gallery_rafaela_items)>gal_cells:
                    textbutton _("Próximo") action [SetVariable('rafaela_page', next_rafaela_page), ShowMenu("rafaela_gallery")]
            frame:
                xpos -750
                ypos 555
                if len(gallery_rafaela_items)>gal_cells:
                    textbutton _("Anterior") action [SetVariable('rafaela_page', previous_rafaela_page), ShowMenu("rafaela_gallery")]