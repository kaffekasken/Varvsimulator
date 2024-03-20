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
        self.etikett_bromsmoment                = ttk.Label(self.root, text= "Bromsmoment", background="White").grid(row=2, column=1, sticky = W)
        self.etikett_antal_bromsar              = ttk.Label(self.root, text= "Antal bromsar", background="White").grid(row=2, column=2, sticky = W)
        self.etikett_däckfriktion               = ttk.Label(self.root, text= "Däckfriktion", background="White").grid(row=2, column=3, sticky = W)
        self.etikett_luftmotstånds_koefficient  = ttk.Label(self.root, text= "Luftmotstånds koefficent", background="White").grid(row=4, column=0, sticky = W)
        self.etikett_snittarea_bil              = ttk.Label(self.root, text= "Snitt area bil", background="White").grid(row=4, column=1, sticky = W)
        self.etikett_lyftkrafts_koefficient     = ttk.Label(self.root, text= "Lyftkrafts koefficient", background="White").grid(row=4, column=2, sticky = W)
        self.etikett_area_vinge                 = ttk.Label(self.root, text= "Area vinge", background="White").grid(row=4, column=3, sticky = W)
        self.etikett_center_av_massa_höjd       = ttk.Label(self.root, text= "Höjd coG", background="White").grid(row=6, column=0, sticky = W)
        self.etikett_avstånd_mellan_axlar       = ttk.Label(self.root, text= "Avstånd: fram- & bakaxel", background="White").grid(row=6, column=1, sticky = W)
        self.etikett_center_av_massa_längd      = ttk.Label(self.root, text= "Längd coG", background="White").grid(row=6, column=2, sticky = W)  
        self.etikett_center_av_tryck_höjd       = ttk.Label(self.root, text= "Höjd coP", background="White").grid(row=6, column=3, sticky = W) 
        self.etikett_center_av_tryck_längd      = ttk.Label(self.root, text= "Längd coP", background="White").grid(row=8, column=0, sticky = W)
        self.etikett_luftens_densitet           = ttk.Label(self.root, text= "Luftens densitet", background="White").grid(row=8, column=1, sticky = W)
        self.etikett_gravitation                = ttk.Label(self.root, text= "Gravitation", background="White").grid(row=8, column=2, sticky = W)

    def inmatning(self) -> None: # Kan inte lägga ihop .grid(...) med inmatning. Verkar inte kunna göra en for loop här heller...
        """Skapar inmatningarna"""
        #inmatningslista  = ["inmatning_massa", "inmatning_utväxling", "inmatning_vridmoment_motor", "inmatning_hjulradie", "inmatning_antal_motorer", \
        #                    "inmatning_bromsmoment", "inmatning_antal_bromsar", "inmatning_däckfriktion", "inmatning_luftmotstånds_koefficient", \
        #                    "inmatning_snittarea_bil", "inmatning_lyftkrafts_koefficient", "inmatning_area_vinge", "inmatning_center_av_massa_höjd", \
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
        self.inmatning_bromsmoment               = ttk.Entry(self.root)
        self.inmatning_antal_bromsar             = ttk.Entry(self.root)
        self.inmatning_däckfriktion              = ttk.Entry(self.root)
        self.inmatning_luftmotstånds_koefficient = ttk.Entry(self.root)
        self.inmatning_snittarea_bil             = ttk.Entry(self.root)
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
                            self.inmatning_bromsmoment, self.inmatning_antal_bromsar, self.inmatning_däckfriktion, self.inmatning_luftmotstånds_koefficient, \
                            self.inmatning_snittarea_bil, self.inmatning_lyftkrafts_koefficient, self.inmatning_area_vinge, self.inmatning_center_av_massa_höjd, \
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

    def grafritning(self, tid: float, sträcka: float, hastighet: float, luftmotstånd: float, downforce: float, däckgrepp: float, viktförändring_fram: float, viktförändring_bak: float, vridmoment: float, låsta_bakhjul: float) -> None:
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

        fig3, (ax1, ax2) = plt.subplots(2, 1, layout='constrained')
        
        ax1.plot(tid, låsta_bakhjul)
        ax1.set_xlabel('Tid (s)')
        ax1.set_ylabel('Låsta bakhjul (N)')
        ax1.grid(True)

        ax2.plot(tid, hastighet)
        ax2.set_ylabel('Hastighet (m/s)')
        ax2.grid(True)
    
        plt.show()

    def spara_data(self, parameter_1: list = [], parameter_2: list = []) -> None:
        """Sparar data till en fil"""
        with open('sparadata.txt', 'w') as file:
            file.truncate(0)   
        with open('sparadata.txt', 'a', encoding='utf-8') as file:
            for i in range(len(parameter_1)):
                file.write(f"{parameter_1[i]} ")
            file.write("\n \n")            
            for j in range (len(parameter_2)):
                file.write(f"{parameter_2[j]} ")
            file.write("\n")

    def start(self) -> None:
        """Här startas simuleringen"""
        # Lista för inmatningsvärden
        inmatningslista  = [self.inmatning_massa, self.inmatning_utväxling, self.inmatning_vridmoment_motor, self.inmatning_hjulradie, self.inmatning_antal_motorer, \
                            self.inmatning_bromsmoment, self.inmatning_antal_bromsar, self.inmatning_däckfriktion, self.inmatning_luftmotstånds_koefficient, \
                            self.inmatning_snittarea_bil, self.inmatning_lyftkrafts_koefficient, self.inmatning_area_vinge, self.inmatning_center_av_massa_höjd, \
                            self.inmatning_avstånd_mellan_axlar, self.inmatning_center_av_massa_längd, self.inmatning_center_av_tryck_höjd,\
                            self.inmatning_center_av_tryck_längd, self.inmatning_luftens_densitet, self.inmatning_gravitation] 
        # Lista på de variabler som kommer användas när vi gör bilen och banan
        startvärdeslista = [Bil.get_massabil(), Bil.get_utväxling(), Bil.get_vridmoment_motor(), Bil.get_hjulradie(), Bil.get_antal_motorer(), Bil.get_bromsmoment(), Bil.get_antal_bromsar(),\
                            Bil.get_däckfriktion(), Bil.get_luftmotstånds_koefficient(), Bil.get_snittarea_bil(), Bil.get_lyftkrafts_koefficient(), Bil.get_area_vinge(), Bil.get_center_av_massa_höjd(),\
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
                                  BROMSMOMENT= VARFÖR[5], ANTAL_BROMSAR= VARFÖR[6], DÄCKFRIKTION= VARFÖR[7], LUFTMOTSTÅNDS_KOEFFICIENT= VARFÖR[8], \
                                    SNITTAREA_BIL= VARFÖR[9], LYFTKRAFTS_KOEFFICIENT= VARFÖR[10], AREA_VINGE= VARFÖR[11], CENTER_AV_MASSA_HÖJD= VARFÖR[12], \
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
        #try:
        position_blixten_mcqueen = Position(blixten_mcqueen, kylarköping)
        krafter_blixten_mcqueen = Krafter(blixten_mcqueen, kylarköping)
        krafter_blixten_mcqueen.kalkylera_maximala_kurvhastighet(self.rullstartsval.get())
        position_blixten_mcqueen.placering()
        print(f"MASSA BIL: {VARFÖR[0]}, UTVÄXLING: {VARFÖR[1]}, VRIDMOMENT MOTOR: {VARFÖR[2]}, HJULRADIE: {VARFÖR[3]}, ANTAL MOTORER: {VARFÖR[4]}, BROMSMOMENT: {VARFÖR[5]},\
            ANTAL_BROMSAR: {VARFÖR[6]}, DÄCKFRIKTION: {VARFÖR[7]}, LUFTMOTSTÅNDS_KOEFFICIENT: {VARFÖR[8]}, SNITTAREA_BIL: {VARFÖR[9]}, LYFTKRAFTS_KOEFFICIENT: {VARFÖR[10]},\
            AREA_VINGE: {VARFÖR[11]}, CENTER_AV_MASSA_HÖJD: {VARFÖR[12]}, AVSTÅND_MELLAN_AXLAR: {VARFÖR[13]}, CENTER_AV_MASSA_LÄNGD: {VARFÖR[14]}, CENTER_AV_TRYCK_HÖJD: {VARFÖR[15]}, \
            CENTER_AV_TRYCK_LÄNGD: {VARFÖR[16]}, LUFTENS_DENSITET: {VARFÖR[17]}, GRAVITATION: {VARFÖR[18]}")
        self.grafritning(kylarköping.tid, blixten_mcqueen.position, blixten_mcqueen.hastighet, blixten_mcqueen.luftmotstånd, blixten_mcqueen.downforce,\
                        blixten_mcqueen.däckgrepp, blixten_mcqueen.viktförändring_fram, blixten_mcqueen.viktförändring_bak, blixten_mcqueen.vridmoment, blixten_mcqueen.låsta_bakhjul)
        self.spara_data(kylarköping.tid, blixten_mcqueen.hastighet)
        #except:
        #    print("Dina inmatningsvärden är troligtvis för stora eller för små")

@dataclass(slots=True)
class Bil:
    """Dataklass med bilens parametrar"""
    # För position
    MASSA_BIL:          float = 270
    UTVÄXLING:          float = 14
    VRIDMOMENT_MOTOR:   float = 21
    HJULRADIE:          float = 0.23
    ANTAL_MOTORER:      int   = 4
    BROMSMOMENT:        float = 400
    ANTAL_BROMSAR:      int   = 4
    DÄCKFRIKTION:       float = 1.3
    # För verkande krafter
    LUFTMOTSTÅNDS_KOEFFICIENT: float = 1.5
    SNITTAREA_BIL:             float = 1
    LYFTKRAFTS_KOEFFICIENT:    float = -5
    AREA_VINGE:                float = 1
    CENTER_AV_MASSA_HÖJD:      float = 0.2032
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
    acceleration:        list[float] = field(default_factory= lambda: [0])
    låsta_bakhjul:       list[float] = field(default_factory= lambda: [0])

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
    def get_bromsmoment(BROMSMOMENT= BROMSMOMENT) -> float:
        return BROMSMOMENT
    def get_antal_bromsar(ANTAL_BROMSAR= ANTAL_BROMSAR) -> float:
        return ANTAL_BROMSAR
    def get_däckfriktion(DÄCKFRIKTION= DÄCKFRIKTION) -> float:
        return DÄCKFRIKTION
    def get_luftmotstånds_koefficient(LUFTMOTSTÅNDS_KOEFFICIENT= LUFTMOTSTÅNDS_KOEFFICIENT) -> float:
        return LUFTMOTSTÅNDS_KOEFFICIENT
    def get_snittarea_bil(SNITTAREA_BIL= SNITTAREA_BIL) -> float:
        return SNITTAREA_BIL
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
        """Använder Euler approximation för att kalkylera hastighet"""
        while self.bil.position[-1] <= position_slut:
            acceleration = Position.acceleration(self)
            hastighet_nu = self.bil.hastighet[-1] + acceleration*self.steg_storlek
            position_nu = self.bil.position[-1] + self.bil.hastighet[-1]*self.steg_storlek
            tid_nu = self.bana.tid[-1] + 1*self.steg_storlek

            bromssträcka = Position.bromssträcka_funktion(self, hastighet_nu, hastighet_slut, acceleration, Position.retardation(self))

            if bromssträcka + self.bil.position[-1] >= position_slut:
                retardation = Position.retardation(self)
                acceleration = Position.acceleration(self)
                hastighet_nu = self.bil.hastighet[-1] + (retardation - acceleration)*self.steg_storlek
                position_nu = self.bil.position[-1] + self.bil.hastighet[-1]*self.steg_storlek
                tid_nu = self.bana.tid[-1] + 1*self.steg_storlek

                Krafter.uppdatera_krafter(self, retardation)
                Krafter.uppdatera_krafter(self, retardation)
                Position.uppdatera_information(self, position_nu, hastighet_nu, tid_nu)
                Position.uppdatera_information(self, position_nu, hastighet_nu, tid_nu)
            else:
                Krafter.uppdatera_krafter(self, acceleration)
                Position.uppdatera_information(self, position_nu, hastighet_nu, tid_nu)

    def kurvhastighet(self, position_slut: float, kurvhastighet) -> None:
        """Kalkylerar kurvhastigheten"""
        while self.bil.hastighet[-1] < kurvhastighet and self.bil.position[-1] <= position_slut:
            hastighet_nu = self.bil.hastighet[-1] + Position.acceleration(self)*self.steg_storlek
            position_nu = self.bil.position[-1] + self.bil.hastighet[-1]*self.steg_storlek
            tid_nu = self.bana.tid[-1] + 1*self.steg_storlek

            Krafter.uppdatera_krafter(self, 0)
            Position.uppdatera_information(self, position_nu, hastighet_nu, tid_nu)
            self.bil.låsta_bakhjul.append(0)

        while self.bil.hastighet[-1] > kurvhastighet and self.bil.position[-1] <= position_slut:
            hastighet_nu = self.bil.hastighet[-1] + (Position.retardation(self) - Position.acceleration(self))*self.steg_storlek
            position_nu = self.bil.position[-1] + self.bil.hastighet[-1]*self.steg_storlek
            tid_nu = self.bana.tid[-1] + 1*self.steg_storlek

            Krafter.uppdatera_krafter(self, 0)
            Position.uppdatera_information(self, position_nu, hastighet_nu, tid_nu)

        while self.bil.position[-1] <= position_slut:
            hastighet_nu = kurvhastighet
            position_nu = self.bil.position[-1] + self.bil.hastighet[-1]*self.steg_storlek
            tid_nu = self.bana.tid[-1] + 1*self.steg_storlek  

            self.bil.vridmoment.append(self.bil.vridmoment[-1])
            Krafter.uppdatera_krafter(self, 0)
            Position.uppdatera_information(self, position_nu, hastighet_nu, tid_nu)
            self.bil.låsta_bakhjul.append(0)

    def retardation(self) -> float:
        """Räknar ut retardation vid nuvarande tidpunkt om bilen bromsar. Innefattar även tillgängligt däckgrepps kalkylation"""
        retardationen = -self.bil.ANTAL_BROMSAR*self.bil.BROMSMOMENT/(self.bil.HJULRADIE*self.bil.MASSA_BIL)\
              - Krafter.luftmotstånd(self, self.bil.hastighet[-1])/self.bil.MASSA_BIL
        
        normalkraft_framaxel = self.bil.viktförändring_fram[-1] * self.bana.GRAVITATION
        normalkraft_bakaxel = self.bil.viktförändring_bak[-1]   * self.bana.GRAVITATION
        potentiell_inbromsningskraft_fram = retardationen*self.bil.MASSA_BIL*0.6
        potentiell_inbromsningskraft_bak = retardationen*self.bil.MASSA_BIL*0.4
        kraft_vid_pedal = Krafter.kraft_vid_pedal(self, normalkraft_bakaxel/2)
        
        if normalkraft_framaxel * self.bil.DÄCKFRIKTION < -potentiell_inbromsningskraft_fram and normalkraft_bakaxel * self.bil.DÄCKFRIKTION < -potentiell_inbromsningskraft_bak:
            retardationen = retardationen * (normalkraft_framaxel * normalkraft_bakaxel * self.bil.DÄCKFRIKTION**2) / (potentiell_inbromsningskraft_bak**2)
            self.bil.låsta_bakhjul.append(kraft_vid_pedal)
        elif normalkraft_framaxel * self.bil.DÄCKFRIKTION < -potentiell_inbromsningskraft_fram:
            retardationen = - retardationen * (normalkraft_framaxel * self.bil.DÄCKFRIKTION) / potentiell_inbromsningskraft_bak
            self.bil.låsta_bakhjul.append(0)
        elif normalkraft_bakaxel * self.bil.DÄCKFRIKTION < -potentiell_inbromsningskraft_bak:
            retardationen = - retardationen * (normalkraft_bakaxel * self.bil.DÄCKFRIKTION) / potentiell_inbromsningskraft_bak
            self.bil.låsta_bakhjul.append(kraft_vid_pedal)
        else:
            self.bil.låsta_bakhjul.append(0)
        
        return retardationen

    def acceleration(self) -> float:
        """Innefattar uträkning för acceleration, rpm, redline, vridmoment och hur mycket grepp som finns tillgängligt"""
        mängd_bly_i_skon = 0
        vridmoment = self.bil.VRIDMOMENT_MOTOR
        min_vridmoment = vridmoment * (17/21)
        rpm = Position.kalkylera_rpm(self, self.bil.hastighet[-1])
        max_rpm = 20000
        max_vridmoment_rpm = 14000
        # Vridmoment
        if rpm > max_vridmoment_rpm:
            vridmoment = min_vridmoment + (max_rpm - rpm) * (vridmoment - min_vridmoment) / (max_rpm - max_vridmoment_rpm)
        # Max acceleration
        accel = self.bil.ANTAL_MOTORER*self.bil.UTVÄXLING*(vridmoment)/(self.bil.HJULRADIE*self.bil.MASSA_BIL) \
              - Krafter.luftmotstånd(self, self.bil.hastighet[-1])/self.bil.MASSA_BIL
        # Redline
        for i in range(20):
            if rpm < max_rpm:
                break
            else:
                accel = self.bil.ANTAL_MOTORER*self.bil.UTVÄXLING*((self.bil.VRIDMOMENT_MOTOR + mängd_bly_i_skon))\
                     /(self.bil.HJULRADIE*self.bil.MASSA_BIL) - Krafter.luftmotstånd(self, self.bil.hastighet[-1])/self.bil.MASSA_BIL
                mängd_bly_i_skon -= self.bil.VRIDMOMENT_MOTOR/20
        # Däckgrepp
        normalkraft_framaxel = Krafter.viktöverföring_fram(self, accel) * self.bana.GRAVITATION
        normalkraft_bakaxel = Krafter.viktöverföring_bak(self, accel) * self.bana.GRAVITATION
        potentiell_kraft_framåt = accel*self.bil.MASSA_BIL/2

        if normalkraft_framaxel * self.bil.DÄCKFRIKTION < potentiell_kraft_framåt and normalkraft_bakaxel * self.bil.DÄCKFRIKTION < potentiell_kraft_framåt:
            accel = accel * (normalkraft_framaxel * normalkraft_bakaxel * self.bil.DÄCKFRIKTION**2) / (potentiell_kraft_framåt**2)
        elif normalkraft_framaxel * self.bil.DÄCKFRIKTION < potentiell_kraft_framåt:
            accel = accel * (normalkraft_framaxel * self.bil.DÄCKFRIKTION) / potentiell_kraft_framåt
        elif normalkraft_bakaxel * self.bil.DÄCKFRIKTION < potentiell_kraft_framåt:
            accel = accel * (normalkraft_bakaxel * self.bil.DÄCKFRIKTION) / potentiell_kraft_framåt
        # Uppdatera info
        self.bil.vridmoment.append(vridmoment)
        return accel

    def bromssträcka_funktion(self, hastighet_nu:float, hastighet_slut:float, acceleration:float, retardition:float) -> float:
        """Kalkylerar bromssträcka"""
        bromssträcka = 0
        while hastighet_nu > hastighet_slut:
            hastighet_nu = hastighet_nu + (retardition - acceleration)*self.steg_storlek
            bromssträcka = bromssträcka + hastighet_nu*self.steg_storlek
        return bromssträcka
    
    def kalkylera_rpm(self, hastighet_nu: float) -> float:
        """Kalkylerar RPM"""
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
            approximerad_kurvhastighet = np.sqrt(self.bil.DÄCKFRIKTION*self.bana.GRAVITATION*kurvradie)
            for i in range(8):
                bättre_approximerad_kurvhastighet = np.sqrt(self.däckgrepp(approximerad_kurvhastighet)/self.bil.MASSA_BIL*kurvradie)
                approximerad_kurvhastighet = bättre_approximerad_kurvhastighet
            self.bana.hastighet_kurvlista.append(approximerad_kurvhastighet)
        if rullstartsval == "PÅ":
            self.bil.hastighet[0] = self.bana.hastighet_kurvlista[-1]
        #print(self.bana.hastighet_kurvlista)

    def luftmotstånd(self, hastighet: float) -> float:
        """Kalkylerar bilens luftmotstånd"""
        drag = 0.5*self.bana.LUFTENS_DENSITET*self.bil.LUFTMOTSTÅNDS_KOEFFICIENT*self.bil.SNITTAREA_BIL*hastighet**2
        return drag
    
    def downforce(self, hastighet: float) -> float:
        """Kalkylerar bilens downforce"""
        downforce_variabel = -0.5*self.bil.LYFTKRAFTS_KOEFFICIENT*self.bana.LUFTENS_DENSITET*self.bil.AREA_VINGE*hastighet**2
        return downforce_variabel
    
    def magic(self, sidohastighet: float) -> float:
        """Kalkylerar den laterala kraften på däcken genom Pacejkas 'magic formula'. Inte användbar ännu"""
        styvhetsfaktor = 0
        formfaktor = 0
        maxvärdet = 0
        grafkurvfaktor = 0
        slip_angle = np.arctan(sidohastighet, self.bil.hastighet[-1])
        lateral_kraft_på_däck = maxvärdet*np.sin(formfaktor*np.arctan(styvhetsfaktor*slip_angle\
                                                - grafkurvfaktor*(styvhetsfaktor*slip_angle - np.arctan(styvhetsfaktor*slip_angle))))
        return lateral_kraft_på_däck
    
    def däckgrepp(self, hastighet: float) -> float:
        """Kalkylerar däckgreppet"""
        normalkraft = self.bil.MASSA_BIL * self.bana.GRAVITATION + Krafter.downforce(self, hastighet)
        däckgrepp = self.bil.DÄCKFRIKTION * normalkraft
        return däckgrepp
    
    def viktöverföring_fram(self, acceleration: float) -> float:
        """Viktöverföringen kalkyleras genom att räkna på den nuvarande vikten på framaxeln"""
        viktförändring_fram = self.bil.MASSA_BIL*self.bil.CENTER_AV_MASSA_LÄNGD/self.bil.AVSTÅND_MELLAN_AXLAR + \
                            (- self.bil.MASSA_BIL*acceleration*self.bil.CENTER_AV_MASSA_HÖJD/self.bil.AVSTÅND_MELLAN_AXLAR\
                            - Krafter.luftmotstånd(self, self.bil.hastighet[-1])*self.bil.CENTER_AV_TRYCK_HÖJD/self.bil.AVSTÅND_MELLAN_AXLAR\
                            + Krafter.downforce(self, self.bil.hastighet[-1])*self.bil.CENTER_AV_TRYCK_LÄNGD/self.bil.AVSTÅND_MELLAN_AXLAR) / self.bana.GRAVITATION
        return viktförändring_fram
    
    def viktöverföring_bak(self, acceleration: float) -> float:
        """Viktöverföringen kalkyleras genom att räkna på den nuvarande vikten på bakaxeln"""
        viktförändring_bak = self.bil.MASSA_BIL - self.bil.MASSA_BIL*self.bil.CENTER_AV_MASSA_LÄNGD/self.bil.AVSTÅND_MELLAN_AXLAR + \
                            (+ self.bil.MASSA_BIL*acceleration*self.bil.CENTER_AV_MASSA_HÖJD/self.bil.AVSTÅND_MELLAN_AXLAR\
                            + Krafter.luftmotstånd(self, self.bil.hastighet[-1])*self.bil.CENTER_AV_TRYCK_HÖJD/self.bil.AVSTÅND_MELLAN_AXLAR\
                            + Krafter.downforce(self, self.bil.hastighet[-1])*(self.bil.AVSTÅND_MELLAN_AXLAR-self.bil.CENTER_AV_TRYCK_LÄNGD)/self.bil.AVSTÅND_MELLAN_AXLAR) / self.bana.GRAVITATION
        return viktförändring_bak
    
    def kraft_vid_pedal(self, normalkraft_bakaxel: float) -> float:
        """Kalkylerar kraften på bromspedalen"""
        diameter_huvud_cylinder     = 14/1000
        diameter_bromsok            = 25/1000
        area_huvud_cylinder         = np.pi*(diameter_huvud_cylinder/2)**2
        area_bromsok                = np.pi*(diameter_bromsok/2)**2
        radie_bromsskiva            = 0.08
        utväxling_hydraul           = area_bromsok/area_huvud_cylinder
        utväxling_bromsskiva_hjul   = radie_bromsskiva/self.bil.HJULRADIE
        utväxling_pedal             = 150/55
        friktionskoefficient        = 0.35

        kraft_pedal = normalkraft_bakaxel*self.bil.DÄCKFRIKTION/(2*utväxling_pedal*utväxling_hydraul*friktionskoefficient*utväxling_bromsskiva_hjul)
        return kraft_pedal

    def uppdatera_krafter(self, accel) -> None:
        """Uppdaterar listorna som innehåller informationen om krafterna för att kunna göra en graf"""
        self.bil.luftmotstånd.append(Krafter.luftmotstånd(self, self.bil.hastighet[-1]))
        self.bil.downforce.append(Krafter.downforce(self, self.bil.hastighet[-1]))
        self.bil.däckgrepp.append(Krafter.däckgrepp(self, self.bil.hastighet[-1]))
        self.bil.viktförändring_fram.append(Krafter.viktöverföring_fram(self, accel))
        self.bil.viktförändring_bak.append(Krafter.viktöverföring_bak(self, accel))

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