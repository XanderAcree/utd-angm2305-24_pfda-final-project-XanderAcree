import pygame
from pygame.locals import *
import button
import EldenRandom
import moviepy

# pygame setup
pygame.init()

pygame.display.set_caption("ELDEN RING CHARACTER ATTRIBUTE RANDOMIZER")

#Base Window Settings
width, height = 1920, 1200
resolution = (width, height)
flags = pygame.SCALED
screen = pygame.display.set_mode(resolution, flags, vsync=1)
pygame.display.toggle_fullscreen()

# setting font
title_font = pygame.font.Font('fonts/Mantinia Regular.otf', 96)
font = pygame.font.Font('fonts/Garamond Premier Pro/Garamond Premier Pro Regular.ttf', 24)
button_font = pygame.font.Font('fonts/Garamond Premier Pro/Garamond Premier Pro Regular.ttf', 27)

#Images, etc.
bg_image = pygame.image.load('images/elden ring.png')
title_img = pygame.image.load('images/title.png')
#textShadow = pygame.image.load('images/textShadow.png')
#shadowSize = textShadow.get_width(), textShadow.get_height()
randResults_grad = pygame.image.load('images/randomizerScreen_gradient.png')
randResults_grad_title = pygame.image.load('images/randomizerScreen_gradient_title.png')
#randResults_screen = pygame.transform.scale(randResults_grad, (1920, 1200))

screenMask = pygame.mask.from_surface(screen)
#Button Class
#class Button():
#    def __init__(self, x, y, image):
#        self.image = image
#        self.rect = self.image.get_rect()
#        self.rect.topleft = (x,y)
#    
#    def draw(self, _x, _y):
#        #Draw button on screen
#        self._pos = (_x, _y)
#        screen.blit(self.image, self._pos)


##Randomize Button
randomize_img = pygame.image.load('images/randomizeButton/randomizeButton_00012.png').convert_alpha()
randomize_button = button.Button(((resolution[0]/2) - (randomize_img.get_width()/2)), 
                                 ((resolution[1]/2) - (randomize_img.get_height()/2)), randomize_img, 1)

eldenFontCol = (200,200,198)

