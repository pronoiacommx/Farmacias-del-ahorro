import tkinter as tk
import meraki
import sys
import os
from tkinter import *
import time

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
		self.general_checkbuttons = {}
		start_time = time.time()
		print(start_time)
		def restart():
			python = sys.executable
			os.execl(python, python, * sys.argv)
		lblTitle = tk.Label(self, text="Ingresa la clave API.")
		lblTitle.place(x=0,y=200)
		lblTitle.pack()
		iptAPI = tk.Entry(self)
		#BORRAR
		iptAPI.delete(0,END)
		#iptAPI.insert(0,"fbce215a1d79aa48a703201fa99435b26cd90c69")#DEV
		iptAPI.insert(0,"40fba9ff0596477f2b355d738b4d5922cc09d0fd")#PRDO
		iptAPI.pack()

		restart_button = tk.Button(self, text="Restart", command=restart)
		lblError = tk.Label(self, text="")
		#button1 = tk.Button(self, text="Buscar", command=lambda: controller.show_frame("ListCategories"))
		btnSearch = tk.Button(self, text="Buscar", command= lambda:validate(self) )#, command=lambda: buscar_redes(self))
		btnSearch.pack()    

		#lbl = tk.Label(self, pady=10, text="Se buscaran redes inalambricas\npara bloquear el acceso a url's.")
		#lbl = tk.Label(self, pady=10, text="")
		#lbl.pack()
		left_frame  =  Frame(self,  width=430,  height=200 ) #,  bg='grey')
		
		right_frame  =  Frame(self,  width=430,  height=200) #,  bg='grey')
		
		lblBlock = tk.Label(left_frame, pady=10, text="URL filtering Block")
		iptUrlBlock = tk.Entry(left_frame) 
		self.apiKey = ""

		lblDeny = tk.Label(left_frame, text="URL filtering Allow")
		iptUrlDeny = tk.Entry(left_frame)

		my_list= Listbox(right_frame, selectmode= MULTIPLE)

		my_list.pack(padx=10,pady=10,fill=tk.BOTH,expand=True)

		responseOrgs = []
		responseNet = []



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
			start_time = time.time()
			#fbce215a1d79aa48a703201fa99435b26cd90c69
			lblError.config(text="Cargando...", foreground="white", width=100)
			lblError.update_idletasks()
			lblError.pack()

			lblTitle.pack_forget()
			iptAPI.pack_forget()
			btnSearch.pack_forget()
			apiKey = iptAPI.get() #
			dashboard = meraki.DashboardAPI(apiKey)
			print ("***************************** Obteniendo Organizaciones ***************************** ")
			responseOrgs = dashboard.organizations.getOrganizations()
			orgsLen = str(len(responseOrgs))
			contadorDeOrganizaciones = 0;
			contadorDeRedes = 0;
			contadorDeTags = 0;
			tags = [];

			
		

			left_frame.pack(side='left',  fill='both',  padx=10,  pady=5,  expand=True)
			right_frame.pack(side='right',  fill='both',  padx=10,  pady=5,  expand=True)
		
			lblDeny.pack()
			iptUrlDeny.pack()  
			iptUrlDeny.delete(0,END)
			iptUrlDeny.insert(0,"10.0.1.11,10.0.1.13,10.0.1.22,10.0.1.23,10.0.1.75,10.0.1.77,10.0.1.78,10.0.1.94,10.0.1.103,10.0.1.104,10.0.1.128,10.0.1.132,10.0.1.134,10.0.1.136,10.0.1.140,10.0.1.137,172.25.7.1,172.20.33.81,172.20.33.82,172.25.5.1,172.25.5.5,172.25.5.17,192.168.152.17,10.81.9.203,172.20.18.161,192.168.69.162,10.81.11.203,172.20.205.1,172.17.1.146,172.25.8.2,10.0.1.5,10.0.1.34,10.0.1.43,10.0.1.64,10.0.1.66,10.0.1.172,10.0.1.175,10.0.1.246,10.0.1.247,10.0.1.248,172.17.0.13,10.0.1.17,10.0.1.45,10.0.1.72,200.77.232.123,10.0.1.87,172.20.205.10,172.20.18.161,200.57.95.33,10.0.1.111,10.0.1.79,10.0.1.80,172.16.0.151,172.17.0.167,172.16.0.26,200.53.163.168,200.57.93.35,200.53.163.169,200.57.136.10,172.25.8.45,23.3.28.217,200.53.186.36,fahorro.com,globaleysurvey.ey.com,support.fahorro.com.mx,facturas.fahorro.com.mx,doc2sign.com,som.fahorro.com.mx,pos.monederodelahorro.net,fahorromex103.ad.fahorro.com.mx:6016,afiliacion.monederodelahorro.net,meet.google.com,welsfargo.com-onlinebanking.com,office.strongencryption.org,34.237.206.61,psm.economia.gob.mx,googleadservices.com,doubleclick.net,172.217.12.66,172.217.195.154,cfdi.uberfacturas.com,uber.com,store-manager.fahorro.com.mx,fahorro.com,docs.google.com,dl.google.com,apps-apis.google.com,google.com,googleapis.com,mail.google.com,calendar.google.com,spreadsheets.google.com,ajax.googleapis.com,blob-s-docs.googlegroups.com,chart.apis.google.com,linkedin.com,groups.google.com,ssl.google-analytics.com,gg.google.com,ssl.gstatic.com,feedserver-enterprise.googleusercontent.com,gmodules.com,aspmx.l.google.com.,sites.google.com,talk.google.com,imap.gmail.com,pop.gmail.com,smtp.gmail.com,apps-apis.google.com,psmtp.com,accounts.google.com,googleapis.com,crl.geotrust.com,g.symcb.com,pki.google.com,g.symcd.com,clients1.google.com,dl.google.com,apps-apis.google.com,google.com,googleapis.com,calendar.google.com,spreadsheets.google.com,ajax.googleapis.com,blob-s-docs.googlegroups.com,chart.apis.google.com,groups.google.com,ssl.google-analytics.com,gg.google.com,ssl.gstatic.com,feedserver-enterprise.googleusercontent.com,gmodules.com,aspmx.l.google.com.,sites.google.com,talk.google.com,imap.gmail.com,pop.gmail.com,smtp.gmail.com,apps-apis.google.com,psmtp.com,accounts.google.com,crl.geotrust.com,g.symcb.com,pki.google.com,g.symcd.com,clients1.google.com,drive.google.com,drive.google.com,sheets.google.com,slides.google.com,takeout.google.com,script.google.com,s.ytimg.com,apis.google.com,googleusercontent.com,gstatic.com,lh[N].google.com,[N].client-channel.google.com,clients[N].google.com,sites.google.com,sites.google.com,googlegroups.com,gmail.com,googleapis.com,gstatic.com,googleusercontent.com,google-analytics.com,googledrive.com,ytimg.com,googlegroups.com,googledrive.com,gartner.com,gartner.com,expansion.fahorro.com.mx,kpionline10.bitam.com,kpionline10.bitam.com/eBavel602/app/fbm_bmd_0070/BAPP0FB2D58E/login,kpionline10.bitam.com/eBavel602/app/fbm_bmd_0070/BAPP3823E51C,portalmx.infonavit.org.mx,infonavit.org.mx,banorte.com,web.whatsapp.com,googleadservices.com,meet.google.com,meet.google.com,drive.google.com,sites.google.com,psm.economia.gob.mx/PSM/,psm.economia.gob.mx,fahorro.tmanager.com.mx/LogIn.aspx,siana.telmex.com/siana/accesoTlmx.view,fahorroxen.jdadelivers.com/Citrix/XenApp/site/default.aspx,detectportal.firefox.com/success.txt,gasweb.oxxogas.com/Facturacion/Account/Login.aspx,m2.fahorro.com,dropbox.com/sh/dri2m26z94ohy9i/AADiWbAbGV4v6INEAdbHqom2a?dl=0,m2.fahorro.com,fahorro.tmanager.com.mx/LogIn.aspx,cloud.acrobat.com/acrobat,cloud.acrobat.com/acrobat,adfs.fahorro.com.mx,adfs.fahorro.com.mx,qlik.fahorro.com.mx/hub/stream/aaec8d41-5201-43ab-809f-3063750dfafd?qlikTicket=7NsxOirLEQb1jfLR,administraciondepracticantes.com,fishers.libellum.com.mx,187.191.75.170/SICAD/(S(c1ozx3ckgxlrwhwb5blz3arm))/WebMain.aspx,doctoranytime.mx,suite.netpay.com.mx,forms.gle/LPw3D9mALfjB1LZb9,centrodeeducaciondigital-fa.com,rp-farmacia-ahorro.batuta.io/auth,cdn-batuta.nyc3.digitaloceanspaces.com,cdn-batuta.nyc3.cdn.digitaloceanspaces.com,pairing.rport.io,api.batuta.io")
			
			lblBlock.pack()
			iptUrlBlock.pack()  
			iptUrlBlock.delete(0,END)
			iptUrlBlock.insert(0,"https://l.ead.me/bditrh,me.com.mx,l.ead.me.com.mx,https://l.ead.me,youtube.com,surveynuts.com,spotify.com,cinecalidad.is,es-la.facebook.com,facebook.com,snapchat.com,twitter.com,instagram.com,validaciones.com,sputnikradio.net,xmlformats.com,exchange.oufca.com.au,141.98.215.99,tibet-gov.web.app,fahorrobuctemp.blob.core.windows.net,dagh6jds.blob.core.windows.net,sd4ygdsadghhfdsfgr.blob.core.windows.net,blob.core.windows.net,baonguyenphoto.com,185.53.46.131")
			
			btnAceptar = tk.Button(self, text="Aceptar", command=lambda: cargar_urls(self))
			btnAceptar.pack() 
			print(apiKey)

			

			if len(responseOrgs) > 1:
				print ("***************************** Se encontraron " + orgsLen + " organizaciones ***************************** ")
			else:
				print ("***************************** Se encontro " + orgsLen + " organizacion ***************************** ")
			# print(responseOrgs[0])
			# responseOrgs = [responseOrgs[0]]			
			print(responseOrgs)

			for org in responseOrgs:
				organizationId = org['id']
				contadorDeOrganizaciones += 1
				print ("***************************** ORGANIZACION " + str(contadorDeOrganizaciones) + " ID: " + organizationId + " NOMBRE: " + org['name'] + " *****************************")
				responseNet = dashboard.organizations.getOrganizationNetworks(organizationId, perPage=2000, tags=["FW16.16.7"])
				
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
				responseNetAux = [];
				responseNetAux.append(responseNet[1])
				
				print(responseNetAux)
				for net in responseNetAux:
					contadorDeRedes += 1        
					print(net['name'] + " Numero de red: " + str(contadorDeRedes))    
					#print("Al inicio tenemos " + str(len(responseCat['categories'])) + "responseCat")
					print(net)
					for productype in net['productTypes']: 	
						print(productype)
						if productype == 'switch' or productype ==  'wireless':
							print("*****************productype NULL************")
							print(net['name'])  

						else:

							responseCat = dashboard.appliance.getNetworkApplianceContentFilteringCategories(net['id'])
							for cat in responseCat['categories']:
								#print(cat['id'] + cat['name'])
								#responseCatList.append([cat['id'], cat['name']])
								if cat['name'] not in responseCatListAux:
									responseCatListAux.append(cat['name'])
									responseCatList.append([cat['id'], cat['name']])
							#print(responseCat)
							if net['tags'] == []:
								print("*****************NULL************")
							else:
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
					



					if contadorDeTags >= 0 and contadorDeTags < 3: #0,1,2,3
						x = 150 * (contadorDeTags + 1)
						
					if contadorDeTags > 2 and contadorDeTags < 6: #4,5,6,7
						x = 150 * (contadorDeTags - 2)
						k=1
						y= y + (50 *k)
					if contadorDeTags > 5 and contadorDeTags < 9: #8,9,10,11
						x = 150 * (contadorDeTags - 5)
						k=2
						y= y + (50 *k)
					if contadorDeTags > 8 and contadorDeTags < 12:
						x = 150 * (contadorDeTags - 8)
						k=3
						y= y + (50 *k)
					if contadorDeTags > 11 and contadorDeTags < 15:
						x = 150 * (contadorDeTags - 11)
						k=4
						y= y + (50 *k)
					if contadorDeTags > 14 and contadorDeTags < 18:
						x = 150 * (contadorDeTags - 14)
						k=5
						y= y + (50 *k)
					if contadorDeTags > 19 and contadorDeTags < 21:
						x = 150 * (contadorDeTags - 19)
						k=6
						y= y + (50 *k)
					if contadorDeTags > 20 and contadorDeTags < 24:
						x = 150 * (contadorDeTags - 20)
						k=7
						y= y + (50 *k)
					 
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

			lblError.config(text="Selecciona los tags que se necesiten", width=100)
			lblError.update_idletasks()
			
			#Now iterate over the list
			#responseCatList.sort()
			responseCatListAux = []
			for item in responseCatList:
				#my_list.insert(END,str(item['id']) + str(item['name']))
				#print(item)
				#print(item['id'])
				valor= str(item[1]) +"_"+ str(item[0])
				responseCatListAux.append(valor)
				#print(valor)
			responseCatListAux.sort()
			#print(responseCatListAux)
			for item in responseCatListAux:
				my_list.insert(END,item)

			print("--- %s seconds ---" % ((time.time() - start_time)/60))
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
				print(self.general_checkbuttons[k][1])
				if(self.general_checkbuttons[k][1].get()==True): # checkbox is checked 
					self.general_checkbuttons[k][0].config(fg='green')
				else: # Checkbox is unchecked
					self.general_checkbuttons[k][0].config(fg='white')

			def cargar_urls(self):
				print('checkbutton values')
				arraySelectedTags = []
				arraySelectedCategories = []
				for key, value in self.general_checkbuttons.items():
					if value[1].get():
						arraySelectedTags.append(self.general_checkbuttons[key][0]['text'])
						print(self.general_checkbuttons[key][0]['text'])
				
				for i in my_list.curselection():
					arraySelectedCategories.append(my_list.get(i).split('_')[1])
					#print(my_list.get(i).split('_')[1])
				print(arraySelectedCategories)
				dashboard = meraki.DashboardAPI(apiKey)
				print ("***************************** Obteniendo Organizaciones ***************************** ")
				responseOrgs = dashboard.organizations.getOrganizations()
				if len(responseOrgs) > 1:
					print ("***************************** Se encontraron " + orgsLen + " organizaciones ***************************** ")
				else:
					print ("***************************** Se encontro " + orgsLen + " organizacion ***************************** ")
				# print(responseOrgs[0])
				# responseOrgs = [responseOrgs[0]]			
				print(responseOrgs)
				contadorDeRedesAux = 0
				for org in responseOrgs:
					organizationId = org['id']
					#responseNet = dashboard.organizations.getOrganizationNetworks(organizationId)
					print("selected tags " + str(arraySelectedTags)) 

					allowedUrlPatterns = iptUrlDeny.get().split(",")
					blockedUrlPatterns = iptUrlBlock.get().split(",")
					for net in responseNet:   
						
						contadorDeRedesAux += 1           
						#print(net['tags']) 
						# if net['tags'] == []:
						# 	print("*****************NULL************")
						# else:
						# 	for tag in net['tags']: 
						# 		if tag in arraySelectedTags:  
						# print("*************VALORES*************")  
						# print(net)     
						# print("*************VALORES*************")  
						# print(iptUrlDeny.get().split(","))   
						# print(iptUrlBlock.get().split(","))   
						#blockedUrlCategories = arraySelectedCategories#[]#['meraki:contentFiltering/category/1', 'meraki:contentFiltering/category/7'] 
						urlCategoryListSize = "topSites"
						print(net)
						response = dashboard.appliance.updateNetworkApplianceContentFiltering(
							net['id'], 
							allowedUrlPatterns= allowedUrlPatterns,
							blockedUrlPatterns=blockedUrlPatterns, 
							#blockedUrlCategories= blockedUrlCategories, 
							blockedUrlCategories= ['meraki:contentFiltering/category/68', 'meraki:contentFiltering/category/10', 'meraki:contentFiltering/category/11', 'meraki:contentFiltering/category/67', 'meraki:contentFiltering/category/70', 'meraki:contentFiltering/category/18', 'meraki:contentFiltering/category/27', 'meraki:contentFiltering/category/34', 'meraki:contentFiltering/category/33', 'meraki:contentFiltering/category/46', 'meraki:contentFiltering/category/64', 'meraki:contentFiltering/category/49', 'meraki:contentFiltering/category/56', 'meraki:contentFiltering/category/60', 'meraki:contentFiltering/category/62', 'meraki:contentFiltering/category/73', 'meraki:contentFiltering/category/31', 'meraki:contentFiltering/category/47', 'meraki:contentFiltering/category/57', 'meraki:contentFiltering/category/58', 'meraki:contentFiltering/category/44', 'meraki:contentFiltering/category/71', 'meraki:contentFiltering/category/30', 'meraki:contentFiltering/category/14', 'meraki:contentFiltering/category/59', 'meraki:contentFiltering/category/48', 'meraki:contentFiltering/category/36', 'meraki:contentFiltering/category/52'], 
							#blockedUrlCategories17= ['meraki:contentFiltering/category/64','meraki:contentFiltering/category/10','meraki:contentFiltering/category/11','meraki:contentFiltering/category/67','meraki:contentFiltering/category/70','meraki:contentFiltering/category/18','meraki:contentFiltering/category/27','meraki:contentFiltering/category/34','meraki:contentFiltering/category/33','meraki:contentFiltering/category/46','meraki:contentFiltering/category/64','meraki:contentFiltering/category/49','meraki:contentFiltering/category/56','meraki:contentFiltering/category/60','meraki:contentFiltering/category/62','meraki:contentFiltering/category/73','meraki:contentFiltering/category/31','meraki:contentFiltering/category/47','meraki:contentFiltering/category/57','meraki:contentFiltering/category/58','meraki:contentFiltering/category/44','meraki:contentFiltering/category/30','meraki:contentFiltering/category/59','meraki:contentFiltering/category/48','meraki:contentFiltering/category/36','meraki:contentFiltering/category/52'], 
							urlCategoryListSize=urlCategoryListSize
						)   
						print("Listo " + str(contadorDeRedesAux))
						# aBlockedUrl = " - ".join(blockedUrlPatterns)
						# print("+++++ SE BLOQUEARON LAS URL: " + aBlockedUrl + " +++++")
						# aAllowed = " - ".join(allowedUrlPatterns)
						# print("+++++ SE DESBLOQUEARON LAS URL: " + aAllowed + " +++++")
						# aBlockedCategories = " - ".join(blockedUrlCategories)
						# print("+++++ SE DESBLOQUEARON LAS CATEGORIAS: " + aBlockedCategories + " +++++")
						# print("+++++ LISTA: " + urlCategoryListSize + " +++++")
							
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
	app.geometry("1000x550")
	app.mainloop()