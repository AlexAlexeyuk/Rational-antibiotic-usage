from tkinter import * 
from tkinter import messagebox
from tkinter import ttk

cefalosporin_1 = ["цефазолин", "цефалексин" ]
cefalosporin_2 = ['цефуроксим']
cefalosporin_3 = ["цефтриаксон", "цефотаксим", "цефдинир"]
cefalosporin_4 = [ "цефтазидим", "цефепим", "цефоперазон", "цефоперазон/сульбактам"]
aminoglicazid_2 = ["амикацин", "гентамицин"]
penicillin_1 = ["амоксициллин/клавулонат", "амоксиклав", "амоклав", "аугументин", "амоксициллин/клавулоновая кислота", "амоксициллин" ]
penicillin_2 = ["пипперациллин/тазобактам"]
macrolids = ["азитромицин", "кларитромицин", "джозамицин", "эритромицин", "макропен", "спирамицин" ]
flourchinolone = ["ципрофлоксацин", "левофлоксацин", "офлоксацин", "моксифлоксацин", "норфлоксацин", "пефлоксацин"]
carbopenems = ["карбопенем", "меропенем", "эртапенем", "имепенем", "имипенем", "дорипенем"]
tetracyclines = ["тетрациклин", "доксициклин"]
glycopeptides = ["ванкомицин", "тейкопланин"]
oxazolidone = ["линезолид"]
polypeptide = ["колистин", "колистат", "полимиксин"]
sulfanilamide = ["ко-тримоксазол", "бисептол"]
nitroimidasol = ["метронидазол", "тинидазол"]
lincozamides = ["линкозамид", "клиндамицин"]

