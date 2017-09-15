"""
This script finishes the function that transfer the png texture to jpeg format image.
I used PIL library to complete this task.
"""
from PIL import Image
import os

class ACFUN_emoji_handler():

    def __init__(self, filepath):
        """
        Load the file list from specify file path.
        """
        self.path = filepath
        self.file_list = os.listdir( self.path )
        self.__convert__()

    def __convert__(self):
        """
        I used a mask which initiate with the png texture, the mask will be
        used as a filter which cover the origin png texture file so the
        origin png file's line will not be cover when you set the background
        as transparent.
        Save the file in current working directory.
        :return: None
        """
        for file in self.file_list:
            try:
                img = Image.open( self.path + file ).convert( 'RGBA' )
                width, height = img.size
                panel = Image.new( 'RGBA', img.size, ( 255, 255, 255, 255 ) )
                panel.paste( img, ( 0, 0 ), img )
                panel.save( file )
            except: print( file )

if __name__ == '__main__':
    instance = ACFUN_emoji_handler( yourfilepath )
