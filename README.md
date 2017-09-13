# png_texture_to_jpeg
Complete via Python PIL library.

Some png format texture may lacks of background. While using it in specify platform with no support with such texture

the picture will show in pure black image. So it's necessary to convert the png texture to other available format.

 


This script use PIL lib converting the png texture with pure white background. The png texture will be cover by a mask

based on itself, so the line in the png file can be obtained. Then I paste the line onto a pure white background 

panel, and output the file to the local filesystem in JPEG format.
