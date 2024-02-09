import matplotlib.pyplot as plt
import numpy as np
from dataclasses import dataclass, field
from tkinter import *
from tkinter import ttk # Varför följer inte den här med "*"?
import sys

class GUI(ttk.Frame):
    """Fönster som frågar användaren om parametrarna till bilen och banan"""
    def __init__(self, parent) -> None:
        """Initierar fönstret"""
        Frame.__init__(self, parent)
        self.root = parent
        self.root.title("Varvsimulator")
        self.root.geometry("550x250")
        self.root["bg"] = "White"
        self.radie_kurvlista     = []
        self.längd_raka_lista    = []
        self.längd_kurva_lista   = []
        self.banfil = StringVar() # Lägg in 'standardbana.txt' här istället när nästa bana är inlagd

    def fyllabaninformationslistorna(self, banfil) -> None:
        """Fyller listorna med information om banan"""
        baninformationslista = [self.radie_kurvlista, self.längd_raka_lista, self.längd_kurva_lista]
        for lista in baninformationslista:
            lista.clear()
        with open(banfil, 'r', encoding='utf-8') as file:
            for lista in baninformationslista:
                for ord in file.readline().split():
                    lista.append(float(ord))

    def etikett(self) -> None: # Lyckas inte göra en for loop här
        """Skapar etiketterna till inmatningarna och placerar dem där de ska vara"""
        self.etikett_massa                      = ttk.Label(self.root, text= "Massa bil", background="White").grid(row=0, column=0, sticky = W)
        self.etikett_utväxling                  = ttk.Label(self.root, text= "Utväxling", background="White").grid(row=0, column=1, sticky = W)
        self.etikett_vridmoment_motor           = ttk.Label(self.root, text= "Vridmoment motor", background="White").grid(row=0, column=2, sticky = W)
        self.etikett_hjulradie                  = ttk.Label(self.root, text= "Hjulradie", background="White").grid(row=0, column=3, sticky = W)
        self.etikett_antal_motorer              = ttk.Label(self.root, text= "Antal motorer", background="White").grid(row=2, column=0, sticky = W)
        self.etikett_bromskraft                 = ttk.Label(self.root, text= "Bromskraft", background="White").grid(row=2, column=1, sticky = W)
        self.etikett_antal_bromsar              = ttk.Label(self.root, text= "Antal bromsar", background="White").grid(row=2, column=2, sticky = W)
        self.etikett_däck_friktion              = ttk.Label(self.root, text= "Däck friktion", background="White").grid(row=2, column=3, sticky = W)
        self.etikett_luftmotstånds_koefficient  = ttk.Label(self.root, text= "Luftmotstånds koefficent", background="White").grid(row=4, column=0, sticky = W)
        self.etikett_snitt_area_bil             = ttk.Label(self.root, text= "Snitt area bil", background="White").grid(row=4, column=1, sticky = W)
        self.etikett_lyftkrafts_koefficient     = ttk.Label(self.root, text= "Lyftkrafts koefficient", background="White").grid(row=4, column=2, sticky = W)
        self.etikett_area_vinge                 = ttk.Label(self.root, text= "Area vinge", background="White").grid(row=4, column=3, sticky = W)
        self.etikett_center_av_massa_höjd       = ttk.Label(self.root, text= "Höjd coG", background="White").grid(row=6, column=0, sticky = W)
        self.etikett_avstånd_mellan_axlar       = ttk.Label(self.root, text= "Avstånd: fram- & bakaxel", background="White").grid(row=6, column=1, sticky = W)
        self.etikett_center_av_massa_längd      = ttk.Label(self.root, text= "Längd coG", background="White").grid(row=6, column=2, sticky = W)  
        self.etikett__center_av_tryck_höjd      = ttk.Label(self.root, text= "Höjd coP", background="White").grid(row=6, column=3, sticky = W) 
        self.etikett__center_av_tryck_längd     = ttk.Label(self.root, text= "Längd coP", background="White").grid(row=8, column=0, sticky = W)
        self.etikett_luftens_densitet           = ttk.Label(self.root, text= "Luftens densitet", background="White").grid(row=8, column=1, sticky = W)
        self.etikett_gravitation                = ttk.Label(self.root, text= "Gravitation", background="White").grid(row=8, column=2, sticky = W)

    def inmatning(self) -> None: # Kan inte lägga ihop .grid(...) med inmatning. Verkar inte kunna göra en for loop här heller...
        """Skapar inmatningarna"""
        #inmatningslista  = ["inmatning_massa", "inmatning_utväxling", "inmatning_vridmoment_motor", "inmatning_hjulradie", "inmatning_antal_motorer", \
        #                    "inmatning_bromskraft", "inmatning_antal_bromsar", "inmatning_däck_friktion", "inmatning_luftmotstånds_koefficient", \
        #                    "inmatning_snitt_area_bil", "inmatning_lyftkrafts_koefficient", "inmatning_area_vinge", "inmatning_center_av_massa_höjd", \
        #                    "inmatning_avstånd_mellan_axlar", "inmatning_center_av_massa_längd", "inmatning_center_av_tryck_höjd",\
        #                    "inmatning_center_av_tryck_längd", "inmatning_luftens_densitet", "inmatning_gravitation"]

        #counter1 = 0
        #counter2 = 0
        #for i in range(1, len(inmatningslista) + 1):
        #    self[inmatningslista[i-1]] = ttk.Entry(self.root).grid(row=(1 + counter1), column=(i - counter2 - 1), sticky = W)
        #    if i % 4 == 0 and i != 0:
        #        counter1 += 2
        #        counter2 += 4 
    
        self.inmatning_massa                     = ttk.Entry(self.root)
        self.inmatning_utväxling                 = ttk.Entry(self.root)
        self.inmatning_vridmoment_motor          = ttk.Entry(self.root)
        self.inmatning_hjulradie                 = ttk.Entry(self.root)
        self.inmatning_antal_motorer             = ttk.Entry(self.root)
        self.inmatning_bromskraft                = ttk.Entry(self.root)
        self.inmatning_antal_bromsar             = ttk.Entry(self.root)
        self.inmatning_däck_friktion             = ttk.Entry(self.root)
        self.inmatning_luftmotstånds_koefficient = ttk.Entry(self.root)
        self.inmatning_snitt_area_bil            = ttk.Entry(self.root)
        self.inmatning_lyftkrafts_koefficient    = ttk.Entry(self.root)
        self.inmatning_area_vinge                = ttk.Entry(self.root)
        self.inmatning_center_av_massa_höjd      = ttk.Entry(self.root) # Just nu tycker jag verkligen inte om tkinter
        self.inmatning_avstånd_mellan_axlar      = ttk.Entry(self.root)
        self.inmatning_center_av_massa_längd     = ttk.Entry(self.root)
        self.inmatning_center_av_tryck_höjd      = ttk.Entry(self.root) 
        self.inmatning_center_av_tryck_längd     = ttk.Entry(self.root) 

        self.inmatning_luftens_densitet          = ttk.Entry(self.root)
        self.inmatning_gravitation               = ttk.Entry(self.root)
        
    def rutnät(self) -> None:
        """Placerar inmatningarna på rutnätet"""
        inmatningslista  = [self.inmatning_massa, self.inmatning_utväxling, self.inmatning_vridmoment_motor, self.inmatning_hjulradie, self.inmatning_antal_motorer, \
                            self.inmatning_bromskraft, self.inmatning_antal_bromsar, self.inmatning_däck_friktion, self.inmatning_luftmotstånds_koefficient, \
                            self.inmatning_snitt_area_bil, self.inmatning_lyftkrafts_koefficient, self.inmatning_area_vinge, self.inmatning_center_av_massa_höjd, \
                            self.inmatning_avstånd_mellan_axlar, self.inmatning_center_av_massa_längd, self.inmatning_center_av_tryck_höjd,\
                            self.inmatning_center_av_tryck_längd, self.inmatning_luftens_densitet, self.inmatning_gravitation]           
        
        counter1 = 0
        counter2 = 0
        for i in range(1, len(inmatningslista) + 1):
            inmatningslista[i-1].grid(row=(1 + counter1), column=(i - counter2 - 1), sticky = W)
            if i % 4 == 0 and i != 0:
                counter1 += 2
                counter2 += 4   

    def knappar(self) -> None:
        """Skapar knapparna"""
        style = ttk.Style()
        style.configure('Wild.TRadiobutton', background="White")
        self.startknappen    = ttk.Button(self.root, text= "Grönt ljus", command= lambda: self.start()).grid(row=100, column = 2)
        self.rullstartsval   = StringVar()
        self.rullstartsknapp = ttk.Checkbutton(self.root, text= "Rullstart", style= 'Wild.TRadiobutton', variable = self.rullstartsval,\
                                                    onvalue = "PÅ", offvalue = "AV").grid(row=99, column = 0)
        self.bana1           = ttk.Radiobutton(self.root, text= "Standardbana", style= 'Wild.TRadiobutton', variable= self.banfil,\
                                                    value= 'standardbana.txt').grid(row=99, column = 1)
        self.bana2           = ttk.Radiobutton(self.root, text= "Hockenheim", style= 'Wild.TRadiobutton', variable= self.banfil,\
                                                    value= 'hockenheim.txt').grid(row=99, column = 2)
        self.bana3           = ttk.Radiobutton(self.root, text= "Skidpad", style= 'Wild.TRadiobutton', variable= self.banfil,\
                                                    value= 'skidpad.txt').grid(row=99, column = 3)
        self.bana4           = ttk.Radiobutton(self.root, text= "Acceleration", style= 'Wild.TRadiobutton', variable= self.banfil,\
                                                    value= 'acceleration.txt').grid(row=100, column = 0)
        self.bana5           = ttk.Radiobutton(self.root, text= "Endurance", style= 'Wild.TRadiobutton', variable= self.banfil,\
                                                    value= 'endurance.txt').grid(row=100, column = 1)

    def grafritning(self, tid: float, sträcka: float, hastighet: float, luftmotstånd: float, downforce: float, däckgrepp: float, viktförändring_fram: float, viktförändring_bak: float, vridmoment: float) -> None:
        """Grafritningen"""
        fig1, (ax1, ax2, ax3, ax4) = plt.subplots(4, 1, layout='constrained')
       # graflista = [ax1, ax2, ax3, ax4]
       # mätvärden = [sträcka, hastighet, luftmotstånd, downforce]
       # enheter   = ['Sträcka (m)', 'Hastighet (m/s)', 'Luftmotstånd (N)']
       # for i in graflista:
       #     graflista[i].plot(tid, mätvärden[i])
       #     graflista[i].set_xlabel('Tid (s)')
       #     graflista[i].set_ylabel(enheter[i])
       #     graflista[i].grid(True)

        #FOR loopen funkar inte pga att "list indices must be integers or slices, not Axes". Verkar som att jag måste hårdkoda skiten
        ax1.plot(tid, sträcka)
        ax1.set_xlabel('Tid (s)')
        ax1.set_ylabel('Sträcka (m)')
        ax1.grid(True)

        ax2.plot(tid, hastighet)
        ax2.set_ylabel('Hastighet (m/s)')
        ax2.grid(True)

        ax3.plot(tid, luftmotstånd)
        ax3.set_ylabel('Luftmotstånd (N)')
        ax3.grid(True)

        ax4.plot(tid, downforce)
        ax4.set_ylabel('Downforce (N)')
        ax4.grid(True)

        plt.show()

        fig2, (ax1, ax2, ax3, ax4) = plt.subplots(4, 1, layout='constrained')
       
        ax1.plot(tid, däckgrepp)
        ax1.set_xlabel('Tid (s)')
        ax1.set_ylabel('Däckgrepp (N)')
        ax1.grid(True)
        
        ax2.plot(tid, viktförändring_fram)
        ax2.set_ylabel('Vikt framaxel (kg)')
        ax2.grid(True)

        ax3.plot(tid, viktförändring_bak)
        ax3.set_ylabel('Vikt bakaxel (kg)')
        ax3.grid(True)

        #ax3.plot(sträcka, hastighet)
        #ax3.set_ylabel('Hastighet / Sträcka')
        #ax3.grid(True)
        
        ax4.plot(tid, vridmoment)
        ax4.set_ylabel('Torque (Nm)')
        ax4.grid(True)

        plt.show()
    
    def spara_data(self, tid: list = [], hastighet: list = []) -> None:
        """Sparar data till en fil"""
        with open('sparadata.txt', 'w') as file:
            file.truncate(0)   
        with open('sparadata.txt', 'a', encoding='utf-8') as file:
            for i in range(len(tid)):
                file.write(f"{tid[i]} ")
            file.write("\n \n")            
            for j in range (len(hastighet)):
                file.write(f"{hastighet[j]} ")
            file.write("\n")

    def start(self) -> None:
        """Här startas simuleringen"""
        # Lista för inmatningsvärden
        inmatningslista  = [self.inmatning_massa, self.inmatning_utväxling, self.inmatning_vridmoment_motor, self.inmatning_hjulradie, self.inmatning_antal_motorer, \
                            self.inmatning_bromskraft, self.inmatning_antal_bromsar, self.inmatning_däck_friktion, self.inmatning_luftmotstånds_koefficient, \
                            self.inmatning_snitt_area_bil, self.inmatning_lyftkrafts_koefficient, self.inmatning_area_vinge, self.inmatning_center_av_massa_höjd, \
                            self.inmatning_avstånd_mellan_axlar, self.inmatning_center_av_massa_längd, self.inmatning_center_av_tryck_höjd,\
                            self.inmatning_center_av_tryck_längd, self.inmatning_luftens_densitet, self.inmatning_gravitation] 
        # Lista på de variabler som kommer användas när vi gör bilen och banan
        startvärdeslista = [Bil.get_massabil(), Bil.get_utväxling(), Bil.get_vridmoment_motor(), Bil.get_hjulradie(), Bil.get_antal_motorer(), Bil.get_bromskraft(), Bil.get_antal_bromsar(),\
                            Bil.get_däck_friktion(), Bil.get_luftmotstånds_koefficient(), Bil.get_snitt_area_bil(), Bil.get_lyftkrafts_koefficient(), Bil.get_area_vinge(), Bil.get_center_av_massa_höjd(),\
                            Bil.get_avstånd_mellan_axlar(), Bil.get_center_av_massa_längd(), Bil.get_center_av_tryck_höjd(), Bil.get_center_av_tryck_längd(), Bana.get_luftens_densitet(), Bana.get_gravitation()]
        
        # Den faktiskta listan som används när vi behöver plocka variabler för att göra bilen och banan
        VARFÖR = [] # Jag ogillar starkt den här listan. Jag vill bara ändra värdena i startvärdeslistan men jag får inte till det
        # Fyller VARFÖR listan
        for i in range(len(inmatningslista)):
            if inmatningslista[i].get() != "":
                try:
                    startvärdeslista[i] = float(inmatningslista[i].get())
                    VARFÖR.append(startvärdeslista[i])
                except:
                    print("Kom ihåg att endast siffror kan användas som input. Programmet kommer ignorera din felaktiga input")
                    VARFÖR.append(startvärdeslista[i])   
            else:
                VARFÖR.append(startvärdeslista[i])


        # Skapar bilen
        blixten_mcqueen     = Bil(MASSA_BIL= VARFÖR[0], UTVÄXLING= VARFÖR[1], VRIDMOMENT_MOTOR= VARFÖR[2], HJULRADIE= VARFÖR[3], ANTAL_MOTORER= VARFÖR[4], \
                                  BROMSKRAFT= VARFÖR[5], ANTAL_BROMSAR= VARFÖR[6], DÄCK_FRIKTION= VARFÖR[7], LUFTMOTSTÅNDS_KOEFFICIENT= VARFÖR[8], \
                                    SNITT_AREA_BIL= VARFÖR[9], LYFTKRAFTS_KOEFFICIENT= VARFÖR[10], AREA_VINGE= VARFÖR[11], CENTER_AV_MASSA_HÖJD= VARFÖR[12], \
                                        AVSTÅND_MELLAN_AXLAR= VARFÖR[13], CENTER_AV_MASSA_LÄNGD= VARFÖR[14], CENTER_AV_TRYCK_HÖJD= VARFÖR[15], CENTER_AV_TRYCK_LÄNGD= VARFÖR[16])
        # Skapar banan
        kylarköping         = Bana(längd_raka_lista= self.längd_raka_lista, längd_kurva_lista= self.längd_kurva_lista, radie_kurvlista= self.radie_kurvlista, \
                                   LUFTENS_DENSITET= VARFÖR[17], GRAVITATION= VARFÖR[18])
        try:
            self.fyllabaninformationslistorna(self.banfil.get())
        except:
            print("Det gick inte att läsa in banans information")
            sys.exit()

        # Startar simuleringen
        try:
            position_blixten_mcqueen = Position(blixten_mcqueen, kylarköping)
            krafter_blixten_mcqueen = Krafter(blixten_mcqueen, kylarköping)
            krafter_blixten_mcqueen.kalkylera_maximala_kurvhastighet(self.rullstartsval.get())
            position_blixten_mcqueen.placering()
            print(f"MASSA BIL: {VARFÖR[0]}, UTVÄXLING: {VARFÖR[1]}, VRIDMOMENT MOTOR: {VARFÖR[2]}, HJULRADIE: {VARFÖR[3]}, ANTAL MOTORER: {VARFÖR[4]}, BROMSKRAFT: {VARFÖR[5]},\
                ANTAL_BROMSAR: {VARFÖR[6]}, DÄCK_FRIKTION: {VARFÖR[7]}, LUFTMOTSTÅNDS_KOEFFICIENT: {VARFÖR[8]}, SNITT_AREA_BIL: {VARFÖR[9]}, LYFTKRAFTS_KOEFFICIENT: {VARFÖR[10]},\
                AREA_VINGE: {VARFÖR[11]}, CENTER_AV_MASSA_HÖJD: {VARFÖR[12]}, AVSTÅND_MELLAN_AXLAR: {VARFÖR[13]}, CENTER_AV_MASSA_LÄNGD: {VARFÖR[14]}, CENTER_AV_TRYCK_HÖJD: {VARFÖR[15]}, \
                CENTER_AV_TRYCK_LÄNGD: {VARFÖR[16]}, LUFTENS_DENSITET: {VARFÖR[17]}, GRAVITATION: {VARFÖR[18]}")
            self.grafritning(kylarköping.tid, blixten_mcqueen.position, blixten_mcqueen.hastighet, blixten_mcqueen.luftmotstånd, blixten_mcqueen.downforce,\
                            blixten_mcqueen.däckgrepp, blixten_mcqueen.viktförändring_fram, blixten_mcqueen.viktförändring_bak, blixten_mcqueen.vridmoment)
            #self.spara_data(kylarköping.tid, blixten_mcqueen.hastighet)
        except:
            print("Dina inmatningsvärden är troligtvis för stora eller för små")

