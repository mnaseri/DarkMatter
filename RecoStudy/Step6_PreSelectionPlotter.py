#! /usr/bin/python

# To change this template, choose Tools | Templates
# and open the template in the editor.
#http://root.cern.ch/viewvc/trunk/tutorials/pyroot/hsimple.py?revision=20881&view=markup
__author__ = "abdollahmohammadi"
__date__ = "$Feb 23, 2013 10:39:33 PM$"

import math
import ROOT
from ROOT import Double
from ROOT import TCanvas
from ROOT import TFile
from ROOT import TH1F
from ROOT import TH2F
from ROOT import TNtuple
from ROOT import TProfile
from ROOT import gBenchmark
from ROOT import gROOT
from ROOT import gRandom
from ROOT import gSystem
from ctypes import *
import ROOT as r
import array

##### Get Jet to Tau FR
from Step1_JetToMuFR import Make_Mu_FakeRate
from Step1_JetToMuFR import _FIT_Jet_Function
##### Get Jet to Tau FR

gROOT.Reset()
import os




ROOT.gROOT.SetBatch(True)
#ROOT.gROOT.ProcessLine('.x rootlogon.C')
SubRootDir = 'OutFiles_PreSelection/'


verbos_ = False
RB_=1

TauScale = [ ""]
#POSTFIX=["","Up","Down"]

signal = ['LQ_']
signalName = ['LQ_']
#mass = [200,250, 300, 350, 400, 450, 500, 550,  600, 650, 700, 750, 800,850,900,950,1000,1050,1100,1150,1200,1250,1300,1350,1400,1450,1500]
#TOTMASS = [200,250, 300, 350, 400, 450, 500, 550,  600, 650, 700, 750, 800,850,900,950,1000,1050,1100,1150,1200,1250,1300,1350,1400,1450,1500]
mass = [1000,1100]
TOTMASS = [1000,1100]
lenghtSig = len(signal) * len(mass) +1
category = [""]

############################################################################################################
def _FileReturn(Name, channel,cat,HistoName):

    if not os.path.exists(SubRootDir):
        os.makedirs(SubRootDir)
    myfile = TFile(SubRootDir + Name + '.root')
    print "##### --->>>>>>> File name is ", SubRootDir + Name + '.root'  "   and histo is -->  ", channel+HistoName + cat
    Histo =  myfile.Get(channel+HistoName + cat)
    if not os.path.exists("Extra"):
        os.makedirs("Extra")
    NewFile=TFile("Extra/XXX.root","RECREATE")
    NewFile.WriteObject(Histo,"XXX")
    myfile.Close()
    return NewFile


####################################################
##   Start Making the Datacard Histograms
####################################################
def MakeTheHistogram(channel,NormMC,NormQCD,ShapeQCD,chl):
    print "\n\n\n\n\n\n ****** ------------------------------>     Starting for ",NormMC, "in Channel= ",channel

    TauScaleOut = [ ""]


#    myOut = TFile("TotalRootForLimit_tauFREtau_"+channel + NormMC+".root" , 'RECREATE') # Name Of the output file
    myOut = TFile("TotalRootForLimit_PreSelection_"+channel + NormMC+".root" , 'RECREATE') # Name Of the output file


    icat=-1
    for NameCat in category:
        icat =icat +1
        print "starting NameCat and channel and HistoName ", NameCat, channel, NormMC

        tDirectory= myOut.mkdir(channel + str(NameCat))
        tDirectory.cd()
        for tscale in range(len(TauScale)):
