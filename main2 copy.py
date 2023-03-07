import tkinter as tk
import meraki
import sys
import os
from tkinter import *

class SampleApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage,StartPage):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    # alternate version of show_frame: comment out one or the other

    def show_frame(self, page_name):
        for frame in self.frames.values():
            frame.grid_remove()
        
        print(page_name)
        print(self.frames)
        frame = self.frames[page_name]
        frame.grid()


class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

    buscador2 = LabelFrame(self, text="Buscador 2", padx=100, pady=100)
    buscador2.grid(row=1,column=0,padx=5, pady=5)

    barra2 = Entry(buscador2, text="¿Buscas algo?").grid(row=0, column=0)
    boton2 = Button(buscador2, text="Buscar").grid(row=0, column=1)


class StartPage1(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.general_checkbuttons = {}

        def restart():
            python = sys.executable
            os.execl(python, python, * sys.argv)

        lblTitle = tk.Label(self, text="Ingresa la clave API.")
        lblTitle.place(x=0,y=200)
        lblTitle.pack()
        iptAPI = tk.Entry(self)
        iptAPI.pack()

        restart_button = tk.Button(self, text="Restart", command=restart)
        lblError = tk.Label(self, text="")
        #button1 = tk.Button(self, text="Buscar", command=lambda: controller.show_frame("ListCategories"))
        btnSearch = tk.Button(self, text="Buscar", command= lambda:validate(self) )#, command=lambda: buscar_redes(self))
        btnSearch.pack()    

        #lbl = tk.Label(self, pady=10, text="Se buscaran redes inalambricas\npara bloquear el acceso a url's.")
        #lbl = tk.Label(self, pady=10, text="")
        #lbl.pack()

        lblBlock = tk.Label(self, pady=10, text="URL filtering Block")
        iptUrlBlock = tk.Entry(self) 
        self.apiKey = ""

        lblDeny = tk.Label(self, text="URL filtering Allow")
        iptUrlDeny = tk.Entry(self)

        my_list= Listbox(self, selectmode= MULTIPLE)

        my_list.pack()

        buscador2 = LabelFrame(self, text="Buscador 2", padx=100, pady=100)
        buscador2.grid(row=1,column=0,padx=5, pady=5)

        barra2 = Entry(buscador2, text="¿Buscas algo?").grid(row=0, column=0)
        boton2 = Button(buscador2, text="Buscar").grid(row=0, column=1)




        #metodo para validar el text
        def show_message(self, error='', color='white'):
            print("Entra a show message")
            print(error)
            print(color)
            lblError.pack()
            lblError['text'] = error
            lblError['foreground'] = color

        def validate(self):
            """
            Validat the email entry
            :param value:
            :return:
            """
            print("Entra a validar")
            value = iptAPI.get()
            #pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
            #if re.fullmatch(pattern, value) is None:
            if len(value) < 1:
                show_message(self, error="Tienes que ingresar la API", color="red")
            else:
                buscar_redes(self)

        def on_invalid(self):
            """
            Show the error message if the data is not valid
            :return:
            """
            self.show_message('Please enter a valid email', 'red')
        vcmd = (self.register(validate), '%P')
        ivcmd = (self.register(on_invalid),)
        #iptAPI.config(validate='focusout', validatecommand=vcmd, invalidcommand=ivcmd)
        # /metodo para validar el text

        

        def buscar_redes(self):
            #fbce215a1d79aa48a703201fa99435b26cd90c69
            lblError.config(text="Cargando...", foreground="white", width=100)
            lblError.update_idletasks()
            lblTitle.pack_forget()
            iptAPI.pack_forget()
            btnSearch.pack_forget()
            apiKey = "fbce215a1d79aa48a703201fa99435b26cd90c69"# iptAPI.get() #
            dashboard = meraki.DashboardAPI(apiKey)
            print ("***************************** Obteniendo Organizaciones ***************************** ")
            responseOrgs = dashboard.organizations.getOrganizations()
            orgsLen = str(len(responseOrgs))
            contadorDeOrganizaciones = 0;
            contadorDeRedes = 0;
            contadorDeTags = 0;
            tags = [];

            
            lblError.config(text="Selecciona los tags que se necesiten", width=100)
            lblError.update_idletasks()

            lblDeny.pack()
            iptUrlDeny.pack(fill='x', expand=1)  

            lblBlock.pack()
            iptUrlBlock.pack(fill='x', expand=1)  

            btnAceptar = tk.Button(self, text="Aceptar", command=lambda: cargar_urls(self))
            btnAceptar.pack() 
            print(apiKey)

            

            if len(responseOrgs) > 1:
                print ("***************************** Se encontraron " + orgsLen + " organizaciones ***************************** ")
            else:
                print ("***************************** Se encontro " + orgsLen + " organizacion ***************************** ")
            for org in responseOrgs:
                organizationId = org['id']
                contadorDeOrganizaciones += 1
                print ("***************************** ORGANIZACION " + str(contadorDeOrganizaciones) + " ID: " + organizationId + " NOMBRE: " + org['name'] + " *****************************")
                responseNet = dashboard.organizations.getOrganizationNetworks(organizationId)
                
#                 print ("***************************** Categorias " + str(contadorDeOrganizaciones) + " ID: " + organizationId + " NOMBRE: " + org['name'] + " *****************************")
#                 responseCat = dashboard.appliance.getNetworkApplianceContentFilteringCategories(
#     network_id
# )
                netLen = str(len(responseNet))
                if len(responseNet) > 1:    
                    print ("***************************** Se encontraron " + netLen + " NETWORKS DE LA ORGANIZACION " + str(contadorDeOrganizaciones) + " " + org['name'] + " ***************************** ")
                else:
                    print ("***************************** Se encontro " + netLen + " NETWORK DE LA ORGANIZACION " + str(contadorDeOrganizaciones) + " " + org['name'] + " ***************************** ")
                responseCatListAux = [];
                responseCatList = [];
                responseNetAux = responseNet[1]
                for net in responseNetAux:
                    contadorDeRedes += 1            
                    responseCat = dashboard.appliance.getNetworkApplianceContentFilteringCategories(net['id'])
                    #print("Al inicio tenemos " + str(len(responseCat['categories'])) + "responseCat")
                    for cat in responseCat['categories']:
                        #print(cat['id'] + cat['name'])
                        #responseCatList.append([cat['id'], cat['name']])
                        if cat['name'] not in responseCatListAux:
                            responseCatListAux.append(cat['name'])
                            responseCatList.append([cat['id'], cat['name']])
                    #print(responseCat)
                    if net['tags'] not in tags:
                        #print("***** Se agrego" + str(net['tags']))
                        if len(net['tags']) > 1:
                            #print("***** entro" + str(net['tags']))
                            for _tag in net['tags']:
                                if _tag not in tags:
                                    tags.append(_tag)
                        else:        
                            tags.append(net['tags'])
                print(tags)
                print(str(len(tags)))
                for i in range(1,len(tags)+1):
                    y=200
                    x= 150
                    



                    if contadorDeTags >= 0 and contadorDeTags < 4: #0,1,2,3
                        x = 150 * (contadorDeTags + 1)
                        
                    if contadorDeTags > 3 and contadorDeTags < 8: #4,5,6,7
                        x = 150 * (contadorDeTags - 3)
                        i=1
                        y= y + (50 *i)
                    if contadorDeTags > 7 and contadorDeTags < 12: #8,9,10,11
                        x = 150 * (contadorDeTags - 7)
                        i=2
                        y= y + (50 *i)
                    if contadorDeTags > 11 and contadorDeTags < 16:
                        x = 150 * (contadorDeTags - 11)
                        i=3
                        y= y + (50 *i)
                    if contadorDeTags > 15 and contadorDeTags < 20:
                        x = 150 * (contadorDeTags - 15)
                        i=4
                        y= y + (50 *i)
                    if contadorDeTags > 19 and contadorDeTags < 24:
                        x = 150 * (contadorDeTags - 19)
                        i=5
                        y= y + (50 *i)
                    if contadorDeTags > 23 and contadorDeTags < 28:
                        x = 150 * (contadorDeTags - 23)
                        i=6
                        y= y + (50 *i)
                    if contadorDeTags > 27 and contadorDeTags < 32:
                        x = 150 * (contadorDeTags - 27)
                        i=7
                        y= y + (50 *i)
                     
                    print(str(contadorDeTags) + " x: " +str(x)+" y: "+ str(y) + " " + str(tags[contadorDeTags]))

                    #print(x)
                    #setattr(self.general_checkbuttons, tags[i],tk.IntVar()) 
                    var=tk.BooleanVar()
                    ck = tk.Checkbutton(self, text=tags[contadorDeTags], 
                        onvalue=True, offvalue=False, variable= var, command=lambda k=i: my_upd(k))
                    ck.place(x=x, y=y)
                    self.general_checkbuttons[i] = [ck,var]

                    contadorDeTags += 1
                    #print(str(i)+".- "+str(c))
                #if not net['isBoundToConfigTemplate']:
                    #print(net['tags'])
                        #print("***************************** NETWORK: " + str(contadorDeRedes) + " ID: " + net['id'] + " DE LA ORGANIZACION " + str(contadorDeOrganizaciones) + " " + org['name'] + " ***************************** ")
                    networkId = net   
            #print("Al final tenemos " + str(len(responseCatList)) + "responseCat")

            
            #Now iterate over the list
            responseCatList.sort()
            for item in responseCatList:
                #my_list.insert(END,str(item['id']) + str(item['name']))
                #print(item)
                #print(item['id'])
                valor= str(item[1]) +"_"+ str(item[0])
                print(valor)
                my_list.insert(END,valor)

            #my_list.pack()
            #print(responseCatList)   
                #print(tags)
            def addList(self):
                for i in range(1, self.height):
                    cb = self.general_checkbuttons[i]
                    varname = cb.cget("variable")
                    value = self.root.getvar(varname)
                    print(f"{i}: {value}")
            
            def my_upd(k): # k is the key of the reference dictionary 
                print("Entra")
                print(self.general_checkbuttons[k][1].get())
                if(self.general_checkbuttons[k][1].get()==True): # checkbox is checked 
                    self.general_checkbuttons[k][0].config(fg='green')
                else: # Checkbox is unchecked
                    self.general_checkbuttons[k][0].config(fg='white')

            
            def cargar_urls(self):
                print('checkbutton values')
                arraySelectedTags = []
                for key, value in self.general_checkbuttons.items():
                    if value[1].get():
                        arraySelectedTags.append(self.general_checkbuttons[key][0]['text'])
                        print(self.general_checkbuttons[key][0]['text'])
                
                dashboard = meraki.DashboardAPI(apiKey)
                print ("***************************** Obteniendo Organizaciones ***************************** ")
                responseOrgs = dashboard.organizations.getOrganizations()
                if len(responseOrgs) > 1:
                    print ("***************************** Se encontraron " + orgsLen + " organizaciones ***************************** ")
                else:
                    print ("***************************** Se encontro " + orgsLen + " organizacion ***************************** ")
                for org in responseOrgs:
                    organizationId = org['id']
                    responseNet = dashboard.organizations.getOrganizationNetworks(organizationId)
                    print("selected tags " + str(arraySelectedTags)) 
                    for net in responseNet:         
                        #print(net['tags'])     
                        if net['tags'][0] in arraySelectedTags:  
                            print(net['id'])     
                            print("*************VALORES*************")  
                            print(iptUrlDeny.get().split(","))   
                            print(iptUrlBlock.get().split(","))   
                            allowedUrlPatterns = iptUrlDeny.get().split(",")
                            blockedUrlPatterns = iptUrlBlock.get().split(",")
                            blockedUrlCategories = []#['meraki:contentFiltering/category/1', 'meraki:contentFiltering/category/7'] 
                            urlCategoryListSize = "topSites"
                            response = dashboard.appliance.updateNetworkApplianceContentFiltering(
                                net['id'], 
                                allowedUrlPatterns= allowedUrlPatterns,
                                blockedUrlPatterns=blockedUrlPatterns, 
                                blockedUrlCategories= blockedUrlCategories, 
                                urlCategoryListSize=urlCategoryListSize
                            )   
                            aBlockedUrl = " - ".join(blockedUrlPatterns)
                            print("+++++ SE BLOQUEARON LAS URL: " + aBlockedUrl + " +++++")
                            aAllowed = " - ".join(allowedUrlPatterns)
                            print("+++++ SE DESBLOQUEARON LAS URL: " + aAllowed + " +++++")
                            aBlockedCategories = " - ".join(blockedUrlCategories)
                            print("+++++ SE DESBLOQUEARON LAS CATEGORIAS: " + aBlockedCategories + " +++++")
                            print("+++++ LISTA: " + urlCategoryListSize + " +++++")
                            
                print("TERMINA")


                lblError.config(text="Se actualizarón la redes con las tags: " + str(arraySelectedTags), foreground="green", width=100)
                lblError.pack()
                lblError.update_idletasks()
                btnAceptar.pack_forget()
                restart_button.pack()
        

# class ListCategories(tk.Frame):
#     def __init__(self, parent, controller):
#         tk.Frame.__init__(self, parent)
#         self.controller = controller
#         label = tk.Label(self, text="Enter something below; the two buttons clear what you type.")
#         label.pack(side="top", fill="x", pady=10)
#         self.wentry = tk.Entry(self)
#         self.wentry.pack(pady = 10)
#         self.text = tk.Text(self)
#         self.text.pack(pady = 10)
#         restart_button = tk.Button(self, text="Restart", command=self.restart)
#         restart_button.pack()
#         refresh_button = tk.Button(self, text="Refresh", command=self.refresh) 
#         refresh_button.pack()  

#     def restart(self):
#         self.refresh()
#         #self.controller.show_frame("StartPage")

#     def refresh(self):
#         self.wentry.delete(0, "end")
#         self.text.delete("1.0", "end")
#         # set focus to any widget except a Text widget so focus doesn't get stuck in a Text widget when page hides
#         self.wentry.focus_set()

if __name__ == "__main__":
    app = SampleApp()
    app.title('Farmacias del ahorro')
    app.geometry("850x550")
    app.mainloop()