def conclusion():
    cheked_1 = combobox_antibiotic_group_1.get()
    cheked_2 = combobox_antibiotic_group_2.get()
    if var.get() == 0:
           
        while cheked_1  in penicillin_1:
           if cheked_2 in carbopenems: 
               conclusion_label.config(text= 'Нерациональная комбинация')
               break
           if cheked_2  in penicillin_1:
               conclusion_label.config(text= 'Нерациональная комбинация')
               break
           if cheked_2  in penicillin_2:
               conclusion_label.config(text= 'Нерациональная комбинация')
               break
           if cheked_2  in  polypeptide:
               conclusion_label.config(text= 'Нерациональная комбинация')
               break
           if cheked_2  in sulfanilamide:
               conclusion_label.config(text= 'Нерациональная комбинация')
               break
           else:
               conclusion_label.config(text= 'Рациональная комбинация')
               break
               
               
           
            
        while cheked_2  in penicillin_1:
           if cheked_1 in carbopenems: 
               conclusion_label.config(text= 'Нерациональная комбинация')
               break
           if cheked_1  in penicillin_1:
               conclusion_label.config(text= 'Нерациональная комбинация')
               break
           if cheked_1  in penicillin_2:
               conclusion_label.config(text= 'Нерациональная комбинация')
               break
           if cheked_1  in  polypeptide:
               conclusion_label.config(text= 'Нерациональная комбинация')
               break
           if cheked_1  in sulfanilamide:
               conclusion_label.config(text= 'Нерациональная комбинация')
               break
           else:
               conclusion_label.config(text= 'Рациональная комбинация')
               break
               
               
        while cheked_1  in penicillin_2:
           if cheked_2 in carbopenems: 
               conclusion_label.config(text= 'Нерациональная комбинация')
               break
           if cheked_2  in penicillin_1:
               conclusion_label.config(text= 'Нерациональная комбинация')
               break
           if cheked_2  in penicillin_2:
               conclusion_label.config(text= 'Нерациональная комбинация')
               break
           if cheked_2  in polypeptide:
               conclusion_label.config(text= 'Нерациональная комбинация')
               break
           if cheked_2  in  sulfanilamide :
               conclusion_label.config(text= 'Нерациональная комбинация')
               break
           else:
               conclusion_label.config(text= 'Рациональная комбинация')    
               break
           
            
        while cheked_2  in penicillin_2:
           if cheked_1 in carbopenems: 
               conclusion_label.config(text= 'Нерациональная комбинация')
               break
           if cheked_1  in penicillin_1:
               conclusion_label.config(text= 'Нерациональная комбинация')
               break
           if cheked_1  in penicillin_2:
               conclusion_label.config(text= 'Нерациональная комбинация')
               break
           if cheked_1  in polypeptide:
               conclusion_label.config(text= 'Нерациональная комбинация')
               break
           if cheked_1  in  sulfanilamide:
               conclusion_label.config(text= 'Нерациональная комбинация')
               break
           else:
               conclusion_label.config(text= 'Рациональная комбинация') 
               break
           
           

        while cheked_1 in cefalosporin_1:
           if cheked_2 in carbopenems:
               conclusion_label.config(text= 'Нерациональная комбинация ')
               break
           if cheked_2 in cefalosporin_1: 
               conclusion_label.config(text= 'Нерациональная комбинация ')
               break
           if cheked_2 in cefalosporin_2: 
               conclusion_label.config(text= 'Нерациональная комбинация ')
               break
           if cheked_2 in cefalosporin_3:
               conclusion_label.config(text= 'Нерациональная комбинация ')
               break
           if cheked_2 in cefalosporin_4:
               conclusion_label.config(text= 'Нерациональная комбинация ')
               break
           if cheked_2 in polypeptide:
               conclusion_label.config(text= 'Нерациональная комбинация, риск нефротоксичности ')
               break
           else:
               conclusion_label.config(text= 'Рациональная комбинация')
               break               
               
        while cheked_2 in cefalosporin_1:
           if cheked_1 in carbopenems:
               conclusion_label.config(text= 'Нерациональная комбинация ')
               break
           if cheked_1 in cefalosporin_1: 
               conclusion_label.config(text= 'Нерациональная комбинация ')
               break
           if cheked_1 in cefalosporin_2: 
               conclusion_label.config(text= 'Нерациональная комбинация ')
               break
           if cheked_1 in cefalosporin_3:
               conclusion_label.config(text= 'Нерациональная комбинация ')
               break
           if cheked_1 in cefalosporin_4:
               conclusion_label.config(text= 'Нерациональная комбинация ')
               break
           if cheked_1 in polypeptide:
               conclusion_label.config(text= 'Нерациональная комбинация, риск нефротоксичности ')
               break
           else:
               conclusion_label.config(text= 'Рациональная комбинация')    
               break                          
               
        while cheked_1 in cefalosporin_2:
           if cheked_2 in carbopenems:
               conclusion_label.config(text= 'Нерациональная комбинация ')
               break
           if cheked_2 in cefalosporin_1: 
               conclusion_label.config(text= 'Нерациональная комбинация ')
               break
           if cheked_2 in cefalosporin_2: 
               conclusion_label.config(text= 'Нерациональная комбинация ')
               break
           if cheked_2 in cefalosporin_3:
               conclusion_label.config(text= 'Нерациональная комбинация ')
               break
           if cheked_2 in cefalosporin_4:
               conclusion_label.config(text= 'Нерациональная комбинация ')
               break
           if cheked_2 in polypeptide:
               conclusion_label.config(text= 'Нерациональная комбинация, риск нефротоксичности ')
               break
           else:
               conclusion_label.config(text= 'Рациональная комбинация')
               break               
               
        while cheked_2 in cefalosporin_2:
           if cheked_1 in carbopenems:
               conclusion_label.config(text= 'Нерациональная комбинация ')
               break
           if cheked_1 in cefalosporin_1: 
               conclusion_label.config(text= 'Нерациональная комбинация ')
               break
           if cheked_1 in cefalosporin_2: 
               conclusion_label.config(text= 'Нерациональная комбинация ')
               break
           if cheked_1 in cefalosporin_3:
               conclusion_label.config(text= 'Нерациональная комбинация ')
               break
           if cheked_1 in cefalosporin_4:
               conclusion_label.config(text= 'Нерациональная комбинация ')
               break
           if cheked_1 in polypeptide:
               conclusion_label.config(text= 'Нерациональная комбинация, риск нефротоксичности ')
               break
           else:
               conclusion_label.config(text= 'Рациональная комбинация')    
               break                         
        while cheked_1 in cefalosporin_3:
           if cheked_2 in carbopenems:
               conclusion_label.config(text= 'Нерациональная комбинация ')
               break
           if cheked_2 in cefalosporin_1: 
               conclusion_label.config(text= 'Нерациональная комбинация ')
               break
           if cheked_2 in cefalosporin_2: 
               conclusion_label.config(text= 'Нерациональная комбинация ')
               break
           if cheked_2 in cefalosporin_3:
               conclusion_label.config(text= 'Нерациональная комбинация ')
               break
           if cheked_2 in cefalosporin_4:
               conclusion_label.config(text= 'Нерациональная комбинация ')
               break
           if cheked_2 in polypeptide:
               conclusion_label.config(text= 'Нерациональная комбинация, риск нефротоксичности ')
               break
           else:
               conclusion_label.config(text= 'Рациональная комбинация')
               break               
               
        while cheked_2 in cefalosporin_3:
           if cheked_1 in carbopenems:
               conclusion_label.config(text= 'Нерациональная комбинация ')
               break
           if cheked_1 in cefalosporin_1: 
               conclusion_label.config(text= 'Нерациональная комбинация ')
               break
           if cheked_1 in cefalosporin_2: 
               conclusion_label.config(text= 'Нерациональная комбинация ')
               break
           if cheked_1 in cefalosporin_3:
               conclusion_label.config(text= 'Нерациональная комбинация ')
               break
           if cheked_1 in cefalosporin_4:
               conclusion_label.config(text= 'Нерациональная комбинация ')
               break
           if cheked_1 in polypeptide:
               conclusion_label.config(text= 'Нерациональная комбинация, риск нефротоксичности ')
               break
           else:
               conclusion_label.config(text= 'Рациональная комбинация')    
               break                          
        while cheked_1 in cefalosporin_4:
           if cheked_2 in carbopenems:
               conclusion_label.config(text= 'Нерациональная комбинация ')
               break
           if cheked_2 in cefalosporin_1: 
               conclusion_label.config(text= 'Нерациональная комбинация ')
               break
           if cheked_2 in cefalosporin_2: 
               conclusion_label.config(text= 'Нерациональная комбинация ')
               break
           if cheked_2 in cefalosporin_3:
               conclusion_label.config(text= 'Нерациональная комбинация ')
               break
           if cheked_2 in cefalosporin_4:
               conclusion_label.config(text= 'Нерациональная комбинация ')
               break
           if cheked_2 in polypeptide:
               conclusion_label.config(text= 'Нерациональная комбинация, риск нефротоксичности ')
               break
           else:
               conclusion_label.config(text= 'Рациональная комбинация')
               break               
               
        while cheked_2 in cefalosporin_4:
           if cheked_1 in carbopenems:
               conclusion_label.config(text= 'Нерациональная комбинация ')
               break
           if cheked_1 in cefalosporin_1: 
               conclusion_label.config(text= 'Нерациональная комбинация ')
               break
           if cheked_1 in cefalosporin_2: 
               conclusion_label.config(text= 'Нерациональная комбинация ')
               break
           if cheked_1 in cefalosporin_3:
               conclusion_label.config(text= 'Нерациональная комбинация ')
               break
           if cheked_1 in cefalosporin_4:
               conclusion_label.config(text= 'Нерациональная комбинация ')
               break
           if cheked_1 in polypeptide:
               conclusion_label.config(text= 'Нерациональная комбинация, риск нефротоксичности ')
               break
           else:
               conclusion_label.config(text= 'Рациональная комбинация')    
               break                          
               
               

        while cheked_2 in carbopenems:
            if cheked_1 in polypeptide:
               conclusion_label.config(text= 'Нерациональная комбинация ')
               break
            if cheked_1 in lincozamides:
               conclusion_label.config(text= 'Нерациональная комбинация ')
               break 
            if cheked_1 in sulfanilamide:
               conclusion_label.config(text= 'Нерациональная комбинация ')
               break                
            if cheked_1 in nitroimidasol:
               conclusion_label.config(text= 'Нерациональная комбинация ')
               break      
            if cheked_1 in carbopenems:
               conclusion_label.config(text= 'Нерациональная комбинация ')
               break 
            if cheked_1 in cefalosporin_1: 
               conclusion_label.config(text= 'Нерациональная комбинация ')
               break
            if cheked_1 in cefalosporin_2: 
               conclusion_label.config(text= 'Нерациональная комбинация ')
               break
            if cheked_1 in cefalosporin_3:
               conclusion_label.config(text= 'Нерациональная комбинация ')
               break
            if cheked_1 in cefalosporin_4:
               conclusion_label.config(text= 'Нерациональная комбинация ')
               break
            if cheked_1 in lincozamides:
               conclusion_label.config(text= 'Нерациональная комбинация ')
               break 
            else:
               conclusion_label.config(text= 'Рациональная комбинация ')
               break 
               
           
        while cheked_1 in carbopenems:
            if cheked_2 in polypeptide:
               conclusion_label.config(text= 'Нерациональная комбинация ')
               break
            if cheked_2 in cefalosporin_1: 
               conclusion_label.config(text= 'Нерациональная комбинация ')
               break
            if cheked_2 in cefalosporin_2: 
               conclusion_label.config(text= 'Нерациональная комбинация ')
               break
            if cheked_2 in cefalosporin_3:
               conclusion_label.config(text= 'Нерациональная комбинация ')
               break
            if cheked_2 in cefalosporin_4:
               conclusion_label.config(text= 'Нерациональная комбинация ')
               break
            if cheked_2 in lincozamides:
               conclusion_label.config(text= 'Нерациональная комбинация ')
               break 
            if cheked_2 in sulfanilamide:
               conclusion_label.config(text= 'Нерациональная комбинация ')
               break                
            if cheked_2 in nitroimidasol:
               conclusion_label.config(text= 'Нерациональная комбинация ')
               break      
            if cheked_2 in carbopenems:
               conclusion_label.config(text= 'Нерациональная комбинация ')
               break    
            if cheked_2 in lincozamides:
               conclusion_label.config(text= 'Нерациональная комбинация ')
               break 
            else:
               conclusion_label.config(text= 'Рациональная комбинация ')
               break 
               
            
        while cheked_1 in aminoglicazid_2:
            if cheked_2 in polypeptide: 
               conclusion_label.config(text= 'Нерациональная комбинация ')
               break 
            if cheked_2 in aminoglicazid_2:
               conclusion_label.config(text= 'Нерациональная комбинация ')
               break 
            else:
               conclusion_label.config(text= 'Рациональная комбинация ')
               break 
          
        while cheked_2 in aminoglicazid_2:
            if cheked_1 in polypeptide: 
               conclusion_label.config(text= 'Нерациональная комбинация ')
               break 
            if cheked_1 in aminoglicazid_2:
               conclusion_label.config(text= 'Нерациональная комбинация ')
               break 
            else:
               conclusion_label.config(text= 'Рациональная комбинация ')
               break 
            
            
            
            
        while cheked_2 in flourchinolone:
            if cheked_1 in sulfanilamide:
               conclusion_label.config(text= 'Нерациональная комбинация ')
               break 
            if cheked_1 in flourchinolone:
               conclusion_label.config(text= 'Нерациональная комбинация ')
               break 
            else:
               conclusion_label.config(text= 'Рациональная комбинация ') 
               break 
        while cheked_1 in flourchinolone:
            if cheked_2 in sulfanilamide:
               conclusion_label.config(text= 'Нерациональная комбинация ')
               break 
            if cheked_2 in flourchinolone:
               conclusion_label.config(text= 'Нерациональная комбинация ')
               break 
            else:
               conclusion_label.config(text= 'Рациональная комбинация ') 
               break 
               
               
        while cheked_1 in tetracyclines:
            if cheked_2 in sulfanilamide:
               conclusion_label.config(text= 'Нерациональная комбинация ')
               break  
            if cheked_2 in tetracyclines:
               conclusion_label.config(text= 'Нерациональная комбинация ')
               break 
            if cheked_2 in glycopeptides:
               conclusion_label.config(text= 'Нерациональная комбинация ')
               break 
            else:
               conclusion_label.config(text= 'Рациональная комбинация ')  
               break 
        while cheked_2 in tetracyclines:
            if cheked_1 in sulfanilamide:
               conclusion_label.config(text= 'Нерациональная комбинация ')
               break  
            if cheked_1 in glycopeptides:
               conclusion_label.config(text= 'Нерациональная комбинация ')
               break 
            if cheked_1 in tetracyclines:
               conclusion_label.config(text= 'Нерациональная комбинация ')
               break 
            else:
               conclusion_label.config(text= 'Рациональная комбинация ')  
               break 
           
            
        while cheked_1 in macrolids:
             if cheked_2 in lincozamides:
               conclusion_label.config(text= 'Нерациональная комбинация ')
               break 
             if cheked_2 in glycopeptides:
               conclusion_label.config(text= 'Нерациональная комбинация ')
               break 
             if cheked_2 in polypeptide: 
               conclusion_label.config(text= 'Нерациональная комбинация ')
               break
             if cheked_2 in oxazolidone:
               conclusion_label.config(text= 'Нерациональная комбинация ')
               break
             if cheked_2 in macrolids:
               conclusion_label.config(text= 'Нерациональная комбинация ')
               break 
             else:
               conclusion_label.config(text= 'Рациональная комбинация ')  
               break                 
        while cheked_2 in macrolids:
             if cheked_1 in lincozamides:
               conclusion_label.config(text= 'Нерациональная комбинация ')
               break 
             if cheked_1 in glycopeptides:
               conclusion_label.config(text= 'Нерациональная комбинация ')
               break 
             if cheked_1 in polypeptide: 
               conclusion_label.config(text= 'Нерациональная комбинация ')
               break
             if cheked_1 in oxazolidone:
               conclusion_label.config(text= 'Нерациональная комбинация ')
               break
             if cheked_1 in macrolids:
               conclusion_label.config(text= 'Нерациональная комбинация ')
               break  
             else:
               conclusion_label.config(text= 'Рациональная комбинация ')  
               break         

        while cheked_1 in lincozamides:
             if cheked_2 in lincozamides:
               conclusion_label.config(text= 'Нерациональная комбинация ')
               break 
             if cheked_2 in glycopeptides:
               conclusion_label.config(text= 'Нерациональная комбинация ')
               break 
             if cheked_2 in polypeptide: 
               conclusion_label.config(text= 'Нерациональная комбинация ')
               break
             if cheked_2 in macrolids:
               conclusion_label.config(text= 'Нерациональная комбинация ')
               break  
             if cheked_2 in oxazolidone:
               conclusion_label.config(text= 'Нерациональная комбинация ')
               break
             if cheked_2 in nitroimidasol:
               conclusion_label.config(text= 'Нерациональная комбинация ')
               break   
             if cheked_1 in carbopenems:
               conclusion_label.config(text= 'Нерациональная комбинация ')
               break   
             else:
               conclusion_label.config(text= 'Рациональная комбинация ')  
               break      
           
        while cheked_2 in lincozamides:
             if cheked_1 in lincozamides:
               conclusion_label.config(text= 'Нерациональная комбинация ')
               break 
             if cheked_1 in macrolids:
               conclusion_label.config(text= 'Нерациональная комбинация ')
               break  
             if cheked_1 in glycopeptides:
               conclusion_label.config(text= 'Нерациональная комбинация ')
               break 
             if cheked_1 in polypeptide: 
               conclusion_label.config(text= 'Нерациональная комбинация ')
               break
             if cheked_1 in oxazolidone:
               conclusion_label.config(text= 'Нерациональная комбинация ')
               break
             if cheked_1 in nitroimidasol:
               conclusion_label.config(text= 'Нерациональная комбинация ')
               break   
             if cheked_1 in carbopenems:
               conclusion_label.config(text= 'Нерациональная комбинация ')
               break   
             else:
               conclusion_label.config(text= 'Рациональная комбинация ')  
               break         
           
            
        while cheked_1 in glycopeptides:
             if cheked_2 in lincozamides:
               conclusion_label.config(text= 'Нерациональная комбинация ')
               break 
             if cheked_2 in macrolids:
               conclusion_label.config(text= 'Нерациональная комбинация ')
               break  
             if cheked_2 in glycopeptides:
               conclusion_label.config(text= 'Нерациональная комбинация ')
               break 
             if cheked_2 in polypeptide: 
               conclusion_label.config(text= 'Нерациональная комбинация ')
               break
             if cheked_2 in oxazolidone:
               conclusion_label.config(text= 'Нерациональная комбинация ')
               break
             if cheked_2 in nitroimidasol:
               conclusion_label.config(text= 'Нерациональная комбинация ')
               break   
             if cheked_2 in sulfanilamide:
               conclusion_label.config(text= 'Нерациональная комбинация ')
               break   
             else:
               conclusion_label.config(text= 'Рациональная комбинация ')  
               break                     


        while cheked_2 in glycopeptides:
             if cheked_1 in lincozamides:
               conclusion_label.config(text= 'Нерациональная комбинация ')
               break 
             if cheked_1 in macrolids:
               conclusion_label.config(text= 'Нерациональная комбинация ')
               break  
             if cheked_1 in glycopeptides:
               conclusion_label.config(text= 'Нерациональная комбинация ')
               break 
             if cheked_1 in polypeptide: 
               conclusion_label.config(text= 'Нерациональная комбинация ')
               break
             if cheked_1 in oxazolidone:
               conclusion_label.config(text= 'Нерациональная комбинация ')
               break
             if cheked_1 in nitroimidasol:
               conclusion_label.config(text= 'Нерациональная комбинация ')
               break   
             if cheked_1 in sulfanilamide:
               conclusion_label.config(text= 'Нерациональная комбинация ')
               break   
             else:
               conclusion_label.config(text= 'Рациональная комбинация ')  
               break               


        while cheked_2 in oxazolidone:
             if cheked_1 in lincozamides:
               conclusion_label.config(text= 'Нерациональная комбинация ')
               break 
             if cheked_1 in macrolids:
               conclusion_label.config(text= 'Нерациональная комбинация ')
               break  
             if cheked_1 in glycopeptides:
               conclusion_label.config(text= 'Нерациональная комбинация ')
               break 
             if cheked_1 in polypeptide: 
               conclusion_label.config(text= 'Нерациональная комбинация ')
               break
             if cheked_1 in oxazolidone:
               conclusion_label.config(text= 'Нерациональная комбинация ')
               break
             if cheked_1 in nitroimidasol:
               conclusion_label.config(text= 'Нерациональная комбинация ')
               break   
             if cheked_1 in sulfanilamide:
               conclusion_label.config(text= 'Нерациональная комбинация ')
               break   
             else:
               conclusion_label.config(text= 'Рациональная комбинация ')  
               break  
           
        while cheked_1 in oxazolidone:
             if cheked_2 in lincozamides:
               conclusion_label.config(text= 'Нерациональная комбинация ')
               break 
             if cheked_2 in macrolids:
               conclusion_label.config(text= 'Нерациональная комбинация ')
               break  
             if cheked_2 in glycopeptides:
               conclusion_label.config(text= 'Нерациональная комбинация ')
               break 
             if cheked_2 in polypeptide: 
               conclusion_label.config(text= 'Нерациональная комбинация ')
               break
             if cheked_2 in oxazolidone:
               conclusion_label.config(text= 'Нерациональная комбинация ')
               break
             if cheked_2 in nitroimidasol:
               conclusion_label.config(text= 'Нерациональная комбинация ')
               break   
             if cheked_2 in sulfanilamide:
               conclusion_label.config(text= 'Нерациональная комбинация ')
               break   
             else:
               conclusion_label.config(text= 'Рациональная комбинация ')  
               break 
           
            
            
        while cheked_1 in polypeptide:
             if cheked_2 in aminoglicazid_2:
               conclusion_label.config(text= 'Рациональная комбинация, риск нефротоксичности ')
               break 
             if cheked_2 in flourchinolone:
               conclusion_label.config(text= 'Рациональная комбинация ')
               break  
             else:
               conclusion_label.config(text= 'Нерациональная комбинация ')  
               break 
                    
           
        while cheked_2 in polypeptide:
             if cheked_1 in aminoglicazid_2:
               conclusion_label.config(text= 'Рациональная комбинация, риск нефротоксичности ')
               break 
             if cheked_1 in flourchinolone:
               conclusion_label.config(text= 'Рациональная комбинация ')
               break  
             else:
               conclusion_label.config(text= 'Нерациональная комбинация ')  
               break 
           
            
    if var.get() == 1:
        cheked_1 = combobox_antibiotic_group_1.get()
        cheked_2 = combobox_antibiotic_group_2.get()
        if cheked_1 in cefalosporin_1 and cheked_2 in aminoglicazid_2 or cheked_2 in cefalosporin_1 and cheked_1 in aminoglicazid_2:
            messagebox.showinfo('Активность', 'Staphylococcus aureus(++) (кроме MRSA),'
                               'Streptococcus pneumoniae(++), Haemophilus influenzae(включая штаммы, вырабатывающие пенициллиназу) '
                               'Escherichia coli, Klebsiella pneumonia (++), Proteus mirabilis, '
                               'Pseudomonas aeruginosa(+\-), Acinetobacter baumanii(+\-) \n '
                               '++ = синергия|+\- = умеренная активность'
                               '\n слабые места: атипичная флора, резистентные штаммы K.pneumoniae, P.aeruginosae, Acinetobacter')
        if cheked_1 in cefalosporin_2 and cheked_2 in aminoglicazid_2 or cheked_2 in cefalosporin_2 and cheked_1 in aminoglicazid_2:
            messagebox.showinfo('Активность', ' Moraxella catarrhalis, Staphylococcus aureus(++) (кроме MRSA),'
                               'Streptococcus pneumoniae(++), Haemophilus influenzae(включая штаммы, вырабатывающие пенициллиназу) '
                               'Escherichia coli, Klebsiella pneumonia (++), Proteus mirabilis, '
                               'Pseudomonas aeruginosa(+\-), Acinetobacter baumanii(+\-) \n '
                               '++ = синергия|+\- = умеренная активность'
                               '\n слабые места: атипичная флора, MRSA,, резистентные штаммы K.pneumoniae, P.aeruginosae, Acinetobacter')
         
        if cheked_1 in cefalosporin_3 and cheked_2 in aminoglicazid_2 or cheked_2 in cefalosporin_3 and cheked_1 in aminoglicazid_2:
            messagebox.showinfo('Активность', ' Moraxella catarrhalis, Staphylococcus aureus(++) (кроме MRSA),'
                               'Streptococcus pneumoniae(++), Haemophilus influenzae(включая штаммы, вырабатывающие пенициллиназу) '
                               'Escherichia coli, Klebsiella pneumonia (++), Proteus mirabilis(++), '
                               'Pseudomonas aeruginosa(+\-), Acinetobacter baumanii(+\-) \n '
                               '++ = синергия|+\- = умеренная активность'
                               '\n слабые места: атипичная флора, MRSA, резистентные штаммы K.pneumoniae, P.aeruginosae, Acinetobacter')
        if cheked_1 in cefalosporin_4 and cheked_2 in aminoglicazid_2 or cheked_2 in cefalosporin_4 and cheked_1 in aminoglicazid_2:
            messagebox.showinfo('Активность', ' Moraxella catarrhalis, Staphylococcus aureus(++) (кроме MRSA),'
                               'Streptococcus pneumoniae(++), Haemophilus influenzae(включая штаммы, вырабатывающие пенициллиназу) '
                               'Escherichia coli, Klebsiella pneumonia (++), Proteus mirabilis(++), '
                               'Pseudomonas aeruginosa(++!), Acinetobacter baumanii(+\-) \n '
                               '++ = синергия|+\- = умеренная активность| ++! = выбор при подозрении'
                               '\n слабые места: атипичная флора, MRSA, резистентные штаммы K.pneumoniae, P.aeruginosae, Acinetobacter')
        
        if cheked_1 in cefalosporin_1 and cheked_2 in macrolids or cheked_2 in cefalosporin_1 and cheked_1 in macrolids:
            messagebox.showinfo('Активность','Staphylococcus aureus (кроме MRSA),'
                               'Streptococcus pneumoniae(+?), Haemophilus influenzae(включая штаммы, вырабатывающие пенициллиназу)(+?) '
                               'Escherichia coli, Klebsiella pneumonia (+\-), Proteus mirabilis, Legionella pneumophila(+!), Mycoplasma pneumoniae(+!),'
                               'Chlamydia pneumoniae(+!),  Moraxella catarrhalis(+/-), Bordetella pertussis(+!) \n'
                               '++ = синергия|+\- = умеренная активность| +! = выбор при подозрении |+?= большинство штаммов резистентны к макролидам'
                               '\n слабые места:  MRSA, резистентные штаммы K.pneumoniae, P.aeruginosae')
        if cheked_1 in cefalosporin_3 and cheked_2 in macrolids or cheked_2 in cefalosporin_3 and cheked_1 in macrolids:
            messagebox.showinfo('Активность','Staphylococcus aureus(++) (кроме MRSA),Moraxella catarrhalis,'
                               'Streptococcus pneumoniae(++), Haemophilus influenzae(включая штаммы, вырабатывающие пенициллиназу)(++) '
                               'Escherichia coli, Klebsiella pneumonia , Proteus mirabilis, Legionella pneumophila(+!), Mycoplasma pneumoniae(+!),'
                               'Chlamydia pneumoniae(+!), Bordetella pertussis(+!) \n'
                               '++ = синергия|+\- = умеренная активность| +! = выбор при подозрении'
                               '\n слабые места:  MRSA, резистентные штаммы K.pneumoniae, P.aeruginosae')
        if cheked_1 in cefalosporin_2 and cheked_2 in macrolids or cheked_2 in cefalosporin_2 and cheked_1 in macrolids:
            messagebox.showinfo('Активность','Staphylococcus aureus(++) (кроме MRSA), Moraxella catarrhalis,'
                               'Streptococcus pneumoniae(++), Haemophilus influenzae(включая штаммы, вырабатывающие пенициллиназу)(++) '
                               'Escherichia coli, Klebsiella pneumonia , Proteus mirabilis, Legionella pneumophila(+!), Mycoplasma pneumoniae(+!),'
                               'Chlamydia pneumoniae(+!), Bordetella pertussis(+!) \n'
                               '++ = синергия|+\- = умеренная активность| +! = выбор при подозрении'
                               '\n слабые места:  MRSA, резистентные штаммы K.pneumoniae, P.aeruginosae')
        if cheked_1 in cefalosporin_4 and cheked_2 in macrolids or cheked_2 in cefalosporin_4 and cheked_1 in macrolids:
            messagebox.showinfo('Активность','Staphylococcus aureus(++) (кроме MRSA), Moraxella catarrhalis,'
                               'Streptococcus pneumoniae(++), Haemophilus influenzae(включая штаммы, вырабатывающие пенициллиназу)(++) '
                               'Escherichia coli, Klebsiella pneumonia , Proteus mirabilis, Legionella pneumophila(+!), Mycoplasma pneumoniae(+!),'
                               'Pseudomonas aeruginosa, Acinetobacter baumanii(+\-)'
                               'Chlamydia pneumoniae(+!), Bordetella pertussis(+!) \n'
                               '++ = синергия|+\- = умеренная активность| +! = выбор при подозрении'
                               '\n слабые места:  MRSA, резистентные штаммы K.pneumoniae, P.aeruginosae')
            
        if cheked_1 in cefalosporin_1 and cheked_2 in tetracyclines or cheked_2 in cefalosporin_1 and cheked_1 in tetracyclines:
            #conclusion_label.config(text="Рациональная комбинация")
            messagebox.showinfo('Активность','Staphylococcus aureus (кроме MRSA)(++),'
                               'Streptococcus pneumoniae(++), Haemophilus influenzae(включая штаммы, вырабатывающие пенициллиназу)(++) '
                               'Escherichia coli, Klebsiella pneumonia (+\-), Proteus mirabilis, Legionella pneumophila(+\-), Mycoplasma pneumoniae(+\-),'
                               'Chlamydia pneumoniae(+\-),  Moraxella catarrhalis(+\-), Bordetella pertussis(+\-) \n'
                               '++ = синергия|+\- = умеренная активность, комбинация может быть рассмотрена при подозрении'
                               '\n слабые места:  MRSA, резистентные штаммы K.pneumoniae, P.aeruginosae')
        if cheked_1 in cefalosporin_2 and cheked_2 in tetracyclines or cheked_2 in cefalosporin_2 and cheked_1 in tetracyclines:
            messagebox.showinfo('Активность','Staphylococcus aureus(++) (кроме MRSA), Moraxella catarrhalis,'
                               'Streptococcus pneumoniae(++), Haemophilus influenzae(включая штаммы, вырабатывающие пенициллиназу)(++) '
                               'Escherichia coli, Klebsiella pneumonia (+\-), Proteus mirabilis, Legionella pneumophila(+\-), Mycoplasma pneumoniae(+\-),'
                               'Chlamydia pneumoniae(+\-), Bordetella pertussis(+\-) \n'
                               '++ = синергия|+\- = умеренная активность, комбинация может быть рассмотрена при подозрении'
                               '\n слабые места:  MRSA, резистентные штаммы K.pneumoniae, P.aeruginosae')
        if cheked_1 in cefalosporin_3 and cheked_2 in tetracyclines or cheked_2 in cefalosporin_3 and cheked_1 in tetracyclines:
            messagebox.showinfo('Активность','Staphylococcus aureus(++) (кроме MRSA), Moraxella catarrhalis,'
                               'Streptococcus pneumoniae(++), Haemophilus influenzae(включая штаммы, вырабатывающие пенициллиназу)(++) '
                               'Escherichia coli, Klebsiella pneumonia, Pseudomonas aeruginosae(+\-), Proteus mirabilis, Legionella pneumophila(+\-), Mycoplasma pneumoniae(+\-),'
                               'Chlamydia pneumoniae(+\-), Bordetella pertussis(+\-) \n'
                               '++ = синергия|+\- = умеренная активность, комбинация может быть рассмотрена при подозрении'
                               '\n слабые места:  MRSA, резистентные штаммы K.pneumoniae, P.aeruginosae')
        if cheked_1 in cefalosporin_4 and cheked_2 in tetracyclines or cheked_2 in cefalosporin_4 and cheked_1 in tetracyclines:
            messagebox.showinfo('Активность','Staphylococcus aureus(++) (кроме MRSA), Moraxella catarrhalis,'
                               'Streptococcus pneumoniae(++), Haemophilus influenzae(включая штаммы, вырабатывающие пенициллиназу)(++) '
                               'Escherichia coli, Klebsiella pneumonia, Pseudomonas aeruginosae , Proteus mirabilis, Legionella pneumophila(+\-), Mycoplasma pneumoniae(+\-),'
                               'Chlamydia pneumoniae(+\-),, Bordetella pertussis(+\-) \n'
                               '++ = синергия|+\- = умеренная активность, комбинация может быть рассмотрена при подозрении'
                               '\n слабые места:  MRSA, резистентные штаммы K.pneumoniae, P.aeruginosae')
        if cheked_1 in cefalosporin_1 and cheked_2 in flourchinolone or cheked_2 in cefalosporin_1 and cheked_1 in flourchinolone:
            messagebox.showinfo ('Активность','Staphylococcus aureus(++)* (кроме MRSA), Moraxella catarrhalis(++)*,'
                               'Streptococcus pneumoniae(++)*, Haemophilus influenzae(включая штаммы, вырабатывающие пенициллиназу)(++)* '
                               'Escherichia coli, Klebsiella pneumonia , Pseudomonas aeruginosae(**), Proteus mirabilis, Legionella pneumophila, Mycoplasma pneumoniae,'
                               'Chlamydia pneumoniae,, Bordetella pertussis \n'
                               '++* = синергия, относится к лево и моксифлоксацину|** = относится к ципрофлоксацину|+\- = умеренная активность, комбинация может быть рассмотрена при подозрении'
                               '\n слабые места:  MRSA, резистентные штаммы K.pneumoniae, P.aeruginosae')
        if cheked_1 in cefalosporin_2 and cheked_2 in flourchinolone or cheked_2 in cefalosporin_2 and cheked_1 in flourchinolone:
            messagebox.showinfo ('Активность','Staphylococcus aureus(++)* (кроме MRSA), Moraxella catarrhalis(++)*,'
                               'Streptococcus pneumoniae(++)*, Haemophilus influenzae(включая штаммы, вырабатывающие пенициллиназу)(++)* '
                               'Escherichia coli, Klebsiella pneumonia , Pseudomonas aeruginosae(**), Proteus mirabilis, Legionella pneumophila, Mycoplasma pneumoniae,'
                               'Chlamydia pneumoniae,, Bordetella pertussis \n'
                               '++* = синергия, относится к лево и моксифлоксацину|** = относится к ципрофлоксацину|+\- = умеренная активность, комбинация может быть рассмотрена при подозрении'
                               '\n слабые места:  MRSA, резистентные штаммы K.pneumoniae, P.aeruginosae')
        if cheked_1 in cefalosporin_3 and cheked_2 in flourchinolone or cheked_2 in cefalosporin_3 and cheked_1 in flourchinolone:
            messagebox.showinfo ('Активность','Staphylococcus aureus(++)* (кроме MRSA), Moraxella catarrhalis(++)*,'
                               'Streptococcus pneumoniae(++)*, Haemophilus influenzae(включая штаммы, вырабатывающие пенициллиназу)(++)* '
                               'Escherichia coli, Klebsiella pneumonia , Pseudomonas aeruginosae(**), Proteus mirabilis, Legionella pneumophila, Mycoplasma pneumoniae,'
                               'Chlamydia pneumoniae,, Bordetella pertussis \n'
                               '++* = синергия, относится к лево и моксифлоксацину|** = относится к ципрофлоксацину|+\- = умеренная активность, комбинация может быть рассмотрена при подозрении'
                               '\n слабые места:  MRSA, резистентные штаммы K.pneumoniae, P.aeruginosae')
       
        if cheked_1 in cefalosporin_4 and cheked_2 in flourchinolone or cheked_2 in cefalosporin_4 and cheked_1 in flourchinolone:
            messagebox.showinfo ('Активность','Staphylococcus aureus(++)* (кроме MRSA), Moraxella catarrhalis(++)*,'
                               'Streptococcus pneumoniae(++)*, Haemophilus influenzae(включая штаммы, вырабатывающие пенициллиназу)(++)* '
                               'Escherichia coli, Klebsiella pneumonia , Pseudomonas aeruginosae(!**), Proteus mirabilis, Legionella pneumophila, Mycoplasma pneumoniae,'
                               'Chlamydia pneumoniae,, Bordetella pertussis \n'
                               '++* = синергия, относится к лево и моксифлоксацину|!** = синергия, относится к ципрофлоксацину, комбинация выбора при подозрении|+\- = умеренная активность, комбинация может быть рассмотрена при подозрении'
                               '\n слабые места:  MRSA, резистентные штаммы K.pneumoniae, P.aeruginosae')
        if cheked_1 in cefalosporin_1 and cheked_2 in lincozamides or cheked_2 in cefalosporin_1 and cheked_1 in lincozamides:
            messagebox.showinfo ('Активность','Staphylococcus aureus(++) (кроме MRSA), '
                               'Streptococcus pneumoniae(++), Haemophilus influenzae(включая штаммы, вырабатывающие пенициллиназу) '
                               'Escherichia coli, Klebsiella pneumonia, анаэробы бактероиды, клостридии, пептококки'
                               '++ = синергия|'
                               '\n слабые места:  атипичная флора, MRSA, резистентные штаммы K.pneumoniae, P.aeruginosae')
        if cheked_1 in cefalosporin_2 and cheked_2 in lincozamides or cheked_2 in cefalosporin_2 and cheked_1 in lincozamides:
            messagebox.showinfo ('Активность','Staphylococcus aureus(++) (кроме MRSA), Moraxella catarrhalis,'
                               'Streptococcus pneumoniae(++), Haemophilus influenzae(включая штаммы, вырабатывающие пенициллиназу) '
                               'Escherichia coli, Klebsiella pneumonia, анаэробы бактероиды, клостридии, пептококки'
                               '++ = синергия|'
                               '\n слабые места:  атипичная флора, MRSA, резистентные штаммы K.pneumoniae, P.aeruginosae')   
        if cheked_1 in cefalosporin_3 and cheked_2 in lincozamides or cheked_2 in cefalosporin_3 and cheked_1 in lincozamides:
            messagebox.showinfo ('Активность','Staphylococcus aureus(++) (кроме MRSA), Moraxella catarrhalis,'
                               'Streptococcus pneumoniae(++), Haemophilus influenzae(включая штаммы, вырабатывающие пенициллиназу) '
                               'Escherichia coli, Klebsiella pneumonia, Pseudomonas aeruginosae(+\-) анаэробы бактероиды, клостридии, пептококки'
                               '++ = синергия|+\- = умеренная активность'
                               '\n слабые места:  атипичная флора, MRSA, резистентные штаммы K.pneumoniae, P.aeruginosae') 
        if cheked_1 in cefalosporin_4 and cheked_2 in lincozamides or cheked_2 in cefalosporin_4 and cheked_1 in lincozamides:
            messagebox.showinfo ('Активность','Staphylococcus aureus(++) (кроме MRSA), Moraxella catarrhalis,'
                               'Streptococcus pneumoniae(++), Haemophilus influenzae(включая штаммы, вырабатывающие пенициллиназу) '
                               'Escherichia coli, Klebsiella pneumonia, Pseudomonas aeruginosae, анаэробы бактероиды, клостридии, пептококки'
                               '++ = синергия'
                               '\n слабые места:  атипичная флора, MRSA, резистентные штаммы K.pneumoniae, P.aeruginosae')            
        if cheked_1 in cefalosporin_1 and cheked_2 in nitroimidasol or cheked_2 in cefalosporin_1 and cheked_1 in nitroimidasol:
            messagebox.showinfo ('Активность','Staphylococcus aureus (кроме MRSA),'
                               'Streptococcus pneumoniae, Haemophilus influenzae(включая штаммы, вырабатывающие пенициллиназу) '
                               'Escherichia coli, Klebsiella pneumonia, анаэробы бактероиды, клостридии, пептококки'
                               '\n слабые места:  атипичная флора, MRSA, резистентные штаммы K.pneumoniae, P.aeruginosae') 
        if cheked_1 in cefalosporin_2 and cheked_2 in nitroimidasol or cheked_2 in cefalosporin_2 and cheked_1 in nitroimidasol:
            messagebox.showinfo ('Активность','Staphylococcus aureus (кроме MRSA), Moraxella catarrhalis,'
                               'Streptococcus pneumoniae, Haemophilus influenzae(включая штаммы, вырабатывающие пенициллиназу) '
                               'Escherichia coli, Klebsiella pneumonia, анаэробы бактероиды, клостридии, пептококки'
                               '\n слабые места:  атипичная флора, MRSA, резистентные штаммы K.pneumoniae, P.aeruginosae') 
        if cheked_1 in cefalosporin_3 and cheked_2 in nitroimidasol or cheked_2 in cefalosporin_3 and cheked_1 in nitroimidasol:
            messagebox.showinfo ('Активность','Staphylococcus aureus (кроме MRSA),Moraxella catarrhalis,'
                               'Streptococcus pneumoniae, Haemophilus influenzae(включая штаммы, вырабатывающие пенициллиназу) '
                               'Escherichia coli, Klebsiella pneumonia, Pseudomonas aeruginosae(+\-) анаэробы бактероиды, клостридии, пептококки'
                               '\n +\- = умеренная активность'
                               '\n слабые места:  атипичная флора, MRSA, резистентные штаммы K.pneumoniae, P.aeruginosae') 
        if cheked_1 in cefalosporin_4 and cheked_2 in nitroimidasol or cheked_2 in cefalosporin_4 and cheked_1 in nitroimidasol:
            messagebox.showinfo ('Активность','Staphylococcus aureus (кроме MRSA), Moraxella catarrhalis,'
                               'Streptococcus pneumoniae, Haemophilus influenzae(включая штаммы, вырабатывающие пенициллиназу) '
                               'Escherichia coli, Klebsiella pneumonia, Pseudomonas aeruginosae, анаэробы бактероиды, клостридии, пептококки'
                               '\n слабые места:  атипичная флора, MRSA, резистентные штаммы K.pneumoniae, P.aeruginosae') 

        if cheked_1 in penicillin_1 and cheked_2 in aminoglicazid_2 or cheked_2 in penicillin_1 and cheked_1 in aminoglicazid_2:
            messagebox.showinfo ('Активность','Staphylococcus aureus (кроме MRSA)(+),'
                               'Streptococcus pneumoniae(+), Haemophilus influenzae(++?) '
                               ' Pseudomonas aeruginosae(+\-)'
                               '\n + = синергия |+\- = умеренная активность| ++? = слабая синергия, многие штаммы вырабатывают пенициллиназы'
                               '\n слабые места:  атипичная флора, MRSA, резистентные штаммы K.pneumoniae, P.aeruginosae') 
        
        if cheked_1 in penicillin_2 and cheked_2 in aminoglicazid_2 or cheked_2 in penicillin_2 and cheked_1 in aminoglicazid_2:
            messagebox.showinfo ('Активность','Staphylococcus aureus (кроме MRSA)(++), Moraxella catarrhalis'
                               'Streptococcus pneumoniae(++), Haemophilus influenzae(++) '
                               ' Pseudomonas aeruginosae(++*), Klebsiella pneumonia(++*)'
                               '\n ++ = синергия, выраженная активность |++* = при выборе пиперациллина, выраженая активность, однако, повышается риск нефротоксичности!|'
                               '\n слабые места:  атипичная флора, MRSA') 
        if cheked_1 in penicillin_1 and cheked_2 in macrolids or cheked_2 in penicillin_1 and cheked_1 in macrolids:
            messagebox.showinfo('Активность','Streptococcus pneumoniae(+?), Haemophilus influenzae(+?) '
                               'Legionella pneumophila(+!), Mycoplasma pneumoniae(+!),'
                               'Chlamydia pneumoniae(+!), Bordetella pertussis(+!) \n'
                               ' +! = выбор при подозрении+ = синергия | +? = слабая синергия, многие штаммы вырабатывают пенициллиназы'
                               '\n слабые места:  MRSA, резистентные штаммы S.pneumoniae, H.influenzae, K.pneumoniae, P.aeruginosae') 
        if cheked_1 in penicillin_2 and cheked_2 in macrolids or cheked_2 in penicillin_2 and cheked_1 in macrolids:
            messagebox.showinfo('Активность','Staphylococcus aureus (кроме MRSA)(++),Moraxella catarrhalis '
                               'Streptococcus pneumoniae(++), Haemophilus influenzae(++) '
                               ' Pseudomonas aeruginosae(++*), Klebsiella pneumonia, анаэробы'
                               'Legionella pneumophila(+!), Mycoplasma pneumoniae(+!),'
                               'Chlamydia pneumoniae(+!), Bordetella pertussis(+!)'
                               '\n ++ = синергия, выраженная активность |++* = при выборе пиперациллина, выраженая активность'
                               '\n слабые места: MRSA, резистентные штаммы K.pneumoniae, P.aeruginosae') 
        if cheked_1 in penicillin_1 and cheked_2 in tetracyclines or cheked_2 in penicillin_1 and cheked_1 in tetracyclines:
            messagebox.showinfo ('Активность','Streptococcus pneumoniae(+?), Haemophilus influenzae(+?) '
                               ' Pseudomonas aeruginosae(?), Klebsiella pneumonia(?)'
                               'Legionella pneumophila(+\-), Mycoplasma pneumoniae(+\-),'
                               'Chlamydia pneumoniae(+\-),, Bordetella pertussis(+\-) \n'
                               '+?"= активны, однако встречаются резистентные штаммы|'
                               '+\- = умеренная активность, комбинация может быть рассмотрена при подозрении | ? = многие штаммы резистентны'
                               '\n слабые места:  MRSA, резистентные штаммы S.pneumoniae, H.influenzae, K.pneumoniae, P.aeruginosae')
        if cheked_1 in penicillin_2 and cheked_2 in tetracyclines or cheked_2 in penicillin_2 and cheked_1 in tetracyclines:
            messagebox.showinfo ('Активность','Staphylococcus aureus (кроме MRSA),Moraxella catarrhalis '
                               'Streptococcus pneumoniae, Haemophilus influenzae '
                               ' Pseudomonas aeruginosae(++*), Klebsiella pneumonia, анаэробы'
                               'Legionella pneumophila(+\-), Mycoplasma pneumoniae(+\-),'
                               'Chlamydia pneumoniae(+\-),, Bordetella pertussis(+\-) \n'
                               '+?"= активны, однако встречаются резистентные штаммы|++* = при выборе пиперациллина, выраженая активность'
                               '+\- = умеренная активность, комбинация может быть рассмотрена при подозрении | ? = многие штаммы резистентны'
                               '\n слабые места:  MRSA,  K.pneumoniae, P.aeruginosae')                              
        if cheked_1 in penicillin_1 and cheked_2 in flourchinolone or cheked_2 in penicillin_1 and cheked_1 in flourchinolone:
            messagebox.showinfo ('Активность','Staphylococcus aureus(++)* (кроме MRSA), Moraxella catarrhalis(++)*,'
                               'Streptococcus pneumoniae(++)*, Haemophilus influenzae(включая штаммы, вырабатывающие пенициллиназу)(++)* '
                               'Escherichia coli, Klebsiella pneumonia , Pseudomonas aeruginosae(**), Proteus mirabilis, Legionella pneumophila, Mycoplasma pneumoniae,'
                               'Chlamydia pneumoniae,, Bordetella pertussis \n'
                               '++* = синергия, относится к лево и моксифлоксацину|** = относится к ципрофлоксацину|'
                               '\n слабые места:  MRSA, резистентные штаммы K.pneumoniae, P.aeruginosae')
        if cheked_1 in penicillin_2 and cheked_2 in flourchinolone or cheked_2 in penicillin_2 and cheked_1 in flourchinolone:
            messagebox.showinfo ('Активность','Staphylococcus aureus(++)* (кроме MRSA), Moraxella catarrhalis(++)*,'
                               'Streptococcus pneumoniae(++)*, Haemophilus influenzae(включая штаммы, вырабатывающие пенициллиназу)(++)* '
                               'Escherichia coli, Klebsiella pneumonia , Pseudomonas aeruginosae(**), Escherichia coli, Proteus mirabilis, Legionella pneumophila, Mycoplasma pneumoniae,'
                               'Chlamydia pneumoniae,, Bordetella pertussis \n'
                               '++* = синергия, относится к лево и моксифлоксацину|** = относится к ципрофлоксацину и пиперациллину|+\- = умеренная активность, комбинация может быть рассмотрена при подозрении'
                               '\n слабые места:  MRSA, резистентные штаммы K.pneumoniae')                                    
        if cheked_1 in penicillin_1 and cheked_2 in lincozamides or cheked_2 in penicillin_1 and cheked_1 in lincozamides:
            messagebox.showinfo ('Активность','Streptococcus pneumoniae(+?), Haemophilus influenzae(+?) '
                                 'анаэробы: бактероиды, клостридии, пептококки'
                                  '\n +?"= активны, однако встречаются резистентные штаммы'
                                  '\n слабые места: атипичные возбудители,  MRSA, резистентные штаммы K.pneumoniae, P.aeruginosae')
        if cheked_1 in penicillin_2 and cheked_2 in lincozamides or cheked_2 in penicillin_2 and cheked_1 in lincozamides:
            messagebox.showinfo ('Активность','Staphylococcus aureus (кроме MRSA),Moraxella catarrhalis '
                               'Streptococcus pneumoniae, Haemophilus influenzae, Escherichia coli, '
                               ' Pseudomonas aeruginosae(++*), Klebsiella pneumonia,'
                                 'анаэробы: бактероиды, клостридии, пептококки'
                                  '\n ++* = выраженная активность пиперациллина'
                                   '\n слабые места: атипичные возбудители, MRSA, резистентные штаммы K.pneumoniae, P.aeruginosae, избыточная активность в отношении анаэробов')        
        if cheked_1 in penicillin_1 and cheked_2 in nitroimidasol or cheked_2 in penicillin_1 and cheked_1 in nitroimidasol:
            messagebox.showinfo('Активность','Streptococcus pneumoniae(+?), Haemophilus influenzae(+?) '
                                 'анаэробы: бактероиды, клостридии, пептококки'
                                  '\n +?"= активны, однако встречаются резистентные штаммы'
                                  '\n слабые места: атипичные возбудители,  MRSA, резистентные штаммы S.pneumoniae, H.influenzae, K.pneumoniae, P.aeruginosae')
        if cheked_1 in penicillin_2 and cheked_2 in nitroimidasol or cheked_2 in penicillin_2 and cheked_1 in nitroimidasol:
            messagebox.showinfo ('Активность','Staphylococcus aureus (кроме MRSA),Moraxella catarrhalis '
                               'Streptococcus pneumoniae, Haemophilus influenzae, Escherichia coli, '
                               ' Pseudomonas aeruginosae(++*), Klebsiella pneumonia,'
                                 'анаэробы: бактероиды, клостридии, пептококки'
                                  '\n ++* = выраженная активность пиперациллина'
                                   '\n слабые места: атипичные возбудители, MRSA, резистентные штаммы K.pneumoniae, P.aeruginosae, избыточная активность в отношении анаэробов')
        if cheked_2 in aminoglicazid_2 and cheked_1 in macrolids or cheked_1 in aminoglicazid_2 and cheked_2 in macrolids:
            messagebox.showinfo('Активность','Streptococcus pneumoniae(+?), Haemophilus influenzae(+?) '
                               ' Klebsiella pneumonia , Pseudomonas aeruginosae, Legionella pneumophila, Mycoplasma pneumoniae,'
                               'Chlamydia pneumoniae,, Bordetella pertussis \n'
                               '+? = синергия, однако многие штаммы резистентны'
                               '\n слабые места: MRSA, резистентные штаммы K.pneumoniae, P.aeruginosae, слабая активность в отношении основных внебольничных возбудителей' )
        if cheked_2 in lincozamides and cheked_1 in macrolids or cheked_1 in lincozamides and cheked_2 in macrolids:
            messagebox.showinfo('Активность','Streptococcus pneumoniae(+?), Haemophilus influenzae(+?) '
                               '  Legionella pneumophila, Mycoplasma pneumoniae,'
                               'Chlamydia pneumoniae,, Bordetella pertussis \n'
                                '+? = синергия, однако многие штаммы резистентны'
                               '\n слабые места: MRSA, резистентные штаммы K.pneumoniae, P.aeruginosae, слабая активность в отношении основных внебольничных возбудителей' )
        if cheked_2 in carbopenems and cheked_1 in macrolids or cheked_1 in carbopenems and cheked_2 in macrolids:
            messagebox.showinfo('Активность', 'Staphylococcus aureus(++) (кроме MRSA), Moraxella catarrhalis(++),'
                               'Streptococcus pneumoniae(++), Haemophilus influenzae(включая штаммы, вырабатывающие пенициллиназу)(++) '
                               'Escherichia coli, Klebsiella pneumonia , Pseudomonas aeruginosae(*), Proteus mirabilis, Legionella pneumophila, Mycoplasma pneumoniae,'
                               'Chlamydia pneumoniae,, Bordetella pertussis, анаэробы, кроме Clostridium difficile \n'
                               '++ = синергия |* = не относится к эртапенему|'
                               '\n слабые места:  MRSA, резистентные штаммы K.pneumoniae, P.aeruginosae, высокая вероятность псевдомембранозного колита')
        if cheked_2 in carbopenems and cheked_1 in flourchinolone or cheked_1 in carbopenems and cheked_2 in flourchinolone:
            messagebox.showinfo('Активность', 'Staphylococcus aureus(++) (кроме MRSA), Moraxella catarrhalis(++),'
                               'Streptococcus pneumoniae(++), Haemophilus influenzae(включая штаммы, вырабатывающие пенициллиназу)(++) '
                               'Escherichia coli, Klebsiella pneumonia(++) , Pseudomonas aeruginosae(*, +!), Proteus mirabilis, Legionella pneumophila, Mycoplasma pneumoniae,'
                               'Chlamydia pneumoniae,, Bordetella pertussis, анаэробы, кроме Clostridium difficile \n'
                               '++ = синергия |* = не относится к эртапенему|*** перекрытие атипичной флоры характерно для лево и моксифлоксацина|+! выраженная активность ципрофлоксацина'
                               '\n слабые места:  MRSA, резистентные штаммы K.pneumoniae, P.aeruginosae, высокая вероятность псевдомембранозного колита')
        if cheked_2 in carbopenems and cheked_1 in aminoglicazid_2 or cheked_1 in carbopenems and cheked_2 in aminoglicazid_2:
            messagebox.showinfo('Активность', 'Staphylococcus aureus(++) (кроме MRSA), Moraxella catarrhalis(++),'
                               'Streptococcus pneumoniae(++), Haemophilus influenzae(включая штаммы, вырабатывающие пенициллиназу)(++) '
                               'Escherichia coli, Klebsiella pneumonia(++) , Pseudomonas aeruginosae(*, ++), Proteus mirabilis,  анаэробы, кроме Clostridium difficile \n'
                               '++ = синергия |* = не относится к эртапенему|'
                               '\n слабые места: атипичные возбудители, MRSA, резистентные штаммы K.pneumoniae, P.aeruginosae, высокая вероятность псевдомембранозного колита')
        if cheked_2 in carbopenems and cheked_1 in tetracyclines or cheked_1 in carbopenems and cheked_2 in tetracyclines:
            messagebox.showinfo('Активность', 'Staphylococcus aureus(++) (кроме MRSA), Moraxella catarrhalis(++),'
                               'Streptococcus pneumoniae(++), Haemophilus influenzae(включая штаммы, вырабатывающие пенициллиназу)(++) '
                               'Escherichia coli, Klebsiella pneumonia , Pseudomonas aeruginosae(*), Proteus mirabilis, Legionella pneumophila(+/-), Mycoplasma pneumoniae(+/-),'
                               'Chlamydia pneumoniae(+/-),, Bordetella pertussis(+/-), анаэробы, кроме Clostridium difficile \n'
                               '++ = |* = не относится к эртапенему|+/- = умеренная активность'
                               '\n слабые места:  MRSA, резистентные штаммы K.pneumoniae, P.aeruginosae, высокая вероятность псевдомембранозного колита')       
        if cheked_2 in tetracyclines and cheked_1 in macrolids or cheked_1 in tetracyclines and cheked_2 in macrolids:
            messagebox.showinfo('Активность','Legionella pneumophila, Mycoplasma pneumoniae,'
                               'Chlamydia pneumoniae,, Bordetella pertussis'
                               'Streptococcus pneumoniae(+?), Haemophilus influenzae(+?)'
                                ' Pseudomonas aeruginosae(?), Klebsiella pneumonia(?)'
                                '+?= активны, некоторые штаммы резистентны | ? = многие штаммы резистентны'
                               '\n слабые места:  MRSA, резистентные штаммы S.pneumoniae, H.influenzae, K.pneumoniae, P.aeruginosae')
        if cheked_2 in tetracyclines and cheked_1 in lincozamides or cheked_1 in  tetracyclines and cheked_2 in lincozamides:
            messagebox.showinfo('Активность', 'Streptococcus pneumoniae(+?), Haemophilus influenzae(включая штаммы, вырабатывающие пенициллиназу)(+?) '
                               ' Klebsiella pneumonia(?) , Pseudomonas aeruginosae(?),  Legionella pneumophila(+/-), Mycoplasma pneumoniae(+/-),'
                               'Chlamydia pneumoniae(+/-),, Bordetella pertussis(+/-), анаэробы, кроме Clostridium difficile \n'
                                '+?= активны, но некоторые штаммы резистентны | ? = многие штаммы резистентны| +/- = умеренная активность'
                               '\n слабые места:  MRSA, резистентные штаммы S.pneumoniae, H.influenzae, K.pneumoniae, P.aeruginosae')
        if cheked_2 in tetracyclines and cheked_1 in nitroimidasol or cheked_1 in  tetracyclines and cheked_2 in nitroimidasol:
            messagebox.showinfo('Активность',  'Streptococcus pneumoniae(+?), Haemophilus influenzae(включая штаммы, вырабатывающие пенициллиназу)(+?) '
                               ' Klebsiella pneumonia(?) , Pseudomonas aeruginosae(?),  Legionella pneumophila(+/-), Mycoplasma pneumoniae(+/-),'
                               'Chlamydia pneumoniae(+/-),, Bordetella pertussis(+/-), анаэробы: клостридии, бактероиды'
                                '+?= активны, но некоторые штаммы резистентны | ? = многие штаммы резистентны| +/- = умеренная активность'
                               '\n слабые места:  MRSA, резистентные штаммы S.pneumoniae, H.influenzae, K.pneumoniae, P.aeruginosae')
        if cheked_2 in aminoglicazid_2 and cheked_1 in flourchinolone or cheked_1 in aminoglicazid_2 and cheked_2 in flourchinolone:
            messagebox.showinfo ('Активность','Staphylococcus aureus(++) (кроме MRSA), Moraxella catarrhalis(++),'
                               'Streptococcus pneumoniae(++), Haemophilus influenzae(включая штаммы, вырабатывающие пенициллиназу)(++) '
                               'Escherichia coli, Klebsiella pneumonia(++) , Pseudomonas aeruginosae(++*), Proteus mirabilis, Legionella pneumophila, Mycoplasma pneumoniae,'
                               'Chlamydia pneumoniae,, Bordetella pertussis'
                               '\n ++ = синегия |++* = преимущественно для ципрофлоксацина|*** перекрытие атипичной флоры характерно для лево и моксифлоксацина|+! выраженная активность ципрофлоксацина'
                               '\n слабые места:  MRSA, резистентные штаммы K.pneumoniae, P.aeruginosae')
        if cheked_2 in aminoglicazid_2 and cheked_1 in lincozamides or cheked_1 in aminoglicazid_2 and cheked_2 in lincozamides:
            messagebox.showinfo ('Активность', 'Pseudomonas aeruginosa, Klebsiella pneumoniae, '
                               'Streptococcus pneumoniae(+?),Staphylococcus aureus(+?) (кроме MRSA), бактероиды '
                               '\n +? = некоторая синергия, однако многие штаммы резистентны'
                               '\n слабые места: плохое перекрытие типичных внебольничных возбудителей, атипичные возбудители, MRSA, резистентные штаммы K.pneumoniae, P.aeruginosae' )
        if cheked_2 in aminoglicazid_2 and cheked_1 in nitroimidasol or cheked_1 in aminoglicazid_2 and cheked_2 in nitroimidasol:
          #  conclusion_label.config(text= "Рациональная комбинация")
            messagebox.showinfo ('Активность','Pseudomonas aeruginosa, Klebsiella pneumoniae, '
                               'Streptococcus pneumoniae(+?),Staphylococcus aureus(+?) (кроме MRSA),анаэробы:клостридии, пептококки, бактероиды '
                               '\n +? =  многие штаммы резистентны'
                               '\n слабые места: плохое перекрытие типичных внебольничных возбудителей, атипичные возбудители, MRSA, резистентные штаммы K.pneumoniae, P.aeruginosae' )
        if cheked_2 in aminoglicazid_2 and cheked_1 in sulfanilamide or cheked_1 in aminoglicazid_2 and cheked_2 in sulfanilamide:
            messagebox.showinfo ('Активность', 'Pseudomonas aeruginosa(++), Klebsiella pneumoniae(++), '
                               'Streptococcus pneumoniae(++),Staphylococcus aureus(++) (в т.ч. MRSA), Escherichia coli,'
                              '/n ++ = синергия'
                              '/n слабые места: атипичные возбудители, слабая активность по отношению к H.influenzae, Moraxella catarrhalis ')
        if cheked_2 in flourchinolone and cheked_1 in lincozamides or cheked_1 in flourchinolone and cheked_2 in lincozamides:
            messagebox.showinfo ('Активность','Staphylococcus aureus (кроме MRSA), Moraxella catarrhalis(++),'
                               'Streptococcus pneumoniae(++), Haemophilus influenzae(включая штаммы, вырабатывающие пенициллиназу)(++) '
                               'Escherichia coli, Klebsiella pneumonia , Pseudomonas aeruginosae(*), Proteus mirabilis, Legionella pneumophila, Mycoplasma pneumoniae,'
                               'Chlamydia pneumoniae,, Bordetella pertussis, бактероиды'
                               '\n ++ = синергия|* = преимущественно для ципрофлоксацина|*** перекрытие атипичной флоры характерно для лево и моксифлоксацина|+! выраженная активность ципрофлоксацина'
                               '\n слабые места:  MRSA, резистентные штаммы K.pneumoniae, P.aeruginosae')                                     
        if cheked_2 in flourchinolone and cheked_1 in glycopeptides or cheked_1 in flourchinolone and cheked_2 in glycopeptides:
            messagebox.showinfo ('Активность','Staphylococcus aureus (в т.ч. MRSA), Moraxella catarrhalis,'
                               'Streptococcus pneumoniae(++), Haemophilus influenzae(включая штаммы, вырабатывающие пенициллиназу) '
                               'Escherichia coli, Klebsiella pneumonia , Pseudomonas aeruginosae(*), Proteus mirabilis, Legionella pneumophila, Mycoplasma pneumoniae,'
                               'Chlamydia pneumoniae,, Bordetella pertussis'
                               '\n * = преимущественно для ципрофлоксацина|*** перекрытие атипичной флоры характерно для лево и моксифлоксацина'
                               '\n слабые места:  ванкомицин-резистентные MRSA, резистентные штаммы K.pneumoniae, P.aeruginosae')
        if cheked_2 in penicillin_1 and cheked_1 in glycopeptides or cheked_1 in penicillin_1 and cheked_2 in glycopeptides:
            messagebox.showinfo ('Активность','Staphylococcus aureus (в т.ч. MRSA),'
                               'Streptococcus pneumoniae(++), Haemophilus influenzae(+?) '
                               '\n ++ = синергия | +? = многие штаммы резистентны'
                               '\n слабые места: атипичная флора,  ванкомицин-резистентные MRSA, практически отсутствие покрытия Грамм- флоры')
        if cheked_2 in penicillin_2 and cheked_1 in glycopeptides or cheked_1 in penicillin_2 and cheked_2 in glycopeptides:
            messagebox.showinfo ('Активность','Staphylococcus aureus (в т.ч. MRSA), Moraxella catarrhalis'
                               'Streptococcus pneumoniae(++), Haemophilus influenzae '
                               ' Pseudomonas aeruginosae(*), Klebsiella pneumonia'
                               '\n ++ = синергия, выраженная активность |* = при выборе пиперациллина, выраженая активность, однако, повышается риск нефротоксичности!|'
                               '\n слабые места:  атипичная флора, ванкомицин-резистентные MRSA') 
        if cheked_2 in cefalosporin_1 and cheked_1 in glycopeptides or cheked_1 in cefalosporin_1 and cheked_2 in glycopeptides:
            messagebox.showinfo ('Активность','Staphylococcus aureus (в т.ч. MRSA),'
                               'Streptococcus pneumoniae(++), Klebsiella pneumonia(+/-) '
                               '\n ++ = синергия | +? = многие штаммы резистентны | +/- = умеренная активность'
                               '\n слабые места: атипичная флора,  ванкомицин-резистентные MRSA, слабое покрытия Грамм- флоры')
        if cheked_2 in cefalosporin_2 and cheked_1 in glycopeptides or cheked_1 in cefalosporin_2 and cheked_2 in glycopeptides:
            messagebox.showinfo ('Активность','Staphylococcus aureus (в т.ч. MRSA)(++), Moraxella catarrhalis'
                               'Streptococcus pneumoniae(++), Escherichia coli, Haemophilus influenzae '
                               ' Klebsiella pneumonia'
                               '\n ++ = синергия, выраженная активность '
                               '\n слабые места:  атипичная флора, резистентные Klebsiella pneumonia, Pseudomonas aeruginosa,  ванкомицин-резистентные MRSA') 
        if cheked_2 in cefalosporin_3 and cheked_1 in glycopeptides or cheked_1 in cefalosporin_3 and cheked_2 in glycopeptides:
            messagebox.showinfo ('Активность','Staphylococcus aureus (в т.ч. MRSA)(++), Moraxella catarrhalis'
                               'Streptococcus pneumoniae(++), Escherichia coli, Haemophilus influenzae '
                               ' Klebsiella pneumonia, Proteus mirabilis'
                               '\n ++ = синергия, выраженная активность '
                               '\n слабые места:  атипичная флора, резистентные Klebsiella pneumonia, Pseudomonas aeruginosa, ванкомицин-резистентные MRSA') 
        if cheked_2 in cefalosporin_4 and cheked_1 in glycopeptides or cheked_1 in cefalosporin_4 and cheked_2 in glycopeptides:
            messagebox.showinfo ('Активность','Staphylococcus aureus (в т.ч. MRSA)(++), Moraxella catarrhalis'
                               'Streptococcus pneumoniae(++), Escherichia coli, Haemophilus influenzae, Pseudomonas aeruginosa, '
                               ' Klebsiella pneumonia, Proteus mirabilis'
                               '\n ++ = синергия, выраженная активность '
                               '\n слабые места:  атипичная флора, резистентные Klebsiella pneumonia,  ванкомицин-резистентные MRSA') 
            
            
        if cheked_2 in penicillin_1 and cheked_1 in oxazolidone or cheked_1 in penicillin_1 and cheked_2 in oxazolidone:
            messagebox.showinfo ('Активность','Staphylococcus aureus (в т.ч. MRSA),'
                               'Streptococcus pneumoniae(++), Haemophilus influenzae(+?) '
                               '\n ++ = синергия | +? = многие штаммы резистентны'
                               '\n слабые места: атипичная флора, практически отсутствие покрытия Грамм- флоры')
        if cheked_2 in penicillin_2 and cheked_1 in oxazolidone or cheked_1 in penicillin_2 and cheked_2 in oxazolidone:
            messagebox.showinfo ('Активность','Staphylococcus aureus (в т.ч. MRSA), Moraxella catarrhalis'
                               'Streptococcus pneumoniae(++), Haemophilus influenzae '
                               ' Pseudomonas aeruginosae(*), Klebsiella pneumonia'
                               '\n ++ = синергия, выраженная активность |* = при выборе пиперациллина, выраженая активность, однако, повышается риск нефротоксичности!|'
                               '\n слабые места:  атипичная флора') 
        if cheked_2 in cefalosporin_1 and cheked_1 in oxazolidone or cheked_1 in cefalosporin_1 and cheked_2 in oxazolidone:
            messagebox.showinfo ('Активность','Staphylococcus aureus (в т.ч. MRSA),'
                               'Streptococcus pneumoniae(++), Klebsiella pneumonia(+/-) '
                               '\n ++ = синергия | +? = многие штаммы резистентны | +/- = умеренная активность'
                               '\n слабые места: атипичная флора,  слабое покрытия Грамм- флоры')
        if cheked_2 in cefalosporin_2 and cheked_1 in oxazolidone or cheked_1 in cefalosporin_2 and cheked_2 in oxazolidone:
            messagebox.showinfo ('Активность','Staphylococcus aureus (в т.ч. MRSA)(++), Moraxella catarrhalis'
                               'Streptococcus pneumoniae(++), Escherichia coli, Haemophilus influenzae '
                               ' Klebsiella pneumonia'
                               '\n ++ = синергия, выраженная активность '
                               '\n слабые места:  атипичная флора, резистентные Klebsiella pneumonia, Pseudomonas aeruginosa, MRSA') 
        if cheked_2 in cefalosporin_3 and cheked_1 in oxazolidone or cheked_1 in cefalosporin_3 and cheked_2 in oxazolidone:
            messagebox.showinfo ('Активность','Staphylococcus aureus (в т.ч. MRSA)(++), Moraxella catarrhalis'
                               'Streptococcus pneumoniae(++), Escherichia coli, Haemophilus influenzae '
                               ' Klebsiella pneumonia, Proteus mirabilis'
                               '\n ++ = синергия, выраженная активность '
                               '\n слабые места:  атипичная флора, резистентные Klebsiella pneumonia, Pseudomonas aeruginosa, MRSA') 
        if cheked_2 in cefalosporin_4 and cheked_1 in oxazolidone or cheked_1 in cefalosporin_4 and cheked_2 in oxazolidone:
            messagebox.showinfo ('Активность','Staphylococcus aureus (в т.ч. MRSA)(++), Moraxella catarrhalis'
                               'Streptococcus pneumoniae(++), Escherichia coli, Haemophilus influenzae, Pseudomonas aeruginosa, '
                               ' Klebsiella pneumonia, Proteus mirabilis'
                               '\n ++ = синергия, выраженная активность '
                               '\n слабые места:  атипичная флора, резистентные Klebsiella pneumonia,  MRSA') 
          
            
        if cheked_2 in flourchinolone and cheked_1 in nitroimidasol or cheked_1 in flourchinolone and cheked_2 in nitroimidasol:
            messagebox.showinfo ('Активность',' Moraxella catarrhalis,'
                               'Streptococcus pneumoniae, Haemophilus influenzae(включая штаммы, вырабатывающие пенициллиназу) '
                               'Escherichia coli, Klebsiella pneumonia , Pseudomonas aeruginosae(*), Proteus mirabilis, Legionella pneumophila, Mycoplasma pneumoniae,'
                               'Chlamydia pneumoniae,, Bordetella pertussis, бактероиды, клостридии, пептококки'
                               '\n* = преимущественно для ципрофлоксацина|*** перекрытие атипичной флоры характерно для лево и моксифлоксацина|+! выраженная активность ципрофлоксацина'
                               '\n слабые места:  MRSA, резистентные штаммы K.pneumoniae, P.aeruginosae')
            
        if cheked_2 in flourchinolone and cheked_1 in polypeptide or cheked_1 in flourchinolone and cheked_2 in polypeptide:
            messagebox.showinfo ('Активность',' Moraxella catarrhalis,'
                               'Streptococcus pneumoniae, Haemophilus influenzae(включая штаммы, вырабатывающие пенициллиназу) '
                               'Escherichia coli, Klebsiella pneumonia(++) , Pseudomonas aeruginosae(*++), Proteus mirabilis, Legionella pneumophila, Mycoplasma pneumoniae,'
                               'Chlamydia pneumoniae,, Bordetella pertussis, бактероиды, клостридии, пептококки'
                               '\n ++ = синергия| * = преимущественно для ципрофлоксацина|*** перекрытие атипичной флоры характерно для лево и моксифлоксацина|+! выраженная активность ципрофлоксацина'
                               '\n слабые места:  MRSA')
            
            
        if cheked_2 in penicillin_1 and cheked_1 in polypeptide or cheked_1 in penicillin_1 and cheked_2 in polypeptide:
            messagebox.showinfo ('Активность','Staphylococcus aureus (кроме MRSA),'
                               'Streptococcus pneumoniae(+?), Haemophilus influenzae(+?) '
                                ' Pseudomonas aeruginosae, Klebsiella pneumonia'
                               '\n  +? = многие штаммы резистентны'
                               '\n слабые места: атипичная флора, MRSA')
        if cheked_2 in penicillin_2 and cheked_1 in polypeptide or cheked_1 in penicillin_2 and cheked_2 in polypeptide:
            messagebox.showinfo ('Активность','Staphylococcus aureus (кроме MRSA), Moraxella catarrhalis'
                               'Streptococcus pneumoniae, Haemophilus influenzae '
                               ' Pseudomonas aeruginosae(++,*), Klebsiella pneumonia'
                               '\n ++ = синергия, выраженная активность |* = при выборе пиперациллина, выраженая активность, однако, повышается риск нефротоксичности!|'
                               '\n слабые места:  атипичная флора') 
        if cheked_2 in cefalosporin_1 and cheked_1 in polypeptide or cheked_1 in cefalosporin_1 and cheked_2 in polypeptide:
            messagebox.showinfo ('Активность','Staphylococcus aureus  (кроме MRSA),'
                               'Streptococcus pneumoniae(++), Klebsiella pneumonia(+/-) '
                               '\n ++ = синергия | +? = многие штаммы резистентны | +/- = умеренная активность'
                               '\n слабые места: атипичная флора,   MRSA')
        if cheked_2 in cefalosporin_2 and cheked_1 in polypeptide or cheked_1 in cefalosporin_2 and cheked_2 in polypeptide:
            messagebox.showinfo ('Активность','Staphylococcus aureus (кроме MRSA), Moraxella catarrhalis'
                               'Streptococcus pneumoniae, Escherichia coli, Haemophilus influenzae, Pseudomonas aeruginosa, '
                               ' Klebsiella pneumonia, Proteus mirabilis'
                               '\n ++ = синергия, выраженная активность '
                               '\n слабые места:  атипичная флора, MRSA') 
        if cheked_2 in cefalosporin_3 and cheked_1 in polypeptide or cheked_1 in cefalosporin_3 and cheked_2 in polypeptide:
            messagebox.showinfo ('Активность','Staphylococcus aureus (кроме MRSA), Moraxella catarrhalis'
                               'Streptococcus pneumoniae, Escherichia coli, Haemophilus influenzae, Pseudomonas aeruginosa, '
                               ' Klebsiella pneumonia, Proteus mirabilis'
                               '\n слабые места:  атипичная флора, MRSA') 
        if cheked_2 in cefalosporin_4 and cheked_1 in polypeptide or cheked_1 in cefalosporin_4 and cheked_2 in polypeptide:
            messagebox.showinfo ('Активность','Staphylococcus aureus (кроме MRSA), Moraxella catarrhalis'
                               'Streptococcus pneumoniae, Escherichia coli, Haemophilus influenzae, Pseudomonas aeruginosa(++), '
                               ' Klebsiella pneumonia, Proteus mirabilis'
                               '\n ++ = синергия, выраженная активность '
                               '\n слабые места:  атипичная флора,  MRSA') 


        if cheked_2 in carbopenems and cheked_1 in polypeptide or cheked_1 in carbopenems and cheked_2 in polypeptide:
            messagebox.showinfo ('Активность','Staphylococcus aureus (кроме MRSA), Moraxella catarrhalis,'
                               'Streptococcus pneumoniae, Haemophilus influenzae(включая штаммы, вырабатывающие пенициллиназу) '
                               'Escherichia coli, Klebsiella pneumonia(++) , Pseudomonas aeruginosae(*, ++), Proteus mirabilis,  анаэробы, кроме Clostridium difficile \n'
                               '++ = синергия |* = не относится к эртапенему|'
                               '\n слабые места: атипичные возбудители, MRSA, резистентные штаммы K.pneumoniae')
            
        if cheked_2 in carbopenems and cheked_1 in oxazolidone or cheked_1 in carbopenems and cheked_2 in oxazolidone:
            messagebox.showinfo ('Активность','Staphylococcus aureus (в т.ч. MRSA), Moraxella catarrhalis,'
                               'Streptococcus pneumoniae(++), Haemophilus influenzae(включая штаммы, вырабатывающие пенициллиназу) '
                               'Escherichia coli, Klebsiella pneumonia , Pseudomonas aeruginosae(*), Proteus mirabilis,  анаэробы, кроме Clostridium difficile \n'
                               '++ = синергия |* = не относится к эртапенему|'
                               '\n слабые места: атипичные возбудители, резистентные штаммы K.pneumoniae')            
        if cheked_2 in carbopenems and cheked_1 in glycopeptides or cheked_1 in carbopenems and cheked_2 in glycopeptides:
            messagebox.showinfo ('Активность','Staphylococcus aureus (в т.ч. MRSA), Moraxella catarrhalis,'
                               'Streptococcus pneumoniae(++), Haemophilus influenzae(включая штаммы, вырабатывающие пенициллиназу) '
                               'Escherichia coli, Klebsiella pneumonia , Pseudomonas aeruginosae(*), Proteus mirabilis,  анаэробы, кроме Clostridium difficile \n'
                               '++ = синергия |* = не относится к эртапенему|'
                               '\n слабые места: атипичные возбудители, ванкомицин-резистентные MRSA, резистентные штаммы K.pneumoniae')               
        if cheked_2 in tetracyclines and cheked_1 in macrolids or cheked_1 in  tetracyclines and cheked_2 in macrolids:
            messagebox.showinfo('Активность',  'Streptococcus pneumoniae(++?), Haemophilus influenzae(включая штаммы, вырабатывающие пенициллиназу)(++?) '
                               ' Klebsiella pneumonia(?) , Pseudomonas aeruginosae(?),  Legionella pneumophila(++), Mycoplasma pneumoniae(++),'
                               'Chlamydia pneumoniae(++),, Bordetella pertussis(++)'
                                '\n ++ = синергия | ++?= синегрия, активны, но некоторые штаммы резистентны | ? = многие штаммы резистентны| +/- = умеренная активность'
                               '\n слабые места:  MRSA, резистентные штаммы S.pneumoniae, H.influenzae, K.pneumoniae, P.aeruginosae')

        if cheked_2 in tetracyclines and cheked_1 in aminoglicazid_2 or cheked_1 in  tetracyclines and cheked_2 in aminoglicazid_2:
            messagebox.showinfo('Активность',  'Streptococcus pneumoniae(+?), Haemophilus influenzae(включая штаммы, вырабатывающие пенициллиназу)(+?) '
                               ' Klebsiella pneumonia , Pseudomonas aeruginosae,  Legionella pneumophila(+/-), Mycoplasma pneumoniae(+/-),'
                               'Chlamydia pneumoniae(+/-),, Bordetella pertussis(+/-)'
                                '+?= активны, но некоторые штаммы резистентны | ? = многие штаммы резистентны| +/- = умеренная активность'
                               '\n слабые места:  MRSA, резистентные штаммы S.pneumoniae, H.influenzae, K.pneumoniae, P.aeruginosae')
        if cheked_2 in carbopenems and cheked_1 in tetracyclines or cheked_1 in carbopenems and cheked_2 in tetracyclines:
            messagebox.showinfo ('Активность','Staphylococcus aureus (кроме MRSA), Moraxella catarrhalis,'
                               'Streptococcus pneumoniae(++), Haemophilus influenzae(включая штаммы, вырабатывающие пенициллиназу) '
                               'Escherichia coli, Klebsiella pneumonia , Pseudomonas aeruginosae(*), Proteus mirabilis, Legionella pneumophila(+/-), Mycoplasma pneumoniae(+/-),'
                               'Chlamydia pneumoniae(+/-),, Bordetella pertussis(+/-)  анаэробы, кроме Clostridium difficile \n'
                               '++ = синергия |* = не относится к эртапенему|'
                               '\n слабые места:  MRSA, резистентные штаммы K.pneumoniae, высокая вероятность псевдомембранозного колита')  
        if cheked_2 in carbopenems and cheked_1 in sulfanilamide or cheked_1 in carbopenems and cheked_2 in sulfanilamide:
            messagebox.showinfo ('Активность','Staphylococcus aureus (в т.ч. MRSA), Moraxella catarrhalis,'
                               'Streptococcus pneumoniae, Haemophilus influenzae(включая штаммы, вырабатывающие пенициллиназу) '
                               'Escherichia coli, Klebsiella pneumonia , Pseudomonas aeruginosae(*), Proteus mirabilis,  анаэробы, кроме Clostridium difficile \n'
                               '* = не относится к эртапенему|'
                               '\n слабые места: атипичные возбудители,  резистентные штаммы K.pneumoniae, высокая вероятность псевдомембранозного колита')  
        if cheked_2 in aminoglicazid_2 and cheked_1 in polypeptide or cheked_1 in aminoglicazid_2 and cheked_2 in polypeptide:
            messagebox.showinfo ('Активность',' Klebsiella pneumonia(++) , Pseudomonas aeruginosae(++) \n'
                                 '++ =  синергия'
                               '\n слабые места: атипичные возбудители, MRSA, слабое покрытие типичной внебольничной флоры')
        if cheked_2 == 'тайгециклин' or cheked_1  == 'тайгециклин':
            messagebox.showinfo ('Активность','Staphylococcus aureus (в т.ч. MRSA), Moraxella catarrhalis,'
                               'Streptococcus pneumoniae, Haemophilus influenzae(включая штаммы, вырабатывающие пенициллиназу) '
                               'Escherichia coli, Klebsiella pneumonia ,  Proteus mirabilis,  анаэробы, кроме Clostridium difficile '
                               '\n слабые места: атипичные возбудители,  Pseudomonas aeruginosae')                  
    if var.get() == 2:
        if cheked_1 == 'меропенем':
            messagebox.showinfo('Режим дозирования меропенема', "При СКФ ниже 50 мл/мин - максимальная дозировка 1,0 2 раза в день"
                                "\n При СКФ ниже 25 мл/мин - 0,5 2 раза в день; ниже 10 - 500 мг 1 раз в сутки")
        if cheked_1 == 'имипенем':
            messagebox.showinfo('Режим дозирования имепенема', 
                                "при СКФ 10-50 мл/мин — по 50% от разовой дозы каждые 8-12 часов; при СКФ ниже 10 мл/мин по 25-50% через 12 ч")
        if cheked_1 == 'левофлоксацин':
            messagebox.showinfo('Режим дозирования левофлоксацина', 
                                "при СКФ более 50 мл/мин — по 500 мг до 2 раз в сутки, при СКФ 21–50 мл/мин — по 500 мг первая доза,"
                                "далее по 250 мг каждые 12 часов, СКФ 20 и ниже мл/мин — о 500 мг первая доза,"
                                "далее по 125 мг каждые 12 часов")

        if cheked_1 == 'амоксициллин/клавулонат':
            messagebox.showinfo('Режим дозирования амоксициллина/клавулоната', 
                                "при СКФ более 30 мл/мин — коррекции дозы не требуется (1,0 до 3 раз в день), при СКФ 10–30 мл/мин 500/125мг 2 раза в сутки,"
                                "СКФ 10 и ниже мл/мин —  500/125 в сутки")
        if cheked_1 == 'амоксициллин':
            messagebox.showinfo('Режим дозирования амоксициллина', 
                                "при СКФ более 50 мл/мин — коррекции дозы не требуется (1,0 до 3 раз в день), при СКФ 10–50 мл/мин 1 гр 2 раза в сутки,"
                                "СКФ 10 и ниже мл/мин —  1 гр в сутки")
        if cheked_1 == 'цефазолин':
            messagebox.showinfo('Режим дозирования цефазолина', 
                                "В/м , в/в (струйно и капельно). Средняя суточная доза для взрослых - 0.25-1 г; кратность введения - 3-4 раза/сут. Максимальная суточная доза — 6 г ( в редких случаях - 12 г). Средняя продолжительность лечения составляет 7-10 дней ."
                               " Для профилактики послеоперационной инфекции - в/в 1 г за 0.5-1 ч до операции, 0.5-1 г - за время операции и по 0.5-1 г - каждые 8 ч в течение первых суток после операции."
                               " Больным с нарушениями функции почек требуется изменение режима дозирования в соответствии со значениями КК: при КК 55 мл/мин и более или при концентрации креатинина в плазме 1.5 мг% и менее можно вводить полную дозу; при КК 54-35 мл/мин или концентрации креатинина в плазме 1.6-3.0 мг% можно вводить полную дозу, но интервалы между инъекциями необходимо увеличить до 8 ч; при КК 34-11 мл/мин или концентрации креатинина в плазме 3.1-4.5 мг% - 1/2 дозы с интервалами 12 ч; при КК 10 мл/мин и менее или при концентрации креатинина в плазме 4.6 мг% и более - 1/2 обычной дозы каждые 18-24 ч. Все рекомендуемые дозы вводят после начальной ударной дозы 500 мг")
            
        if cheked_1 == 'колистин':
            messagebox.showinfo('Режим дозирования колистина', 
                                "Расчёт загрузочной дозы (вне зависимости от ХБП): масса(кг) / 7,5 (макс. 10 МЛН ЕД) в теч. 30-120 минут;"
                                "Масса тела рассчитывается по формуле: для мужчин = 52 + 1.9х(0,394 х рост(см) - 60) \n"
                                "для женщина = 49 + 1,7 х (0,394 х рост(см) - 60)"
                                "последующая поддерживающая доза - через 24 часа \n"
                                "Расчёт дозы: МЛН ЕД = СКФ/10+2 на 2-3 введения ежедневно (по формуле Кокрофт-Голта)"
                                "Поддерживающая доза при СКФ ниже 10 мл/мин - каждые 12 часов, если больше 10 - либо каждые 12, либо 8 часов"
                                )
                                    
        if cheked_1 == 'ванкомицин':
            messagebox.showinfo('Режим дозирования ванкомицина', 
                                "при СКФ > 80 мл/мин	500 мг или 1 г	каждые 12 ч, при СКФ = 80-50 мл/мин 1 г	 каждые 24 ч,"
                                "СКФ 50-10 мл/мин	1 г в трое суток")
            
        if cheked_1 == 'линезолид':
            messagebox.showinfo('Режим дозирования линезолида', 
                                "Рекомендуемый режим дозирования: 600 мг 2 раза в сутки")            
            messagebox.showinfo('Режим дозирования доксициклина', 
                                "Внутрь, у взрослых и детей старше 12 лет с массой тела более 45 кг средняя суточная доза - 200 мг в первый день (делится на 2 приема - по 100 мг 2 раза в сутки), далее по 100 мг/сут. При СКФ ниже 10  мл/мин - не применяется")                    
        if cheked_1 == 'ципрофлоксацин':
            messagebox.showinfo("Режим дозирования ципрофлоксацина" , 
                                "при СКФ > 50 мл/мин - 100% каждые 12 часов; при СКФ 10-50 мл/мин - 50-100%  каждые 12-18 часов; при СКФ менее 10 - 50% каждые 18-24 часа"
                                "при СКФ ниже 10 мл/мин - нагрузочная доза, затем 10% от нагрузочной дозы каждые 72-96 часа/в введения разовая доза - 200-400 мг, кратность введения - 2 раза/сут; продолжительность лечения - 1-2 недели, при необходимости и более. Можно вводить в/в струйно, но более предпочтительно капельное введение в течение 30 мин.")                    
  
        if cheked_1 == 'кларитромицин':
            messagebox.showinfo("Режим дозирования кларитромицина" , 
                                "При приеме внутрь для взрослых суточная доза 0,5-1 г, частота приема 2 раза/сут"
                                "СКФ 10-50 мл/мин или 75% от разовой дозы каждые 12 ч, при СКФ менее 10 - 50% от разовой дозы каждые 12 ч")
        if cheked_1 == 'клиндамицин':
            messagebox.showinfo("Режим дозирования клиндамицина" , 
                                "Внутрь, взрослым  при заболеваниях средней тяжести назначают по 1 капсуле (150 мг) 4 раза/сут(каждые 6 ч)."
                                "При в/м и в/в введении рекомендуемая доза для взрослых - 300 мг 2 раза/сут. При тяжелых инфекциях - до 1.2-2.7 г /сут, разделенные на 3-4 введения. Не рекомендуется в/м назначение однократной дозы, превышающей 600 мг. Максимальная разовая доза для в/в введения – 1.2 г в течение 1 ч."
                                "Пациентам с тяжелой печеночной и/или почечной недостаточностью не требуется коррекция режима дозирования в случае назначения препарата с интервалом не менее 8 ч."
                                "Для в/в введения препарат разводят до концентрации не выше 6 мг/мл; разбавленный раствор вводят в/в капельно в течение 10-60 мин."
                                "Не рекомендуется вводить препарат в/в струйно."
                                "Разведение и продолжительность инфузии рекомендуется выполнять по схеме доза – объем растворителя - длительность инфузии (соответственно): 300 мг - 50 мл - 10 мин; 600 мг – 100 мл - 20 мин; 900 мг - 150 мл - 30 мин; 1200 мг - 200 мл - 45 мин. В качестве растворителя могут быть использованы следующие растворы: 0,9% раствор натрия хлорида и 5% раствор декстрозы.")
        if cheked_1 == 'гентамицин':
            messagebox.showinfo("Режим дозирования гентамицина" , 
                                "При СКФ более 60 мл/мин нагрузочная доза: 4-7 мг/кг 1 раз, затем через 24 часа 1,7 мг/кг каждые 8 часов"
                                "\n при СКФ 40-59 мл/мин нагрузочная доза: 4-7 мг/кг 1 раз, затем через 36 часа 1,7 мг/кг каждые 12 часов"
                                "\n при СКФ 30-39 мл/мин нагрузочная доза: 4-7 мг/кг 1 раз, затем через 48 часа 1,7 мг/кг каждые 24 часа"
                                "\n при СКФ ниже 30 мл/мин нагрузочная доза не рекомендуется:  1,7 мг/кг каждые 24 часа"
                                "\n при СКФ ниже 20 мл/мин нагрузочная доза не рекомендуется:  необходим контроль концентрации"
                                "\n при подозрении на Гр+ инфекцию нагрузочная доза не используется(когда хотим добиться синергии), противопоказано назначение нагрузочной дозы при беременности, ожогах, асците")
        if cheked_1 == 'амикацин':
            messagebox.showinfo("Режим дозирования амикацина" , 
                                " При СКФ более 60 мл/мин нагрузочная доза: 15-20 мг/кг 1 раз, затем через 24 часа 5-7,5 мг/кг каждые 8 часов"
                                "\n при СКФ 40-59 мл/мин нагрузочная доза: 15 мг/кг 1 раз, затем через 36 часа 5-7,5 мг/кг каждые 12 часов"
                                "\n при СКФ 30-39 мл/мин нагрузочная доза: 15 мг/кг 1 раз, затем через 48 часа 5-7,5 мг/кг каждые 24 часа"
                                "\n при СКФ ниже 30 мл/мин нагрузочная доза не рекомендуется:   5-7,5 мг/кг каждые 24 часа"
                                "\n при СКФ ниже 20 мл/мин нагрузочная доза не рекомендуется:  необходим контроль концентрации"
                                "\n при подозрении на Гр+ инфекцию нагрузочная доза не используется(когда хотим добиться синергии), противопоказано назначение нагрузочной дозы при беременности, ожогах, асците")
        if cheked_1 == 'пипперациллин/тазобактам':
            messagebox.showinfo("Режим дозирования пипперациллин/тазобактама" , 
                                "При СКФ более 50 мл/мин - 100% доза каждые 6 часов; при СКФ 10-50мл/мин - 60-70% каждые 6 часов; при СКФ менее 10 - 60-70% каждые 8 часов")
        if cheked_1 == 'цефоперазон/сульбактам':
            messagebox.showinfo("Режим дозирования цефоперазон/сульбактама" , 
                                "При СКФ более 50 мл/мин - 100% доза каждые 12 часов; при СКФ 10-50мл/мин - 50-75% каждые 12-24 часа; при СКФ менее 10 - 25-50% каждые 24-48 часов")
        if cheked_1 == 'ко-тримоксазол':
            messagebox.showinfo("Режим дозирования ко-тримоксазола" , 
                                "При СКФ более 50 мл/мин - 100% (стандартная дозировка); при СКФ 10-50мл/мин - 50% (от стандартной дозировке); при СКФ менее 10 - противопоказан")        
       
        else:
            messagebox.showinfo("Не требуют корректировки дозы при ХБП", "Джозамицин, линезолид, клиндамицин, метронидазол, мидекамицин, оксациллин, рокситромицин, цефтриаксон, цефоперазон, орнидазол, метронидазол, доксициклин, азитромицин"
                                "\n Противопоказаны при почечной недостаточности: нитрофурантоины, сульфаниламиды,тетрациклин, нефторированные хинолоны")
  
