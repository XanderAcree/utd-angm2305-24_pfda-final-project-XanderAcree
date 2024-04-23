import pygame
from pygame.locals import *
import random
import button

class EldenRandom():
    def eldenAttribute(numRange = 255):
        randAttribute = random.randrange(numRange)
        return randAttribute
    
    def set_r():
        r = random.randrange(255)
        return r
    def get_r():
        _r = EldenRandom.set_r()
        return _r
    def set_g():
        g = random.randrange(255)
        return g
    def get_g():
        _g = EldenRandom.set_g()
        return _g
    def set_b():
        b = random.randrange(255)
        return b
    def get_b():
        _b = EldenRandom.set_b()
        return _b
    def eldenColor(returnAllValues = False):
        r = EldenRandom.get_r()
        g = EldenRandom.get_g()
        b = EldenRandom.get_b()

        returnValues = returnAllValues

        randColor = pygame.Color(r,g,b)
        colorReturnList = (r,g,b)
        if returnAllValues == True:
            return colorReturnList
        else:
            return randColor

    def __init__(self, _numRange = 255, isAttribute = True, isColor = False, isBool = False):
        col = EldenRandom.eldenColor(True)

        _randAttribute = EldenRandom.eldenAttribute(_numRange)
        self._randAttribute = _randAttribute

        _randColor = EldenRandom.eldenColor()
        self._randColor = _randColor

        _randCol_r = col[0]
        self._randCol_r = _randCol_r

        _randCol_g = col[1]
        self._randCol_g = _randCol_g

        _randCol_b = col[2]
        self._randCol_b = _randCol_b

        #__init__ Boolean Variables
        self.isAttribute = isAttribute
        self.isColor = isColor
        self.isBool = isBool
    
    # Base
    ## Origin: The class that you'll start off as in Elden Ring when creating a new character.
    def origin():
        randRange = EldenRandom.eldenAttribute(10)
        _origin = {0: 'Vagabond',
                     1: 'Warrior',
                     2: 'Hero',
                     3: 'Bandit',
                     4: 'Astrologer',
                     5: 'Prophet', 
                     6: 'Samurai',
                     7: 'Prisoner',
                     8: 'Confessor',
                     9: 'Wretch'}
        return _origin(randRange)
    ## Body Type -- Whether you want your character to look more masculine or feminine
    def bodyType():
        randRange = EldenRandom.eldenAttribute(2)
        _bodyType = {0: 'Type A',
                    1: 'Type B'}
        return _bodyType(randRange)   
    ## Keepsake -- Optional choice, essentially gives your character an additiona item that they'll start with
    def keepsake():
        randRange = EldenRandom.eldenAttribute(10)
        _keepsake = {0: 'None',
                     1: 'Crimson Amber Medallion', 
                     2: 'Lands Between Rune', 
                     3: 'Golden Seed',
                     4: 'Fanged Imp Ashes',
                     5: 'Cracked Pot',
                     6: 'Stonesword Key',
                     7: 'Bewitching Branch', 
                     8: 'Boiled Prawn',
                     9: 'Shabriri\'s Woe'}
        
        return _keepsake(randRange)
    
    # Detailed Appearance
    def age():
        randRange = EldenRandom.eldenAttribute(3)
        _age = {0: 'Young', 
                1: 'Mature', 
                2: 'Aged'}
        return _age(randRange)
    def voice():
        randRange = EldenRandom.eldenAttribute(6)
        _voice = {0: 'Young Voice 1',
                  1: 'Young Voice 2',
                  2: 'Mature Voice 1',
                  3: 'Mature Voice 2',
                  4: 'Aged Voice 1',
                  5: 'Aged Voice 2'}
        return _voice(randRange)
    def skinColor():
        _skinColor = EldenRandom.eldenColor(False)
        return _skinColor
    
    # Alter Face & Hair

    ## Face Structure
    
    def facial_balance():
        nose_size = EldenRandom.eldenAttribute(255)
        nose_forehead_ratio = EldenRandom.eldenAttribute(255)
        face_protrusion = EldenRandom.eldenAttribute(255)
        vert_face_ratio = EldenRandom.eldenAttribute(255)
        facial_feature_slant = EldenRandom.eldenAttribute(255)
        horiz_face_ratio = EldenRandom.eldenAttribute(255)
        output = [nose_size, nose_forehead_ratio, face_protrusion, vert_face_ratio, facial_feature_slant, horiz_face_ratio]
        return output
    def forehead_glabella():
        forehead_depth = EldenRandom.eldenAttribute(255)
        forehead_protrusion = EldenRandom.eldenAttribute(255)
        nose_bridge_height = EldenRandom.eldenAttribute(255)
        bridge_protrusion_1 = EldenRandom.eldenAttribute(255)
        bridge_protrusion_2 = EldenRandom.eldenAttribute(255)
        nose_bridge_width = EldenRandom.eldenAttribute(255)
        output = [forehead_depth, forehead_protrusion, nose_bridge_height, bridge_protrusion_1, bridge_protrusion_2, nose_bridge_width]
        return output
    def brow_ridge():
        brow_ridge_height = EldenRandom.eldenAttribute(255)
        inner_brow_ridge = EldenRandom.eldenAttribute(255)
        outer_brow_ridge = EldenRandom.eldenAttribute(255)
        output = [brow_ridge_height, inner_brow_ridge, outer_brow_ridge]
        return output
    def eyes():
        eye_pos = EldenRandom.eldenAttribute(255)
        eye_size = EldenRandom.eldenAttribute(255)
        eye_slant = EldenRandom.eldenAttribute(255)
        eye_spacing = EldenRandom.eldenAttribute(255)
        output = [eye_pos, eye_size, eye_slant, eye_spacing]
        return output
    def nose_ridge():
        nose_ridge_depth = EldenRandom.eldenAttribute(255)
        nose_ridge_len = EldenRandom.eldenAttribute(255)
        nose_pos = EldenRandom.eldenAttribute(255)
        nose_tip_height = EldenRandom.eldenAttribute(255)
        nose_protrusion = EldenRandom.eldenAttribute(255)
        nose_height = EldenRandom.eldenAttribute(255)
        nose_slant = EldenRandom.eldenAttribute(255)
        output = [nose_ridge_depth, nose_ridge_len, nose_pos, nose_tip_height, nose_protrusion, nose_height, nose_slant]
        return output
    def nostrils():
        nostril_slant = EldenRandom.eldenAttribute(255)
        nostril_size = EldenRandom.eldenAttribute(255)
        nostril_width = EldenRandom.eldenAttribute(255)
        output = [nostril_slant, nostril_size, nostril_width]
        return output
    def cheeks():
        height = EldenRandom.eldenAttribute(255)
        depth = EldenRandom.eldenAttribute(255)
        width = EldenRandom.eldenAttribute(255)
        protrusion = EldenRandom.eldenAttribute(255)
        _cheeks = EldenRandom.eldenAttribute(255)
        output = [height, depth, width, protrusion, _cheeks]
        return output
    def lips():
        lip_shape = EldenRandom.eldenAttribute(255)
        mouth_expression = EldenRandom.eldenAttribute(255)
        lip_fullness = EldenRandom.eldenAttribute(255)
        lip_size = EldenRandom.eldenAttribute(255)
        lip_protrusion = EldenRandom.eldenAttribute(255)
        lip_thickness = EldenRandom.eldenAttribute(255)
        output = [lip_shape, mouth_expression, lip_fullness, lip_size, lip_protrusion, lip_thickness]
        return output
    def mouth():
        mouth_protrusion = EldenRandom.eldenAttribute(255)
        mouth_slant = EldenRandom.eldenAttribute(255)
        occlusion = EldenRandom.eldenAttribute(255)
        mouth_pos = EldenRandom.eldenAttribute(255)
        mouth_width = EldenRandom.eldenAttribute(255)
        mouth_chin_dist = EldenRandom.eldenAttribute(255)
        output = [mouth_protrusion, mouth_slant, occlusion, mouth_pos, mouth_width, mouth_chin_dist]
        return output
    def chin():
        chin_tip_pos = EldenRandom.eldenAttribute(255)
        chin_len = EldenRandom.eldenAttribute(255)
        chin_protrusion = EldenRandom.eldenAttribute(255)
        chin_depth = EldenRandom.eldenAttribute(255)
        chin_size = EldenRandom.eldenAttribute(255)
        chin_height = EldenRandom.eldenAttribute(255)
        chin_width = EldenRandom.eldenAttribute(255)
        output = [chin_tip_pos, chin_len, chin_protrusion, chin_depth, chin_size, chin_height, chin_width]
        return output
    def jaw():
        jaw_protrusion = EldenRandom.eldenAttribute(255)
        jaw_width = EldenRandom.eldenAttribute(255)
        lower_jaw = EldenRandom.eldenAttribute(255)
        jaw_contour = EldenRandom.eldenAttribute(255)


    ## Hair
    def hair():
        hairstyle = EldenRandom.eldenAttribute(32)
        hair_col = EldenRandom.eldenColor(False)
        luster = EldenRandom.eldenAttribute(255)
        root_darkness = EldenRandom.eldenAttribute(255)
        white_hairs = EldenRandom.eldenAttribute(255)
        return [hairstyle, hair_col, luster, root_darkness, white_hairs]
        
    ## Eyebrows
    def eyebrows(matchBrowCol = True, matchLuster = True, matchRootDark = True, matchWhiteHairs = True):
        brow_matchCase = EldenRandom.hair()
        brow = EldenRandom.eldenAttribute(17) + 1
        if matchBrowCol == True:
            brow_col = brow_matchCase[1]
        elif matchBrowCol == False:
            brow_col = EldenRandom.eldenColor(False)
        
        if matchLuster == True:
            brow_luster = brow_matchCase[2]
        elif matchLuster == False:
            brow_luster = EldenRandom.eldenAttribute(255)
        
        if matchRootDark == True: 
            brow_root_dark = brow_matchCase[3]
        elif matchRootDark == False: 
            brow_root_dark = EldenRandom.eldenAttribute(255)
        
        if matchWhiteHairs == True:
            brow_white_hairs = brow_matchCase[4]
        elif matchWhiteHairs == False:
            brow_white_hairs = EldenRandom.eldenAttribute(255)
        
        output = [brow_col, brow_luster, brow_root_dark, brow_white_hairs]
        return output

    ## Facial Hair
    def facialHair(matchFacialCol = True, matchLuster = True, matchRootDark = True, matchWhiteHairs = True):
        beard = EldenRandom.eldenAttribute(12)
        facial_matchCase = EldenRandom.hair()
        if matchFacialCol == True:
            beard_col = facial_matchCase[1]
        elif matchFacialCol == False:
            beard_col = EldenRandom.eldenColor(False)
            

    ## Eyelashes


    ## Eyes


    ## Skin Features


    ## Cosmetics


    ## Tattoo/Mark/Eyepatch



def main():
    print(EldenRandom.hair())

if __name__ == "__main__":
    main()