def addhzzbr(lines,processes):
    line = "hzz_br lnN"
    for pr in processes :
        if "back" not in pr : 
            line =  line + " 1.02"
        else :
             line = line + " -"
    
    lines.append(line)    
    


def addlumi(lines,processes):
    line = "lumi_13TeV lnN"
    for pr in processes :
        line =  line + " 1.016/0.984" 
    #line = line + " \n"
    #taken from https://twiki.cern.ch/twiki/bin/view/CMS/TWikiLUM#SummaryTable
    #inclusive lumi
    lines.append(line)    



def addlumi16(lines,processes):
    line = "lumi_13TeV_2016 lnN"
    for pr in processes :
        line =  line + " 1.0082/0.9918" 
    #line = line + " \n"
    #taken from https://twiki.cern.ch/twiki/bin/view/CMS/TWikiLUM#SummaryTable
    #inclusive lumi
    lines.append(line)    

def addlumi17(lines,processes):
    line = "lumi_13TeV_2017 lnN"
    for pr in processes :
        line =  line + " 1.0088/0.9912" 
    #line = line + " \n"
    #taken from https://twiki.cern.ch/twiki/bin/view/CMS/TWikiLUM#SummaryTable
    #inclusive lumi
    lines.append(line)    

def addlumi18(lines,processes):
    line = "lumi_13TeV_2018 lnN"
    for pr in processes :
        line =  line + " 1.0106/0.9894" 
    #line = line + " \n"
    #taken from https://twiki.cern.ch/twiki/bin/view/CMS/TWikiLUM#SummaryTable
    #inclusive lumi
    lines.append(line)    



    
def addQCDscale_muR_ggH(lines,processes):
    line = "QCDscale_muF_qqH lnN"
    for pr in processes :
        if "ggH" in pr : 
            line =  line + " 1.07110716651/0.906525580474"
        else :
             line = line + " -"
    #line = line + " \n"    
    lines.append(line)


    
def addQCDscale_muR_qqH(lines,processes):
    line = "QCDscale_muR_qqH lnN"
    for pr in processes :
        if "qqH" in pr : 
            line =  line + " 0.990706673021/1.00745328795"
        else :
             line = line + " -"
    #line = line + " \n"    
    lines.append(line)

def addQCDscale_muF_ggH(lines,processes):
    line = "QCDscale_muF_ggH lnN"
    for pr in processes :
        if "ggH" in pr : 
            line =  line + " 0.980003776978/1.01624735028"
        else :
             line = line + " -"
    #line = line + " \n"    
    lines.append(line)


    
def addQCDscale_muF_qqH(lines,processes):
    line = "QCDscale_muF_qqH lnN"
    for pr in processes :
        if "qqH" in pr : 
            line =  line + " 1.003290476/1.00409718125"
        else :
             line = line + " -"
    #line = line + " \n"    
    lines.append(line)


def addCMS_EFF_mu(lines,processes):
    line = "CMS_eff_mu lnN"
    
    for pr in processes :
        if "back_qqZZ" not in pr:  
            line = line + " 1.0191/0.9799"
        else :
            line = line + " -"
    lines.append(line)
        
def addCMS_EFF_e(lines,processes):
    line = "CMS_eff_e lnN"
    
    for pr in processes :
        if "back_qqZZ" not in pr:  
            line = line + " 1.0584/0.9383"
        else :
            line = line + " -"    
    lines.append(line)
        


def addEWcorr_qqZZ(lines,processes):
    line = "EWcorr_qqZZ lnN"
    for pr in processes :
        if "back_qqZZ" in pr : 
            line =  line + " 0.99900110477/1.0009987799"
        else :
            line = line + " -"
    #line = line + " \n"    
    lines.append(line)


def addkf_ggZZ_background(lines,processes):
    line = "kf_ggZZ_back lnN"
    for pr in processes :
        if "back_ggZZ" in pr : 
            line =  line + " 1.1/0.9"
        elif  "offggH_g11g21" in pr:

            line =  line + " 1.032/0.968"
        else:     
            line = line + " -"
    #line = line + " \n"    
    lines.append(line)

def add_pythiatune(lines,processes,category):
    line = "CMS_pythia_tune lnN"
    for pr in processes :
        if "back_qqZZ" not in pr: 
            if "Untagged" in category :
                line =  line + " 0.9985/1.0032"
            if "VHtagged" in category :
                line = line + " 1.0075/0.9973"
            if "VBFtagged" in category :
                line = line + " 1.0105/0.9967"
        else:     
            line = line + " -"

    lines.append(line)



def addkfew_as(lines,processes):
    line = "kfas_ew lnN"
    for pr in processes :
        if "offqqH" in pr: 
            line =  line + " 1.0065/0.993500"
        else:     
            line = line + " -"

    lines.append(line)
    

def addkfew_pdf(lines,processes):
    line = "kfpdf_ew lnN"
    for pr in processes :
        if "offqqH" in pr: 
            line =  line + " 1.0189/0.9811"
        else:     
            line = line + " -"

    lines.append(line)
    
def addkfew_qcdscale(lines,processes):
    line = "kfqcd_ew lnN"
    for pr in processes :
        if "offqqH" in pr: 
            line =  line + " 1.0133/0.992"
        else:      
            line = line + " -"

    lines.append(line)



    