def show_lit():
    messagebox.showinfo("Литература", "Stanford Hospital & Clinics Aminoglycoside Dosing Guidelines 2013"
                        "\n Rachel F. Eyler, Kristina Shvets Clin J Am Soc Nephrol. 2019 Jul 5; 14(7): 1080–1090. Published online 2019 Mar 12. doi: 10.2215/CJN.08140718"
                        "\n Яковлев Сергей Владимирович Новая концепция рационального применения антибиотиков в амбулаторной практике // Антибиотики и химиотерапия. 2019. №3-4. URL: https://cyberleninka.ru/article/n/novaya-kontseptsiya-ratsionalnogo-primeneniya-antibiotikov-v-ambulatornoy-praktike (дата обращения: 27.03.2020)"
                        "\n Приказ МЗ РБ от 29.12.2015 № 1301 О мерах по снижению антибиотикорезистентности организмов")
    
    
root = Tk()
root.title("Рациональная антибактериальная комбинация")
root.geometry('900x700+300+200')
root.resizable(False, False)
conclusion_label = Label(root, text= ' 1', font='Times 12', fg='grey')

first_label = Label(text="Введите первый антибиотик:")
second_label = Label(text="Введите второй антибиотик:")
conclusion_label.pack()
first_label.place(x=250,y=180)
second_label.place(x=500,y=180)
third_lable = Label(text="Выберите тип анализа")
var = IntVar()
var.set(0)
analysis_type_1 = Radiobutton(text="Взаимодействие", variable=var, value=0)
analysis_type_2 = Radiobutton(text="Антимикробная активность", variable=var, value=1)
analysis_type_3 = Radiobutton(text="Режим дозирования в зависимотси от СКФ (определяется для первого антибиотика)", variable=var, value=2)
analysis_type_1.pack()
analysis_type_2.pack()
analysis_type_3.pack()
combobox_antibiotic_group_1 = ttk.Combobox( values=[u'амоксициллин', u"пипперациллин/тазобактам", u'цефазолин',  u'цефалексин', u'цефуроксим', u'цефтриаксон', u'цефотаксим', u'цефдинир', u'цефтазидим', u'цефепим', u'цефоперазон', u'цефоперазон/сульбактам', u'амикацин', u'гентамицин', u'амоксициллин/клавулонат', u'пипперациллин/тазобактам', u'азитромицин', u'кларитромицин', u'джозамицин', u'эритромицин', u'макропен', u'спирамицин', u'ципрофлоксацин', u'левофлоксацин', u'офлоксацин', u'моксифлоксацин', u'норфлоксацин', u'пефлоксацин', u'меропенем', u'эртапенем',  u'имипенем', u'дорипенем', u'тетрациклин', u'доксициклин', u'тайгециклин', u'ванкомицин', u'тейкопланин', u'линезолид', u'колистин',  u'полимиксин', u'ко-тримоксазол', u'метронидазол', u'тинидазол', u'линкозамид', u'клиндамицин'])
#combobox_antibiotic_group_1(0)
combobox_antibiotic_group_1.place(x=250, y=200)
combobox_antibiotic_group_2 = ttk.Combobox( values=[u'амоксициллин', u"пипперациллин/тазобактам", u'цефазолин',  u'цефалексин', u'цефуроксим', u'цефтриаксон', u'цефотаксим', u'цефдинир', u'цефтазидим', u'цефепим', u'цефоперазон', u'цефоперазон/сульбактам', u'амикацин', u'гентамицин', u'амоксициллин/клавулонат', u'пипперациллин/тазобактам', u'азитромицин', u'кларитромицин', u'джозамицин', u'эритромицин', u'макропен', u'спирамицин', u'ципрофлоксацин', u'левофлоксацин', u'офлоксацин', u'моксифлоксацин', u'норфлоксацин', u'пефлоксацин', u'меропенем', u'эртапенем',  u'имипенем', u'дорипенем', u'тетрациклин', u'доксициклин', u'тайгециклин', u'ванкомицин', u'тейкопланин', u'линезолид', u'колистин',  u'полимиксин', u'ко-тримоксазол', u'метронидазол', u'тинидазол', u'линкозамид', u'клиндамицин'])
#combobox_antibiotic_group_2(0)
combobox_antibiotic_group_2.place(x=500, y=200)
#first_entry.grid(row=0,column=1, padx=5,)
#second_entry.grid(row=1,column=1, padx=5, pady=5)
message_button = Button( width=19, height=2, activebackground = 'grey', text="Анализировать", command=conclusion)
#message_button.grid(row=2,column=1, padx=5, pady=5, sticky="e")
message_button.place(x=400, y=300)
message_button_2 = Button( width=20, height=2, activebackground = 'grey', text="Список литературы", command=show_lit)
message_button_2.place(x=650, y=600)
root.mainloop()