#
##           ################################################
##           #   Filling Signal
###           ################################################
#            for sig in range(len(signal)):
#                for m in range(len(mass)):#    for m in range(110, 145, 5):
#
#                    print "--------------------------------------------------->     Processing LQ Signal ", signal[sig],mass[m]
#                    tDirectory.cd()
#
#                    Name= str(signal[sig])+str(mass[m])
#                    NameOut= str(signalName[sig]) +str(TOTMASS[m])+str(TauScaleOut[tscale])
#
#
#                    NormFile= _FileReturn(Name, channel,NameCat, NormMC)
#                    NormHisto=NormFile.Get("XXX")
#
#                    RebinedHist= NormHisto.Rebin(RB_)
#                    tDirectory.WriteObject(RebinedHist,NameOut)

            ################################################
            #  Filling SingleTop
            ################################################
            print "--------------------------------------------------->     Processing SingleTop"
            tDirectory.cd()
        
            Name= "SingleTop"
            NameOut= "SingleTop"+str(TauScaleOut[tscale])
            
            NormFile= _FileReturn(Name, channel,NameCat, NormMC)
            NormHisto=NormFile.Get("XXX")
            
            ShapeFile= _FileReturn(Name, channel,NameCat, NormMC)
            ShapeHisto=ShapeFile.Get("XXX")
            
            if ShapeHisto and NormHisto:
                ShapeHisto.Scale(NormHisto.Integral()/ShapeHisto.Integral())
                RebinedHist= ShapeHisto.Rebin(RB_)
                tDirectory.WriteObject(RebinedHist,NameOut)
            ################################################
            #  Filling VV
            ################################################
            print "--------------------------------------------------->     Processing VV"
            tDirectory.cd()
        
            Name= "VV"
            NameOut= "VV"+str(TauScaleOut[tscale])
            
            NormFile= _FileReturn(Name, channel,NameCat, NormMC)
            NormHisto=NormFile.Get("XXX")
            
            ShapeFile= _FileReturn(Name, channel,NameCat, NormMC)
            ShapeHisto=ShapeFile.Get("XXX")
            
            if ShapeHisto and NormHisto:
                ShapeHisto.Scale(NormHisto.Integral()/ShapeHisto.Integral())
                RebinedHist= ShapeHisto.Rebin(RB_)
                tDirectory.WriteObject(RebinedHist,NameOut)


            ################################################
            #  Filling TOP
            ################################################
            print "--------------------------------------------------->     Processing TOP"
            tDirectory.cd()

            Name= "TTJets"
            NameOut= "TT"+str(TauScaleOut[tscale])

            NormFile= _FileReturn(Name, channel,NameCat, NormMC)
            NormHisto=NormFile.Get("XXX")
        
            ShapeFile= _FileReturn(Name, channel,NameCat, NormMC)
            ShapeHisto=ShapeFile.Get("XXX")

            if ShapeHisto and NormHisto:
                ShapeHisto.Scale(NormHisto.Integral()/ShapeHisto.Integral())
                RebinedHist= ShapeHisto.Rebin(RB_)
                tDirectory.WriteObject(RebinedHist,NameOut)
            
            ################################################
            #  Filling ZTT
            ################################################
            print "--------------------------------------------------->     Processing ZTT"
            tDirectory.cd()

            Name= "DYJetsToLL"
            NameOut= "ZTT"+str(TauScaleOut[tscale])
            
            NormFile= _FileReturn(Name, channel,NameCat, NormMC)
            NormHisto=NormFile.Get("XXX")
            
            ShapeFile= _FileReturn(Name, channel,NameCat, NormMC)
            ShapeHisto=ShapeFile.Get("XXX")
            
            ShapeHisto.Scale(NormHisto.Integral()/ShapeHisto.Integral())
            RebinedHist= ShapeHisto.Rebin(RB_)
            tDirectory.WriteObject(RebinedHist,NameOut)


            ################################################
            #  Filling W
            ################################################
            print "--------------------------------------------------->     Processing W"
            tDirectory.cd()

            Name="WJetsToLNu"
            NameOut= "W"+str(TauScaleOut[tscale])

            NormFile= _FileReturn(Name, channel,NameCat, NormMC)
            NormHisto=NormFile.Get("XXX")
            
            ShapeFile= _FileReturn(Name, channel,NameCat, NormMC)
            ShapeHisto=ShapeFile.Get("XXX")
            
            ShapeHisto.Scale(NormHisto.Integral()/ShapeHisto.Integral())
            RebinedHist= ShapeHisto.Rebin(RB_)
            tDirectory.WriteObject(RebinedHist,NameOut)
#
#            ################################################
#            #  Filling QCD
#            ################################################
            print "--------------------------------------------------->     Processing QCD"
            tDirectory.cd()
            
            Name= "SingleTop"
            SingleTSampleQCDNorm= _FileReturn(Name, channel,NameCat, NormQCD)
            SingleTSampleQCDShape= _FileReturn(Name, channel,NameCat, ShapeQCD)
            
            Name= "VV"
            VVSampleQCDNorm= _FileReturn(Name, channel,NameCat, NormQCD)
            VVSampleQCDShape= _FileReturn(Name, channel,NameCat, ShapeQCD)

            Name= "TTJets"
            TTSampleQCDNorm= _FileReturn(Name, channel,NameCat, NormQCD)
            TTSampleQCDShape= _FileReturn(Name, channel,NameCat, ShapeQCD)

            Name= "DYJetsToLL"
            ZTTSampleQCDNorm= _FileReturn(Name, channel,NameCat, NormQCD)
            ZTTSampleQCDShape= _FileReturn(Name, channel,NameCat, ShapeQCD)

            Name= "WJetsToLNu"
            WSampleQCDNorm= _FileReturn(Name, channel,NameCat, NormQCD)
            WSampleQCDShape= _FileReturn(Name, channel,NameCat, ShapeQCD)
                        
            Name="Data"
            DataSampleQCDNorm= _FileReturn(Name, channel,NameCat, NormQCD)
            DataSampleQCDShape= _FileReturn(Name, channel,NameCat, ShapeQCD)



            SingleTSampleQCDShapeHist=SingleTSampleQCDShape.Get("XXX")
            VVSampleQCDShapeHist=VVSampleQCDShape.Get("XXX")
            TTSampleQCDShapeHist=TTSampleQCDShape.Get("XXX")
            ZTTSampleQCDShapeHist=ZTTSampleQCDShape.Get("XXX")
            WSampleQCDShapeHist=WSampleQCDShape.Get("XXX")
            DataSampleQCDShapeHist=DataSampleQCDShape.Get("XXX")
