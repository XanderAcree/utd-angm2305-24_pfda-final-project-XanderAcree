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
def main():
    # Game loop
    running = True
    clock = pygame.time.Clock()
    attributes = EldenRandom.EldenRandom.returnAll()

    origin_results = button_font.render(attributes[0], True, (200,200,198))
    origin_w, origin_h = button_font.size(attributes[0])

    bodytype_results = button_font.render(attributes[1], True, (200,200,198))
    bodytype_w, bodytype_h = button_font.size(attributes[1])

    keepsake_results = button_font.render(attributes[2], True, (200,200,198))
    keepsake_w, keepsake_h = button_font.size(attributes[2])

    age_results = button_font.render(attributes[3], True, (200,200,198))
    age_w, age_h = button_font.size(attributes[3])

    voice_results = button_font.render(attributes[4], True, (200,200,198))
    voice_w, voice_h = button_font.size(attributes[4])

    bonestructure_results = button_font.render(str(attributes[6][0]), True, (200,200,198))
    bonestructure_w, bonestructure_h = button_font.size(str(attributes[6][0]))

    formemphasis_results = button_font.render(str(attributes[6][1]), True, (200,200,198))
    formemphasis_w, formemphasis_h = button_font.size(str(attributes[6][1]))

    apparent_age_results = button_font.render(str(attributes[6][2]), True, (200,200,198))
    apparent_age_w, apparent_age_h = button_font.size(str(attributes[6][2]))

    facial_aesthetic_results = button_font.render(str(attributes[6][3]), True, (200,200,198))
    facial_aesthetic_w, facial_aesthetic_h = button_font.size(str(attributes[6][3]))

    nose_size_results = button_font.render(str(attributes[7][0][0]), True, (200,200,198))
    nose_size_w, nose_size_h = button_font.size(str(attributes[7][0][0]))

    nf_ratio_results = button_font.render(str(attributes[7][0][1]), True, (200,200,198))
    nf_ratio_w, nf_ratio_h = button_font.size(str(attributes[7][0][1]))

    face_prot_results = button_font.render(str(attributes[7][0][2]), True, (200,200,198))
    face_prot_w, face_prot_h = button_font.size(str(attributes[7][0][2]))

    vface_ratio_results = button_font.render(str(attributes[7][0][3]), True, (200,200,198))
    vface_ratio_w, vface_ratio_h = button_font.size(str(attributes[7][0][3]))

    faceSlant_results = button_font.render(str(attributes[7][0][4]), True, (200,200,198))
    faceSlant_w, faceSlant_h = button_font.size(str(attributes[7][0][4]))

    hFaceRatio_results = button_font.render(str(attributes[7][0][5]), True, (200,200,198))
    hFaceRatio_w, hFaceRatio_h = button_font.size(str(attributes[7][0][5]))

    foreheadDepth_results = button_font.render(str(attributes[7][1][0]), True, (200,200,198))
    foreheadDepth_w, foreheadDepth_h = button_font.size(str(attributes[7][1][0]))

    foreheadProt_results = button_font.render(str(attributes[7][1][1]), True, (200,200,198))
    foreheadProt_w, foreheadProt_h = button_font.size(str(attributes[7][1][1]))

    noseBridgeH_results = button_font.render(str(attributes[7][1][2]), True, (200,200,198))
    noseBridgeH_w, noseBridgeH_h = button_font.size(str(attributes[7][1][2]))

    n_bridgeProt1_results = button_font.render(str(attributes[7][1][3]), True, (200,200,198))
    n_bridgeProt1_w, n_bridgeProt1_h = button_font.size(str(attributes[7][1][3]))

    n_bridgeProt2_results = button_font.render(str(attributes[7][1][4]), True, (200,200,198))
    n_bridgeProt2_w, n_bridgeProt2_h = button_font.size(str(attributes[7][1][4]))

    noseBridgeW_results = button_font.render(str(attributes[7][1][5]), True, (200,200,198))
    noseBridgeW_w, noseBridgeW_h = button_font.size(str(attributes[7][1][5]))

    browRidgeH_results = button_font.render(str(attributes[7][2][0]), True, (200,200,198))
    browRidgeH_w, browRidgeH_h = button_font.size(str(attributes[7][2][0]))

    innerBrow_results = button_font.render(str(attributes[7][2][1]), True, (200,200,198))
    innerBrow_w, innerBrow_h = button_font.size(str(attributes[7][2][1]))

    outerBrow_results = button_font.render(str(attributes[7][2][2]), True, (200,200,198))
    outerBrow_w, outerBrow_h = button_font.size(str(attributes[7][2][2]))

    eyePos_results = button_font.render(str(attributes[7][3][0]), True, (200,200,198))
    eyePos_w, eyePos_h = button_font.size(str(attributes[7][3][0]))

    eyeSize_results = button_font.render(str(attributes[7][3][1]), True, (200,200,198))
    eyeSize_w, eyeSize_h = button_font.size(str(attributes[7][3][1]))

    eyeSlant_results = button_font.render(str(attributes[7][3][2]), True, (200,200,198))
    eyeSlant_w, eyeSlant_h = button_font.size(str(attributes[7][3][2]))

    eyeSpacing_results = button_font.render(str(attributes[7][3][3]), True, (200,200,198))
    eyeSpacing_w, eyeSpacing_h = button_font.size(str(attributes[7][3][3]))

    #skinCol = pygame.draw.rect(screen,attributes[5],(505,401,398,31))

    titlePos = ((resolution[0]/2) - (title_img.get_width()/2), 0 + (title_img.get_height()/4))
    isRandButtonClicked = False
    scrollWheel = 0
    uiOffset = -(77*2)
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
        
        nostrils_img = pygame.image.load('images/ER_nostrils.png').convert_alpha()
        nostrils_button = button.Button((nostrils_img.get_width()/2) - (nostrils_img.get_width()/3) + (77*3) + uiOffset,
                                    213+(60*47)+scrollWheel,nostrils_img,1)
        
        cheeks_img = pygame.image.load('images/ER_cheeks.png').convert_alpha()
        cheeks_button = button.Button((cheeks_img.get_width()/2) - (cheeks_img.get_width()/3) + (77*3) + uiOffset,
                                    213+(60*51)+scrollWheel,cheeks_img,1)
        
        lips_img = pygame.image.load('images/ER_lips.png').convert_alpha()
        lips_button = button.Button((lips_img.get_width()/2) - (lips_img.get_width()/3) + (77*3) + uiOffset,
                                    213+(60*57)+scrollWheel,lips_img,1)
        
        mouth_img = pygame.image.load('images/ER_mouth.png').convert_alpha()
        mouth_button = button.Button((mouth_img.get_width()/2) - (mouth_img.get_width()/3) + (77*3) + uiOffset,
                                    213+(60*64)+scrollWheel,mouth_img,1)
        
        chin_img = pygame.image.load('images/ER_chin.png').convert_alpha()
        chin_button = button.Button((chin_img.get_width()/2) - (chin_img.get_width()/3) + (77*3) + uiOffset,
                                    213+(60*71)+scrollWheel,chin_img,1)
        
        jaw_img = pygame.image.load('images/ER_jaw.png').convert_alpha()
        jaw_button = button.Button((jaw_img.get_width()/2) - (jaw_img.get_width()/3) + (77*3) + uiOffset,
                                    213+(60*79)+scrollWheel,jaw_img,1)
        
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
                        (((bonestructure_img.get_width())*(1-0.44326617179)) + (77/(1-0.38693467336))*3 + (199) - (bonestructure_w*3) + uiOffset,
                        213+(60*11)+(bonestructure_h/2.5)+scrollWheel))
            
            formemphasis_button.draw(screen)
            screen.blit(formemphasis_results, 
                        (((formemphasis_img.get_width())*(1-0.44326617179)) + (77/(1-0.38693467336))*3 + (199) - (formemphasis_w*3) + uiOffset,
                        213+(60*12)+(formemphasis_h/2.5)+scrollWheel))
            
            apparent_age_button.draw(screen)
            screen.blit(apparent_age_results, 
                        (((apparent_age_img.get_width())*(1-0.44326617179)) + (77/(1-0.38693467336))*3 + (199) - (apparent_age_w*3) + uiOffset,
                        213+(60*13)+(apparent_age_h/2.5)+scrollWheel))
            
            facial_aesthetic_button.draw(screen)
            screen.blit(facial_aesthetic_results, 
                        (((facial_aesthetic_img.get_width())*(1-0.44326617179)) + (77/(1-0.38693467336))*3 + (199) - (facial_aesthetic_w*3) + uiOffset,
                        213+(60*14)+(facial_aesthetic_h/2.5)+scrollWheel))
            
            ## Facial Structure Section
            facialstructure_button.draw(screen)

            facialbalance_button.draw(screen)

            nose_size_button.draw(screen)
            screen.blit(nose_size_results, 
                        (((nose_size_img.get_width())*(1-0.44326617179)) + (77/(1-0.38693467336))*4 + (199) - (nose_size_w*3) + uiOffset,
                        213+(60*17)+(nose_size_h/2.5)+scrollWheel))
            nf_ratio_button.draw(screen)
            screen.blit(nf_ratio_results, 
                        (((nf_ratio_img.get_width())*(1-0.44326617179)) + (77/(1-0.38693467336))*4 + (199) - (nf_ratio_w*3) + uiOffset,
                        213+(60*18)+(nf_ratio_h/2.5)+scrollWheel))
            face_prot_button.draw(screen)
            screen.blit(face_prot_results, 
                        (((face_prot_img.get_width())*(1-0.44326617179)) + (77/(1-0.38693467336))*4 + (199) - (face_prot_w*3) + uiOffset,
                        213+(60*19)+(face_prot_h/2.5)+scrollWheel))
            vface_ratio_button.draw(screen)
            screen.blit(vface_ratio_results, 
                        (((vface_ratio_img.get_width())*(1-0.44326617179)) + (77/(1-0.38693467336))*4 + (199) - (vface_ratio_w*3) + uiOffset,
                        213+(60*20)+(vface_ratio_h/2.5)+scrollWheel))
            faceSlant_button.draw(screen)
            screen.blit(faceSlant_results,
                        (((faceSlant_img.get_width())*(1-0.44326617179)) + (77/(1-0.38693467336))*4 + (199) - (faceSlant_w*3) + uiOffset,
                        213+(60*21)+(faceSlant_h/2.5)+scrollWheel))
            hFaceRatio_button.draw(screen)
            screen.blit(hFaceRatio_results,
                        (((hFaceRatio_img.get_width())*(1-0.44326617179)) + (77/(1-0.38693467336))*4 + (199) - (hFaceRatio_w*3) + uiOffset,
                        213+(60*22)+(hFaceRatio_h/2.5)+scrollWheel))
            
            ## Forehead/Glabella Section
            foreheadGlabella_button.draw(screen)

            foreheadDepth_button.draw(screen)
            screen.blit(foreheadDepth_results,
                        (((foreheadDepth_img.get_width())*(1-0.44326617179)) + (77/(1-0.38693467336))*4 + (199) - (foreheadDepth_w*3) + uiOffset,
                        213+(60*24)+(foreheadDepth_h/2.5)+scrollWheel))
            foreheadProt_button.draw(screen)
            screen.blit(foreheadProt_results,
                        (((foreheadProt_img.get_width())*(1-0.44326617179)) + (77/(1-0.38693467336))*4 + (199) - (foreheadProt_w*3) + uiOffset,
                        213+(60*25)+(foreheadProt_h/2.5)+scrollWheel))
            noseBridgeH_button.draw(screen)
            screen.blit(noseBridgeH_results,
                        (((noseBridgeH_img.get_width())*(1-0.44326617179)) + (77/(1-0.38693467336))*4 + (199) - (noseBridgeH_w*3) + uiOffset,
                        213+(60*26)+(noseBridgeH_h/2.5)+scrollWheel))
            n_bridgeProt1_button.draw(screen)
            screen.blit(n_bridgeProt1_results,
                        (((n_bridgeProt1_img.get_width())*(1-0.44326617179)) + (77/(1-0.38693467336))*4 + (199) - (n_bridgeProt1_w*3) + uiOffset,
                        213+(60*27)+(n_bridgeProt1_h/2.5)+scrollWheel))
            n_bridgeProt2_button.draw(screen)
            screen.blit(n_bridgeProt2_results,
                        (((n_bridgeProt2_img.get_width())*(1-0.44326617179)) + (77/(1-0.38693467336))*4 + (199) - (n_bridgeProt2_w*3) + uiOffset,
                        213+(60*28)+(n_bridgeProt2_h/2.5)+scrollWheel))
            noseBridgeW_button.draw(screen)
            screen.blit(noseBridgeW_results,
                        (((noseBridgeW_img.get_width())*(1-0.44326617179)) + (77/(1-0.38693467336))*4 + (199) - (noseBridgeW_w*3) + uiOffset,
                        213+(60*29)+(noseBridgeW_h/2.5)+scrollWheel))
            
            ## Brow Ridge Section
            browRidge_button.draw(screen)

            browRidgeH_button.draw(screen)
            screen.blit(browRidgeH_results,
                        (((browRidgeH_img.get_width())*(1-0.44326617179)) + (77/(1-0.38693467336))*4 + (199) - (browRidgeH_w*3) + uiOffset,
                        213+(60*31)+(browRidgeH_h/2.5)+scrollWheel))
            innerBrow_button.draw(screen)
            screen.blit(innerBrow_results,
                        (((innerBrow_img.get_width())*(1-0.44326617179)) + (77/(1-0.38693467336))*4 + (199) - (innerBrow_w*3) + uiOffset,
                        213+(60*32)+(innerBrow_h/2.5)+scrollWheel))
            outerBrow_button.draw(screen)
            screen.blit(outerBrow_results,
                        (((outerBrow_img.get_width())*(1-0.44326617179)) + (77/(1-0.38693467336))*4 + (199) - (outerBrow_w*3) + uiOffset,
                        213+(60*33)+(outerBrow_h/2.5)+scrollWheel))
            ## Eyes Section
            eyes_button.draw(screen)

            eyePos_button.draw(screen)
            screen.blit(eyePos_results,
                        (((eyePos_img.get_width())*(1-0.44326617179)) + (77/(1-0.38693467336))*4 + (199) - (eyePos_w*3) + uiOffset,
                        213+(60*35)+(eyePos_h/2.5)+scrollWheel))
            eyeSize_button.draw(screen)
            screen.blit(eyeSize_results,
                        (((eyeSize_img.get_width())*(1-0.44326617179)) + (77/(1-0.38693467336))*4 + (199) - (eyeSize_w*3) + uiOffset,
                        213+(60*36)+(eyeSize_h/2.5)+scrollWheel))
            eyeSlant_button.draw(screen)
            screen.blit(eyeSlant_results,
                        (((eyeSlant_img.get_width())*(1-0.44326617179)) + (77/(1-0.38693467336))*4 + (199) - (eyeSlant_w*3) + uiOffset,
                        213+(60*37)+(eyeSlant_h/2.5)+scrollWheel))
            eyeSpacing_button.draw(screen)
            screen.blit(eyeSpacing_results,
                        (((eyeSpacing_img.get_width())*(1-0.44326617179)) + (77/(1-0.38693467336))*4 + (199) - (eyeSpacing_w*3) + uiOffset,
                        213+(60*38)+(eyeSpacing_h/2.5)+scrollWheel))
            ## Nose Ridge Section
            noseRidge_button.draw(screen)

            ## Nostrils Section
            nostrils_button.draw(screen)

            ## Cheeks Section
            cheeks_button.draw(screen)

            ## Lips Section
            lips_button.draw(screen)

            ## Mouth Section
            mouth_button.draw(screen)

            ## Chin Section
            chin_button.draw(screen)

            ## Jaw Section
            jaw_button.draw(screen)
            
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