@dataclass(slots=True)
class Bil:
    """Dataklass med bilens parametrar"""
    # För position
    MASSA_BIL:          float = 270
    UTVÄXLING:          float = 14
    VRIDMOMENT_MOTOR:   float = 21
    HJULRADIE:          float = 0.23
    ANTAL_MOTORER:      int   = 4
    BROMSKRAFT:         float = 400
    ANTAL_BROMSAR:      int   = 4
    DÄCK_FRIKTION:      float = 0.9
    # För verkande krafter
    LUFTMOTSTÅNDS_KOEFFICIENT: float = 1.5
    SNITT_AREA_BIL:            float = 1
    LYFTKRAFTS_KOEFFICIENT:    float = -6
    AREA_VINGE:                float = 1
    CENTER_AV_MASSA_HÖJD:      float = 0.23
    AVSTÅND_MELLAN_AXLAR:      float = 1.535
    CENTER_AV_MASSA_LÄNGD:     float = 0.9
    CENTER_AV_TRYCK_HÖJD:      float = 0.5
    CENTER_AV_TRYCK_LÄNGD:     float = 1
    # Listor med information om vad bilen gör nu
    position:            list[float] = field(default_factory= lambda: [0])
    hastighet:           list[float] = field(default_factory= lambda: [0])
    luftmotstånd:        list[float] = field(default_factory= lambda: [0])
    downforce:           list[float] = field(default_factory= lambda: [0])
    däckgrepp:           list[float] = field(default_factory= lambda: [0])
    viktförändring_fram: list[float] = field(default_factory= lambda: [0])
    viktförändring_bak:  list[float] = field(default_factory= lambda: [0])
    vridmoment:          list[float] = field(default_factory= lambda: [0])
