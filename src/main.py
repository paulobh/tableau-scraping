from tableauscraper import TableauScraper as TS

# url = "https://tableau.ons.org.br/t/ONS_Publico/views/DemandaMxima/HistricoDemandaMxima"
url = "https://tableau.ons.org.br/t/ONS_Publico/views/CargadeEnergia/HistricoCargadeEnergia"
# params = {
#     ":embed": "y",
#     ":display_count": "n",
#     ":tab": "no",
#     ":showAppBanner": "false",
#     ":showVizHome": "n",
#     ":origin": "viz_share_link"
# }

ts = TS()
# ts.loads(url, params=params)
ts.loads(url)
wb = ts.getWorkbook()

print(wb.getStoryPoints())
# print("go to specific storypoint")
sp = wb.goToStoryPoint(storyPointId=5)

# sp = sp.setParameter("Escala de Tempo CE Simp 4", "Dia")
sp = sp.setParameter("Escala de Tempo CE Comp 3", "Dia")

# show parameters values / column
# parameters = sp.getParameters()
# print(parameters)

# # Set units
# sp = sp.setParameter("Selecione CE Comp 3", "Carga de Energia (MWmed)")
# sp = sp.setParameter("Selecione CE Simp 4", "Carga de Energia (MWmed)")

# Set time resolution
# sp = sp.setParameter("Escala de Tempo CE Comp 3", "Dia")
sp = sp.setParameter("Escala de Tempo CE Simp 4", "Dia")


# # Set the start date
sp = sp.setParameter("Início Primeiro Período CE Comp 3", "01/01/2022")
# sp.setParameter("Início Primeiro Período CE Simp 4", "01/01/2022")

# Set the end date
sp = sp.setParameter("Fim Primeiro Período CE Comp 3", "30/06/2022")
# sp = sp.setParameter("Fim Primeiro Período CE Simp 4", "30/06/2022")


print(sp.getWorksheetNames())
for t in sp.worksheets:
    print(f"worksheet name : {t.name}") #show worksheet name
    print(t.data) #show dataframe for this worksheet

# Retrieve worksheet
# ws = sp.getWorksheet("Comparativo Carga de Energia Mês")
# ws = ts.getWorksheet("Comparativo Carga de Energia Semana")
ws = ts.getWorksheet("Comparativo Carga de Energia Dia Hora")
# ws = ts.getWorksheet("CE Dias Comp 3")

# show selectable values
selections = sp.getSelectableItems()
print(selections)

print(ws.data[['Data Escala de Tempo 1 DM Simp 4-value',
               'SOMA(Selecione Tipo de DM Simp 4)-value', 'ATRIB(Subsistema)-alias']])

print(ws.data[['Data Escala de Tempo 1 DM Simp 4-value',
               'SOMA(Selecione Tipo de DM Simp 4)-value', 'ATRIB(Subsistema)-alias']])

ws = wb.getWorksheet("Simples Demanda Máxima Ano")
print(ws.getFilters())

# Select subsystem
wb = ws.setFilter("Subsistema", "N")
ws = wb.getWorksheet("Simples Demanda Máxima Semana Dia")

print(ws.data[['Data Escala de Tempo 1 DM Simp 4-value',
               'SOMA(Selecione Tipo de DM Simp 4)-value', 'ATRIB(Subsistema)-alias']])









url = 'https://tableau.ons.org.br/t/ONS_Publico/views/DemandaMxima/HistricoDemandaMxima'
ts = TS()
ts.loads(url)

wb = ts.getWorkbook()

# switch to daily
wb = wb.setParameter("Escala de Tempo DM Simp 4", "Dia")

# dataframe with daily data
ws = wb.getWorksheet("Simples Demanda Máxima Semana Dia")
print(ws.data)

# Set units
wb.setParameter("Selecione DM Simp 4", "Demanda Máxima Instântanea (MW)")

# Set to daily resolution
wb.setParameter("Escala de Tempo DM Simp 4", "Dia")

# # Set the start date
wb.setParameter("Início Primeiro Período DM Simp 4", "01/01/2017")

# Set the end date
wb = wb.setParameter("Fim Primeiro Período DM Simp 4", "31/12/2017")

# Retrieve daily worksheet
ws = wb.getWorksheet("Simples Demanda Máxima Semana Dia")