def main():
    # Game loop
    running = True
    clock = pygame.time.Clock()
    attributes = EldenRandom.EldenRandom.returnAll()

    origin_results = button_font.render(attributes[0], True, eldenFontCol)
    origin_w, origin_h = button_font.size(attributes[0])

    bodytype_results = button_font.render(attributes[1], True, eldenFontCol)
    bodytype_w, bodytype_h = button_font.size(attributes[1])

    keepsake_results = button_font.render(attributes[2], True, eldenFontCol)
    keepsake_w, keepsake_h = button_font.size(attributes[2])

    age_results = button_font.render(attributes[3], True, eldenFontCol)
    age_w, age_h = button_font.size(attributes[3])

    voice_results = button_font.render(attributes[4], True, eldenFontCol)
    voice_w, voice_h = button_font.size(attributes[4])

    bonestructure_results = button_font.render(str(attributes[6][0]), True, eldenFontCol)
    bonestructure_w, bonestructure_h = button_font.size(str(attributes[6][0]))

    formemphasis_results = button_font.render(str(attributes[6][1]), True, eldenFontCol)
    formemphasis_w, formemphasis_h = button_font.size(str(attributes[6][1]))

    apparent_age_results = button_font.render(str(attributes[6][2]), True, eldenFontCol)
    apparent_age_w, apparent_age_h = button_font.size(str(attributes[6][2]))

    facial_aesthetic_results = button_font.render(str(attributes[6][3]), True, eldenFontCol)
    facial_aesthetic_w, facial_aesthetic_h = button_font.size(str(attributes[6][3]))

    nose_size_results = button_font.render(str(attributes[7][0][0]), True, eldenFontCol)
    nose_size_w, nose_size_h = button_font.size(str(attributes[7][0][0]))
    nf_ratio_results = button_font.render(str(attributes[7][0][1]), True, eldenFontCol)
    nf_ratio_w, nf_ratio_h = button_font.size(str(attributes[7][0][1]))
    face_prot_results = button_font.render(str(attributes[7][0][2]), True, eldenFontCol)
    face_prot_w, face_prot_h = button_font.size(str(attributes[7][0][2]))
    vface_ratio_results = button_font.render(str(attributes[7][0][3]), True, eldenFontCol)
    vface_ratio_w, vface_ratio_h = button_font.size(str(attributes[7][0][3]))
    faceSlant_results = button_font.render(str(attributes[7][0][4]), True, eldenFontCol)
    faceSlant_w, faceSlant_h = button_font.size(str(attributes[7][0][4]))
    hFaceRatio_results = button_font.render(str(attributes[7][0][5]), True, eldenFontCol)
    hFaceRatio_w, hFaceRatio_h = button_font.size(str(attributes[7][0][5]))

    foreheadDepth_results = button_font.render(str(attributes[7][1][0]), True, eldenFontCol)
    foreheadDepth_w, foreheadDepth_h = button_font.size(str(attributes[7][1][0]))
    foreheadProt_results = button_font.render(str(attributes[7][1][1]), True, eldenFontCol)
    foreheadProt_w, foreheadProt_h = button_font.size(str(attributes[7][1][1]))

    noseBridgeH_results = button_font.render(str(attributes[7][1][2]), True, eldenFontCol)
    noseBridgeH_w, noseBridgeH_h = button_font.size(str(attributes[7][1][2]))
    n_bridgeProt1_results = button_font.render(str(attributes[7][1][3]), True, eldenFontCol)
    n_bridgeProt1_w, n_bridgeProt1_h = button_font.size(str(attributes[7][1][3]))
    n_bridgeProt2_results = button_font.render(str(attributes[7][1][4]), True, eldenFontCol)
    n_bridgeProt2_w, n_bridgeProt2_h = button_font.size(str(attributes[7][1][4]))
    noseBridgeW_results = button_font.render(str(attributes[7][1][5]), True, eldenFontCol)
    noseBridgeW_w, noseBridgeW_h = button_font.size(str(attributes[7][1][5]))

    browRidgeH_results = button_font.render(str(attributes[7][2][0]), True, eldenFontCol)
    browRidgeH_w, browRidgeH_h = button_font.size(str(attributes[7][2][0]))
    innerBrow_results = button_font.render(str(attributes[7][2][1]), True, eldenFontCol)
    innerBrow_w, innerBrow_h = button_font.size(str(attributes[7][2][1]))
    outerBrow_results = button_font.render(str(attributes[7][2][2]), True, eldenFontCol)
    outerBrow_w, outerBrow_h = button_font.size(str(attributes[7][2][2]))

    eyePos_results = button_font.render(str(attributes[7][3][0]), True, eldenFontCol)
    eyePos_w, eyePos_h = button_font.size(str(attributes[7][3][0]))
    eyeSize_results = button_font.render(str(attributes[7][3][1]), True, eldenFontCol)
    eyeSize_w, eyeSize_h = button_font.size(str(attributes[7][3][1]))
    eyeSlant_results = button_font.render(str(attributes[7][3][2]), True, eldenFontCol)
    eyeSlant_w, eyeSlant_h = button_font.size(str(attributes[7][3][2]))
    eyeSpacing_results = button_font.render(str(attributes[7][3][3]), True, eldenFontCol)
    eyeSpacing_w, eyeSpacing_h = button_font.size(str(attributes[7][3][3]))

    noseRidgeDepth_results = button_font.render(str(attributes[7][4][0]), True, eldenFontCol)
    noseRidgeDepth_w, noseRidgeDepth_h = button_font.size(str(attributes[7][4][0]))
    noseRidgeLen_results = button_font.render(str(attributes[7][4][1]), True, eldenFontCol)
    noseRidgeLen_w, noseRidgeLen_h = button_font.size(str(attributes[7][4][1]))
    nosePos_results = button_font.render(str(attributes[7][4][2]), True, eldenFontCol)
    nosePos_w, nosePos_h = button_font.size(str(attributes[7][4][2]))
    noseTipH_results = button_font.render(str(attributes[7][4][3]), True, eldenFontCol)
    noseTipH_w, noseTipH_h = button_font.size(str(attributes[7][4][3]))
    noseProt_results = button_font.render(str(attributes[7][4][4]), True, eldenFontCol)
    noseProt_w, noseProt_h = button_font.size(str(attributes[7][4][4]))
    noseH_results = button_font.render(str(attributes[7][4][5]), True, eldenFontCol)
    noseH_w, noseH_h = button_font.size(str(attributes[7][4][5]))
    noseSlant_results = button_font.render(str(attributes[7][4][6]), True, eldenFontCol)
    noseSlant_w, noseSlant_h = button_font.size(str(attributes[7][4][6]))

    nostrilSlant_results = button_font.render(str(attributes[7][5][0]), True, eldenFontCol)
    nostrilSlant_w, nostrilSlant_h = button_font.size(str(attributes[7][5][0]))
    nostrilSize_results = button_font.render(str(attributes[7][5][1]), True, eldenFontCol)
    nostrilSize_w, nostrilSize_h = button_font.size(str(attributes[7][5][1]))
    nostrilWidth_results = button_font.render(str(attributes[7][5][2]), True, eldenFontCol)
    nostrilWidth_w, nostrilWidth_h = button_font.size(str(attributes[7][5][2]))

    cheekHeight_results = button_font.render(str(attributes[7][6][0]), True, eldenFontCol)
    cheekHeight_w, cheekHeight_h = button_font.size(str(attributes[7][6][0]))
    cheekDepth_results = button_font.render(str(attributes[7][6][1]), True, eldenFontCol)
    cheekDepth_w, cheekDepth_h = button_font.size(str(attributes[7][6][1]))
    cheekWidth_results = button_font.render(str(attributes[7][6][2]), True, eldenFontCol)
    cheekWidth_w, cheekWidth_h = button_font.size(str(attributes[7][6][2]))
    cheekProt_results = button_font.render(str(attributes[7][6][3]), True, eldenFontCol)
    cheekProt_w, cheekProt_h = button_font.size(str(attributes[7][6][3]))
    _cheeks_results = button_font.render(str(attributes[7][6][4]), True, eldenFontCol)
    _cheeks_w, _cheeks_h = button_font.size(str(attributes[7][6][4]))

    lipShape_results = button_font.render(str(attributes[7][7][0]), True, eldenFontCol)
    lipShape_w, lipShape_h = button_font.size(str(attributes[7][7][0]))
    mouthEx_results = button_font.render(str(attributes[7][7][1]), True, eldenFontCol)
    mouthEx_w, mouthEx_h = button_font.size(str(attributes[7][7][1]))
    lipFull_results = button_font.render(str(attributes[7][7][2]), True, eldenFontCol)
    lipFull_w, lipFull_h = button_font.size(str(attributes[7][7][2]))
    lipSize_results = button_font.render(str(attributes[7][7][3]), True, eldenFontCol)
    lipSize_w, lipSize_h = button_font.size(str(attributes[7][7][3]))
    lipProt_results = button_font.render(str(attributes[7][7][4]), True, eldenFontCol)
    lipProt_w, lipProt_h = button_font.size(str(attributes[7][7][4]))
    lipThick_results = button_font.render(str(attributes[7][7][5]), True, eldenFontCol)
    lipThick_w, lipThick_h = button_font.size(str(attributes[7][7][5]))

    mouthProt_results = button_font.render(str(attributes[7][8][0]), True, eldenFontCol)
    mouthProt_w, mouthProt_h = button_font.size(str(attributes[7][8][0]))
    mouthSlant_results = button_font.render(str(attributes[7][8][1]), True, eldenFontCol)
    mouthSlant_w, mouthSlant_h = button_font.size(str(attributes[7][8][1]))
    occlusion_results = button_font.render(str(attributes[7][8][2]), True, eldenFontCol)
    occlusion_w, occlusion_h = button_font.size(str(attributes[7][8][2]))
    mouthPos_results = button_font.render(str(attributes[7][8][3]), True, eldenFontCol)
    mouthPos_w, mouthPos_h = button_font.size(str(attributes[7][8][3]))
    mouthWidth_results = button_font.render(str(attributes[7][8][4]), True, eldenFontCol)
    mouthWidth_w, mouthWidth_h = button_font.size(str(attributes[7][8][4]))
    mouthChinDist_results = button_font.render(str(attributes[7][8][5]), True, eldenFontCol)
    mouthChinDist_w, mouthChinDist_h = button_font.size(str(attributes[7][8][5]))

    chinTipPos_results = button_font.render(str(attributes[7][9][0]), True, eldenFontCol)
    chinTipPos_w, chinTipPos_h = button_font.size(str(attributes[7][9][0]))
    chinLen_results = button_font.render(str(attributes[7][9][1]), True, eldenFontCol)
    chinLen_w, chinLen_h = button_font.size(str(attributes[7][9][1]))
    chinProt_results = button_font.render(str(attributes[7][9][2]), True, eldenFontCol)
    chinProt_w, chinProt_h = button_font.size(str(attributes[7][9][2]))
    chinDepth_results = button_font.render(str(attributes[7][9][3]), True, eldenFontCol)
    chinDepth_w, chinDepth_h = button_font.size(str(attributes[7][9][3]))
    chinSize_results = button_font.render(str(attributes[7][9][4]), True, eldenFontCol)
    chinSize_w, chinSize_h = button_font.size(str(attributes[7][9][4]))
    chinHeight_results = button_font.render(str(attributes[7][9][5]), True, eldenFontCol)
    chinHeight_w, chinHeight_h = button_font.size(str(attributes[7][9][5]))
    chinWidth_results = button_font.render(str(attributes[7][9][6]), True, eldenFontCol)
    chinWidth_w, chinWidth_h = button_font.size(str(attributes[7][9][6]))

    jawProt_results = button_font.render(str(attributes[7][10][0]), True, eldenFontCol)
    jawProt_w, jawProt_h = button_font.size(str(attributes[7][10][0]))
    jawWidth_results = button_font.render(str(attributes[7][10][1]), True, eldenFontCol)
    jawWidth_w, jawWidth_h = button_font.size(str(attributes[7][10][1]))
    lowerJaw_results = button_font.render(str(attributes[7][10][2]), True, eldenFontCol)
    lowerJaw_w, lowerJaw_h = button_font.size(str(attributes[7][10][2]))
    jawContour_results = button_font.render(str(attributes[7][10][3]), True, eldenFontCol)
    jawContour_w, jawContour_h = button_font.size(str(attributes[7][10][3]))


    hairstyle_results = button_font.render(str(attributes[8][0]), True, eldenFontCol)
    hairstyle_w, hairstyle_h = button_font.size(str(attributes[8][0]))
    hairLuster_results = button_font.render(str(attributes[8][2]), True, eldenFontCol)
    hairLuster_w, hairLuster_h = button_font.size(str(attributes[8][2]))
    hairRootDark_results = button_font.render(str(attributes[8][3]), True, eldenFontCol)
    hairRootDark_w, hairRootDark_h = button_font.size(str(attributes[8][3]))
    hairWhite_results = button_font.render(str(attributes[8][4]), True, eldenFontCol)
    hairWhite_w, hairWhite_h = button_font.size(str(attributes[8][4]))
    
    brow_results = button_font.render(str(attributes[9][0]), True, eldenFontCol)
    brow_w, brow_h = button_font.size(str(attributes[9][0]))
    browLuster_results = button_font.render(str(attributes[9][2]), True, eldenFontCol)
    browLuster_w, browLuster_h = button_font.size(str(attributes[9][2]))
    browRootDark_results = button_font.render(str(attributes[9][3]), True, eldenFontCol)
    browRootDark_w, browRootDark_h = button_font.size(str(attributes[9][3]))
    browWhiteHairs_results = button_font.render(str(attributes[9][4]), True, eldenFontCol)
    browWhiteHairs_w, browWhiteHairs_h = button_font.size(str(attributes[9][4]))

    beard_results = button_font.render(str(attributes[10][0]), True, eldenFontCol)
    beard_w, beard_h = button_font.size(str(attributes[10][0]))
    facialHairLuster_results = button_font.render(str(attributes[10][2]), True, eldenFontCol)
    facialHairLuster_w, facialHairLuster_h = button_font.size(str(attributes[10][2]))
    facialHairRootDark_results = button_font.render(str(attributes[10][3]), True, eldenFontCol)
    facialHairRootDark_w, facialHairRootDark_h = button_font.size(str(attributes[10][3]))
    facialHairWhiteHairs_results = button_font.render(str(attributes[10][4]), True, eldenFontCol)
    facialHairWhiteHairs_w, facialHairWhiteHairs_h = button_font.size(str(attributes[10][4]))
    facialHairStubble_results = button_font.render(str(attributes[10][5]), True, eldenFontCol)
    facialHairStubble_w, facialHairStubble_h = button_font.size(str(attributes[10][5]))

    eyelash_results = button_font.render(str(attributes[11][0]), True, eldenFontCol)
    eyelash_w, eyelash_h = button_font.size(str(attributes[11][0]))

    irisSizeR_results = button_font.render(str(attributes[12][0]), True, eldenFontCol)
    irisSizeR_w, irisSizeR_h = button_font.size(str(attributes[12][0]))
    eyeCloudR_results = button_font.render(str(attributes[12][2]), True, eldenFontCol)
    eyeCloudR_w, eyeCloudR_h = button_font.size(str(attributes[12][2]))
    eyePosR_results = button_font.render(str(attributes[12][5]), True, eldenFontCol)
    eyePosR_w, eyePosR_h = button_font.size(str(attributes[12][5]))
    irisSizeL_results = button_font.render(str(attributes[12][6]), True, eldenFontCol)
    irisSizeL_w, irisSizeL_h = button_font.size(str(attributes[12][6]))
    eyeCloudL_results = button_font.render(str(attributes[12][8]), True, eldenFontCol)
    eyeCloudL_w, eyeCloudL_h = button_font.size(str(attributes[12][8]))
    eyePosL_results = button_font.render(str(attributes[12][11]), True, eldenFontCol)
    eyePosL_w, eyePosL_h = button_font.size(str(attributes[12][11]))

    pores_results = button_font.render(str(attributes[13][0]), True, eldenFontCol)
    pores_w, pores_h = button_font.size(str(attributes[13][0]))
    skinLuster_results = button_font.render(str(attributes[13][1]), True, eldenFontCol)
    skinLuster_w, skinLuster_h = button_font.size(str(attributes[13][1]))
    darkCircles_results = button_font.render(str(attributes[13][2]), True, eldenFontCol)
    darkCircles_w, darkCircles_h = button_font.size(str(attributes[13][2]))

    eyeliner_results = button_font.render(str(attributes[14][0]), True, eldenFontCol)
    eyeliner_w, eyeliner_h = button_font.size(str(attributes[14][0]))
    eyeshadowUpper_results = button_font.render(str(attributes[14][2]), True, eldenFontCol)
    eyeShadowUpper_w, eyeShadowUpper_h = button_font.size(str(attributes[14][2]))
    eyeShadowLower_results = button_font.render(str(attributes[14][4]), True, eldenFontCol)
    eyeShadowLower_w, eyeShadowLower_h = button_font.size(str(attributes[14][4]))
    cosmeticsCheeks_results = button_font.render(str(attributes[14][6]), True, eldenFontCol)
    cosmeticsCheeks_w, cosmeticsCheeks_h = button_font.size(str(attributes[14][6]))
    lipstick_results = button_font.render(str(attributes[14][8]))
    lipstick_w, lipstick_h = button_font.size(str(attributes[14][8]))


    #skinCol = pygame.draw.rect(screen,attributes[5],(505,401,398,31))

    titlePos = ((resolution[0]/2) - (title_img.get_width()/2), 0 + (title_img.get_height()/4))
    isRandButtonClicked = False
    scrollWheel = 0
    uiOffset = -(77*2)

    # DEBUG FOR COLORS
    print("---------- DEBUG VALUES FOR COLOR OUTPUTS ----------")
    print(f"Skin Color: {attributes[5]}") ## SKIN COLOR
    print(f"Hair Color: {attributes[8][1]}") ## HAIR COLOR
    print(f"Brow Color: {attributes[9][1]}") ## BROW COLOR
    print(f"Beard Color: {attributes[10][1]}") ## BEARD COLOR
    print(f"Eyelash Color: {attributes[11][1]}") ## EYELASH COLOR
    print(f"Right Iris Color: {attributes[12][1]}") ## RIGHT IRIS COLOR
    print(f"Right Iris Clouding Color: {attributes[12][3]}") ## RIGHT IRIS CLOUDING COLOR
    print(f"Right Sclera/Eye White Color: {attributes[12][4]}") ## RIGHT SCLERA/EYE WHITE COLOR
    print(f"Left Iris Color: {attributes[12][7]}") ## LEFT IRIS COLOR
    print(f"Left Iris Clouding Color: {attributes[12][9]}") ## LEFT IRIS CLOUDING COLOR
    print(f"Left Sclera/Eye White Color: {attributes[12][10]}") ## LEFT SCLERA/EYE WHITE COLOR
    print(f"Dark Circles Color: {attributes[13][3]}") ## DARK CIRCLES COLOR

    while running:
        origin_img = pygame.image.load('images/ER_origin.png').convert_alpha()
        origin_button = button.Button((origin_img.get_width()/2) - (origin_img.get_width()/3) + 77 + uiOffset,
                                    213+60+scrollWheel,origin_img,1)
        bodytype_img = pygame.image.load('images/ER_bodytype.png').convert_alpha()
        bodytype_button = button.Button((bodytype_img.get_width()/2) - (bodytype_img.get_width()/3) + 77 + uiOffset,
                                    213+(60*2)+scrollWheel,bodytype_img,1)
        keepsake_img = pygame.image.load('images/ER_keepsake.png').convert_alpha()
        keepsake_button = button.Button((keepsake_img.get_width()/2) - (keepsake_img.get_width()/3) + 77 + uiOffset,
                                    213+(60*3)+scrollWheel,keepsake_img,1)
        detailed_appearance_img = pygame.image.load('images/ER_detailedAppearance.png').convert_alpha()
        detailed_appearance_button = button.Button((detailed_appearance_img.get_width()/2) - (detailed_appearance_img.get_width()/3) + 77 + uiOffset,
                                    213+(60*5)+scrollWheel,detailed_appearance_img,1)
        age_img = pygame.image.load('images/ER_age.png').convert_alpha()
        age_button = button.Button((age_img.get_width()/2) - (age_img.get_width()/3) + (77*2) + uiOffset,
                                    213+(60*6)+scrollWheel,age_img,1)
        voice_img = pygame.image.load('images/ER_voice.png').convert_alpha()
        voice_button = button.Button((voice_img.get_width()/2) - (voice_img.get_width()/3) + (77*2) + uiOffset,
                                    213+(60*7)+scrollWheel,voice_img,1)
        skinCol_img = pygame.image.load('images/ER_skincol.png').convert_alpha()
        skinCol_button = button.Button((skinCol_img.get_width()/2) - (skinCol_img.get_width()/3) + (77*2) + uiOffset,
                                    213+(60*8)+scrollWheel,skinCol_img,1)
        face_hair_img = pygame.image.load('images/ER_face-hair.png').convert_alpha()
        face_hair_button = button.Button((face_hair_img.get_width()/2) - (face_hair_img.get_width()/3) + (77) + uiOffset,
                                    213+(60*9)+scrollWheel,face_hair_img,1)
        facetemplate_img = pygame.image.load('images/ER_facetemplate.png').convert_alpha()
        facetemplate_button = button.Button((facetemplate_img.get_width()/2) - (facetemplate_img.get_width()/3) + (77*2) + uiOffset,
                                    213+(60*10)+scrollWheel,facetemplate_img,1)
        bonestructure_img = pygame.image.load('images/ER_bonestructure.png').convert_alpha()
        bonestructure_button = button.Button((bonestructure_img.get_width()/2) - (bonestructure_img.get_width()/3) + (77*3) + uiOffset,
                                    213+(60*11)+scrollWheel,bonestructure_img,1)
        formemphasis_img = pygame.image.load('images/ER_formemphasis.png').convert_alpha()
        formemphasis_button = button.Button((formemphasis_img.get_width()/2) - (formemphasis_img.get_width()/3) + (77*3) + uiOffset,
                                    213+(60*12)+scrollWheel,formemphasis_img,1)
        apparent_age_img = pygame.image.load('images/ER_apparent_age.png').convert_alpha()
        apparent_age_button = button.Button((apparent_age_img.get_width()/2) - (apparent_age_img.get_width()/3) + (77*3) + uiOffset,
                                    213+(60*13)+scrollWheel,apparent_age_img,1)
        facial_aesthetic_img = pygame.image.load('images/ER_facial-aesthetic.png').convert_alpha()
        facial_aesthetic_button = button.Button((facial_aesthetic_img.get_width()/2) - (facial_aesthetic_img.get_width()/3) + (77*3) + uiOffset,
                                    213+(60*14)+scrollWheel,facial_aesthetic_img,1)
        
        facialstructure_img = pygame.image.load('images/ER_facialstructure.png').convert_alpha()
        facialstructure_button = button.Button((facialstructure_img.get_width()/2) - (facialstructure_img.get_width()/3) + (77*2) + uiOffset,
                                    213+(60*15)+scrollWheel,facialstructure_img,1)
        
        facialbalance_img = pygame.image.load('images/ER_facialbalance.png').convert_alpha()
        facialbalance_button = button.Button((facialbalance_img.get_width()/2) - (facialbalance_img.get_width()/3) + (77*3) + uiOffset,
                                    213+(60*16)+scrollWheel,facialbalance_img,1)
        nose_size_img = pygame.image.load('images/ER_nose_size.png').convert_alpha()
        nose_size_button = button.Button((nose_size_img.get_width()/2) - (nose_size_img.get_width()/3) + (77*4) + uiOffset,
                                    213+(60*17)+scrollWheel,nose_size_img,1)
        nf_ratio_img = pygame.image.load('images/ER_nose_forehead_ratio.png').convert_alpha()
        nf_ratio_button = button.Button((nf_ratio_img.get_width()/2) - (nf_ratio_img.get_width()/3) + (77*4) + uiOffset,
                                    213+(60*18)+scrollWheel,nf_ratio_img,1)
        face_prot_img = pygame.image.load('images/ER_face_protrusion.png').convert_alpha()
        face_prot_button = button.Button((face_prot_img.get_width()/2) - (face_prot_img.get_width()/3) + (77*4) + uiOffset,
                                    213+(60*19)+scrollWheel,face_prot_img,1)
        vface_ratio_img = pygame.image.load('images/ER_vert_face_ratio.png').convert_alpha()
        vface_ratio_button = button.Button((vface_ratio_img.get_width()/2) - (vface_ratio_img.get_width()/3) + (77*4) + uiOffset,
                                    213+(60*20)+scrollWheel,vface_ratio_img,1)
        faceSlant_img = pygame.image.load('images/ER_facial_feature_slant.png').convert_alpha()
        faceSlant_button = button.Button((faceSlant_img.get_width()/2) - (faceSlant_img.get_width()/3) + (77*4) + uiOffset,
                                    213+(60*21)+scrollWheel,faceSlant_img,1)
        hFaceRatio_img = pygame.image.load('images/ER_horiz_face_ratio.png').convert_alpha()
        hFaceRatio_button = button.Button((hFaceRatio_img.get_width()/2) - (hFaceRatio_img.get_width()/3) + (77*4) + uiOffset,
                                    213+(60*22)+scrollWheel,hFaceRatio_img,1)
        
        foreheadGlabella_img = pygame.image.load('images/ER_forehead-glabella.png').convert_alpha()
        foreheadGlabella_button = button.Button((foreheadGlabella_img.get_width()/2) - (foreheadGlabella_img.get_width()/3) + (77*3) + uiOffset,
                                    213+(60*23)+scrollWheel,foreheadGlabella_img,1)
        foreheadDepth_img = pygame.image.load('images/ER_forehead_depth.png').convert_alpha()
        foreheadDepth_button = button.Button((foreheadDepth_img.get_width()/2) - (foreheadDepth_img.get_width()/3) + (77*4) + uiOffset,
                                    213+(60*24)+scrollWheel,foreheadDepth_img,1)
        foreheadProt_img = pygame.image.load('images/ER_forehead_protrusion.png').convert_alpha()
        foreheadProt_button = button.Button((foreheadProt_img.get_width()/2) - (foreheadProt_img.get_width()/3) + (77*4) + uiOffset,
                                    213+(60*25)+scrollWheel,foreheadProt_img,1)
        noseBridgeH_img = pygame.image.load('images/ER_nose_bridge_h.png').convert_alpha()
        noseBridgeH_button = button.Button((noseBridgeH_img.get_width()/2) - (noseBridgeH_img.get_width()/3) + (77*4) + uiOffset,
                                    213+(60*26)+scrollWheel,noseBridgeH_img,1)
        n_bridgeProt1_img = pygame.image.load('images/ER_bridge_protrusion_1.png').convert_alpha()
        n_bridgeProt1_button = button.Button((n_bridgeProt1_img.get_width()/2) - (n_bridgeProt1_img.get_width()/3) + (77*4) + uiOffset,
                                    213+(60*27)+scrollWheel,n_bridgeProt1_img,1)
        n_bridgeProt2_img = pygame.image.load('images/ER_bridge_protrusion_2.png').convert_alpha()
        n_bridgeProt2_button = button.Button((n_bridgeProt2_img.get_width()/2) - (n_bridgeProt2_img.get_width()/3) + (77*4) + uiOffset,
                                    213+(60*28)+scrollWheel,n_bridgeProt2_img,1)
        noseBridgeW_img = pygame.image.load('images/ER_nose_bridge_w.png').convert_alpha()
        noseBridgeW_button = button.Button((noseBridgeW_img.get_width()/2) - (noseBridgeW_img.get_width()/3) + (77*4) + uiOffset,
                                    213+(60*29)+scrollWheel,noseBridgeW_img,1)
        browRidge_img = pygame.image.load('images/ER_brow-ridge.png').convert_alpha()
        browRidge_button = button.Button((browRidge_img.get_width()/2) - (browRidge_img.get_width()/3) + (77*3) + uiOffset,
                                    213+(60*30)+scrollWheel,browRidge_img,1)
        browRidgeH_img = pygame.image.load('images/ER_brow_ridge_height.png').convert_alpha()
        browRidgeH_button = button.Button((browRidgeH_img.get_width()/2) - (browRidgeH_img.get_width()/3) + (77*4) + uiOffset,
                                    213+(60*31)+scrollWheel,browRidgeH_img,1)
        innerBrow_img = pygame.image.load('images/ER_inner_brow_ridge.png').convert_alpha()
        innerBrow_button = button.Button((innerBrow_img.get_width()/2) - (innerBrow_img.get_width()/3) + (77*4) + uiOffset,
                                    213+(60*32)+scrollWheel,innerBrow_img,1)
        outerBrow_img = pygame.image.load('images/ER_outer_brow_ridge.png').convert_alpha()
        outerBrow_button = button.Button((outerBrow_img.get_width()/2) - (outerBrow_img.get_width()/3) + (77*4) + uiOffset,
                                    213+(60*33)+scrollWheel,outerBrow_img,1)
        
        eyes_img = pygame.image.load('images/ER_eyes.png').convert_alpha()
        eyes_button = button.Button((eyes_img.get_width()/2) - (eyes_img.get_width()/3) + (77*3) + uiOffset,
                                    213+(60*34)+scrollWheel,eyes_img,1)
        eyePos_img = pygame.image.load('images/ER_eye_pos.png').convert_alpha()
        eyePos_button = button.Button((eyePos_img.get_width()/2) - (eyePos_img.get_width()/3) + (77*4) + uiOffset,
                                    213+(60*35)+scrollWheel,eyePos_img,1)
        eyeSize_img = pygame.image.load('images/ER_eye_size.png').convert_alpha()
        eyeSize_button = button.Button((eyeSize_img.get_width()/2) - (eyeSize_img.get_width()/3) + (77*4) + uiOffset,
                                    213+(60*36)+scrollWheel,eyeSize_img,1)
        eyeSlant_img = pygame.image.load('images/ER_eye_slant.png').convert_alpha()
        eyeSlant_button = button.Button((eyeSlant_img.get_width()/2) - (eyeSlant_img.get_width()/3) + (77*4) + uiOffset,
                                    213+(60*37)+scrollWheel,eyeSlant_img,1)
        eyeSpacing_img = pygame.image.load('images/ER_eye_spacing.png').convert_alpha()
        eyeSpacing_button = button.Button((eyeSpacing_img.get_width()/2) - (eyeSpacing_img.get_width()/3) + (77*4) + uiOffset,
                                    213+(60*38)+scrollWheel,eyeSpacing_img,1)
        
        noseRidge_img = pygame.image.load('images/ER_nose_ridge.png').convert_alpha()
        noseRidge_button = button.Button((noseRidge_img.get_width()/2) - (noseRidge_img.get_width()/3) + (77*3) + uiOffset,
                                    213+(60*39)+scrollWheel,noseRidge_img,1)
        noseRidgeDepth_img = pygame.image.load('images/ER_nose_ridge_depth.png').convert_alpha()
        noseRidgeDepth_button = button.Button((noseRidgeDepth_img.get_width()/2) - (noseRidgeDepth_img.get_width()/3) + (77*4) + uiOffset,
                                    213+(60*40)+scrollWheel,noseRidgeDepth_img,1)
        noseRidgeLen_img = pygame.image.load('images/ER_nose_ridge_len.png').convert_alpha()
        noseRidgeLen_button = button.Button((noseRidgeLen_img.get_width()/2) - (noseRidgeLen_img.get_width()/3) + (77*4) + uiOffset,
                                    213+(60*41)+scrollWheel,noseRidgeLen_img,1)
        nosePos_img = pygame.image.load('images/ER_nose_pos.png').convert_alpha()
        nosePos_button = button.Button((nosePos_img.get_width()/2) - (nosePos_img.get_width()/3) + (77*4) + uiOffset,
                                    213+(60*42)+scrollWheel,nosePos_img,1)
        noseTipH_img = pygame.image.load('images/ER_nose_tip_h.png').convert_alpha()
        noseTipH_button = button.Button((noseTipH_img.get_width()/2) - (noseTipH_img.get_width()/3) + (77*4) + uiOffset,
                                    213+(60*43)+scrollWheel,noseTipH_img,1)
        noseProt_img = pygame.image.load('images/ER_nose_protrusion.png').convert_alpha()
        noseProt_button = button.Button((noseProt_img.get_width()/2) - (noseProt_img.get_width()/3) + (77*4) + uiOffset,
                                    213+(60*44)+scrollWheel,noseProt_img,1)
        noseH_img = pygame.image.load('images/ER_nose_h.png').convert_alpha()
        noseH_button = button.Button((noseH_img.get_width()/2) - (noseH_img.get_width()/3) + (77*4) + uiOffset,
                                    213+(60*45)+scrollWheel,noseH_img,1)
        noseSlant_img = pygame.image.load('images/ER_nose_slant.png').convert_alpha()
        noseSlant_button = button.Button((noseSlant_img.get_width()/2) - (noseSlant_img.get_width()/3) + (77*4) + uiOffset,
                                    213+(60*46)+scrollWheel,noseSlant_img,1)
        
        nostrils_img = pygame.image.load('images/ER_nostrils.png').convert_alpha()
        nostrils_button = button.Button((nostrils_img.get_width()/2) - (nostrils_img.get_width()/3) + (77*3) + uiOffset,
                                    213+(60*47)+scrollWheel,nostrils_img,1)
        nostrilSlant_img = pygame.image.load('images/ER_nostril_slant.png').convert_alpha()
        nostrilSlant_button = button.Button((nostrilSlant_img.get_width()/2) - (nostrilSlant_img.get_width()/3) + (77*4) + uiOffset,
                                    213+(60*48)+scrollWheel,nostrilSlant_img,1)
        nostrilSize_img = pygame.image.load('images/ER_nostril_size.png').convert_alpha()
        nostrilSize_button = button.Button((nostrilSize_img.get_width()/2) - (nostrilSize_img.get_width()/3) + (77*4) + uiOffset,
                                    213+(60*49)+scrollWheel,nostrilSize_img,1)
        nostrilWidth_img = pygame.image.load('images/ER_nostril_width.png').convert_alpha()
        nostrilWidth_button = button.Button((nostrilWidth_img.get_width()/2) - (nostrilWidth_img.get_width()/3) + (77*4) + uiOffset,
                                    213+(60*50)+scrollWheel,nostrilWidth_img,1)
        
        cheeks_img = pygame.image.load('images/ER_cheeks.png').convert_alpha()
        cheeks_button = button.Button((cheeks_img.get_width()/2) - (cheeks_img.get_width()/3) + (77*3) + uiOffset,
                                    213+(60*51)+scrollWheel,cheeks_img,1)
        cheekHeight_img = pygame.image.load('images/ER_cheek_height.png').convert_alpha()
        cheekHeight_button = button.Button((cheekHeight_img.get_width()/2) - (cheekHeight_img.get_width()/3) + (77*4) + uiOffset,
                                    213+(60*52)+scrollWheel,cheekHeight_img,1)
        cheekDepth_img = pygame.image.load('images/ER_cheek_depth.png').convert_alpha()
        cheekDepth_button = button.Button((cheekDepth_img.get_width()/2) - (cheekDepth_img.get_width()/3) + (77*4) + uiOffset,
                                    213+(60*53)+scrollWheel,cheekDepth_img,1)
        cheekWidth_img = pygame.image.load('images/ER_cheek_width.png').convert_alpha()
        cheekWidth_button = button.Button((cheekWidth_img.get_width()/2) - (cheekWidth_img.get_width()/3) + (77*4) + uiOffset,
                                    213+(60*54)+scrollWheel,cheekWidth_img,1)
        cheekProt_img = pygame.image.load('images/ER_cheek_protrusion.png').convert_alpha()
        cheekProt_button = button.Button((cheekProt_img.get_width()/2) - (cheekProt_img.get_width()/3) + (77*4) + uiOffset,
                                    213+(60*55)+scrollWheel,cheekProt_img,1)
        _cheeks_img = pygame.image.load('images/ER__cheeks.png').convert_alpha()
        _cheeks_button = button.Button((_cheeks_img.get_width()/2) - (_cheeks_img.get_width()/3) + (77*4) + uiOffset,
                                    213+(60*56)+scrollWheel,_cheeks_img,1)
        
        lips_img = pygame.image.load('images/ER_lips.png').convert_alpha()
        lips_button = button.Button((lips_img.get_width()/2) - (lips_img.get_width()/3) + (77*3) + uiOffset,
                                    213+(60*57)+scrollWheel,lips_img,1)
        lipShape_img = pygame.image.load('images/ER_lip_shape.png').convert_alpha()
        lipShape_button = button.Button((lipShape_img.get_width()/2) - (lipShape_img.get_width()/3) + (77*4) + uiOffset,
                                    213+(60*58)+scrollWheel,lipShape_img,1)
        mouthEx_img = pygame.image.load('images/ER_mouth_expression.png').convert_alpha()
        mouthEx_button = button.Button((mouthEx_img.get_width()/2) - (mouthEx_img.get_width()/3) + (77*4) + uiOffset,
                                    213+(60*59)+scrollWheel,mouthEx_img,1)
        lipFull_img = pygame.image.load('images/ER_lip_fullness.png').convert_alpha()
        lipFull_button = button.Button((lipFull_img.get_width()/2) - (lipFull_img.get_width()/3) + (77*4) + uiOffset,
                                    213+(60*60)+scrollWheel,lipFull_img,1)
        lipSize_img = pygame.image.load('images/ER_lip_size.png').convert_alpha()
        lipSize_button = button.Button((lipSize_img.get_width()/2) - (lipSize_img.get_width()/3) + (77*4) + uiOffset,
                                    213+(60*61)+scrollWheel,lipSize_img,1)
        lipProt_img = pygame.image.load('images/ER_lip_protrusion.png').convert_alpha()
        lipProt_button = button.Button((lipProt_img.get_width()/2) - (lipProt_img.get_width()/3) + (77*4) + uiOffset,
                                    213+(60*62)+scrollWheel,lipProt_img,1)
        lipThick_img = pygame.image.load('images/ER_lip_thickness.png').convert_alpha()
        lipThick_button = button.Button((lipThick_img.get_width()/2) - (lipThick_img.get_width()/3) + (77*4) + uiOffset,
                                    213+(60*63)+scrollWheel,lipThick_img,1)
        
        mouth_img = pygame.image.load('images/ER_mouth.png').convert_alpha()
        mouth_button = button.Button((mouth_img.get_width()/2) - (mouth_img.get_width()/3) + (77*3) + uiOffset,
                                    213+(60*64)+scrollWheel,mouth_img,1)
        mouthProt_img = pygame.image.load('images/ER_mouth_protrusion.png').convert_alpha()
        mouthProt_button = button.Button((mouthProt_img.get_width()/2) - (mouthProt_img.get_width()/3) + (77*4) + uiOffset,
                                    213+(60*65)+scrollWheel,mouthProt_img,1)
        mouthSlant_img = pygame.image.load('images/ER_mouth_slant.png').convert_alpha()
        mouthSlant_button = button.Button((mouthSlant_img.get_width()/2) - (mouthSlant_img.get_width()/3) + (77*4) + uiOffset,
                                    213+(60*66)+scrollWheel,mouthSlant_img,1)
        occlusion_img = pygame.image.load('images/ER_occlusion.png').convert_alpha()
        occlusion_button = button.Button((occlusion_img.get_width()/2) - (occlusion_img.get_width()/3) + (77*4) + uiOffset,
                                    213+(60*67)+scrollWheel,occlusion_img,1)
        mouthPos_img = pygame.image.load('images/ER_mouth_position.png').convert_alpha()
        mouthPos_button = button.Button((mouthPos_img.get_width()/2) - (mouthPos_img.get_width()/3) + (77*4) + uiOffset,
                                    213+(60*68)+scrollWheel,mouthPos_img,1)
        mouthWidth_img = pygame.image.load('images/ER_mouth_width.png').convert_alpha()
        mouthWidth_button = button.Button((mouthWidth_img.get_width()/2) - (mouthWidth_img.get_width()/3) + (77*4) + uiOffset,
                                    213+(60*69)+scrollWheel,mouthWidth_img,1)
        mouthChinDist_img = pygame.image.load('images/ER_mouth_chin_dist.png').convert_alpha()
        mouthChinDist_button = button.Button((mouthChinDist_img.get_width()/2) - (mouthChinDist_img.get_width()/3) + (77*4) + uiOffset,
                                    213+(60*70)+scrollWheel,mouthChinDist_img,1)
        
        chin_img = pygame.image.load('images/ER_chin.png').convert_alpha()
        chin_button = button.Button((chin_img.get_width()/2) - (chin_img.get_width()/3) + (77*3) + uiOffset,
                                    213+(60*71)+scrollWheel,chin_img,1)
        chinTipPos_img = pygame.image.load('images/ER_chin_tip_pos.png').convert_alpha()
        chinTipPos_button = button.Button((chinTipPos_img.get_width()/2) - (chinTipPos_img.get_width()/3) + (77*4) + uiOffset,
                                    213+(60*72)+scrollWheel,chinTipPos_img,1)
        chinLen_img = pygame.image.load('images/ER_chin_len.png').convert_alpha()
        chinLen_button = button.Button((chinLen_img.get_width()/2) - (chinLen_img.get_width()/3) + (77*4) + uiOffset,
                                    213+(60*73)+scrollWheel,chinLen_img,1)
        chinProt_img = pygame.image.load('images/ER_chin_prot.png').convert_alpha()
        chinProt_button = button.Button((chinProt_img.get_width()/2) - (chinProt_img.get_width()/3) + (77*4) + uiOffset,
                                    213+(60*74)+scrollWheel,chinProt_img,1)
        chinDepth_img = pygame.image.load('images/ER_chin_depth.png').convert_alpha()
        chinDepth_button = button.Button((chinDepth_img.get_width()/2) - (chinDepth_img.get_width()/3) + (77*4) + uiOffset,
                                    213+(60*75)+scrollWheel,chinDepth_img,1)
        chinSize_img = pygame.image.load('images/ER_chin_size.png').convert_alpha()
        chinSize_button = button.Button((chinSize_img.get_width()/2) - (chinSize_img.get_width()/3) + (77*4) + uiOffset,
                                    213+(60*76)+scrollWheel,chinSize_img,1)
        chinHeight_img = pygame.image.load('images/ER_chin_height.png').convert_alpha()
        chinHeight_button = button.Button((chinHeight_img.get_width()/2) - (chinHeight_img.get_width()/3) + (77*4) + uiOffset,
                                    213+(60*77)+scrollWheel,chinHeight_img,1)
        chinWidth_img = pygame.image.load('images/ER_chin_width.png').convert_alpha()
        chinWidth_button = button.Button((chinWidth_img.get_width()/2) - (chinWidth_img.get_width()/3) + (77*4) + uiOffset,
                                    213+(60*78)+scrollWheel,chinWidth_img,1)
        
        jaw_img = pygame.image.load('images/ER_jaw.png').convert_alpha()
        jaw_button = button.Button((jaw_img.get_width()/2) - (jaw_img.get_width()/3) + (77*3) + uiOffset,
                                    213+(60*79)+scrollWheel,jaw_img,1)
        jawProt_img = pygame.image.load('images/ER_jaw_prot.png').convert_alpha()
        jawProt_button = button.Button((jawProt_img.get_width()/2) - (jawProt_img.get_width()/3) + (77*4) + uiOffset,
                                    213+(60*80)+scrollWheel,jawProt_img,1)
        jawWidth_img = pygame.image.load('images/ER_jaw_width.png').convert_alpha()
        jawWidth_button = button.Button((jawWidth_img.get_width()/2) - (jawWidth_img.get_width()/3) + (77*4) + uiOffset,
                                    213+(60*81)+scrollWheel,jawWidth_img,1)
        lowerJaw_img = pygame.image.load('images/ER_lower_jaw.png').convert_alpha()
        lowerJaw_button = button.Button((lowerJaw_img.get_width()/2) - (lowerJaw_img.get_width()/3) + (77*4) + uiOffset,
                                    213+(60*82)+scrollWheel,lowerJaw_img,1)
        jawContour_img = pygame.image.load('images/ER_jaw_contour.png').convert_alpha()
        jawContour_button = button.Button((jawContour_img.get_width()/2) - (jawContour_img.get_width()/3) + (77*4) + uiOffset,
                                    213+(60*83)+scrollWheel,jawContour_img,1)
        

        hair_img = pygame.image.load('images/ER_hair.png').convert_alpha()
        hair_button = button.Button((hair_img.get_width()/2) - (hair_img.get_width()/3) + (77*3) + uiOffset,
                                    213+(60*84)+scrollWheel,hair_img,1)
        hairstyle_img = pygame.image.load('images/ER_hairstyle.png').convert_alpha()
        hairstyle_button = button.Button((hairstyle_img.get_width()/2) - (hair_img.get_width()/3) + (77*4) + uiOffset,
                                    213+(60*85)+scrollWheel,hairstyle_img,1)
        hairCol_img = pygame.image.load('images/ER_hair_col.png').convert_alpha()
        hairCol_button = button.Button((hairCol_img.get_width()/2) - (hairCol_img.get_width()/3) + (77*4) + uiOffset,
                                    213+(60*86)+scrollWheel,hairCol_img,1)
        hairLuster_img = pygame.image.load('images/ER_hairluster.png').convert_alpha()
        hairLuster_button = button.Button((hairLuster_img.get_width()/2) - (hairLuster_img.get_width()/3) + (77*4) + uiOffset,
                                    213+(60*87)+scrollWheel,hairLuster_img,1)
        hairRootDark_img = pygame.image.load('images/ER_hair_root_dark.png').convert_alpha()
        hairRootDark_button = button.Button((hairRootDark_img.get_width()/2) - (hairRootDark_img.get_width()/3) + (77*4) + uiOffset,
                                    213+(60*88)+scrollWheel,hairRootDark_img,1)
        hairWhite_img = pygame.image.load('images/ER_hairwhite.png').convert_alpha()
        hairWhite_button = button.Button((hairWhite_img.get_width()/2) - (hairWhite_img.get_width()/3) + (77*4) + uiOffset,
                                    213+(60*89)+scrollWheel,hairWhite_img,1)
        
        eyebrow_img = pygame.image.load('images/ER_eyebrows.png').convert_alpha()
        eyebrow_button = button.Button((eyebrow_img.get_width()/2) - (eyebrow_img.get_width()/3) + (77*3) + uiOffset,
                                    213+(60*90)+scrollWheel,eyebrow_img,1)
        brow_img = pygame.image.load('images/ER_brow.png').convert_alpha()
        brow_button = button.Button((brow_img.get_width()/2) - (brow_img.get_width()/3) + (77*4) + uiOffset,
                                    213+(60*91)+scrollWheel,brow_img,1)
        browCol_img = pygame.image.load('images/ER_brow_col.png').convert_alpha()
        browCol_button = button.Button((browCol_img.get_width()/2) - (browCol_img.get_width()/3) + (77*4) + uiOffset,
                                    213+(60*92)+scrollWheel,browCol_img,1)
        browLuster_img = pygame.image.load('images/ER_brow_luster.png').convert_alpha()
        browLuster_button = button.Button((browLuster_img.get_width()/2) - (browLuster_img.get_width()/3) + (77*4) + uiOffset,
                                    213+(60*93)+scrollWheel,browLuster_img,1)
        browRootDark_img = pygame.image.load('images/ER_brow_root_dark.png').convert_alpha()
        browRootDark_button = button.Button((browRootDark_img.get_width()/2) - (browRootDark_img.get_width()/3) + (77*4) + uiOffset,
                                    213+(60*94)+scrollWheel,browRootDark_img,1)
        browWhiteHairs_img = pygame.image.load('images/ER_brow_white_hairs.png').convert_alpha()
        browWhiteHairs_button = button.Button((browWhiteHairs_img.get_width()/2) - (browWhiteHairs_img.get_width()/3) + (77*4) + uiOffset,
                                    213+(60*95)+scrollWheel,browWhiteHairs_img,1)
        
        facialHair_img = pygame.image.load('images/ER_facial_hair.png').convert_alpha()
        facialHair_button = button.Button((facialHair_img.get_width()/2) - (facialHair_img.get_width()/3) + (77*3) + uiOffset,
                                    213+(60*96)+scrollWheel,facialHair_img,1)
        beard_img = pygame.image.load('images/ER_beard.png').convert_alpha()
        beard_button = button.Button((beard_img.get_width()/2) - (beard_img.get_width()/3) + (77*4) + uiOffset,
                                    213+(60*97)+scrollWheel,beard_img,1)
        facialHairCol_img = pygame.image.load('images/ER_facial_hair_col.png').convert_alpha()
        facialHairCol_button = button.Button((facialHairCol_img.get_width()/2) - (facialHairCol_img.get_width()/3) + (77*4) + uiOffset,
                                    213+(60*98)+scrollWheel,facialHairCol_img,1)
        facialHairLuster_img = pygame.image.load('images/ER_facial_hair_luster.png').convert_alpha()
        facialHairLuster_button = button.Button((facialHairLuster_img.get_width()/2) - (facialHairLuster_img.get_width()/3) + (77*4) + uiOffset,
                                    213+(60*99)+scrollWheel,facialHairLuster_img,1)
        facialHairRootDark_img = pygame.image.load('images/ER_facial_hair_root_dark.png').convert_alpha()
        facialHairRootDark_button = button.Button((facialHairRootDark_img.get_width()/2) - (facialHairRootDark_img.get_width()/3) + (77*4) + uiOffset,
                                    213+(60*100)+scrollWheel,facialHairRootDark_img,1)
        facialHairWhiteHairs_img = pygame.image.load('images/ER_facial_hair_white_hairs.png').convert_alpha()
        facialHairWhiteHairs_button = button.Button((facialHairWhiteHairs_img.get_width()/2) - (facialHairWhiteHairs_img.get_width()/3) + (77*4) + uiOffset,
                                    213+(60*101)+scrollWheel,facialHairWhiteHairs_img,1)
        facialHairStubble_img = pygame.image.load('images/ER_facial_hair_stubble.png').convert_alpha()
        facialHairStubble_button = button.Button((facialHairStubble_img.get_width()/2) - (facialHairStubble_img.get_width()/3) + (77*4) + uiOffset,
                                    213+(60*102)+scrollWheel,facialHairStubble_img,1)
        
        eyelash_img = pygame.image.load('images/ER_eyelashes.png').convert_alpha()
        eyelash_button = button.Button((eyelash_img.get_width()/2) - (eyelash_img.get_width()/3) + (77*3) + uiOffset,
                                    213+(60*103)+scrollWheel,eyelash_img,1)
        eyelash__img = pygame.image.load('images/ER_eyelashes_.png').convert_alpha()
        eyelash__button = button.Button((eyelash__img.get_width()/2) - (eyelash__img.get_width()/3) + (77*4) + uiOffset,
                                    213+(60*104)+scrollWheel,eyelash__img,1)
        eyelashCol_img = pygame.image.load('images/ER_eyelash_col.png').convert_alpha()
        eyelashCol_button = button.Button((eyelashCol_img.get_width()/2) - (eyelash__img.get_width()/3) + (77*4) + uiOffset,
                                    213+(60*105)+scrollWheel,eyelashCol_img,1)
        
        ## Eye R
        eyesCol_img = pygame.image.load('images/ER_eyes_col.png').convert_alpha()
        eyesCol_button = button.Button((eyesCol_img.get_width()/2) - (eyesCol_img.get_width()/3) + (77*3) + uiOffset,
                                    213+(60*106)+scrollWheel,eyesCol_img,1)
        irisSizeR_img = pygame.image.load('images/ER_iris_size_r.png').convert_alpha()
        irisSizeR_button = button.Button((irisSizeR_img.get_width()/2) - (irisSizeR_img.get_width()/3) + (77*4) + uiOffset,
                                    213+(60*107)+scrollWheel,irisSizeR_img,1)
        irisColR_img = pygame.image.load('images/ER_iris_col_r.png').convert_alpha()
        irisColR_button = button.Button((irisColR_img.get_width()/2) - (irisColR_img.get_width()/3) + (77*4) + uiOffset,
                                    213+(60*108)+scrollWheel,irisColR_img,1)
        eyeCloudR_img = pygame.image.load('images/ER_eye_clouding_r.png').convert_alpha()
        eyeCloudR_button = button.Button((eyeCloudR_img.get_width()/2) - (eyeCloudR_img.get_width()/3) + (77*4) + uiOffset,
                                    213+(60*109)+scrollWheel,eyeCloudR_img,1)
        cloudingColR_img = pygame.image.load('images/ER_clouding_col_r.png').convert_alpha()
        cloudingColR_button = button.Button((cloudingColR_img.get_width()/2) - (cloudingColR_img.get_width()/3) + (77*4) + uiOffset,
                                    213+(60*110)+scrollWheel,cloudingColR_img,1)
        eyeWhiteR_img = pygame.image.load('images/ER_eye_white_r.png').convert_alpha()
        eyeWhiteR_button = button.Button((eyeWhiteR_img.get_width()/2) - (eyeWhiteR_img.get_width()/3) + (77*4) + uiOffset,
                                    213+(60*111)+scrollWheel,eyeWhiteR_img,1)
        eyePosR_img = pygame.image.load('images/ER_eye_pos_r.png').convert_alpha()
        eyePosR_button = button.Button((eyePosR_img.get_width()/2) - (eyePosR_img.get_width()/3) + (77*4) + uiOffset,
                                    213+(60*112)+scrollWheel,eyePosR_img,1)
        irisSizeL_img = pygame.image.load('images/ER_iris_size_l.png').convert_alpha()
        irisSizeL_button = button.Button((irisSizeL_img.get_width()/2) - (irisSizeL_img.get_width()/3) + (77*4) + uiOffset,
                                    213+(60*113)+scrollWheel,irisSizeL_img,1)
        irisColL_img = pygame.image.load('images/ER_iris_col_l.png').convert_alpha()
        irisColL_button = button.Button((irisColL_img.get_width()/2) - (irisColL_img.get_width()/3) + (77*4) + uiOffset,
                                    213+(60*114)+scrollWheel,irisColL_img,1)
        eyeCloudL_img = pygame.image.load('images/ER_eye_clouding_l.png').convert_alpha()
        eyeCloudL_button = button.Button((eyeCloudL_img.get_width()/2) - (eyeCloudL_img.get_width()/3) + (77*4) + uiOffset,
                                    213+(60*115)+scrollWheel,eyeCloudL_img,1)
        cloudingColL_img = pygame.image.load('images/ER_clouding_col_l.png').convert_alpha()
        cloudingColL_button = button.Button((cloudingColL_img.get_width()/2) - (cloudingColL_img.get_width()/3) + (77*4) + uiOffset,
                                    213+(60*116)+scrollWheel,cloudingColL_img,1)
        eyeWhiteL_img = pygame.image.load('images/ER_eye_white_l.png').convert_alpha()
        eyeWhiteL_button = button.Button((eyeWhiteL_img.get_width()/2) - (eyeWhiteL_img.get_width()/3) + (77*4) + uiOffset,
                                    213+(60*117)+scrollWheel,eyeWhiteL_img,1)
        eyePosL_img = pygame.image.load('images/ER_eye_pos_l.png').convert_alpha()
        eyePosL_button = button.Button((eyePosL_img.get_width()/2) - (eyePosL_img.get_width()/3) + (77*4) + uiOffset,
                                    213+(60*118)+scrollWheel,eyePosL_img,1)
        
        #Skin Features
        skinFeatures_img = pygame.image.load('images/ER_skin_features.png').convert_alpha()
        skinFeatures_button = button.Button((skinFeatures_img.get_width()/2) - (skinFeatures_img.get_width()/3) + (77*3) + uiOffset,
                                    213+(60*119)+scrollWheel,skinFeatures_img,1)
        pores_img = pygame.image.load('images/ER_pores.png').convert_alpha()
        pores_button = button.Button((pores_img.get_width()/2) - (pores_img.get_width()/3) + (77*4) + uiOffset,
                                    213+(60*120)+scrollWheel,pores_img,1)
        skinLuster_img = pygame.image.load('images/ER_skin_luster.png').convert_alpha()
        skinLuster_button = button.Button((skinLuster_img.get_width()/2) - (skinLuster_img.get_width()/3) + (77*4) + uiOffset,
                                    213+(60*121)+scrollWheel,skinLuster_img,1)
        darkCircles_img = pygame.image.load('images/ER_dark_circles.png').convert_alpha()
        darkCircles_button = button.Button((darkCircles_img.get_width()/2) - (darkCircles_img.get_width()/3) + (77*4) + uiOffset,
                                    213+(60*122)+scrollWheel,darkCircles_img,1)
        darkCirclesCol_img = pygame.image.load('images/ER_dark_circles_col.png').convert_alpha()
        darkCirclesCol_button = button.Button((darkCirclesCol_img.get_width()/2) - (darkCirclesCol_img.get_width()/3) + (77*4) + uiOffset,
                                    213+(60*123)+scrollWheel,darkCirclesCol_img,1)
        
        #Cosmetics
        cosmetics_img = pygame.image.load('images/ER_cosmetics.png').convert_alpha()
        cosmetics_button = button.Button((cosmetics_img.get_width()/2) - (cosmetics_img.get_width()/3) + (77*3) + uiOffset,
                                    213+(60*124)+scrollWheel,cosmetics_img,1)
        eyeliner_img = pygame.image.load('images/ER_eyeliner.png').convert_alpha()
        eyeliner_button = button.Button((eyeliner_img.get_width()/2) - (eyeliner_img.get_width()/3) + (77*4) + uiOffset,
                                    213+(60*125)+scrollWheel,eyeliner_img,1)
        eyelinerCol_img = pygame.image.load('images/ER_eyeliner_col.png').convert_alpha()
        eyelinerCol_button = button.Button((eyelinerCol_img.get_width()/2) - (eyelinerCol_img.get_width()/3) + (77*4) + uiOffset,
                                    213+(60*126)+scrollWheel,eyelinerCol_img,1)
        eyeshadowUpper_img = pygame.image.load('images/ER_eyeshadow_upper.png').convert_alpha()
        eyeshadowUpper_button = button.Button((eyeshadowUpper_img.get_width()/2) - (eyeshadowUpper_img.get_width()/3) + (77*4) + uiOffset,
                                    213+(60*127)+scrollWheel,eyeshadowUpper_img,1)
        eyeShadowUpperCol_img = pygame.image.load('images/ER_eyeliner.png').convert_alpha()
        eyeShadowUpperCol_button = button.Button((eyeShadowUpperCol_img.get_width()/2) - (eyeShadowUpperCol_img.get_width()/3) + (77*4) + uiOffset,
                                    213+(60*128)+scrollWheel,eyeShadowUpperCol_img,1)
        eyeshadowLower_img = pygame.image.load('images/ER_eyeliner.png').convert_alpha()
        eyeshadowLower_button = button.Button((eyeshadowLower_img.get_width()/2) - (eyeshadowLower_img.get_width()/3) + (77*4) + uiOffset,
                                    213+(60*129)+scrollWheel,eyeshadowLower_img,1)
        eyeShadowLowerCol_img = pygame.image.load('images/ER_eyeliner.png').convert_alpha()
        eyeShadowLowerCol_button = button.Button((eyeShadowLowerCol_img.get_width()/2) - (eyeShadowLowerCol_img.get_width()/3) + (77*4) + uiOffset,
                                    213+(60*130)+scrollWheel,eyeShadowLowerCol_img,1)
        cosmeticsCheeks_img = pygame.image.load('images/ER__cheeks.png').convert_alpha()
        cosmeticsCheeks_button = button.Button((cosmeticsCheeks_img.get_width()/2) - (cosmeticsCheeks_img.get_width()/3) + (77*4) + uiOffset,
                                    213+(60*131)+scrollWheel,cosmeticsCheeks_img,1)
        cheeksCol_img = pygame.image.load('images/ER_cheeks_col.png').convert_alpha()
        cheeksCol_button = button.Button((cheeksCol_img.get_width()/2) - (cheeksCol_img.get_width()/3) + (77*4) + uiOffset,
                                    213+(60*132)+scrollWheel,cheeksCol_img,1)
        lipstick_img = pygame.image.load('images/ER_lipstick.png').convert_alpha()
        lipstick_button = button.Button((lipstick_img.get_width()/2) - (lipstick_img.get_width()/3) + (77*4) + uiOffset,
                                    213+(60*133)+scrollWheel,lipstick_img,1)
        lipstickCol_img = pygame.image.load('images/ER_eyeliner.png').convert_alpha()
        lipstickCol_button = button.Button((lipstickCol_img.get_width()/2) - (lipstickCol_img.get_width()/3) + (77*4) + uiOffset,
                                    213+(60*134)+scrollWheel,lipstickCol_img,1)
        
        #Randomizer Results Screen
        if randomize_button.draw(screen) == True or isRandButtonClicked == True:
            isRandButtonClicked = True
            screen.fill((24,21,15))
            screen.blit(randResults_grad, (((resolution[0]) - (randResults_grad.get_width())),
                                        ((resolution[1]) - (randResults_grad.get_height()))))
            origin_button.draw(screen)
            screen.blit(origin_results, 
                        (((origin_img.get_width())*(1-0.44326617179)) + (199) + (origin_w/2) + uiOffset,
                        213+(60*1)+(origin_h/2.5)+scrollWheel))
            
            bodytype_button.draw(screen)
            screen.blit(bodytype_results, 
                        (((bodytype_img.get_width())*(1-0.44326617179)) + (199) + (bodytype_w/2) + uiOffset,
                        213+(60*2)+(bodytype_h/2.5)+scrollWheel))
            
            keepsake_button.draw(screen)
            screen.blit(keepsake_results, 
                        (((keepsake_img.get_width())*(1-0.44326617179)) + (199) + (keepsake_w/2) + uiOffset,
                        213+(60*3)+(keepsake_h/2.5)+scrollWheel))
            
            detailed_appearance_button.draw(screen)

            age_button.draw(screen)
            screen.blit(age_results, 
                        (((age_img.get_width())*(1-0.44326617179)) + (77/(1-0.38693467336)) + (199) + (age_w/2) + uiOffset,
                        213+(60*6)+(age_h/2.5)+scrollWheel))
            
            voice_button.draw(screen)
            screen.blit(voice_results, 
                        (((voice_img.get_width())*(1-0.44326617179)) + (77/(1-0.38693467336)) + (199) + (voice_w/2) + uiOffset,
                        213+(60*7)+(voice_h/2.5)+scrollWheel))
            
            skinCol_x = 505 - 42 + 154 + (77/2) + 5 + (77/(1))
            skinCol_y = 401+40-(age_img.get_height()/2) + (60*5)
            skinCol_button.draw(screen)
            pygame.draw.rect(screen,attributes[5],(skinCol_x + uiOffset,skinCol_y+scrollWheel,380,31))

            # Adjust Face/Hair Section
            face_hair_button.draw(screen)

            ## Face Template Section
            facetemplate_button.draw(screen)

            bonestructure_button.draw(screen)
            screen.blit(bonestructure_results, 
                        (((bonestructure_img.get_width())*(1-0.44326617179)) + (77/(1-0.38693467336))*3 + (199) - (39*3) + uiOffset,
                        213+(60*11)+(bonestructure_h/2.5)+scrollWheel))
            
            formemphasis_button.draw(screen)
            screen.blit(formemphasis_results, 
                        (((formemphasis_img.get_width())*(1-0.44326617179)) + (77/(1-0.38693467336))*3 + (199) - (39*3) + uiOffset,
                        213+(60*12)+(formemphasis_h/2.5)+scrollWheel))
            
            apparent_age_button.draw(screen)
            screen.blit(apparent_age_results, 
                        (((apparent_age_img.get_width())*(1-0.44326617179)) + (77/(1-0.38693467336))*3 + (199) - (39*3) + uiOffset,
                        213+(60*13)+(apparent_age_h/2.5)+scrollWheel))
            
            facial_aesthetic_button.draw(screen)
            screen.blit(facial_aesthetic_results, 
                        (((facial_aesthetic_img.get_width())*(1-0.44326617179)) + (77/(1-0.38693467336))*3 + (199) - (39*3) + uiOffset,
                        213+(60*14)+(facial_aesthetic_h/2.5)+scrollWheel))
            
            ## Facial Structure Section
            facialstructure_button.draw(screen)

            facialbalance_button.draw(screen)

            nose_size_button.draw(screen)
            screen.blit(nose_size_results, 
                        (((nose_size_img.get_width())*(1-0.44326617179)) + (77/(1-0.38693467336))*4 + (199) - (39*3) + uiOffset,
                        213+(60*17)+(nose_size_h/2.5)+scrollWheel))
            nf_ratio_button.draw(screen)
            screen.blit(nf_ratio_results, 
                        (((nf_ratio_img.get_width())*(1-0.44326617179)) + (77/(1-0.38693467336))*4 + (199) - (39*3) + uiOffset,
                        213+(60*18)+(nf_ratio_h/2.5)+scrollWheel))
            face_prot_button.draw(screen)
            screen.blit(face_prot_results, 
                        (((face_prot_img.get_width())*(1-0.44326617179)) + (77/(1-0.38693467336))*4 + (199) - (39*3) + uiOffset,
                        213+(60*19)+(face_prot_h/2.5)+scrollWheel))
            vface_ratio_button.draw(screen)
            screen.blit(vface_ratio_results, 
                        (((vface_ratio_img.get_width())*(1-0.44326617179)) + (77/(1-0.38693467336))*4 + (199) - (39*3) + uiOffset,
                        213+(60*20)+(vface_ratio_h/2.5)+scrollWheel))
            faceSlant_button.draw(screen)
            screen.blit(faceSlant_results,
                        (((faceSlant_img.get_width())*(1-0.44326617179)) + (77/(1-0.38693467336))*4 + (199) - (39*3) + uiOffset,
                        213+(60*21)+(faceSlant_h/2.5)+scrollWheel))
            hFaceRatio_button.draw(screen)
            screen.blit(hFaceRatio_results,
                        (((hFaceRatio_img.get_width())*(1-0.44326617179)) + (77/(1-0.38693467336))*4 + (199) - (39*3) + uiOffset,
                        213+(60*22)+(hFaceRatio_h/2.5)+scrollWheel))
            
            ## Forehead/Glabella Section
            foreheadGlabella_button.draw(screen)

            foreheadDepth_button.draw(screen)
            screen.blit(foreheadDepth_results,
                        (((foreheadDepth_img.get_width())*(1-0.44326617179)) + (77/(1-0.38693467336))*4 + (199) - (39*3) + uiOffset,
                        213+(60*24)+(foreheadDepth_h/2.5)+scrollWheel))
            foreheadProt_button.draw(screen)
            screen.blit(foreheadProt_results,
                        (((foreheadProt_img.get_width())*(1-0.44326617179)) + (77/(1-0.38693467336))*4 + (199) - (39*3) + uiOffset,
                        213+(60*25)+(foreheadProt_h/2.5)+scrollWheel))
            noseBridgeH_button.draw(screen)
            screen.blit(noseBridgeH_results,
                        (((noseBridgeH_img.get_width())*(1-0.44326617179)) + (77/(1-0.38693467336))*4 + (199) - (39*3) + uiOffset,
                        213+(60*26)+(noseBridgeH_h/2.5)+scrollWheel))
            n_bridgeProt1_button.draw(screen)
            screen.blit(n_bridgeProt1_results,
                        (((n_bridgeProt1_img.get_width())*(1-0.44326617179)) + (77/(1-0.38693467336))*4 + (199) - (39*3) + uiOffset,
                        213+(60*27)+(n_bridgeProt1_h/2.5)+scrollWheel))
            n_bridgeProt2_button.draw(screen)
            screen.blit(n_bridgeProt2_results,
                        (((n_bridgeProt2_img.get_width())*(1-0.44326617179)) + (77/(1-0.38693467336))*4 + (199) - (39*3) + uiOffset,
                        213+(60*28)+(n_bridgeProt2_h/2.5)+scrollWheel))
            noseBridgeW_button.draw(screen)
            screen.blit(noseBridgeW_results,
                        (((noseBridgeW_img.get_width())*(1-0.44326617179)) + (77/(1-0.38693467336))*4 + (199) - (39*3) + uiOffset,
                        213+(60*29)+(noseBridgeW_h/2.5)+scrollWheel))
            
            ## Brow Ridge Section
            browRidge_button.draw(screen)

            browRidgeH_button.draw(screen)
            screen.blit(browRidgeH_results,
                        (((browRidgeH_img.get_width())*(1-0.44326617179)) + (77/(1-0.38693467336))*4 + (199) - (39*3) + uiOffset,
                        213+(60*31)+(browRidgeH_h/2.5)+scrollWheel))
            innerBrow_button.draw(screen)
            screen.blit(innerBrow_results,
                        (((innerBrow_img.get_width())*(1-0.44326617179)) + (77/(1-0.38693467336))*4 + (199) - (39*3) + uiOffset,
                        213+(60*32)+(innerBrow_h/2.5)+scrollWheel))
            outerBrow_button.draw(screen)
            screen.blit(outerBrow_results,
                        (((outerBrow_img.get_width())*(1-0.44326617179)) + (77/(1-0.38693467336))*4 + (199) - (39*3) + uiOffset,
                        213+(60*33)+(outerBrow_h/2.5)+scrollWheel))
            ## Eyes Section
            eyes_button.draw(screen)

            eyePos_button.draw(screen)
            screen.blit(eyePos_results,
                        (((eyePos_img.get_width())*(1-0.44326617179)) + (77/(1-0.38693467336))*4 + (199) - (39*3) + uiOffset,
                        213+(60*35)+(eyePos_h/2.5)+scrollWheel))
            eyeSize_button.draw(screen)
            screen.blit(eyeSize_results,
                        (((eyeSize_img.get_width())*(1-0.44326617179)) + (77/(1-0.38693467336))*4 + (199) - (39*3) + uiOffset,
                        213+(60*36)+(eyeSize_h/2.5)+scrollWheel))
            eyeSlant_button.draw(screen)
            screen.blit(eyeSlant_results,
                        (((eyeSlant_img.get_width())*(1-0.44326617179)) + (77/(1-0.38693467336))*4 + (199) - (39*3) + uiOffset,
                        213+(60*37)+(eyeSlant_h/2.5)+scrollWheel))
            eyeSpacing_button.draw(screen)
            screen.blit(eyeSpacing_results,
                        (((eyeSpacing_img.get_width())*(1-0.44326617179)) + (77/(1-0.38693467336))*4 + (199) - (39*3) + uiOffset,
                        213+(60*38)+(eyeSpacing_h/2.5)+scrollWheel))
            ## Nose Ridge Section
            noseRidge_button.draw(screen)

            noseRidgeDepth_button.draw(screen)
            screen.blit(noseRidgeDepth_results,
                        (((noseRidgeDepth_img.get_width())*(1-0.44326617179)) + (77/(1-0.38693467336))*4 + (199) - (39*3) + uiOffset,
                        213+(60*40)+(noseRidgeDepth_h/2.5)+scrollWheel))
            noseRidgeLen_button.draw(screen)
            screen.blit(noseRidgeLen_results,
                        (((noseRidgeLen_img.get_width())*(1-0.44326617179)) + (77/(1-0.38693467336))*4 + (199) - (39*3) + uiOffset,
                        213+(60*41)+(noseRidgeLen_h/2.5)+scrollWheel))
            nosePos_button.draw(screen)
            screen.blit(nosePos_results,
                        (((nosePos_img.get_width())*(1-0.44326617179)) + (77/(1-0.38693467336))*4 + (199) - (39*3) + uiOffset,
                        213+(60*42)+(nosePos_h/2.5)+scrollWheel))
            noseTipH_button.draw(screen)
            screen.blit(noseTipH_results,
                        (((noseTipH_img.get_width())*(1-0.44326617179)) + (77/(1-0.38693467336))*4 + (199) - (39*3) + uiOffset,
                        213+(60*43)+(noseTipH_h/2.5)+scrollWheel))
            noseProt_button.draw(screen)
            screen.blit(noseProt_results,
                        (((noseProt_img.get_width())*(1-0.44326617179)) + (77/(1-0.38693467336))*4 + (199) - (39*3) + uiOffset,
                        213+(60*44)+(noseProt_h/2.5)+scrollWheel))
            noseH_button.draw(screen)
            screen.blit(noseH_results,
                        (((noseH_img.get_width())*(1-0.44326617179)) + (77/(1-0.38693467336))*4 + (199) - (39*3) + uiOffset,
                        213+(60*45)+(noseH_h/2.5)+scrollWheel))
            noseSlant_button.draw(screen)
            screen.blit(noseSlant_results,
                        (((noseSlant_img.get_width())*(1-0.44326617179)) + (77/(1-0.38693467336))*4 + (199) - (39*3) + uiOffset,
                        213+(60*46)+(noseSlant_h/2.5)+scrollWheel))
            ## Nostrils Section
            nostrils_button.draw(screen)

            nostrilSlant_button.draw(screen)
            screen.blit(nostrilSlant_results,
                        (((nostrilSlant_img.get_width())*(1-0.44326617179)) + (77/(1-0.38693467336))*4 + (199) - (39*3) + uiOffset,
                        213+(60*48)+(nostrilSlant_h/2.5)+scrollWheel))
            nostrilSize_button.draw(screen)
            screen.blit(nostrilSize_results,
                        (((nostrilSize_img.get_width())*(1-0.44326617179)) + (77/(1-0.38693467336))*4 + (199) - (39*3) + uiOffset,
                        213+(60*49)+(nostrilSize_h/2.5)+scrollWheel))
            nostrilWidth_button.draw(screen)
            screen.blit(nostrilWidth_results,
                        (((nostrilWidth_img.get_width())*(1-0.44326617179)) + (77/(1-0.38693467336))*4 + (199) - (39*3) + uiOffset,
                        213+(60*50)+(nostrilWidth_h/2.5)+scrollWheel))
            ## Cheeks Section
            cheeks_button.draw(screen)

            cheekHeight_button.draw(screen)
            screen.blit(cheekHeight_results,
                        (((cheekHeight_img.get_width())*(1-0.44326617179)) + (77/(1-0.38693467336))*4 + (199) - (39*3) + uiOffset,
                        213+(60*52)+(cheekHeight_h/2.5)+scrollWheel))
            cheekDepth_button.draw(screen)
            screen.blit(cheekDepth_results,
                        (((cheekDepth_img.get_width())*(1-0.44326617179)) + (77/(1-0.38693467336))*4 + (199) - (39*3) + uiOffset,
                        213+(60*53)+(cheekDepth_h/2.5)+scrollWheel))
            cheekWidth_button.draw(screen)
            screen.blit(cheekWidth_results,
                        (((cheekWidth_img.get_width())*(1-0.44326617179)) + (77/(1-0.38693467336))*4 + (199) - (39*3) + uiOffset,
                        213+(60*54)+(cheekWidth_h/2.5)+scrollWheel))
            cheekProt_button.draw(screen)
            screen.blit(cheekProt_results,
                        (((cheekProt_img.get_width())*(1-0.44326617179)) + (77/(1-0.38693467336))*4 + (199) - (39*3) + uiOffset,
                        213+(60*55)+(cheekProt_h/2.5)+scrollWheel))
            _cheeks_button.draw(screen)
            screen.blit(_cheeks_results,
                        (((_cheeks_img.get_width())*(1-0.44326617179)) + (77/(1-0.38693467336))*4 + (199) - (39*3) + uiOffset,
                        213+(60*56)+(_cheeks_h/2.5)+scrollWheel))
            ## Lips Section
            lips_button.draw(screen)

            lipShape_button.draw(screen)
            screen.blit(lipShape_results,
                        (((lipShape_img.get_width())*(1-0.44326617179)) + (77/(1-0.38693467336))*4 + (199) - (39*3) + uiOffset,
                        213+(60*58)+(lipShape_h/2.5)+scrollWheel))
            mouthEx_button.draw(screen)
            screen.blit(mouthEx_results,
                        (((mouthEx_img.get_width())*(1-0.44326617179)) + (77/(1-0.38693467336))*4 + (199) - (39*3) + uiOffset,
                        213+(60*59)+(mouthEx_h/2.5)+scrollWheel))
            lipFull_button.draw(screen)
            screen.blit(lipFull_results,
                        (((lipFull_img.get_width())*(1-0.44326617179)) + (77/(1-0.38693467336))*4 + (199) - (39*3) + uiOffset,
                        213+(60*60)+(lipFull_h/2.5)+scrollWheel))
            lipSize_button.draw(screen)
            screen.blit(lipSize_results,
                        (((lipSize_img.get_width())*(1-0.44326617179)) + (77/(1-0.38693467336))*4 + (199) - (39*3) + uiOffset,
                        213+(60*61)+(lipSize_h/2.5)+scrollWheel))
            lipProt_button.draw(screen)
            screen.blit(lipProt_results,
                        (((lipProt_img.get_width())*(1-0.44326617179)) + (77/(1-0.38693467336))*4 + (199) - (39*3) + uiOffset,
                        213+(60*62)+(lipProt_h/2.5)+scrollWheel))
            lipThick_button.draw(screen)
            screen.blit(lipThick_results,
                        (((lipThick_img.get_width())*(1-0.44326617179)) + (77/(1-0.38693467336))*4 + (199) - (39*3) + uiOffset,
                        213+(60*63)+(lipThick_h/2.5)+scrollWheel))
            
            ## Mouth Section
            mouth_button.draw(screen)

            mouthProt_button.draw(screen)
            screen.blit(mouthProt_results,
                        (((mouthProt_img.get_width())*(1-0.44326617179)) + (77/(1-0.38693467336))*4 + (199) - (39*3) + uiOffset,
                        213+(60*65)+(mouthProt_h/2.5)+scrollWheel))
            mouthSlant_button.draw(screen)
            screen.blit(mouthSlant_results,
                        (((mouthSlant_img.get_width())*(1-0.44326617179)) + (77/(1-0.38693467336))*4 + (199) - (39*3) + uiOffset,
                        213+(60*66)+(mouthSlant_h/2.5)+scrollWheel))
            occlusion_button.draw(screen)
            screen.blit(occlusion_results,
                        (((occlusion_img.get_width())*(1-0.44326617179)) + (77/(1-0.38693467336))*4 + (199) - (39*3) + uiOffset,
                        213+(60*67)+(occlusion_h/2.5)+scrollWheel))
            mouthPos_button.draw(screen)
            screen.blit(mouthPos_results,
                        (((mouthPos_img.get_width())*(1-0.44326617179)) + (77/(1-0.38693467336))*4 + (199) - (39*3) + uiOffset,
                        213+(60*68)+(mouthPos_h/2.5)+scrollWheel))
            mouthWidth_button.draw(screen)
            screen.blit(mouthWidth_results,
                        (((mouthWidth_img.get_width())*(1-0.44326617179)) + (77/(1-0.38693467336))*4 + (199) - (39*3) + uiOffset,
                        213+(60*69)+(mouthWidth_h/2.5)+scrollWheel))
            mouthChinDist_button.draw(screen)
            screen.blit(mouthChinDist_results,
                        (((mouthChinDist_img.get_width())*(1-0.44326617179)) + (77/(1-0.38693467336))*4 + (199) - (39*3) + uiOffset,
                        213+(60*70)+(mouthChinDist_h/2.5)+scrollWheel))
            ## Chin Section
            chin_button.draw(screen)
            
            chinTipPos_button.draw(screen)
            screen.blit(chinTipPos_results,
                        (((chinTipPos_img.get_width())*(1-0.44326617179)) + (77/(1-0.38693467336))*4 + (199) - (39*3) + uiOffset,
                        213+(60*72)+(chinTipPos_h/2.5)+scrollWheel))
            chinLen_button.draw(screen)
            screen.blit(chinLen_results,
                        (((chinLen_img.get_width())*(1-0.44326617179)) + (77/(1-0.38693467336))*4 + (199) - (39*3) + uiOffset,
                        213+(60*73)+(chinLen_h/2.5)+scrollWheel))
            chinProt_button.draw(screen)
            screen.blit(chinProt_results,
                        (((chinProt_img.get_width())*(1-0.44326617179)) + (77/(1-0.38693467336))*4 + (199) - (39*3) + uiOffset,
                        213+(60*74)+(chinProt_h/2.5)+scrollWheel))
            chinDepth_button.draw(screen)
            screen.blit(chinDepth_results,
                        (((chinDepth_img.get_width())*(1-0.44326617179)) + (77/(1-0.38693467336))*4 + (199) - (39*3) + uiOffset,
                        213+(60*75)+(chinDepth_h/2.5)+scrollWheel))
            chinSize_button.draw(screen)
            screen.blit(chinSize_results,
                        (((chinSize_img.get_width())*(1-0.44326617179)) + (77/(1-0.38693467336))*4 + (199) - (39*3) + uiOffset,
                        213+(60*76)+(chinSize_h/2.5)+scrollWheel))
            chinHeight_button.draw(screen)
            screen.blit(chinHeight_results,
                        (((chinHeight_img.get_width())*(1-0.44326617179)) + (77/(1-0.38693467336))*4 + (199) - (39*3) + uiOffset,
                        213+(60*77)+(chinHeight_h/2.5)+scrollWheel))
            chinWidth_button.draw(screen)
            screen.blit(chinWidth_results,
                        (((chinWidth_img.get_width())*(1-0.44326617179)) + (77/(1-0.38693467336))*4 + (199) - (39*3) + uiOffset,
                        213+(60*78)+(chinWidth_h/2.5)+scrollWheel))
            ## Jaw Section
            jaw_button.draw(screen)

            jawProt_button.draw(screen)
            screen.blit(jawProt_results,
                        (((jawProt_img.get_width())*(1-0.44326617179)) + (77/(1-0.38693467336))*4 + (199) - (39*3) + uiOffset,
                        213+(60*80)+(jawProt_h/2.5)+scrollWheel))
            jawWidth_button.draw(screen)
            screen.blit(jawWidth_results,
                        (((jawWidth_img.get_width())*(1-0.44326617179)) + (77/(1-0.38693467336))*4 + (199) - (39*3) + uiOffset,
                        213+(60*81)+(jawWidth_h/2.5)+scrollWheel))
            lowerJaw_button.draw(screen)
            screen.blit(lowerJaw_results,
                        (((lowerJaw_img.get_width())*(1-0.44326617179)) + (77/(1-0.38693467336))*4 + (199) - (39*3) + uiOffset,
                        213+(60*82)+(lowerJaw_h/2.5)+scrollWheel))
            jawContour_button.draw(screen)
            screen.blit(jawContour_results,
                        (((jawContour_img.get_width())*(1-0.44326617179)) + (77/(1-0.38693467336))*4 + (199) - (39*3) + uiOffset,
                        213+(60*83)+(jawContour_h/2.5)+scrollWheel))

            ## Hair Section
            hair_button.draw(screen)

            hairstyle_button.draw(screen)
            screen.blit(hairstyle_results,
                        (((hairstyle_img.get_width())*(1-0.44326617179)) + (77/(1-0.38693467336))*4 + (199) - (39*3) + uiOffset,
                        213+(60*85)+(hairstyle_h/2.5)+scrollWheel))

            hairCol_x = 505 - 42 + 154 + (77/2) + 5 + (77/(1))*3
            hairCol_y = 401+40-(hairCol_img.get_height()/2) + (60*83)
            hairCol_button.draw(screen)
            pygame.draw.rect(screen,attributes[8][1],(hairCol_x + uiOffset,hairCol_y+scrollWheel,380,31))
            hairLuster_button.draw(screen)
            screen.blit(hairLuster_results,
                        (((hairLuster_img.get_width())*(1-0.44326617179)) + (77/(1-0.38693467336))*4 + (199) - (39*3) + uiOffset,
                        213+(60*87)+(hairLuster_h/2.5)+scrollWheel))
            hairRootDark_button.draw(screen)
            screen.blit(hairRootDark_results,
                        (((hairRootDark_img.get_width())*(1-0.44326617179)) + (77/(1-0.38693467336))*4 + (199) - (39*3) + uiOffset,
                        213+(60*88)+(hairRootDark_h/2.5)+scrollWheel))
            hairWhite_button.draw(screen)
            screen.blit(hairWhite_results,
                        (((hairWhite_img.get_width())*(1-0.44326617179)) + (77/(1-0.38693467336))*4 + (199) - (39*3) + uiOffset,
                        213+(60*89)+(hairWhite_h/2.5)+scrollWheel))
            
            ## Eyebrow Section
            eyebrow_button.draw(screen)

            brow_button.draw(screen)
            screen.blit(brow_results,
                        (((brow_img.get_width())*(1-0.44326617179)) + (77/(1-0.38693467336))*4 + (199) - (39*3) + uiOffset,
                        213+(60*91)+(brow_h/2.5)+scrollWheel))

            browCol_x = 505 - 42 + 154 + (77/2) + 5 + (77/(1))*3
            browCol_y = 401+40-(hairCol_img.get_height()/2) + (60*89)
            browCol_button.draw(screen)
            pygame.draw.rect(screen,attributes[9][1],(browCol_x + uiOffset,browCol_y+scrollWheel,380,31))
            browLuster_button.draw(screen)
            screen.blit(browLuster_results,
                        (((browLuster_img.get_width())*(1-0.44326617179)) + (77/(1-0.38693467336))*4 + (199) - (39*3) + uiOffset,
                        213+(60*93)+(browLuster_h/2.5)+scrollWheel))
            browRootDark_button.draw(screen)
            screen.blit(browRootDark_results,
                        (((browRootDark_img.get_width())*(1-0.44326617179)) + (77/(1-0.38693467336))*4 + (199) - (39*3) + uiOffset,
                        213+(60*94)+(browRootDark_h/2.5)+scrollWheel))
            browWhiteHairs_button.draw(screen)
            screen.blit(browWhiteHairs_results,
                        (((browWhiteHairs_img.get_width())*(1-0.44326617179)) + (77/(1-0.38693467336))*4 + (199) - (39*3) + uiOffset,
                        213+(60*95)+(browWhiteHairs_h/2.5)+scrollWheel))
            
            #Facial Hair
            facialHair_button.draw(screen)

            beard_button.draw(screen)
            screen.blit(beard_results,
                        (((beard_img.get_width())*(1-0.44326617179)) + (77/(1-0.38693467336))*4 + (199) - (39*3) + uiOffset,
                        213+(60*97)+(beard_h/2.5)+scrollWheel))
            facialHairCol_x = 505 - 42 + 154 + (77/2) + 5 + (77/(1))*3
            facialHairCol_y = 401+40-(facialHairCol_img.get_height()/2) + (60*95)
            facialHairCol_button.draw(screen)
            pygame.draw.rect(screen,attributes[10][1],(facialHairCol_x + uiOffset,facialHairCol_y+scrollWheel,380,31))
            facialHairLuster_button.draw(screen)
            screen.blit(facialHairLuster_results,
                        (((facialHairLuster_img.get_width())*(1-0.44326617179)) + (77/(1-0.38693467336))*4 + (199) - (39*3) + uiOffset,
                        213+(60*99)+(facialHairLuster_h/2.5)+scrollWheel))
            facialHairRootDark_button.draw(screen)
            screen.blit(facialHairRootDark_results,
                        (((facialHairRootDark_img.get_width())*(1-0.44326617179)) + (77/(1-0.38693467336))*4 + (199) - (39*3) + uiOffset,
                        213+(60*100)+(facialHairRootDark_h/2.5)+scrollWheel))
            facialHairWhiteHairs_button.draw(screen)
            screen.blit(facialHairWhiteHairs_results,
                        (((facialHairWhiteHairs_img.get_width())*(1-0.44326617179)) + (77/(1-0.38693467336))*4 + (199) - (39*3) + uiOffset,
                        213+(60*101)+(facialHairWhiteHairs_h/2.5)+scrollWheel))
            facialHairStubble_button.draw(screen)
            screen.blit(facialHairStubble_results,
                        (((facialHairStubble_img.get_width())*(1-0.44326617179)) + (77/(1-0.38693467336))*4 + (199) - (39*3) + uiOffset,
                        213+(60*102)+(facialHairStubble_h/2.5)+scrollWheel))
            
            #Eyelashes
            eyelash_button.draw(screen)
            eyelash__button.draw(screen)
            screen.blit(eyelash_results,
                        (((eyelash__img.get_width())*(1-0.44326617179)) + (77/(1-0.38693467336))*4 + (199) - (39*3) + uiOffset,
                        213+(60*104)+(eyelash_h/2.5)+scrollWheel))
            eyelashCol_x = 505 - 42 + 154 + (77/2) + 5 + (77/(1))*3
            eyelashCol_y = 401+40-(facialHairCol_img.get_height()/2) + (60*102)
            eyelashCol_button.draw(screen)
            pygame.draw.rect(screen,attributes[11][1],(eyelashCol_x + uiOffset,eyelashCol_y+scrollWheel,380,31))

            eyesCol_button.draw(screen)

            #Eye R
            irisSizeR_button.draw(screen)
            screen.blit(irisSizeR_results,
                        (((irisSizeR_img.get_width())*(1-0.44326617179)) + (77/(1-0.38693467336))*4 + (199) - (39*3) + uiOffset,
                        213+(60*107)+(irisSizeR_h/2.5)+scrollWheel))
            irisColR_x = 505 - 42 + 154 + (77/2) + 5 + (77/(1))*3
            irisColR_y = 401+40-(irisColR_img.get_height()/2) + (60*105)
            irisColR_button.draw(screen)
            pygame.draw.rect(screen,attributes[12][1],(irisColR_x + uiOffset,irisColR_y+scrollWheel,380,31))
            eyeCloudR_button.draw(screen)
            screen.blit(eyeCloudR_results,
                        (((irisSizeR_img.get_width())*(1-0.44326617179)) + (77/(1-0.38693467336))*4 + (199) - (39*3) + uiOffset,
                        213+(60*109)+(eyeCloudR_h/2.5)+scrollWheel))
            cloudingColR_x = 505 - 42 + 154 + (77/2) + 5 + (77/(1))*3
            cloudingColR_y = 401+40-(cloudingColR_img.get_height()/2) + (60*107)
            cloudingColR_button.draw(screen)
            pygame.draw.rect(screen,attributes[12][3],(cloudingColR_x + uiOffset,cloudingColR_y+scrollWheel,380,31))
            eyeWhiteR_x = 505 - 42 + 154 + (77/2) + 5 + (77/(1))*3
            eyeWhiteR_y = 401+40-(cloudingColR_img.get_height()/2) + (60*108)
            eyeWhiteR_button.draw(screen)
            pygame.draw.rect(screen,attributes[12][4],(eyeWhiteR_x + uiOffset,eyeWhiteR_y+scrollWheel,380,31))
            eyePosR_button.draw(screen)
            screen.blit(eyePosR_results,
                        (((eyePosR_img.get_width())*(1-0.44326617179)) + (77/(1-0.38693467336))*4 + (199) - (39*3) + uiOffset,
                        213+(60*112)+(eyePosR_h/2.5)+scrollWheel))
            #Eye L
            irisSizeL_button.draw(screen)
            screen.blit(irisSizeL_results,
                        (((irisSizeL_img.get_width())*(1-0.44326617179)) + (77/(1-0.38693467336))*4 + (199) - (39*3) + uiOffset,
                        213+(60*113)+(irisSizeL_h/2.5)+scrollWheel))
            irisColL_x = 505 - 42 + 154 + (77/2) + 5 + (77/(1))*3
            irisColL_y = 401+40-(irisColL_img.get_height()/2) + (60*111)
            irisColL_button.draw(screen)
            pygame.draw.rect(screen,attributes[12][7],(irisColL_x + uiOffset,irisColL_y+scrollWheel,380,31))
            eyeCloudL_button.draw(screen)
            screen.blit(eyeCloudL_results,
                        (((irisSizeL_img.get_width())*(1-0.44326617179)) + (77/(1-0.38693467336))*4 + (199) - (39*3) + uiOffset,
                        213+(60*115)+(eyeCloudL_h/2.5)+scrollWheel))
            cloudingColL_x = 505 - 42 + 154 + (77/2) + 5 + (77/(1))*3
            cloudingColL_y = 401+40-(cloudingColL_img.get_height()/2) + (60*113)
            cloudingColL_button.draw(screen)
            pygame.draw.rect(screen,attributes[12][9],(cloudingColL_x + uiOffset,cloudingColL_y+scrollWheel,380,31))
            eyeWhiteL_x = 505 - 42 + 154 + (77/2) + 5 + (77/(1))*3
            eyeWhiteL_y = 401+40-(cloudingColR_img.get_height()/2) + (60*114)
            eyeWhiteL_button.draw(screen)
            pygame.draw.rect(screen,attributes[12][10],(eyeWhiteL_x + uiOffset,eyeWhiteL_y+scrollWheel,380,31))
            eyePosL_button.draw(screen)
            screen.blit(eyePosL_results,
                        (((eyePosL_img.get_width())*(1-0.44326617179)) + (77/(1-0.38693467336))*4 + (199) - (39*3) + uiOffset,
                        213+(60*118)+(eyePosL_h/2.5)+scrollWheel))
            
            #Skin Features
            skinFeatures_button.draw(screen)
            pores_button.draw(screen)
            screen.blit(pores_results,
                        (((pores_img.get_width())*(1-0.44326617179)) + (77/(1-0.38693467336))*4 + (199) - (39*3) + uiOffset,
                        213+(60*120)+(pores_h/2.5)+scrollWheel))
            skinLuster_button.draw(screen)
            screen.blit(skinLuster_results,
                        (((skinLuster_img.get_width())*(1-0.44326617179)) + (77/(1-0.38693467336))*4 + (199) - (39*3) + uiOffset,
                        213+(60*121)+(skinLuster_h/2.5)+scrollWheel))
            darkCircles_button.draw(screen)
            screen.blit(darkCircles_results,
                        (((darkCircles_img.get_width())*(1-0.44326617179)) + (77/(1-0.38693467336))*4 + (199) - (39*3) + uiOffset,
                        213+(60*122)+(darkCircles_h/2.5)+scrollWheel))
            darkCircCol_x = 505 - 42 + 154 + (77/2) + 5 + (77/(1))*3
            darkCircCol_y = 401+40-(darkCirclesCol_img.get_height()/2) + (60*120)
            darkCirclesCol_button.draw(screen)
            pygame.draw.rect(screen,attributes[13][3],(darkCircCol_x + uiOffset,darkCircCol_y+scrollWheel,380,31))

            #Cosmetics
            cosmetics_button.draw(screen)
            eyeliner_button.draw(screen)
            screen.blit(eyeliner_results,
                        (((eyeliner_img.get_width())*(1-0.44326617179)) + (77/(1-0.38693467336))*4 + (199) - (39*3) + uiOffset,
                        213+(60*125)+(eyeliner_h/2.5)+scrollWheel))
            eyelinerCol_x = 505 - 42 + 154 + (77/2) + 5 + (77/(1))*3
            eyelinerCol_y = 401+40-(darkCirclesCol_img.get_height()/2) + (60*(126-3))
            eyelinerCol_button.draw(screen)
            pygame.draw.rect(screen,attributes[14][1],(eyelinerCol_x + uiOffset,eyelinerCol_y+scrollWheel,380,31))
            eyeshadowUpper_button.draw(screen)
            screen.blit(eyeshadowUpper_results,
                        (((eyeshadowUpper_img.get_width())*(1-0.44326617179)) + (77/(1-0.38693467336))*4 + (199) - (39*3) + uiOffset,
                        213+(60*127)+(eyeShadowUpper_h/2.5)+scrollWheel))
            eyeshadowUpperCol_x = 505 - 42 + 154 + (77/2) + 5 + (77/(1))*3
            eyeshadowUpperCol_y = 401+40-(eyeShadowUpperCol_img.get_height()/2) + (60*(128-3))
            eyeShadowUpperCol_button.draw(screen)
            pygame.draw.rect(screen,attributes[14][3],(eyeshadowUpperCol_x + uiOffset,eyeshadowUpperCol_y+scrollWheel,380,31))
            eyeshadowLower_button.draw(screen)
            screen.blit(eyeShadowLower_results,
                        (((eyeshadowLower_img.get_width())*(1-0.44326617179)) + (77/(1-0.38693467336))*4 + (199) - (39*3) + uiOffset,
                        213+(60*129)+(eyeShadowLower_h/2.5)+scrollWheel))
            eyeshadowLowerCol_x = 505 - 42 + 154 + (77/2) + 5 + (77/(1))*3
            eyeshadowLowerCol_y = 401+40-(eyeShadowUpperCol_img.get_height()/2) + (60*(130-3))
            eyeShadowLowerCol_button.draw(screen)
            pygame.draw.rect(screen,attributes[14][5],(eyeshadowLowerCol_x + uiOffset,eyeshadowLowerCol_y+scrollWheel,380,31))
            cosmeticsCheeks_button.draw(screen)
            screen.blit(cosmeticsCheeks_results,
                        (((cosmeticsCheeks_img.get_width())*(1-0.44326617179)) + (77/(1-0.38693467336))*4 + (199) - (39*3) + uiOffset,
                        213+(60*131)+(cosmeticsCheeks_h/2.5)+scrollWheel))
            cheeksCol_x = 505 - 42 + 154 + (77/2) + 5 + (77/(1))*3
            cheeksCol_y = 401+40-(cheeksCol_img.get_height()/2) + (60*(132-3))
            cheeksCol_button.draw(screen)
            pygame.draw.rect(screen,attributes[14][7],(cheeksCol_x + uiOffset,cheeksCol_y+scrollWheel,380,31))
            lipstick_button.draw(screen)
            screen.blit(lipstick_results,
                        (((lipstick_img.get_width())*(1-0.44326617179)) + (77/(1-0.38693467336))*4 + (199) - (39*3) + uiOffset,
                        213+(60*132)+(lipstick_h/2.5)+scrollWheel))
            lipstickCol_x = 505 - 42 + 154 + (77/2) + 5 + (77/(1))*3
            lipstickCol_y = 401+40-(lipstickCol_img.get_height()/2) + (60*(133-3))
            lipstickCol_button.draw(screen)
            pygame.draw.rect(screen,attributes[14][9],(lipstickCol_x + uiOffset,lipstickCol_y+scrollWheel,380,31))


            
            # Randomizer Screen Title Overlay
            screen.blit(randResults_grad_title, (((resolution[0]) - (randResults_grad.get_width())),
                                        ((resolution[1]) - (randResults_grad_title.get_height()))))
        #Title Screen
        elif randomize_button.draw(screen) == False and detailed_appearance_button.draw(screen) == False:
            screen.fill((0,0,0))
            #Background and Title
            bg_image.set_alpha(50)
            screen.blit(bg_image, (((resolution[0]/2) - (bg_image.get_width()/2)),((resolution[1]/2) - (bg_image.get_height()/2))))
            #screen.blit(bg_image, (0,0))
            
            screen.blit(title_img, (titlePos))

            # Randomizer text under title
            title_text = title_font.render("Attribute Randomizer", True, (228, 190, 125))
            titleRand_w, titleRand_h = title_text.get_width(), title_text.get_height()
            #titleRand_shadow = pygame.transform.scale(textShadow, ((titleRand_w*2), titleRand_h*1.5))

            #screen.blit(titleRand_shadow, ((resolution[0]/2) - (titleRand_shadow.get_width())/2, titlePos[1] + (titleRand_h*1.25)))

            screen.blit(title_text, ((resolution[0]/2) - titleRand_w/2, titlePos[1] + (titleRand_h*1.5)))
            randomize_button.draw(screen)

            #randomize_button.draw(((resolution[0]/2) - (randomize_img.get_width()/2)), ((resolution[1]/2) - (randomize_img.get_height()/2)))

        # Event Handler
        for event in pygame.event.get():
            # Quit Game
            if event.type == pygame.QUIT: #or (event.type == KEYDOWN and pygame.key.get_pressed(K_q))
                running = False
            if event.type == pygame.KEYDOWN and pygame.key.get_pressed()[pygame.K_q]:
                isRandButtonClicked = False
            if event.type == pygame.MOUSEWHEEL:
                scrollWheel += (event.y)*25

        pygame.display.update()

        # flip() to display everything on screen
        #pygame.display.flip


        clock.tick(60)
    
    pygame.quit()

if __name__ == "__main__":
    main()