#    @property #TypeError: unsupported operand type(s) for *: 'property' and 'float'. VAFAN???
    def get_massabil(MASSA_BIL= MASSA_BIL) -> float:
        return MASSA_BIL
    def get_utväxling(UTVÄXLING= UTVÄXLING) -> float:
        return UTVÄXLING
    def get_vridmoment_motor(VRIDMOMENT_MOTOR= VRIDMOMENT_MOTOR) -> float:
        return VRIDMOMENT_MOTOR
    def get_hjulradie(HJULRADIE= HJULRADIE) -> float:
        return HJULRADIE
    def get_antal_motorer(ANTAL_MOTORER= ANTAL_MOTORER) -> float:
        return ANTAL_MOTORER
    def get_bromskraft(BROMSKRAFT= BROMSKRAFT) -> float:
        return BROMSKRAFT
    def get_antal_bromsar(ANTAL_BROMSAR= ANTAL_BROMSAR) -> float:
        return ANTAL_BROMSAR
    def get_däck_friktion(DÄCK_FRIKTION= DÄCK_FRIKTION) -> float:
        return DÄCK_FRIKTION
    def get_luftmotstånds_koefficient(LUFTMOTSTÅNDS_KOEFFICIENT= LUFTMOTSTÅNDS_KOEFFICIENT) -> float:
        return LUFTMOTSTÅNDS_KOEFFICIENT
    def get_snitt_area_bil(SNITT_AREA_BIL= SNITT_AREA_BIL) -> float:
        return SNITT_AREA_BIL
    def get_lyftkrafts_koefficient(LYFTKRAFTS_KOEFFICIENT= LYFTKRAFTS_KOEFFICIENT) -> float:
        return LYFTKRAFTS_KOEFFICIENT
    def get_area_vinge(AREA_VINGE= AREA_VINGE) -> float:
        return AREA_VINGE
    def get_center_av_massa_höjd(CENTER_AV_MASSA_HÖJD= CENTER_AV_MASSA_HÖJD) -> float:
        return CENTER_AV_MASSA_HÖJD
    def get_avstånd_mellan_axlar(AVSTÅND_MELLAN_AXLAR= AVSTÅND_MELLAN_AXLAR) -> float:
        return AVSTÅND_MELLAN_AXLAR
    def get_center_av_massa_längd(CENTER_AV_MASSA_LÄNGD= CENTER_AV_MASSA_LÄNGD) -> float:
        return CENTER_AV_MASSA_LÄNGD
    def get_center_av_tryck_höjd(CENTER_AV_TRYCK_HÖJD= CENTER_AV_TRYCK_HÖJD) -> float:
        return CENTER_AV_TRYCK_HÖJD
    def get_center_av_tryck_längd(CENTER_AV_TRYCK_LÄNGD= CENTER_AV_TRYCK_LÄNGD) -> float:
        return CENTER_AV_TRYCK_LÄNGD

