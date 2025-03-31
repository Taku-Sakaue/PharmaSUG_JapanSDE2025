import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


st.title('Streamlit Web Application Sample')

# DM domainのimport
dfDM = pd.read_csv(r"SDTM_sample/dm.csv")

# AE domainのimport
dfAE = pd.read_csv(r"SDTM_sample/ae.csv")

# VS domainのimport
dfVS = pd.read_csv(r"SDTM_sample/vs.csv")




# DMテーブルの表示
st.markdown("## - _DM domain_")
st.write(dfDM)


# 患者のセレクターを表示
selectedPts = st.multiselect("Select Patient#", dfDM['USUBJID'])


st.markdown("## - _AE domain_")
# セレクターで選択した患者の有害事象の表示
if(st.button("Show Adverse Events")):
		
	if(len(selectedPts) > 0):
				
		# セレクターで選択した患者の有害事象を抽出
		dfSelAE = dfAE[dfAE['USUBJID'].isin(selectedPts)]
		# dataframeを表示する
		st.write(dfSelAE)
		
		# 抽出したデータをCSVファイルとしてダウンロードする
		st.download_button("Download AE file", 
		                    data=dfSelAE.to_csv(index=False), 
		                    file_name='selected_AE.csv', 
		                    mime='text/mime')



# プロット用オブジェクトの生成
fig = plt.figure(figsize=(10, 10))
	
if(len(selectedPts) > 0):
	
	st.markdown("## - _VS domain_")
	
	# セレクターで選択した患者のvital signを抽出
	dfSelVS = dfVS[dfVS['USUBJID'].isin(selectedPts)]
	# 表示対象のvital signパラメータを取得
	vsParam = dfSelVS['VSTEST'].drop_duplicates().values
		
	# プロット表示領域の定義 (vsParam数行 x 1列)
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
