import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(layout="wide")
st.title('Streamlit Web Application Sample')

# DM domainのimport
dfDM = pd.read_csv(r"C:\Users\165639\OneDrive - CHUGAI PHARMACEUTICAL CO.,LTD\デスクトップ\PharmaSUG_data\dm.csv")

# AE domainのimport
dfAE = pd.read_csv(r"C:\Users\165639\OneDrive - CHUGAI PHARMACEUTICAL CO.,LTD\デスクトップ\PharmaSUG_data\ae.csv")

# VS domainのimport
dfVS = pd.read_csv(r"C:\Users\165639\OneDrive - CHUGAI PHARMACEUTICAL CO.,LTD\デスクトップ\PharmaSUG_data\vs.csv")



# 患者のセレクターを表示
selectedPts = st.sidebar.multiselect("Select Patient#", dfDM['USUBJID'])


tabs = st.tabs(['DM domain', 'AE domain', 'VS domain'])


# DM domain tab
with tabs[0]:
	st.header('Demographic Data')
	
	if(len(selectedPts) > 0):
		
		dfSelDM = dfDM[dfDM['USUBJID'].isin(selectedPts)]
		st.dataframe(dfSelDM)


# AE domain tab
with tabs[1]:
	st.header('Adverse Events Data')
	
	if(len(selectedPts) > 0):
		
		dfSelAE = dfAE[dfAE['USUBJID'].isin(selectedPts)]
		st.dataframe(dfSelAE)
	

# VS domain tab
with tabs[2]:
	st.header('Vistal Signs Data')
	
	col1, col2, col3 = st.columns([3, 3, 4])
	
	fig = plt.figure(figsize=(10, 10))
	
	with col1:
		
		if(len(selectedPts) > 0):
			
			dfSelVS = dfVS[dfVS['USUBJID'].isin(selectedPts)]
			
			vsParam = dfSelVS['VSTEST'].drop_duplicates().values
			
			ppanel = fig.subplots(len(vsParam), 1)
			
			# vital sign毎にグラフ作成
			for i in range(0, len(vsParam)):
				
				# 表示パラメータデータの抽出
				dfDispParam = dfSelVS[dfSelVS['VSTEST'] == vsParam[i]]
				
				# グラフタイトルの設定
				ppanel[i].set_title(vsParam[i])
				
				# 患者毎のグラフを作成
				for p in selectedPts:
					
					# 推移図をプロット
					ppanel[i].plot(dfDispParam[dfDispParam['USUBJID'] == p]['VSDY'],
					               dfDispParam[dfDispParam['USUBJID'] == p]['VSSTRESN'],
					               label=p
					               )
			    
			# 凡例の設定
			plt.legend(bbox_to_anchor=(0, -1), loc='upper left')
			# グラフの表示
			plt.subplots_adjust(hspace=1)
			st.pyplot(plt)