#
            print "\n##########\n DataSampleQCDShapeHist before=",    DataSampleQCDShapeHist.Integral()

            if SingleTSampleQCDShapeHist: DataSampleQCDShapeHist.Add(SingleTSampleQCDShapeHist, -1)
            if VVSampleQCDShapeHist: DataSampleQCDShapeHist.Add(VVSampleQCDShapeHist, -1)
            DataSampleQCDShapeHist.Add(TTSampleQCDShapeHist, -1)
            DataSampleQCDShapeHist.Add(ZTTSampleQCDShapeHist, -1)
            DataSampleQCDShapeHist.Add(WSampleQCDShapeHist, -1)

            print "\n##########\n DataSampleQCDShapeHist after=",    DataSampleQCDShapeHist.Integral()


            SingleTSampleQCDNormHist=SingleTSampleQCDNorm.Get("XXX")
            VVSampleQCDNormHist=VVSampleQCDNorm.Get("XXX")
            TTSampleQCDNormHist=TTSampleQCDNorm.Get("XXX")
            ZTTSampleQCDNormHist=ZTTSampleQCDNorm.Get("XXX")
            WSampleQCDNormHist=WSampleQCDNorm.Get("XXX")
            DataSampleQCDNormHist=DataSampleQCDNorm.Get("XXX")
            
            print "\n%%%%%%%%%%%%%\n channelDataSampleQCDNormHist before=", channel,   DataSampleQCDNormHist.Integral()
            if SingleTSampleQCDNormHist:  DataSampleQCDNormHist.Add(SingleTSampleQCDNormHist, -1)
            if VVSampleQCDNormHist: DataSampleQCDNormHist.Add(VVSampleQCDNormHist, -1)
            DataSampleQCDNormHist.Add(TTSampleQCDNormHist, -1)
            DataSampleQCDNormHist.Add(ZTTSampleQCDNormHist, -1)
            DataSampleQCDNormHist.Add(WSampleQCDNormHist, -1)
            print "\n%%%%%%%%%%%%%\n DataSampleQCDNormHist after=",  channel,  DataSampleQCDNormHist.Integral()
            

            FR_FitMaram=Make_Mu_FakeRate(channel)
            QCDEstimation=0
            for bin in xrange(50,1000):
                value=DataSampleQCDNormHist.GetBinContent(bin)
                if value < 0 : value=0
                FR= _FIT_Jet_Function(bin+1.5,FR_FitMaram)
                if FR> 0.9: FR=0.9
                QCDEstimation += value * FR/(1-FR)
            print "\n##########\n QCDEstimation",    QCDEstimation


            NameOut= "QCD"+str(TauScaleOut[tscale])
            DataSampleQCDShapeHist.Scale(QCDEstimation/DataSampleQCDShapeHist.Integral())  # The shape is from btag-Loose Need get back norm
            RebinedHist= DataSampleQCDShapeHist.Rebin(RB_)
            tDirectory.WriteObject(RebinedHist,NameOut)
#
            ################################################
            #  Filling Data
            ################################################
            print "--------------------------------------------------->     Processing Data"
            tDirectory.cd()

            Name='Data'
            NameOut='data_obs'

            NormFile= _FileReturn(Name, channel,NameCat, NormMC)
            NormHisto=NormFile.Get("XXX")
        
            ShapeFile= _FileReturn(Name, channel,NameCat, NormMC) #for data Shape and Norm should be the same
            ShapeHisto=ShapeFile.Get("XXX")
            
#            ShapeHisto.Scale(NormHisto.Integral()/ShapeHisto.Integral())
            RebinedHist= ShapeHisto.Rebin(RB_)
            tDirectory.WriteObject(RebinedHist,NameOut)




    myOut.Close()






if __name__ == "__main__":

    
    
#    PlotName= ["_WRegionMT"]
    PlotName= ["_tmass_MuMet","_tmass_JetMet","_tmass_LQMet","_LepEta","_LepPt","_LepIso","_JetPt","_JetEta","_MET","_LQMass","_dPhi_Jet_Met","_dPhi_Mu_Met","_nVtx","_nVtx_NoPU"]
#    Isolation=["_Iso", "_AntiIso","_Total"]
    Isolation=["_Iso"]
    MT=["_NoMT", "_LowMT","_HighMT"]
#    MT= ["_NoMT"]
#    JPT=["_LowDPhi", "_HighDPhi","_RelaxDphi"];
    JPT=[ "_HighDPhi"];

    for NormMC in PlotName:
        for iso in Isolation:
            for mt in MT:
                for jpt in JPT:
                        MakeTheHistogram("MuJet",NormMC+mt+jpt+iso,"_CloseJetLepPt"+mt+jpt+"_AntiIso",NormMC+mt+jpt+"_AntiIso",1)