@dataclass(slots=True)
class Bana:
    """Dataklass med banans parametrar"""
    längd_raka_lista:    list[float] = field(default_factory= list)
    längd_kurva_lista:   list[float] = field(default_factory= list)
    radie_kurvlista:     list[float] = field(default_factory= list)
    hastighet_kurvlista: list[float] = field(default_factory= list) # Denna måste börja som en tom lista!
    tid:                 list[float] = field(default_factory= lambda: [0])
    LUFTENS_DENSITET:    float = 1.3
    GRAVITATION:         float = 9.82

    def get_luftens_densitet(LUFTENS_DENSITET= LUFTENS_DENSITET):
        return LUFTENS_DENSITET
    def get_gravitation(GRAVITATION= GRAVITATION):
        return GRAVITATION

class Position:
    """Position förändrar positionen bilen är placerad på"""
    def __init__(self, bil: Bil, bana: Bana) -> None:
        self.bil  = bil
        self.bana = bana
        self.steg_storlek = 0.001
    def placering(self) -> None:
        """Använder resterande metoder för att ta reda på bilens placering"""
        raksträcka = True # Det antas att det är varannan raksträcka och kurva
        for i in range(len(self.bana.längd_raka_lista + self.bana.längd_kurva_lista)):
            if raksträcka:
                hastighet_slut = self.bana.hastighet_kurvlista[i//2]
                Position.hastighet(self, self.bana.längd_raka_lista[i//2], hastighet_slut)
                raksträcka = False
            else:
                Position.kurvhastighet(self, self.bana.längd_kurva_lista[i//2], hastighet_slut)
                raksträcka = True

    def hastighet(self, position_slut: float, hastighet_slut: float) -> None:
        """Använder Euler approximation för att räkna ut hastighet"""
        while self.bil.position[-1] <= position_slut:
            hastighet_nu = self.bil.hastighet[-1] + Position.acceleration(self)*self.steg_storlek
            position_nu = self.bil.position[-1] + self.bil.hastighet[-1]*self.steg_storlek
            tid_nu = self.bana.tid[-1] + 1*self.steg_storlek

            Position.uppdatera_information(self, position_nu, hastighet_nu, tid_nu)

            broms_sträcka = Position.broms_sträcka_funktion(self, hastighet_nu, hastighet_slut, Position.retardation(self))

            if broms_sträcka + self.bil.position[-1] >= position_slut:
                hastighet_nu = self.bil.hastighet[-1] + (Position.retardation(self) - Position.acceleration(self))*self.steg_storlek
                position_nu = self.bil.position[-1] + self.bil.hastighet[-1]*self.steg_storlek
                tid_nu = self.bana.tid[-1] + 1*self.steg_storlek

                Position.uppdatera_information(self, position_nu, hastighet_nu, tid_nu)

    def kurvhastighet(self, position_slut: float, kurvhastighet) -> None:
        """Kalkylerar kurvhastigheten"""
        while self.bil.hastighet[-1] < kurvhastighet and self.bil.position[-1] <= position_slut:
            hastighet_nu = self.bil.hastighet[-1] + Position.acceleration(self)*self.steg_storlek
            position_nu = self.bil.position[-1] + self.bil.hastighet[-1]*self.steg_storlek
            tid_nu = self.bana.tid[-1] + 1*self.steg_storlek

            Position.uppdatera_information(self, position_nu, hastighet_nu, tid_nu)

        while self.bil.hastighet[-1] > kurvhastighet and self.bil.position[-1] <= position_slut:
            hastighet_nu = self.bil.hastighet[-1] + (Position.retardation(self) - Position.acceleration(self))*self.steg_storlek
            position_nu = self.bil.position[-1] + self.bil.hastighet[-1]*self.steg_storlek
            tid_nu = self.bana.tid[-1] + 1*self.steg_storlek

            Position.uppdatera_information(self, position_nu, hastighet_nu, tid_nu)

        while self.bil.position[-1] <= position_slut:
            hastighet_nu = kurvhastighet
            position_nu = self.bil.position[-1] + self.bil.hastighet[-1]*self.steg_storlek
            tid_nu = self.bana.tid[-1] + 1*self.steg_storlek  

            Position.uppdatera_information(self, position_nu, hastighet_nu, tid_nu)
            Krafter.uppdatera_krafter(self, self.bil.VRIDMOMENT_MOTOR)

    def retardation(self) -> float:
        """Räknar ut retardation vid nuvarande tidpunkt om bilen bromsar"""
        retardationen = -self.bil.ANTAL_BROMSAR*(self.bil.BROMSKRAFT\
                 + Krafter.luftmotstånd(self, self.bil.hastighet[-1])/self.bil.MASSA_BIL)/(self.bil.HJULRADIE*self.bil.MASSA_BIL)
        return retardationen

    def acceleration(self) -> float:
        """Räknar ut acceleration vid nuvarande tidpunkt om bilen gasar"""
        mängd_bly_i_skon = 0
        vridmoment = self.bil.VRIDMOMENT_MOTOR
        min_vridmoment = vridmoment * (17/21)
        rpm = Position.kalkylera_rpm(self, self.bil.hastighet[-1])
        max_rpm = 20000
        max_vridmoment_rpm = 14000

        if rpm > max_vridmoment_rpm:
            vridmoment = min_vridmoment + (max_rpm - rpm) * (vridmoment - min_vridmoment) / (max_rpm - max_vridmoment_rpm)

        accel = self.bil.ANTAL_MOTORER*self.bil.UTVÄXLING*(vridmoment\
                     - Krafter.luftmotstånd(self, self.bil.hastighet[-1])/self.bil.MASSA_BIL)/(self.bil.HJULRADIE*self.bil.MASSA_BIL)

        for i in range(20):
            if rpm < max_rpm:
                break
            else:
                accel = self.bil.ANTAL_MOTORER*self.bil.UTVÄXLING*((self.bil.VRIDMOMENT_MOTOR + mängd_bly_i_skon)\
                     - Krafter.luftmotstånd(self, self.bil.hastighet[-1])/self.bil.MASSA_BIL)/(self.bil.HJULRADIE*self.bil.MASSA_BIL)
                mängd_bly_i_skon -= self.bil.VRIDMOMENT_MOTOR/20

        nuvarande_vikt_fram = Krafter.viktöverföring_fram(self, accel)
        nuvarande_vikt_bak = Krafter.viktöverföring_bak(self, accel)
        #vikt_fram = self.bil.MASSA_BIL*self.bil.CENTER_AV_MASSA_LÄNGD/self.bil.AVSTÅND_MELLAN_AXLAR
        vikt_fram = self.bil.MASSA_BIL/2
        vikt_bak = self.bil.MASSA_BIL/2
        
        if nuvarande_vikt_fram < vikt_fram and nuvarande_vikt_bak < vikt_bak:
            accel = nuvarande_vikt_fram/vikt_fram * nuvarande_vikt_bak/vikt_bak * accel

        elif nuvarande_vikt_fram < vikt_fram:
            accel = nuvarande_vikt_fram/vikt_fram * accel
        
        elif nuvarande_vikt_bak < vikt_bak:
            accel = nuvarande_vikt_bak/vikt_bak * accel

        Krafter.uppdatera_krafter(self, vridmoment)
        return accel

    def broms_sträcka_funktion(self, hastighet_nu:float, hastighet_slut:float, retardition:float) -> float:
        """Kalkylerar hur långbromsträckan skulle bli om inbromsningen skulle ske vid tidpunkt t"""
        broms_sträcka = 0
        while hastighet_nu > hastighet_slut:
            hastighet_nu = hastighet_nu + retardition/2*self.steg_storlek
            broms_sträcka = broms_sträcka + hastighet_nu*self.steg_storlek
        return broms_sträcka
    
    def kalkylera_rpm(self, hastighet_nu: float) -> float:
        rpm = hastighet_nu*60*14/(2*np.pi*self.bil.HJULRADIE)
        return rpm
    
    def uppdatera_information(self, position_nu: float, hastighet_nu: float, tid_nu: float):
        """Uppdaterar positionen, hastigheten och tiden"""
        self.bil.position.append(position_nu)
        self.bil.hastighet.append(hastighet_nu)
        self.bana.tid.append(tid_nu)

class Krafter:
    """Förändrar krafterna som verkar på bilen"""
    def __init__(self, bil: Bil, bana: Bana) -> None:
        self.bil  = bil
        self.bana = bana

    def kalkylera_maximala_kurvhastighet(self, rullstartsval) -> None:
        """Kalkylerar maximala möjliga kurvhastighet. Detta sker i 3 steg. 1. Utan downforce 2. Med downforce 3. Med downforce igen för lite mer precision."""
        for kurvradie in self.bana.radie_kurvlista:
            approximerad_kurvhastighet = np.sqrt(self.bil.DÄCK_FRIKTION*self.bana.GRAVITATION*kurvradie)
            for i in range(8):
                bättre_approximerad_kurvhastighet = np.sqrt(self.däckgrepp(approximerad_kurvhastighet)/self.bil.MASSA_BIL*kurvradie)
                approximerad_kurvhastighet = bättre_approximerad_kurvhastighet
            self.bana.hastighet_kurvlista.append(approximerad_kurvhastighet)
        if rullstartsval == "PÅ":
            self.bil.hastighet[0] = self.bana.hastighet_kurvlista[-1]
        #print(self.bana.hastighet_kurvlista)

    def luftmotstånd(self, hastighet: float) -> float:
        """Kalkylerar bilens luftmotstånd"""
        drag = 0.5*self.bana.LUFTENS_DENSITET*self.bil.LUFTMOTSTÅNDS_KOEFFICIENT*self.bil.SNITT_AREA_BIL*hastighet**2
        return drag
    
    def downforce(self, hastighet: float) -> float:
        """Kalkylerar bilens downforce"""
        downforce_variabel = 0.5*self.bil.LYFTKRAFTS_KOEFFICIENT*self.bana.LUFTENS_DENSITET*self.bil.AREA_VINGE*hastighet**2
        return downforce_variabel
    
    def magic(self, sidohastighet: float) -> float:
        """Kalkylerar den laterala kraften på däcken genom Pacejkas 'magic formula'. Inte användbar ännu"""
        styvhetsfaktor = 0.714
        formfaktor = 1.4
        maxvärdet = 1.00
        grafkurvfaktor = -0.20
        slip_angle = np.arctan(sidohastighet, self.bil.hastighet[-1])
        lateral_kraft_på_däck = maxvärdet*np.sin(formfaktor*np.arctan(styvhetsfaktor*slip_angle\
                                                - grafkurvfaktor*(styvhetsfaktor*slip_angle - np.arctan(styvhetsfaktor*slip_angle))))
        return lateral_kraft_på_däck
    
    def däckgrepp(self, hastighet: float) -> float:
        """Kalkylerar däckgreppet"""
        normalkraft = self.bil.MASSA_BIL * self.bana.GRAVITATION - Krafter.downforce(self, hastighet)
        däckgrepp = self.bil.DÄCK_FRIKTION * normalkraft
        return däckgrepp
    
    def viktöverföring_fram(self, acceleration: float) -> float:
        """Viktöverföringen kalkyleras genom att räkna på den nuvarande vikten på framaxeln"""
        viktförändring_fram = self.bil.MASSA_BIL*self.bil.CENTER_AV_MASSA_LÄNGD/self.bil.AVSTÅND_MELLAN_AXLAR + \
                            (- self.bil.MASSA_BIL*acceleration*self.bil.CENTER_AV_MASSA_HÖJD/self.bil.AVSTÅND_MELLAN_AXLAR\
                            - Krafter.luftmotstånd(self, self.bil.hastighet[-1])*self.bil.CENTER_AV_TRYCK_HÖJD/self.bil.AVSTÅND_MELLAN_AXLAR\
                            - Krafter.downforce(self, self.bil.hastighet[-1])*self.bil.CENTER_AV_TRYCK_LÄNGD/self.bil.AVSTÅND_MELLAN_AXLAR) / self.bana.GRAVITATION
        return viktförändring_fram
    
    def viktöverföring_bak(self, acceleration: float) -> float:
        """Viktöverföringen kalkyleras genom att räkna på den nuvarande vikten på framaxeln"""
        viktförändring_bak = self.bil.MASSA_BIL - self.bil.MASSA_BIL*self.bil.CENTER_AV_MASSA_LÄNGD/self.bil.AVSTÅND_MELLAN_AXLAR + \
                            (+ self.bil.MASSA_BIL*acceleration*self.bil.CENTER_AV_MASSA_HÖJD/self.bil.AVSTÅND_MELLAN_AXLAR\
                            + Krafter.luftmotstånd(self, self.bil.hastighet[-1])*self.bil.CENTER_AV_TRYCK_HÖJD/self.bil.AVSTÅND_MELLAN_AXLAR\
                            - Krafter.downforce(self, self.bil.hastighet[-1])*(self.bil.AVSTÅND_MELLAN_AXLAR-self.bil.CENTER_AV_TRYCK_LÄNGD)/self.bil.AVSTÅND_MELLAN_AXLAR) / self.bana.GRAVITATION
        return viktförändring_bak

    def uppdatera_krafter(self, vridmoment) -> None:
        """Uppdaterar listorna som innehåller informationen om krafterna för att kunna göra en graf"""
        self.bil.luftmotstånd.append(Krafter.luftmotstånd(self, self.bil.hastighet[-1]))
        self.bil.downforce.append(Krafter.downforce(self, self.bil.hastighet[-1]))
        self.bil.däckgrepp.append(Krafter.däckgrepp(self, self.bil.hastighet[-1]))
        self.bil.viktförändring_fram.append(Krafter.viktöverföring_fram(self, self.bil.hastighet[-1]))
        self.bil.viktförändring_bak.append(Krafter.viktöverföring_bak(self, self.bil.hastighet[-1]))
        self.bil.vridmoment.append(vridmoment)

def main():
    root = Tk()
    gui = GUI(root)
    gui.etikett()
    gui.inmatning()
    gui.rutnät()
    gui.knappar()
    root.mainloop()

if __name__ == '__main__':
    main()