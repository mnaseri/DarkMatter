import os
import ROOT
from ROOT import *


File=TFile("test.root")
His=File.Get("Efficiency")
can=TCanvas("can","",800,800)

His.Draw("hist")
His.SetFillColor(9)
His.SetFillStyle(3009)
His.SetTitle("")
gStyle.SetOptStat(0)
His.GetXaxis().SetBinLabel(1,"All")
His.GetXaxis().SetBinLabel(2,"One 60 GeV Muon")
His.GetXaxis().SetBinLabel(3,"One 100 GeV Jet")
His.GetXaxis().SetBinLabel(4,"No electron")
His.GetXaxis().SetBinLabel(5,"No tau")
His.GetXaxis().SetBinLabel(6,"No bjet")
His.GetXaxis().SetBinLabel(7,"M_{T} > 150")
His.GetXaxis().SetBinLabel(8,"MET > 700")
His.GetXaxis().SetRangeUser(0,8)
can.SetGridx()

can.SaveAs("outEff.pdf")

400/440


cp -r pp_mm_mix_gen2_lq pp_mm_mix_gen2_lq_LQ1000_DM_400_X_440
cp -r pp_mm_mix_gen2_lq pp_mm_mix_gen2_lq_LQ1100_DM_450_X_495
cp -r pp_mm_mix_gen2_lq pp_mm_mix_gen2_lq_LQ1200_DM_500_X_550
cp -r pp_mm_mix_gen2_lq pp_mm_mix_gen2_lq_LQ1300_DM_550_X_605
cp -r pp_mm_mix_gen2_lq pp_mm_mix_gen2_lq_LQ1400_DM_600_X_660
cp -r pp_mm_mix_gen2_lq pp_mm_mix_gen2_lq_LQ1500_DM_650_X_715
cp -r pp_mm_mix_gen2_lq pp_mm_mix_gen2_lq_LQ1600_DM_700_X_770
cp -r pp_mm_mix_gen2_lq pp_mm_mix_gen2_lq_LQ1700_DM_750_X_825
cp -r pp_mm_mix_gen2_lq pp_mm_mix_gen2_lq_LQ1800_DM_800_X_880
cp -r pp_mm_mix_gen2_lq pp_mm_mix_gen2_lq_LQ1900_DM_850_X_935
cp -r pp_mm_mix_gen2_lq pp_mm_mix_gen2_lq_LQ2000_DM_900_X_990

cp -r pp_mm_mix_gen2_lq pp_mm_mix_gen2_lq_LQ1000_DM_400_X_460
cp -r pp_mm_mix_gen2_lq pp_mm_mix_gen2_lq_LQ1100_DM_450_X_520
cp -r pp_mm_mix_gen2_lq pp_mm_mix_gen2_lq_LQ1200_DM_500_X_575
cp -r pp_mm_mix_gen2_lq pp_mm_mix_gen2_lq_LQ1300_DM_550_X_635
cp -r pp_mm_mix_gen2_lq pp_mm_mix_gen2_lq_LQ1400_DM_600_X_690
cp -r pp_mm_mix_gen2_lq pp_mm_mix_gen2_lq_LQ1500_DM_650_X_750
cp -r pp_mm_mix_gen2_lq pp_mm_mix_gen2_lq_LQ1600_DM_700_X_805
cp -r pp_mm_mix_gen2_lq pp_mm_mix_gen2_lq_LQ1700_DM_750_X_865
cp -r pp_mm_mix_gen2_lq pp_mm_mix_gen2_lq_LQ1800_DM_800_X_920
cp -r pp_mm_mix_gen2_lq pp_mm_mix_gen2_lq_LQ1900_DM_850_X_980
cp -r pp_mm_mix_gen2_lq pp_mm_mix_gen2_lq_LQ2000_DM_900_X_1035

cp -r pp_mm_mix_gen2_lq pp_mm_mix_gen2_lq_LQ1000_DM_400_X_420
cp -r pp_mm_mix_gen2_lq pp_mm_mix_gen2_lq_LQ1100_DM_450_X_475
cp -r pp_mm_mix_gen2_lq pp_mm_mix_gen2_lq_LQ1200_DM_500_X_525
cp -r pp_mm_mix_gen2_lq pp_mm_mix_gen2_lq_LQ1300_DM_550_X_580
cp -r pp_mm_mix_gen2_lq pp_mm_mix_gen2_lq_LQ1400_DM_600_X_630
cp -r pp_mm_mix_gen2_lq pp_mm_mix_gen2_lq_LQ1500_DM_650_X_685
cp -r pp_mm_mix_gen2_lq pp_mm_mix_gen2_lq_LQ1600_DM_700_X_735
cp -r pp_mm_mix_gen2_lq pp_mm_mix_gen2_lq_LQ1700_DM_750_X_790
cp -r pp_mm_mix_gen2_lq pp_mm_mix_gen2_lq_LQ1800_DM_800_X_840
cp -r pp_mm_mix_gen2_lq pp_mm_mix_gen2_lq_LQ1900_DM_850_X_895
cp -r pp_mm_mix_gen2_lq pp_mm_mix_gen2_lq_LQ2000_DM_900_X_945

cp -r pp_mm_mix_gen2_lq pp_mm_mix_gen2_lq_LQ1200_DM_600_X_600
cp -r pp_mm_mix_gen2_lq pp_mm_mix_gen2_lq_LQ1300_DM_600_X_600
cp -r pp_mm_mix_gen2_lq pp_mm_mix_gen2_lq_LQ1400_DM_600_X_600
cp -r pp_mm_mix_gen2_lq pp_mm_mix_gen2_lq_LQ1500_DM_600_X_600
cp -r pp_mm_mix_gen2_lq pp_mm_mix_gen2_lq_LQ1600_DM_600_X_600
cp -r pp_mm_mix_gen2_lq pp_mm_mix_gen2_lq_LQ1700_DM_600_X_600
cp -r pp_mm_mix_gen2_lq pp_mm_mix_gen2_lq_LQ1800_DM_600_X_600




set param_card  frblock  1  4.000000e+02
set param_card  frblock  2  4.400000e+02
set param_card  frblock  3  4.400000e+02
set param_card  frblock  4  1.000000e+03
set param_card  frblock  5  1.000000e+03
set param_card  frblock  6  1.000000e-01
set param_card  frblock8 1 1  0.000000e-01
set param_card  frblock8 2 2  1.414000e-01
set param_card  frblock8 3 3  0.000000e-01
set param_card  frblock9 1 1  0.000000e-01
set param_card  frblock9 2 2  0.000000e-01
set param_card  frblock9 3 3  0.000000e-01







