import ROOT
import copy
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
histolist=[]
nlist=[0]*len(bkglist)
'''
__BoostedGGF_SR_MEKDTAG_M1500_C0.01
__BoostedGGF_SR_NoMEKDCut
__BoostedGGF_SR_UNTAGGED_M1500_C0.01
__BoostedVBF_SR_MEKDTAG_M1500_C0.01
__BoostedVBF_SR_NoMEKDCut
__BoostedVBF_SR_UNTAGGED_M1500_C0.01

'''
cutname1='__BoostedVBF_SR_NoMEKDCut'
#cutname2='__BoostedGGF_SR_MEKDTAG_M1500_C0.01'
#cutname3='__BoostedGGF_SR_UNTAGGED_M1500_C0.01'
variablename='WW_mass'
inputf='inputfiles_Boost/2016.root'

f=ROOT.TFile.Open(inputf)

#for bkg in bkglist:
for ibkg in range(0,len(bkglist)):

    #print ibkg
    histoname='histo_'+bkglist[ibkg]
    #print histoname
    if ibkg==0:
        htotal1=f.Get(cutname1+'/'+variablename+'/'+histoname)
        #htotal2=f.Get(cutname2+'/'+variablename+'/'+histoname)
        #htotal3=f.Get(cutname3+'/'+variablename+'/'+histoname)
        histolist.append(copy.deepcopy(htotal1))
    else:
        h1=f.Get(cutname1+'/'+variablename+'/'+histoname)
        #h2=f.Get(cutname2+'/'+variablename+'/'+histoname)
        #h3=f.Get(cutname3+'/'+variablename+'/'+histoname)
        
        htotal1.Add(h1)
        #htotal2.Add(h2)
        #htotal3.Add(h3)
        histolist.append(copy.deepcopy(h1))




Nbin=htotal1.GetNbinsX()
print 'Nbin',Nbin

list_binnumber=[]
tempsum1=0.
#binwidth=0.
n_min=6
for ibin in range(Nbin):

    #for ibkg in range(len(bkglist)):
    #    if not histolist[ibkg].GetBinError(ibin)==0:
            
    #        #nlist[ibkg]=0.
    #        #else:
    #        nlist[ibkg]+=(htotal1.GetBinContent(ibin)/htotal1.GetBinError(ibin))**2
    #        #print "nlist[ibkg]",nlist[ibkg]
    if htotal1.GetBinError(ibin)==0:
        n1=0.
    else:
        n1=(htotal1.GetBinContent(ibin)/htotal1.GetBinError(ibin))**2
    tempsum1+=n1
    

    #print tempsum1,tempsum2,tempsum3
    #if tempsum1>9 and tempsum2 > 9 and tempsum3 > 9:
    if tempsum1>10:
        print 'tempsum1',tempsum1
        list_binnumber.append(ibin)
        tempsum1=0.
    #allpass=True
    #for n in nlist:
    #    #print n
    #    if n < n_min and n!=0 : allpass=False

    #if allpass:
    #    list_binnumber.append(ibin)
    #    nlist=[0]*len(bkglist)


print list_binnumber


list_bin=[0.]
for binnumber in list_binnumber:
    x=htotal1.GetBinLowEdge(binnumber)+htotal1.GetBinWidth(binnumber)
    print x
    list_bin.append(x)
list_bin.append(4000.)
print 'len(list_bin)',len(list_bin)
print list_bin
f.Close()
