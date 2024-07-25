from GUI.config import windowsconfig
from GUI.frames.areaframe import *


from typing import Literal
import customtkinter as ctk


class Falcon:
    
    def __init__(self, *ctk_instancia:object, status:Literal['X',"OK"], message:str,windowTitle:str=None, color_appearance:Literal['light','dark']='light') -> None:
        # Objetos
        #------------------------------
        self.master = None
        self.ctk_instancia = ctk_instancia
        self.color_appearance = color_appearance
        self.message = message
        self.status = status.upper()
        self.windowTitle = windowTitle if not windowTitle == None else status
        #------------------------------
        
        self.run()
        
        
    def run(self):
        self.__config_GUI_inicializacao()
        FQ = FrameQuadro(self)
        
        self.master.mainloop()
        
    
    def __config_GUI_inicializacao(self):
        if not self.ctk_instancia:
            self.master = ctk.CTk() 
        else:
            self.master = self.ctk_instancia.CTkToplevel(self.master)

        self.master.title(self.windowTitle)

        self.total_weight = self.master.winfo_screenwidth()
        self.total_height = self.master.winfo_screenheight()  
        
        
        x = (self.total_weight - int(windowsconfig.WINDOW_SIZE.split('x')[0])) // 2
        y = ((self.total_height - int(windowsconfig.WINDOW_SIZE.split('x')[1])) - 100) // 2
        windowsconfig.WINDOW_POSITION = '+'.join([str(x),str(y)])
        
        ctk.set_appearance_mode(self.color_appearance)
        
        self.master.geometry(f'{windowsconfig.WINDOW_SIZE}+{windowsconfig.WINDOW_POSITION}')
        self.master.resizable(False, False)
        
        
    def destroy(self):
        self.master.destroy()