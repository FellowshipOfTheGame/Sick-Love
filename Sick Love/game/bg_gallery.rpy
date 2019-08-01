#BG Gallery

#init-1:
#    image bg sc01 = "01.png"
#    image bg sc02 = "bf27888.jpg"
#    image bg sc03 = "c099f80.jpg"
#    image bg sc04 = "f7d7b0e.jpg"
#    image bg sc05 = "105320c.jpg"
#    image bg sc06 = "cf24501.jpg"
#    image bg sc07 = "538adc8.jpg"
#    image bg sc08 = "1c56479.jpg"
#    image bg sc09 = "ae34943.jpg"
#    image bg sc10 = "20420d5.jpg"
#    image bg sc11 = "9796f4a78d.jpg"
#    image bg sc12 = "2fXx6.jpg"

init python:
    #Galleries settings - start
    #list the CG gallery images here:
    gallery_bg_items = ["bg classroom", "bg room", "bg library", "bg gym", "bg stadium", "bg museum", "bg arcade", "bg movies", "bg rave", "bg subway", "bg campus"]
    #how many rows and columns in the gallery screens?
    gal_rows = 3
    gal_cols = 3
    #thumbnail size in pixels:
    thumbnail_x = 182
    thumbnail_y = 136
    #the setting above will work well with 4:3 screen ratio. Make sure to adjust it, if your are using 16:9 (such as 267x150) or something else.
    #Galleries settings - end
    
    gal_cells = gal_rows * gal_cols    
    g_bg = Gallery()
    for gal_item in gallery_bg_items:
        g_bg.button(gal_item + " butt")
        g_bg.unlock_image(gal_item)
    g_bg.transition = fade
    bg_page=0
    
init +1 python:
    #Here we create the thumbnails. We use a special "locked" image for CGs to prevent spoilers.
    for gal_item in gallery_bg_items:
        renpy.image (gal_item + " butt", im.Scale(ImageReference(gal_item), thumbnail_x, thumbnail_y))
        
screen bg_gallery():
    tag menu
    use game_menu(_("Galeria de Cenários"), scroll="viewport"):
        hbox:
            grid gal_cols gal_rows:
                spacing 35
                $ i = 0
                $ next_bg_page = bg_page + 1
                $ previous_bg_page = bg_page - 1
                if next_bg_page > int(len(gallery_bg_items)/gal_cells):
                    $ next_bg_page = 0
                if previous_bg_page < 0:
                    $ previous_bg_page = int(len(gallery_bg_items)/gal_cells)
                for gal_item in gallery_bg_items:
                    $ i += 1
                    if i <= (bg_page+1)*gal_cells and i>bg_page*gal_cells:
                        add g_bg.make_button(gal_item + " butt", gal_item + " butt", im.Scale("gui/gallocked.png", thumbnail_x, thumbnail_y), xalign=0.5, yalign=0.5, idle_border=None, background=None, bottom_margin=0)
                for j in range(i, (bg_page+1)*gal_cells): #we need this to fully fill the grid
                    null
            frame:
                xpos -150
                ypos 555
                if len(gallery_bg_items)>gal_cells:
                    textbutton _("Próximo") action [SetVariable('bg_page', next_bg_page), ShowMenu("bg_gallery")]
            frame:
                xpos -750
                ypos 555
                if len(gallery_bg_items)>gal_cells:
                    textbutton _("Anterior") action [SetVariable('bg_page', previous_bg_page), ShowMenu("bg_gallery")]