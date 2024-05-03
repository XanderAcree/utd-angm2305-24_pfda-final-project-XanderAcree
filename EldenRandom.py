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

    #### EldenRandom.all index: 0 ([0][0][0])
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
        return _origin.get(randRange)
    ## Body Type -- Whether you want your character to look more masculine or feminine

    #### EldenRandom.all index: 1 ([1][0][0])
    def bodyType():
        randRange = EldenRandom.eldenAttribute(2)
        _bodyType = {0: 'Type A',
                    1: 'Type B'}
        return _bodyType.get(randRange)   
    ## Keepsake -- Optional choice, essentially gives your character an additiona item that they'll start with

    #### EldenRandom.all index: 2 ([2][0][0])
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
        
        return _keepsake.get(randRange)
    
    # Detailed Appearance

    #### EldenRandom.all index: 3 ([3][0][0])
    def age():
        randRange = EldenRandom.eldenAttribute(3)
        _age = {0: 'Young', 
                1: 'Mature', 
                2: 'Aged'}
        return _age.get(randRange)
    
    #### EldenRandom.all index: 4 ([4][0][0])
    def voice():
        randRange = EldenRandom.eldenAttribute(6)
        _voice = {0: 'Young Voice 1',
                  1: 'Young Voice 2',
                  2: 'Mature Voice 1',
                  3: 'Mature Voice 2',
                  4: 'Aged Voice 1',
                  5: 'Aged Voice 2'}
        return _voice.get(randRange)
    
    #### EldenRandom.all index: 5 [5][0][0]
    def skinColor():
        _skinColor = EldenRandom.eldenColor(False)
        return _skinColor
    
    # Alter Face & Hair

    ## Adjust Face Template

    #### EldenRandom.all index: 6 [6][0][0]
    def face_template():
        bone_structure = random.randrange(6)
        form_emphasis = EldenRandom.eldenAttribute()
        apparent_age = EldenRandom.eldenAttribute()
        facial_aesthetic = EldenRandom.eldenAttribute()
        output = [bone_structure, form_emphasis, apparent_age, facial_aesthetic] #[6][0-3][0]
        return output

    ## Face Structure

    #### EldenRandom.all index: 7 [x][o][o]
    def facial_structure():
        # Facial Balance
        nose_size = EldenRandom.eldenAttribute(255)
        nose_forehead_ratio = EldenRandom.eldenAttribute(255)
        face_protrusion = EldenRandom.eldenAttribute(255)
        vert_face_ratio = EldenRandom.eldenAttribute(255)
        facial_feature_slant = EldenRandom.eldenAttribute(255)
        horiz_face_ratio = EldenRandom.eldenAttribute(255)
        facial_balance = [nose_size, nose_forehead_ratio, face_protrusion, 
                          vert_face_ratio, facial_feature_slant, horiz_face_ratio] #[7][0][0-5]
        
        #Forehead/Glabella
        forehead_depth = EldenRandom.eldenAttribute(255)
        forehead_protrusion = EldenRandom.eldenAttribute(255)
        nose_bridge_height = EldenRandom.eldenAttribute(255)
        bridge_protrusion_1 = EldenRandom.eldenAttribute(255)
        bridge_protrusion_2 = EldenRandom.eldenAttribute(255)
        nose_bridge_width = EldenRandom.eldenAttribute(255)
        forehead_glabella = [forehead_depth, forehead_protrusion, nose_bridge_height, 
                             bridge_protrusion_1, bridge_protrusion_2, nose_bridge_width] #[7][1][0-5]

        #Brow Ridge
        brow_ridge_height = EldenRandom.eldenAttribute(255)
        inner_brow_ridge = EldenRandom.eldenAttribute(255)
        outer_brow_ridge = EldenRandom.eldenAttribute(255)
        brow_ridge = [brow_ridge_height, inner_brow_ridge, outer_brow_ridge] #[7][2][0-2]

        #Eyes
        eye_pos = EldenRandom.eldenAttribute(255)
        eye_size = EldenRandom.eldenAttribute(255)
        eye_slant = EldenRandom.eldenAttribute(255)
        eye_spacing = EldenRandom.eldenAttribute(255)
        eyes = [eye_pos, eye_size, eye_slant, eye_spacing] #[7][3][0-3]

        #Nose Ridge
        nose_ridge_depth = EldenRandom.eldenAttribute(255)
        nose_ridge_len = EldenRandom.eldenAttribute(255)
        nose_pos = EldenRandom.eldenAttribute(255)
        nose_tip_height = EldenRandom.eldenAttribute(255)
        nose_protrusion = EldenRandom.eldenAttribute(255)
        nose_height = EldenRandom.eldenAttribute(255)
        nose_slant = EldenRandom.eldenAttribute(255)
        nose_ridge = [nose_ridge_depth, nose_ridge_len, nose_pos, 
                      nose_tip_height, nose_protrusion, nose_height, nose_slant] #[7][4][0-6]

        #Nostrils
        nostril_slant = EldenRandom.eldenAttribute(255)
        nostril_size = EldenRandom.eldenAttribute(255)
        nostril_width = EldenRandom.eldenAttribute(255)
        nostrils = [nostril_slant, nostril_size, nostril_width] #[7][5][0-2]

        #Cheeks
        cheek_height = EldenRandom.eldenAttribute(255)
        cheek_depth = EldenRandom.eldenAttribute(255)
        cheek_width = EldenRandom.eldenAttribute(255)
        cheek_protrusion = EldenRandom.eldenAttribute(255)
        _cheeks = EldenRandom.eldenAttribute(255)
        cheeks = [cheek_height, cheek_depth, cheek_width, cheek_protrusion, _cheeks] #[7][6][0-5]

        #Lips
        lip_shape = EldenRandom.eldenAttribute(255)
        mouth_expression = EldenRandom.eldenAttribute(255)
        lip_fullness = EldenRandom.eldenAttribute(255)
        lip_size = EldenRandom.eldenAttribute(255)
        lip_protrusion = EldenRandom.eldenAttribute(255)
        lip_thickness = EldenRandom.eldenAttribute(255)
        lips = [lip_shape, mouth_expression, lip_fullness, lip_size, lip_protrusion, lip_thickness] #[7][7][0-5]

        #Mouth
        mouth_protrusion = EldenRandom.eldenAttribute(255)
        mouth_slant = EldenRandom.eldenAttribute(255)
        occlusion = EldenRandom.eldenAttribute(255)
        mouth_pos = EldenRandom.eldenAttribute(255)
        mouth_width = EldenRandom.eldenAttribute(255)
        mouth_chin_dist = EldenRandom.eldenAttribute(255)
        mouth = [mouth_protrusion, mouth_slant, occlusion, mouth_pos, mouth_width, mouth_chin_dist] #[7][8][0-5]

        #Chin
        chin_tip_pos = EldenRandom.eldenAttribute(255)
        chin_len = EldenRandom.eldenAttribute(255)
        chin_protrusion = EldenRandom.eldenAttribute(255)
        chin_depth = EldenRandom.eldenAttribute(255)
        chin_size = EldenRandom.eldenAttribute(255)
        chin_height = EldenRandom.eldenAttribute(255)
        chin_width = EldenRandom.eldenAttribute(255)
        chin = [chin_tip_pos, chin_len, chin_protrusion, chin_depth, chin_size, chin_height, chin_width] #[7][9][0-6]

        #Jaw
        jaw_protrusion = EldenRandom.eldenAttribute(255)
        jaw_width = EldenRandom.eldenAttribute(255)
        lower_jaw = EldenRandom.eldenAttribute(255)
        jaw_contour = EldenRandom.eldenAttribute(255)
        jaw = [jaw_protrusion, jaw_width, lower_jaw, jaw_contour] #[7][10][0-3]

        output = [facial_balance, forehead_glabella, brow_ridge, 
                  eyes, nose_ridge, nostrils, cheeks, lips, mouth, 
                  chin, jaw] #[7][0-10]
        return output

    ## Hair

    #### EldenRandom.all index: 8 [8][0][0]
    def hair():
        hairstyle = EldenRandom.eldenAttribute(32)
        hair_col = EldenRandom.eldenColor(False)
        luster = EldenRandom.eldenAttribute(255)
        root_darkness = EldenRandom.eldenAttribute(255)
        white_hairs = EldenRandom.eldenAttribute(255)
        return [hairstyle, hair_col, luster, root_darkness, white_hairs] #[8][0-4]
    ## Eyebrows

    #### EldenRandom.all index: 9 [9][0][0]
    def eyebrows():
        matchCase = [0,0,0,0]
        brow_matchCase = EldenRandom.hair()
        brow = EldenRandom.eldenAttribute(17) + 1

        for i in range(4):
            randomBool = EldenRandom.eldenAttribute(2)
            matchCase[i] = randomBool
        if matchCase[0] == 1:
            brow_col = brow_matchCase[1]
        elif matchCase[0] == 0:
            brow_col = EldenRandom.eldenColor(False)
        
        if matchCase[1] == 1:
            brow_luster = brow_matchCase[2]
        elif matchCase[1] == 0:
            brow_luster = EldenRandom.eldenAttribute(255)
        
        if matchCase[2] == 1: 
            brow_root_dark = brow_matchCase[3]
        elif matchCase[2] == 0: 
            brow_root_dark = EldenRandom.eldenAttribute(255)
        
        if matchCase[3] == 1:
            brow_white_hairs = brow_matchCase[4]
        elif matchCase[3] == 0:
            brow_white_hairs = EldenRandom.eldenAttribute(255)
        
        output = [brow, brow_col, brow_luster, brow_root_dark, brow_white_hairs] #[9][0-4]
        return output
    ## Facial Hair

    #### EldenRandom.all index: 10 [10][0][0]
    def facialHair():
        beard = EldenRandom.eldenAttribute(12)
        match_case = [0,0,0,0]
        for i in range(4):
            randBool = EldenRandom.eldenAttribute(2)
            match_case[i] = randBool
        facial_matchCase = EldenRandom.hair()
        if match_case[0] == True:
            beard_col = facial_matchCase[1]
        elif match_case[0] == False:
            beard_col = EldenRandom.eldenColor(False)
        
        if match_case[1] == True:
            beard_luster = facial_matchCase[2]
        elif match_case[1] == False:
            beard_luster = EldenRandom.eldenAttribute(255)
        
        if match_case[2] == True:
            beardRootDark = facial_matchCase[3]
        elif match_case[2] == False:
            beardRootDark = EldenRandom.eldenAttribute(255)
        
        if match_case[3] == True:
            beardWhiteHairs = facial_matchCase[4]
        elif match_case[3] == False:
            beardWhiteHairs = EldenRandom.eldenAttribute(255)

        beard_stubble = EldenRandom.eldenAttribute(255)
        
        output = [beard_col, beard_luster, beardRootDark, beardWhiteHairs, beard_stubble] #[10][0-4]
        return output
    ## Eyelashes

    #### EldenRandom.all index: 11 [11][0][0]
    def eyelashes():
        matchHair = random.randrange(2)
        _eyelashes = EldenRandom.eldenAttribute(4)
        lash_matchCase = EldenRandom.hair()
        if matchHair == 1: 
            eyelash_col = lash_matchCase[1]
        elif matchHair == 0:
            eyelash_col = EldenRandom.eldenColor()
        
        output = [_eyelashes, eyelash_col] #[11][0-1]
        return output
    ## Eyes

    #### EldenRandom.all index: 12 [12][0][0]
    def eyes_col():
        matchEye = [True, True, True, True, True, True]
        i = 0
        for i in range(6):
            match_eye = EldenRandom.eldenAttribute(2)
            if match_eye == 0:
                matchEye[i] = False
            else:
                matchEye[i] = True

        iris_size_r = EldenRandom.eldenAttribute(255)
        iris_col_r = EldenRandom.eldenColor()
        eye_clouding_r = EldenRandom.eldenAttribute(255)
        clouding_col_r = EldenRandom.eldenColor()
        eye_white_r = EldenRandom.eldenColor()
        eye_pos_r = EldenRandom.eldenAttribute(255)

        if matchEye[0] == True:
            iris_size_l = iris_size_r
        elif matchEye[0] == False:
            iris_size_l = EldenRandom.eldenAttribute(255)
        
        if matchEye[1] == True:
            iris_col_l = iris_col_r
        elif matchEye[1] == False:
            iris_col_l = EldenRandom.eldenColor()
        
        if matchEye[2] == True:
            eye_clouding_l = eye_clouding_r
        elif matchEye[2] == False:
            eye_clouding_l = EldenRandom.eldenAttribute(255)
        
        if matchEye[3] == True:
            clouding_col_l = clouding_col_r
        elif matchEye[3] == False:
            clouding_col_l = EldenRandom.eldenColor()
        
        if matchEye[4] == True:
            eye_white_l = eye_white_r
        elif matchEye[4] == False:
            eye_white_l = EldenRandom.eldenColor()
        
        if matchEye[5] == True:
            eye_pos_l = eye_pos_r
        elif matchEye[5] == False:
            eye_pos_l = EldenRandom.eldenAttribute(255)
        
        output = [iris_size_r, iris_col_r, eye_clouding_r, clouding_col_r, eye_white_r, eye_pos_r,
                  iris_size_l, iris_col_l, eye_clouding_l, clouding_col_l, eye_white_l, eye_pos_l] #[12][0-11]
        return output

    ## Skin Features
    #### EldenRandom.all index: 13 [13][0][0]
    def skin_features():
        pores = EldenRandom.eldenAttribute(255)
        skin_luster = EldenRandom.eldenAttribute(255)
        dark_circles = EldenRandom.eldenAttribute(255)
        dark_circles_col = EldenRandom.eldenColor()
        output = [pores, skin_luster, dark_circles, dark_circles_col] #[13][0-3]
        return output
    ## Cosmetics
    #### EldenRandom.all index: 14 [14][0][0]
    def cosmetics():
        eyeliner, eyeliner_col = EldenRandom.eldenAttribute(255), EldenRandom.eldenColor()
        eyeshadow_upper, eyeshadow_upper_col = EldenRandom.eldenAttribute(255), EldenRandom.eldenColor()
        eyeshadow_lower, eyeshadow_lower_col = EldenRandom.eldenAttribute(255), EldenRandom.eldenColor()
        cheeks, cheeks_col = EldenRandom.eldenAttribute(255), EldenRandom.eldenColor()
        lipstick, lipstick_col = EldenRandom.eldenAttribute(255), EldenRandom.eldenColor()

        output = [eyeliner, eyeliner_col, 
                  eyeshadow_upper, eyeshadow_upper_col, 
                  eyeshadow_lower, eyeshadow_lower_col, 
                  cheeks, cheeks_col, 
                  lipstick, lipstick_col] #[14][0-9]
        return output
    ## Tattoo/Mark/Eyepatch
    #### EldenRandom.all index: 15 [15][0][0]
    def face_misc():
        tattoo_mark = EldenRandom.eldenAttribute(38)
        tattoo_mark_col = EldenRandom.eldenColor()

        #Variables for tattoo_mark_tweak
        pos_vert = EldenRandom.eldenAttribute(255)
        pos_horiz = EldenRandom.eldenAttribute(255)
        angle = EldenRandom.eldenAttribute(255)
        expansion = EldenRandom.eldenAttribute(255)
        _flip = EldenRandom.eldenAttribute(2)

        tattoo_mark_tweak = [pos_vert, pos_horiz, angle, expansion, _flip]
        eyepatch = EldenRandom.eldenAttribute(4)
        eyepatch_col = EldenRandom.eldenColor()
        
        output = [tattoo_mark, tattoo_mark_col, tattoo_mark_tweak, eyepatch, eyepatch_col] #[15][0-4]
        return output

    # Alter Body
    #### EldenRandom.all index: 16 [16][0][0]
    def body_attributes():
        match_case = EldenRandom.hair()
        head = EldenRandom.eldenAttribute()
        chest = EldenRandom.eldenAttribute()
        abdomen = EldenRandom.eldenAttribute()
        arms = EldenRandom.eldenAttribute()
        legs = EldenRandom.eldenAttribute()
        body_hair = EldenRandom.eldenAttribute()
        match_hair = random.randrange(2)
        if match_hair == 0:
            body_hair_col = EldenRandom.eldenColor()
        else: 
            body_hair_col = match_case[1]
        
        musculature = random.randrange(2)

        if head - 128 > 0:
            if chest - 90 > 0:
                if abdomen - 90 > 0:
                    if arms - 90 > 0:
                        if legs - 90 > 0:
                            if abdomen + (legs - 90) > 255:
                                abdomen = 255
                            else: 
                                abdomen = abdomen + (legs - 90)
                        if chest + (arms - 90) > 255:
                            chest = 255
                        else:
                            chest = chest + (arms - 90)
                    if legs + (abdomen - 90) > 255:
                        legs = 255
                    else:
                        legs = legs + (abdomen - 90)
                    if chest + (abdomen - 90) > 255:
                        chest = 255
                    else:
                        chest = chest + (abdomen - 90)
                if abdomen + (chest - 90) > 255:
                    abdomen = 255
                else: 
                    abdomen = abdomen + (chest - 90)
                if arms + (chest - 90) > 255:
                    arms = 255
                else:
                    arms = arms + (chest - 90)
            if chest + (head-128) > 255:
                chest = 255
            else:
                chest = chest + (head-128)
        output = [head, chest, abdomen, arms, legs, body_hair, body_hair_col, musculature] #[16][0-7]
        return output
    
    #returns all of the values/lists
    def returnAll():     
        returnList = [EldenRandom.origin(),EldenRandom.bodyType(),EldenRandom.keepsake(),EldenRandom.age(),EldenRandom.voice(),
                      EldenRandom.skinColor(),EldenRandom.face_template(),EldenRandom.facial_structure(),EldenRandom.hair(),
                      EldenRandom.eyebrows(),EldenRandom.facialHair(),EldenRandom.eyelashes(),EldenRandom.eyes_col(),
                      EldenRandom.skin_features(),EldenRandom.cosmetics(),EldenRandom.face_misc(),EldenRandom.body_attributes()]
        return returnList

#def main():
#    facetemp = EldenRandom.face_template()
#    bonestructure = facetemp[0]
#    print(bonestructure)

#if __name__ == "__main__":
#    main() 