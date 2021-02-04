import ROOT

bkglist=['qqWWqq',
'tW',
'DY',
'WW',
'ggWW',
'SingleTop',
'Wjets',
'ZHWWlnuqq_M125',
'WpHWWlnuqq_M125',
'WmHWWlnuqq_M125',
'TT',
'MultiV',
'QCD',
]

'''
__BoostedGGF_SR_MEKDTAG_M1500_C0.01
__BoostedGGF_SR_NoMEKDCut
__BoostedGGF_SR_UNTAGGED_M1500_C0.01
__BoostedVBF_SR_MEKDTAG_M1500_C0.01
__BoostedVBF_SR_NoMEKDCut
__BoostedVBF_SR_UNTAGGED_M1500_C0.01

'''
cutname1='__BoostedVBF_SR_NoMEKDCut'
cutname2='__BoostedGGF_SR_MEKDTAG_M1500_C0.01'
cutname3='__BoostedGGF_SR_UNTAGGED_M1500_C0.01'
variablename='WW_mass'
inputf='inputfiles/2018.root'

f=ROOT.TFile.Open(inputf)

#for bkg in bkglist:
for ibkg in range(0,len(bkglist)):

    #print ibkg
    histoname='histo_'+bkglist[ibkg]
    #print histoname
    if ibkg==0:
        htotal1=f.Get(cutname1+'/'+variablename+'/'+histoname)
        htotal2=f.Get(cutname2+'/'+variablename+'/'+histoname)
        htotal3=f.Get(cutname3+'/'+variablename+'/'+histoname)
    else:
        h1=f.Get(cutname1+'/'+variablename+'/'+histoname)
        h2=f.Get(cutname2+'/'+variablename+'/'+histoname)
        h3=f.Get(cutname3+'/'+variablename+'/'+histoname)
        
        htotal1.Add(h1)
        htotal2.Add(h2)
        htotal3.Add(h3)




Nbin=htotal1.GetNbinsX()
print 'Nbin',Nbin

list_binnumber=[]
tempsum1=0.
tempsum2=0.
tempsum3=0.
binwidth=0.
for ibin in range(Nbin):
    binwidth+=10
    y1=htotal1.GetBinContent(ibin)
    y2=htotal2.GetBinContent(ibin)
    y3=htotal3.GetBinContent(ibin)
    #print y

    tempsum1+=y1
    tempsum2+=y2
    tempsum3+=y3
    if tempsum1/binwidth>0.01 and tempsum2/binwidth>0.01 and tempsum3/binwidth>0.01:
        list_binnumber.append(ibin)
        tempsum1=0.
        tempsum2=0.
        tempsum3=0.
        binwidth=0.
print list_binnumber


list_bin=[]
for binnumber in list_binnumber:
    x=htotal1.GetBinLowEdge(binnumber)+htotal1.GetBinWidth(binnumber)
    print x
    list_bin.append(x)
print 'len(list_bin)',len(list_bin)
print list_bin
f.Close()
