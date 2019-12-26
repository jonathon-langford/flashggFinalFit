# Config file: options for signal fitting

_year = '2018'

backgroundScriptCfg = {
  
  # Setup
  'inputWSDir':'/vols/cms/jl2117/hgg/ws/Jan20/stage1_1_%s'%_year, 
  #Procs will be inferred automatically from filenames
  'cats':'RECO_0J_PTH_0_10_Tag0,RECO_VBFTOPO_JET3VETO_LOWMJJ,RECO_0J_PTH_0_10_Tag1,RECO_GE2J_PTH_0_60_Tag1,RECO_1J_PTH_0_60_Tag0,RECO_0J_PTH_GT10_Tag0,RECO_VBFTOPO_JET3VETO_HIGHMJJ,RECO_GE2J_PTH_60_120_Tag1,RECO_VBFTOPO_BSM,RECO_GE2J_PTH_120_200_Tag1,RECO_1J_PTH_0_60_Tag1,RECO_GE2J_PTH_60_120_Tag0,RECO_1J_PTH_60_120_Tag1,RECO_GE2J_PTH_0_60_Tag0,RECO_VBFTOPO_JET3_HIGHMJJ,RECO_1J_PTH_60_120_Tag0,RECO_GE2J_PTH_120_200_Tag0,RECO_1J_PTH_120_200_Tag1,RECO_1J_PTH_120_200_Tag0,RECO_PTH_GT200_Tag0,RECO_PTH_GT200_Tag1,RECO_VBFTOPO_VHHAD,RECO_VBFLIKEGGH,RECO_0J_PTH_GT10_Tag1,RECO_VBFTOPO_JET3_LOWMJJ',
  'ext':'stage1_1_%s'%_year,
  'year':'%s'%_year, 
  'unblind':0,

  # Job submission options
  'batch':'IC',
  'queue':'hep.q',

  # Mode allows script to carry out single function
  'mode':'fTestOnly', # Options: [std,fTestOnly,bkgPlotsOnly]
  
}
