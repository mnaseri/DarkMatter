from WMCore.Configuration import Configuration

config = Configuration()

config.section_("General")
#config.General.requestName   = 'my_MiniAODv2_task' #task-dependent
config.General.transferLogs = True

config.section_("JobType")
config.JobType.pluginName  = 'Analysis'
config.JobType.psetName    = 'MiniAODv2_1_cfg.py' #the config file you created with cmsDriver

config.section_("Data")
#config.Data.inputDataset = '/my_signal/abdollah-DIGI-RECO-2-7acb7139bf84d3a816d33703984a9cf5/USER'
#'/ZPrimeToQQ-200GeV-v4/kreis-group-space-DIGI-RECO-2-413386f6eddb08329706f28eff10fb19/USER' ##change this to the DR2 dataset published in the previous step
config.Data.inputDBS = 'phys03'
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 1
#config.Data.totalUnits = 249 
config.Data.publication = True

# This string is used to construct the output dataset name
config.Data.outputDatasetTag  = 'MiniAODv2' #something you like

config.section_("Site")
# Where the output files will be transmitted to
config.Site.storageSite = 'T3_US_FNALLPC'



if __name__ == '__main__':

    from CRABAPI.RawCommand import crabCommand
    from CRABClient.ClientExceptions import ClientException
    from httplib import HTTPException

    # We want to put all the CRAB project directories from the tasks we submit here into one common directory.
    # That's why we need to set this parameter (here or above in the configuration file, it does not matter, we will not overwrite it).
    config.General.workArea = 'crab_projects2'

    def submit(config):
        try:
            crabCommand('submit', config = config)
        except HTTPException as hte:
            print "Failed submitting task: %s" % (hte.headers)
        except ClientException as cle:
            print "Failed submitting task: %s" % (cle)

    #############################################################################################
    ## From now on that's what users should modify: this is the a-la-CRAB2 configuration part. ##
    #############################################################################################




    Sample=[
#['1000_400_440','/DM_Codex_1200_500_550/abdollah-DIGI-RECO-1-9c549b5207abdfb5ae0876b07ca1f88d/USER'],
['1200_500_550','/DM_Codex_1200_500_550/abdollah-DIGI-RECO-1-9c549b5207abdfb5ae0876b07ca1f88d/USER'],
#['1400_600_660','/DM_Codex_1400_600_660/abdollah-GEN-SIM-8ecf21deb7c86694de43d2ad8e8e2292/USER'],
['1600_700_770','/DM_Codex_1600_700_770/abdollah-DIGI-RECO-1-9c549b5207abdfb5ae0876b07ca1f88d/USER'],
['1800_800_880','/DM_Codex_1800_800_880/abdollah-DIGI-RECO-1-9c549b5207abdfb5ae0876b07ca1f88d/USER'],
['2000_900_990','/DM_Codex_2000_900_990/abdollah-DIGI-RECO-1-9c549b5207abdfb5ae0876b07ca1f88d/USER']
]

    for sam in Sample:
            config.General.requestName   = 'DM_Codex_%s'%sam[0] #task-dependent
            config.Data.inputDataset = sam[1]
            submit(config)


'''
    config.General.requestName = 'LQ1000_DM400_X440'
    config.Data.inputDataset = '/Codex_LQ1000_DM400_X440_V3/abdollah-DIGI-RECO-2-7acb7139bf84d3a816d33703984a9cf5/USER'
    submit(config)

    config.General.requestName = 'LQ1400_DM600_X660'
    config.Data.inputDataset = '/Codex_LQ1400_DM600_X660_V3/abdollah-DIGI-RECO-2-7acb7139bf84d3a816d33703984a9cf5/USER'
    submit(config)

    config.General.requestName = 'LQ1800_DM800_X880'
    config.Data.inputDataset = '/Codex_LQ1800_DM800_X880_V3/abdollah-DIGI-RECO-2-7acb7139bf84d3a816d33703984a9cf5/USER'
    submit(config)


    config.General.requestName = 'LQ1200_DM400_X440'
    config.Data.inputDataset = '/Codex_LQ1200_DM400_X440/abdollah-DIGI-RECO-2-7acb7139bf84d3a816d33703984a9cf5/USER'


#/Codex_LQ1200_DM400_X440/abdollah-GEN-SIM-539ad005d03d5f717f49017dfdaee19f/USER'
    submit(config)

    config.General.requestName = 'LQ1500_DM400_X440'
    config.Data.inputDataset = '/Codex_LQ1500_DM400_X440/abdollah-DIGI-RECO-2-7acb7139bf84d3a816d33703984a9cf5/USER'
#abdollah-GEN-SIM-539ad005d03d5f717f49017dfdaee19f/USER'
    submit(config)

    config.General.requestName = 'LQ1800_DM400_X440'
    config.Data.inputDataset = '/Codex_LQ1800_DM400_X440/abdollah-DIGI-RECO-2-7acb7139bf84d3a816d33703984a9cf5/USER'
#abdollah-GEN-SIM-539ad005d03d5f717f49017dfdaee19f/USER'
    submit(config)

    config.General.requestName = 'LQ1500_DM400_X460'
    config.Data.inputDataset = '/Codex_LQ1500_DM400_X460/abdollah-DIGI-RECO-2-7acb7139bf84d3a816d33703984a9cf5/USER'
#abdollah-GEN-SIM-539ad005d03d5f717f49017dfdaee19f/USER'
    submit(config)

    config.General.requestName = 'LQ1500_DM500_X550'
    config.Data.inputDataset = '/Codex_LQ1500_DM500_X550/abdollah-DIGI-RECO-2-7acb7139bf84d3a816d33703984a9cf5/USER'
#abdollah-GEN-SIM-539ad005d03d5f717f49017dfdaee19f/USER'
    submit(config)

    config.General.requestName = 'LQ1500_DM300_X330'
    config.Data.inputDataset = '/Codex_LQ1500_DM300_X330/abdollah-DIGI-RECO-2-7acb7139bf84d3a816d33703984a9cf5/USER'
#abdollah-GEN-SIM-539ad005d03d5f717f49017dfdaee19f/USER'
    submit(config)

    config.General.requestName = 'LQ1500_DM400_X420'
    config.Data.inputDataset = '/Codex_LQ1500_DM400_X420/abdollah-DIGI-RECO-2-7acb7139bf84d3a816d33703984a9cf5/USER'
#abdollah-GEN-SIM-539ad005d03d5f717f49017dfdaee19f/USER'
    submit(config)


'''
