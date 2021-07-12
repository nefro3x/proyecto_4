Fecha=["2021-07-09"]
rango_etareo_m_0a4 =[21306,21611,21920,22179,22423,22596,22853]
rango_etareo_m_5a9 =[23087,23431,23786,24093,24350,24577,24858]
rango_etareo_m_10a14=[29681,30147,30631,31041,31427,31732,32078]
rango_etareo_m_15a19=[45275,46039,46740,47290,47814,48181,48621]
rango_etareo_m_20a24=[80389,81416,82376,83172,83869,84397,84988]
rango_etareo_m_25a29=[106534,107695,108775,109637,110415,110980,111643]
rango_etareo_m_30a34=[106742,107861,108945,109811,110605,111188,111839]
rango_etareo_m_35a39=[87029,87957,88837,89525,90120,90569,91144]
rango_etareo_m_40a44=[72802,73535,74263,74832,75380,75802,76311]
rango_etareo_m_45a49=[69078,69694,70361,70857,71344,71726,72114]
rango_etareo_m_50a54=[63349,63964,64521,65003,65434,65770,66155]
rango_etareo_m_55a59=[58809,59343,59869,60313,60726,61057,61446]
rango_etareo_m_60a64=[43978,44464,44959,45344,45717,46019,46368]
rango_etareo_m_65a69=[28345,28692,29082,29392,29657,29880,30139]
rango_etareo_m_70a74=[19565,19831,20125,20355,20556,20743,20961]
rango_etareo_m_75a79=[13634,13812,13992,14154,14318,14461,14580]
rango_etareo_m_80o=[15961,16152,16378,16575,16750,16895,17052]
rango_etareo_f_0a4=[19271,19531,19804,20022,20225,20406,20612]
rango_etareo_f_5a9=[22222,22560,22872,23185,23468,23693,23931]
rango_etareo_f_10a14=[31230,31762,32268,32688,33118,33440,33785]
rango_etareo_f_15a19=[50972,51791,52556,53115,53693,54143,54594]
rango_etareo_f_20a24=[85067,86143,87143,87949,88727,89287,89909]
rango_etareo_f_25a29=[107293,108498,109756,110659,111534,112194,112862]
rango_etareo_f_30a34=[101747,102866,104021,104891,105798,106401,107079]
rango_etareo_f_35a39=[82222,83215,84137,84846,85504,86058,86632]
rango_etareo_f_40a44=[70582,71378,72112,72715,73289,73749,74208]
rango_etareo_f_45a49=[69251,69934,70651,71182,71692,72116,72543]
rango_etareo_f_50a54=[64564,65172,65807,66341,66860,67278,67692]
rango_etareo_f_55a59=[59085,59651,60250,60758,61223,61603,62026]
rango_etareo_f_60a64=[43276,43786,44343,44765,45174,45516,45903]
rango_etareo_f_65a69=[28738,29093,29482,29784,30089,30324,30618]
rango_etareo_f_70a74=[20919,21182,21448,21693,21903,22072,22281]
rango_etareo_f_75a79=[15605,15809,16027,16184,16344,16485,16635]
rango_etareo_f_80o=[24492,24772,25093,25367,25635,25858,26115]
contagios_total_M=[]
contagios_total_F=[]
p=[]
contagios_total_M.append(rango_etareo_m_0a4[6]+rango_etareo_m_5a9[6]+rango_etareo_m_10a14[6]+rango_etareo_m_15a19[6]+rango_etareo_m_20a24[6]+
                         rango_etareo_m_25a29[6]+rango_etareo_m_30a34[6]+rango_etareo_m_35a39[6]+rango_etareo_m_40a44[6]+rango_etareo_m_45a49[6]+
                         rango_etareo_m_50a54[6]+rango_etareo_m_55a59[6]+rango_etareo_m_60a64[6]+rango_etareo_m_65a69[6]+rango_etareo_m_70a74[6]+
                         rango_etareo_m_75a79[6]+rango_etareo_m_80o[6])
contagios_total_F.append(rango_etareo_f_0a4[6]+rango_etareo_f_5a9[6]+rango_etareo_f_10a14[6]+rango_etareo_f_15a19[6]+rango_etareo_f_20a24[6]+
                         rango_etareo_f_25a29[6]+rango_etareo_f_30a34[6]+rango_etareo_f_35a39[6]+rango_etareo_f_40a44[6]+rango_etareo_f_45a49[6]+
                         rango_etareo_f_50a54[6]+rango_etareo_f_55a59[6]+rango_etareo_f_60a64[6]+rango_etareo_f_65a69[6]+rango_etareo_f_70a74[6]+
                         rango_etareo_f_75a79[6]+rango_etareo_f_80o[6])

p=contagios_total_F[0]-contagios_total_M[0]

import matplotlib.pyplot as plt
plt.plot(Fecha,p,marker = 'o')
plt.show()

