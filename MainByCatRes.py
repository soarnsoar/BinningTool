import ROOT
import numpy as np
def BinningByCat(cutname1,Year,bincut=0.1):
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
    #import sys
    #Year=sys.argv[1]
    

    #cutname1='___ResolvedVBF__SR_UNTAGGED_M400_C0.01'
    #cutname1='___ResolvedGGF__SR_UNTAGGED_M400_C0.01'
    #cutname1='___ResolvedVBF__SR_NoMEKDCut'
    

    

    #cutname1='__BoostedVBF_SR_NoMEKDCut'
    #cutname2='__BoostedGGF_SR_MEKDTAG_M1500_C0.01'
    #cutname1='__BoostedGGF_SR_MEKDTAG_M1500_C0.01'
    #cutname3='__BoostedGGF_SR_UNTAGGED_M1500_C0.01'
    #cutname1='__BoostedGGF_SR_UNTAGGED_M1500_C0.01'
    variablename='WW_mass'
    inputf='inputfiles_Resol/'+Year+'.root'
    
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
        else:
            h1=f.Get(cutname1+'/'+variablename+'/'+histoname)
            #h2=f.Get(cutname2+'/'+variablename+'/'+histoname)
            #h3=f.Get(cutname3+'/'+variablename+'/'+histoname)
            
            htotal1.Add(h1)
        #htotal2.Add(h2)
        #htotal3.Add(h3)
        


    ##--
    
    #hdata1=f.Get(cutname1+'/'+variablename+'/histo_DATA')
    #hdata2=f.Get(cutname2+'/'+variablename+'/histo_DATA')
    #hdata3=f.Get(cutname3+'/'+variablename+'/histo_DATA')

    
    Nbin=htotal1.GetNbinsX()
    print 'Nbin',Nbin
    
    list_binnumber=[]
    tempsum1=0.
    #tempsum2=0.
    #tempsum3=0.
    #tempsum1data=0.
    #tempsum2data=0.
    #tempsum3data=0.
    
    binwidth=0.
    for ibin in range(Nbin):
        binwidth+=10
        y1=htotal1.GetBinContent(ibin)
        #y2=htotal2.GetBinContent(ibin)
        #y3=htotal3.GetBinContent(ibin)
        
        #y1data=hdata1.GetBinContent(ibin)
        #y2data=hdata2.GetBinContent(ibin)
        #y3data=hdata3.GetBinContent(ibin)
        #print y
        
        tempsum1+=y1
        #tempsum2+=y2
        #tempsum3+=y3
        
        #tempsum1data+=y1data
        #tempsum2data+=y2data
        #tempsum3data+=y3data
        #if tempsum1/binwidth>0.01 and tempsum2/binwidth>0.01 and tempsum3/binwidth>0.01 and tempsum1data/binwidth>0.01 and tempsum2data/binwidth>0.01 and tempsum3data/binwidth>0.01:
        #if tempsum1/binwidth>0.01 and tempsum2/binwidth>0.01 and tempsum3/binwidth>0.01 :
        if tempsum1/binwidth>bincut :
            list_binnumber.append(ibin)
            tempsum1=0.
            #tempsum2=0.
            #tempsum3=0.
            
            #tempsum1data=0.
            #tempsum2data=0.
            #tempsum3data=0.
            
            binwidth=0.
    print list_binnumber


    list_bin=[]
    for binnumber in list_binnumber:
        #x=htotal1.GetBinLowEdge(binnumber)+htotal1.GetBinWidth(binnumber)
        x=htotal1.GetBinLowEdge(binnumber)
        y1=htotal1.GetBinContent(binnumber)
        #y2=htotal2.GetBinContent(binnumber)
        #y3=htotal3.GetBinContent(binnumber)
        #print x,y1,y2,y3
        list_bin.append(x)
    list_bin+=[3000.]
    print 'len(list_bin)',len(list_bin)
    hrebin1=htotal1.Rebin(len(list_bin)-1,'hnew1',np.asarray(sorted(list_bin)))
    #hrebin2=htotal2.Rebin(len(list_bin)-1,'hnew2',np.asarray(sorted(list_bin)))
    #hrebin3=htotal3.Rebin(len(list_bin)-1,'hnew3',np.asarray(sorted(list_bin)))
    
    c=ROOT.TCanvas()
    c.SetLogy()
    hrebin1.Draw()
    c.SaveAs(cutname1+'_'+Year+".pdf")
    #hrebin2.Draw()
    #c.SaveAs("GGF_bst_"+Year+".pdf")
    #hrebin3.Draw()
    #c.SaveAs("UNT_bst_"+Year+".pdf")
    
    print list_bin
    f.Close()
if __name__ == '__main__':
    '''
        ___ResolvedVBF__SR_UNTAGGED_M400_C0.01                                                                                                                                                                  
    ___ResolvedGGF__SR_UNTAGGED_M400_C0.01                                                                                                                                                                  
    ___ResolvedVBF__SR_MEKDTAG_M400_C0.01                                                                                                                                                                   
    ___ResolvedVBF__SR_NoMEKDCut                                                                                                                                                                            
    ___ResolvedGGF__SR_NoMEKDCut                                                                                                                                                                            
    ___ResolvedGGF__SR_MEKDTAG_M400_C0.01                                                                                                                                                                   


    '''
    import sys
    cutname=sys.argv[1]
    Year=sys.argv[2]
    bincut=float(sys.argv[3])
    if cutname=='1':
        cutname='___ResolvedGGF__SR_MEKDTAG_M400_C0.01'
        print '___ResolvedGGF__SR_MEKDTAG_M400_C0.01'
    if cutname=='2':
        cutname='___ResolvedGGF__SR_UNTAGGED_M400_C0.01'
        print '___ResolvedGGF__SR_UNTAGGED_M400_C0.01'
    if cutname=='3':
        cutname='___ResolvedVBF__SR_NoMEKDCut'
        print '___ResolvedVBF__SR_NoMEKDCut'
    #BinningByCat(cutname,Year):
    BinningByCat(cutname,Year,bincut)
    #cutname1='__BoostedVBF_SR_NoMEKDCut'
    #cutname2='__BoostedGGF_SR_MEKDTAG_M1500_C0.01'
    #cutname1='__BoostedGGF_SR_MEKDTAG_M1500_C0.01'
    #cutname3='__BoostedGGF_SR_UNTAGGED_M1500_C0.01'
    #cutname1='__BoostedGGF_SR_UNTAGGED_M1500_C0.01'
