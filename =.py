import random
import hashlib
import os
import base64;import secrets

data = [
    'sha', 'md', 'Yt-p', '4rg', 'uui9', '0-0', 'r5f', 'R5p', 'OpO', 'Qw+=', 'p*1', 'p3!',
    'q!-1', 'gGg1', 'ghj)', 'r1()', 'k)=-', 'v9+-', 'g8g@', 'gop!@', 'lop%', 'f!@#$',
    'RT$', 'mz-*&', 'y*?<', 'k3-%$', 'q{]g}h', 'k2(_)', 'dfHj', '1#^#', 'l-+167', '6^:',
    'sk*a', 'md5!', 'Yt%p', '9rg', 'uu%1', '0#0', 'r}{f', 'R0-=p', 'O;O', 'Q;+=', 'p*&1', 'p3+',
    'q+--1', 'DsSl1', '%&*@)', 'r1(!)', 'k!=-', 'v9^-', 'gq2g@', 'g*(p!@', 'luip%', 'f!@_#$',
    'Rz$', 'xx-*&', 'y>?<', 'k3,%$', 'q{><g}h', 'k2(,)', 'dfHj.', '1.#^.#', 'l-.+10-7', '6..:',
    's95', '@@d', 'er2-p', '33}P', ':Li9', '0;0', '90-f', 'R+*/p', 'O9O', 'Q=', 'j#1', 'p3#!',
    'q!#-1', 'g=0fg1', 'ghj;)', 'r:(:)', 'k)+-*', 'iop+-', '1**', 'heTy!@', 'l([+_])', 'f$h',
    'R0$', 'm4-*&', 'y*&?<', 'k3-&%$', 'q{]?g}h', 'k2(?)', 'dfhj', '1?^#', 'l-?167', '6?:',
    'sk*=a', 'md5=', 'Yt(%p', '9<>rg', 'uu12%1', '000', 'p}e{f', 'R-==p', 'O]O', 'Qz+=', 'p1', 'p3',
    'q+-1', 'Dsl1', '%&@)', 'r(!)', 'k=-', 'v9-', 'gqg@', 'g(p!@', 'lup%', 'f@_#$',
    'Rz$$', 'xx-*$&', 'y>?$', 'k3,%$$', 'q{>$<g}h', 'k2$(,)', 'dfH$j.', '1.#$^.#', 'l$-.+10-7', '6$..:',
    '#T8', ')(!#UEI)', '!@)*YU', '!@($UEH)', '!@(#UE)', '!PIEH', '**',
    '_!@OEK', '12elr', '13rl', '+~@E_', '!RKFM', '><!3er', '+_',
    '_', '1-2e', '!@#$ERF', '!"#134', "!#;=", '134', '9234', '92384',
    '1356', '13049', '!$@$', '+!)$', '!)#$(),', '3409!)', '-3195',
    'q', 'f', 'g', '4', '=3', '3<', 'root!@#', '0213rj', '=034', '*',
    'Rz$$', 'xx-*$&', 'y>?$', 'k3,%$$', 'q{>$<g}h',
    'k2$(,)', 'dfH$j.', '1.#$^.#', 'l$-.+10-7', '6$..:',
    '!@;', '||+', 'FEq', '||123e', ':!3e', '12034i', '103ei',
    '}_{@#+eo}', '!)(@#&eud)', '!|}@#p+)iod', '!@_#))e!i#(du)',
    '!#ERF', '(_R)@UPIFEHJD', '+@#)UREOFIH:DWCLJ}', '!_)#$R(@UPYEFIHLgj)',
    '@_#(RUPEFIHLJDVb)', '#R})C<@#P(EFIHLJ)', '_#I)EF{OUW:DHKVLJb',
    '#_@}IR)E*OUF:WHIDL}', '@}#}_RI$EFOU:HIWDLVJb}', '!(_#d3ref)',
    '!_#}RUE@OY:IFHL', '!)$@_(REUOFIH)', ')@e[fiupihgdh]',
    '|+#_}@fj32ef', '!#_}f-=+', '!#_(@)w3efr', '+)#_vf320re[foh]',
    '!#+_R}I)@E}OFUiwhdljb}', '$#R#*/FOEHJ}', '12-3e0fjefdfv'
]

xx = secrets.SystemRandom()

data1 = [
    'a1f4f','r$_p03','h4fu7','3fh&8**','maiop9_=$21q','h3cj48c+','><j38cm34ef','>2j,132ef',
    '39rwjf23','21opemdmji03','q3opjri33f','2039rjf_','10943jfn','12-09wfdvj','2390efjd',
    '!@_)euj13ef','!@)_IDjq3r',"@_#(RU23p94uy)",'}!P#)_(Y13u4t),','{!_+}4342rfefsfg3',
    'uiqwhru9her','wkdjfiojriu','eirjfi02jrfiv,','0234934','2349283498','@(#(@$()#))',
    '!#)$+!)#$_+)_+!','!@#*!*#(*!#(_$*),)',"_()#*)#URFIOHO#*)$", '3u4382408','13-40',
    '***#*$****$','10001010101','0001010101000','1920393849','304903940394','0000000',
    '4455454554','j13j431jr24','034irfjimrv','+__++__+__@3','i-1-1-1-1','}PJ^234234425',
    '2oi3yuig32g4','12p3ue8o8eqr80123y','123ueoeqf8y132ueeh','1232oeudo3o1','1382983948',
    '+)**@(#()*@#),','!&#&*&!#@(*#&&())','-+-@#+-#;№?','!№:(:!№?(;:?()))','::#:@##$@',
    '№№"№%+_)?','r487jr№','1+1==1','102qwoejdc','13-9ejwrfmc','239uejdicxk','123ye8ri',
    '239refwi,','239urejifd','!@_+EI)WODJ','10339930494039','031499-2349-82493-48',
    '130903914924-090','2349294092409','3240923940924','394=092049','3249294',
    '314993409','+_!@@+#)_','109302eif','}{<><>2','jgfhhgh','nbnbn','-=-eceerf',
    '?>>@L3,wd3e','qede323efe','p;32+3',')@30k2o-3-ke','}{+3e}','134erfd','3****',
    '101010010-','1+***+_)(#)','232erf','%$WERDg','_({)(*PI&UH)})','W$ETDF',
    '&%ITY2egf','12op3peuduig','123iuewduowg*/','OI{L":;}','i390euefu','912e9uwd98y',
    'ouiew9d0cyhi3iewid','!()@&E*)&!*)#&*)','!)@*EY*!&#@*)&','!(@E*)&!#)E&*','*-_93',
    '1-038e80fywh','!@(%&#TOUEGLJB)','>><>><<>2','root#$>','134rie9fji','><!@3e/',
    '13408r6e8tfryg','!@(&T#EUGWJ)','!@(&#TUEGWJD)','!№"?*)31948','0987633457',
     '!#ERF','(_R)@UPIFEHJD','+@#)UREOFIH:DWCLJ}','!_)#$R(@UPYEFIHLgj)',
    '@_#(RUPEFIHLJDVb)','#R})C<@#P(EFIHLJ)','_#I)EF{OUW:DHKVLJb',
    '#_@}IR)E*OUF:WHIDL}','@}#}_RI$EFOU:HIWDLVJb}','!(_#d3ref)',
    '!_#}RUE@OY:IFHL','!)$@_(REUOFIH)',')@e[fiupihgdh]',
    '|+#_}@fj32ef','!#_}f-=+','!#_(@)w3efr','+)#_vf320re[foh]',
    '!#+_R}I)@E}OFUiwhdljb}','$#R#*/FOEHJ}','12-3e0fjefdfv'
    
    ]

data2 = [
    '#T8',')(!#UEI)','!@)*YU','!@($UEH)','!@(#UE)','!PIEH','**',
    '_!@OEK','12elr','13rl','+~@E_','!RKFM','><!3er','+_','',
    '_','1-2e','!@#$ERF','!"№134',"!№;=",'134','9234','92384',
    '1356','13049','!$@$','+!)$','!)#$(),','3409!)','-3195',
    'q','f','g','4','=3','3<','root!@#','0213rj','=034','*',
      'Rz$$','xx-*$&','y>?$<','k3,%$$','q{>$<g}h',
      'k2$(,)','dfH$j.','1.#$^.№','l$-.+10-7','6$..:',
      '!@;','||+','FEq','||123e',':!3e','12034i','103ei',
       '!#ERF','(_R)@UPIFEHJD','+@#)UREOFIH:DWCLJ}','!_)#$R(@UPYEFIHLgj)',
    '@_#(RUPEFIHLJDVb)','#R})C<@#P(EFIHLJ)','_#I)EF{OUW:DHKVLJb',
    '#_@}IR)E*OUF:WHIDL}','@}#}_RI$EFOU:HIWDLVJb}','!(_#d3ref)',
    '!_#}RUE@OY:IFHL','!)$@_(REUOFIH)',')@e[fiupihgdh]',
    '|+#_}@fj32ef','!#_}f-=+','!#_(@)w3efr','+)#_vf320re[foh]',
    '!#+_R}I)@E}OFUiwhdljb}','$#R#*/FOEHJ}','12-3e0fjefdfv' 
    ]

data3 = [
    '#T8', ')(!#UEI)', '!@)*YU', '!@($UEH)', '!@(#UE)', '!PIEH', '**',
    '_!@OEK', '12elr', '13rl', '+~@E_', '!RKFM', '><!3er', '+_',
    '_', '1-2e', '!@#$ERF', '!"#134', "!#;=", '134', '9234', '92384',
    '1356', '13049', '!$@$', '+!)$', '!)#$(),', '3409!)', '-3195',
    'q', 'f', 'g', '4', '=3', '3<', 'root!@#', '0213rj', '=034', '*',
    'Rz$$', 'xx-*$&', 'y>?$<', 'k3,%$$', 'q{>$<g}h',
    'k2$(,)', 'dfH$j.', '1.#$^.#', 'l$-.+10-7', '6$..:',
    '!@;', '||+', 'FEq', '||123e', ':!3e', '12034i', '103ei',
    'sha', 'md', 'Yt-p', '4rg', 'uui9', '0-0', 'r5f', 'R5p', 'OpO', 'Qw+=', 'p*1', 'p3!',
    'q!-1', 'gGg1', 'ghj)', 'r1()', 'k)=-', 'v9+-', 'g8g@', 'gop!@', 'lop%', 'f!@#$',
    'RT$', 'mz-*&', 'y*?<', 'k3-%$', 'q{]g}h', 'k2(_)', 'dfHj', '1#^#', 'l-+167', '6^:',
    'sk*a', 'md5!', 'Yt%p', '9rg', 'uu%1', '0#0', 'r}{f', 'R0-=p', 'O;O', 'Q;+=', 'p*&1', 'p3+',
    'q+--1', 'DsSl1', '%&*@)', 'r1(!)', 'k!=-', 'v9^-', 'gq2g@', 'g*(p!@', 'luip%', 'f!@_#$',
    'Rz$', 'xx-*&', 'y>?<', 'k3,%$', 'q{><g}h', 'k2(,)', 'dfHj.', '1.#^.#', 'l-.+10-7', '6..:',
    's95', '@@d', 'er2-p', '33}P', ':Li9', '0;0', '90-f', 'R+*/p', 'O9O', 'Q=', 'j#1', 'p3#!',
    'q!#-1', 'g=0fg1', 'ghj;)', 'r:(:)', 'k)+-*', 'iop+-', '1**', 'heTy!@', 'l([+_])', 'f$h',
    'R0$', 'm4-*&', 'y*&?<', 'k3-&%$', 'q{]?g}h', 'k2(?)', 'dfhj', '1?^#', 'l-?167', '6?:',
    'sk*=a', 'md5=', 'Yt(%p', '9<>rg', 'uu12%1', '000', 'p}e{f', 'R-==p', 'O]O', 'Qz+=', 'p1', 'p3',
    'q+-1', 'Dsl1', '%&@)', 'r(!)', 'k=-', 'v9-', 'gqg@', 'g(p!@', 'lup%', 'f@_#$',
    'Rz$$', 'xx-*$&', 'y>?$<', 'k3,%$$', 'q{>$<g}h', 'k2$(,)', 'dfH$j.', '1.#$^.#', 'l$-.+10-7', '6$..:',
    '&&&&&*&', '$$$$$!',
    'a1f4f', 'r$_p03', 'h4fu7', '3fh&8**', 'maiop9_=$21q', 'h3cj48c+', '><j38cm34ef', '>2j,132ef',
    '39rwjf23', '21opemdmji03', 'q3opjri33f', '2039rjf_', '10943jfn', '12-09wfdvj', '2390efjd',
    '!@_)euj13ef', '!@)_IDjq3r', "@_#(RU23p94uy)", '}!P#)_(Y13u4t),', '{!_+}4342rfefsfg3',
    'uiqwhru9her', 'wkdjfiojriu', 'eirjfi02jrfiv,', '0234934', '2349283498', '@(#(@$()#))',
    '!#)$+!)#$_+)_+!', '!@#*!*#(*!#(_$*),)', "_()#*)#URFIOHO#*)$", '3u4382408', '13-40',
    '***#*$****$', '10001010101', '0001010101000', '1920393849', '304903940394', '0000000',
    '4455454554', 'j13j431jr24', '034irfjimrv', '+__++__+__@3', 'i-1-1-1-1', '}PJ^234234425',
    '2oi3yuig32g4', '12p3ue8o8eqr80123y', '123ueoeqf8y132ueeh', '1232oeudo3o1', '1382983948',
    '+)**@(#()*@#),', '!&#&*&!#@(*#&&())', '-+-@#+-#;#?', '!#:(:!#?(;:?()))', '::#:@##$@',
    '##"#%+_)?', 'r487jr#', '1+1==1', '102qwoejdc', '13-9ejwrfmc', '239uejdicxk', '123ye8ri',
    '239refwi,', '239urejifd', '!@_+EI)WODJ', '10339930494039', '031499-2349-82493-48',
    '130903914924-090', '2349294092409', '3240923940924', '394=092049', '3249294',
    '314993409', '+_!@@+#)_', '109302eif', '}{<><>2', 'jgfhhgh', 'nbnbn', '-=-eceerf',
    '?>>@L3,wd3e', 'qede323efe', 'p;32+3', ')@30k2o-3-ke', '}{+3e}', '134erfd', '3****',
    '101010010-', '1+***+_)(#)', '232erf', '%$WERDg', '_({)(*PI&UH)})', 'W$ETDF',
    '&%ITY2egf', '12op3peuduig', '123iuewduowg*/', 'OI{L":;}', 'i390euefu', '912e9uwd98y',
    'ouiew9d0cyhi3iewid', '!()@&E*)&!*)#&*)', '!)@*EY*!&#@*)&', '!(@E*)&!#)E&*', '*-_93',
    '1-038e80fywh', '!@(%&#TOUEGLJB)', '>><>><<>2', 'root#$>', '134rie9fji', '><!@3e/',
    '13408r6e8tfryg', '!@(&T#EUGWJ)', '!@(&#TUEGWJD)', '!#"?*)31948', '0987633457'
]


data4 = [
    '!#ERF','(_R)@UPIFEHJD','+@#)UREOFIH:DWCLJ}','!_)#$R(@UPYEFIHLgj)',
    '@_#(RUPEFIHLJDVb)','#R})C<@#P(EFIHLJ)','_#I)EF{OUW:DHKVLJb',
    '#_@}IR)E*OUF:WHIDL}','@}#}_RI$EFOU:HIWDLVJb}','!(_#d3ref)',
    '!_#}RUE@OY:IFHL','!)$@_(REUOFIH)',')@e[fiupihgdh]',
    '|+#_}@fj32ef','!#_}f-=+','!#_(@)w3efr','+)#_vf320re[foh]',
    '!#+_R}I)@E}OFUiwhdljb}','$#R#*/FOEHJ}','12-3e0fjefdfv',
    '+++++++','+++++=====','{---3',':3',':::;;:::;;::::;;;:',
    '~@P(!OGH123erfwdv)','!@+#*(M#EOU:DIYLJGH)','!@|+_EIOUDHJ',
    '!@{)#UIYELFUWGHD}','!-#@|+F}_)PIDLUHDD}','*+','+','+#_)EOIUIU)_#)',
    '@*(E#IYUDGH!)','WIOQIHCDWGN','&!^@RUEWPEIYD','#_E@IFYUDH',
    '_P"E:<D','!#PEODW%IFHG}','UI&&HY&Y&YY&Y','*+OF*RF','_-_JJj',
    ')(*#&YEDGBC)','(1)(2)(3)(4)(5)(((10)))','([([)])])'
]

data5 = [
    '~_~','~~~','1~`_+','~~~324r','~#!edf','~=~=~=','~OR1=1--','nma~p',
    'linux3!#~','OR', '1=1~~','--','~_+I)OJK','~.,/,||',
    '~|~|~','~|~','|rf~|'
]
data6 = [
    '!\/\/', '@|\|', '#~@!$%', '$=-_+', '%Z^^^', '43&', '*$#$', '(', ')',
    '~_~', '!', '?', '@_@', '#_#', '$==$', '***', '&&&','><<>><<>><<><',
    '?>?<?<?>?<?<?<?<','*+-+*+--+','!(@#&()&!#&!)#&)!&#','}{[]}}','?!',
    '|\/\/\/\/\/|','|_|_|_|_|','::::;:;;;::;::::5','[[[[[[[[[]]]]]]]]]',
    '****************','||||||||||||||||||||','~~~~~~~~~~~~~~~~~~~~~~~`'
]

data7 = [
    'RM96ksPA==','QeThO0==','|\||==',"$E^RDf==",'DTVY==',
    'T*&YUHo==','^*!#EGWUD==','!@U#UEWJIPDE==','==','!#@EJOP==',
    '****==','//??==','!#)I()EJ==','====','2owe0do==','||==',
    '@WOIJD==','-+*/==','@Ieowdked==','!~WU!hdbkcjhijefu9==',
    '@Pew[d==]==','ewydfdouj==','93yuef==','/z/xc/x=='
    '/x1/x1/x1==','x1==','x11==',':::==','+_!)W(@IEUGYDWFWGUY(U==',
    '&&&&&==','_@)EWUIyduudw2791==','10001110001==','~root#%~==',
    '100x100x100x==','=+==','_@wew=--==','~~!~~!]]=='
    ]


RED = '\033[31m'
GREEN = '\033[32m'
END = '\033[0m'

def random_pw():
    global q
    A = random.randint(1,29)
    if A == 1:
        q1 = xx.choice(data6)
        q2 = xx.choice(data1)
        q3 = xx.choice(data2)
        q4 = xx.choice(data7)
        q5 = xx.choice(data3)
    elif A == 2:
        q1 = xx.choice(data7)
        q2 = xx.choice(data1)
        q3 = xx.choice(data1)
        q4 = xx.choice(data3)
        q5 = xx.choice(data)
    elif A == 3:
        q1 = xx.choice(data7)
        q2 = xx.choice(data3)
        q3 = xx.choice(data1)
        q4 = xx.choice(data6)
        q5 = xx.choice(data7)
    elif A == 4:
        q1 = xx.choice(data1)
        q2 = xx.choice(data1)
        q3 = xx.choice(data1)
        q4 = xx.choice(data1)
        q5 = xx.choice(data1)
    elif A == 5:
        q1 = xx.choice(data)
        q2 = xx.choice(data7)
        q3 = xx.choice(data)
        q4 = xx.choice(data7)
        q5 = xx.choice(data)
    elif A == 6:
        q1 = xx.choice(data3)
        q2 = xx.choice(data7)
        q3 = xx.choice(data3)
        q4 = xx.choice(data3)
        q5 = xx.choice(data3)
    elif A == 7:
        q1 = xx.choice(data2)
        q2 = xx.choice(data2)
        q3 = xx.choice(data6)
        q4 = xx.choice(data2)
        q5 = xx.choice(data2)
    elif A == 8:
        q1 = xx.choice(data1)
        q2 = xx.choice(data5)
        q3 = xx.choice(data7)
        q4 = xx.choice(data3)
        q5 = xx.choice(data6)
    elif A == 9:
        q1 = xx.choice(data6)
        q2 = xx.choice(data3)
        q3 = xx.choice(data5)
        q4 = xx.choice(data3)
        q5 = xx.choice(data7)
    elif A == 10:
        q1 = xx.choice(data7)
        q2 = xx.choice(data5)
        q3 = xx.choice(data1)
        q4 = xx.choice(data2)
        q5 = xx.choice(data3)
    elif A == 11:
        q1 = xx.choice(data)
        q2 = xx.choice(data7)
        q3 = xx.choice(data1)
        q4 = xx.choice(data)
        q5 = xx.choice(data)
    elif A == 12:
        q1 = xx.choice(data)
        q2 = xx.choice(data3)
        q3 = xx.choice(data6)
        q4 = xx.choice(data)
        q5 = xx.choice(data7)
    elif A == 13:
        q1 = xx.choice(data5)
        q2 = xx.choice(data)
        q3 = xx.choice(data)
        q4 = xx.choice(data6)
        q5 = xx.choice(data7)
    elif A == 14:
        q1 = xx.choice(data3)
        q2 = xx.choice(data4)
        q3 = xx.choice(data7)
        q4 = xx.choice(data2)
        q5 = xx.choice(data5)
    elif A == 15:
        q1 = xx.choice(data5)
        q2 = xx.choice(data6)
        q3 = xx.choice(data3)
        q4 = xx.choice(data4)
        q5 = xx.choice(data7)
    elif A == 16:
        q1 = xx.choice(data3)
        q2 = xx.choice(data6)
        q3 = xx.choice(data3)
        q4 = xx.choice(data7)
        q5 = xx.choice(data3)
    elif A == 17:
        q1 = xx.choice(data1)
        q2 = xx.choice(data3)
        q3 = xx.choice(data1)
        q4 = xx.choice(data)
        q5 = xx.choice(data7)
    elif A == 18:
        q1 = xx.choice(data7)
        q2 = xx.choice(data3)
        q3 = xx.choice(data)
        q4 = xx.choice(data6)
        q5 = xx.choice(data2)
    elif A == 19:
        q1 = xx.choice(data4)
        q2 = xx.choice(data7)
        q3 = xx.choice(data5)
        q4 = xx.choice(data)
        q5 = xx.choice(data2) 
    elif A == 20:
        q1 = xx.choice(data4)
        q2 = xx.choice(data4)
        q3 = xx.choice(data4)
        q4 = xx.choice(data4)
        q5 = xx.choice(data2) 
    elif A == 21:
        q1 = xx.choice(data1)
        q2 = xx.choice(data2)
        q3 = xx.choice(data7)
        q4 = xx.choice(data5)
        q5 = xx.choice(data6) 
    elif A == 22:
        q1 = xx.choice(data4)
        q2 = xx.choice(data4)
        q3 = xx.choice(data4)
        q4 = xx.choice(data7)
        q5 = xx.choice(data4) 
    elif A == 23:
        q1 = xx.choice(data3)
        q2 = xx.choice(data4)
        q3 = xx.choice(data5)
        q4 = xx.choice(data4)
        q5 = xx.choice(data5) 
    elif A == 24:
        q1 = xx.choice(data3)
        q2 = xx.choice(data3)
        q3 = xx.choice(data4)
        q4 = xx.choice(data4)
        q5 = xx.choice(data5) 
    elif A == 25:
        q1 = xx.choice(data3)
        q2 = xx.choice(data5)
        q3 = xx.choice(data7)
        q4 = xx.choice(data5)
        q5 = xx.choice(data3)
    elif A == 26:
        q1 = xx.choice(data7)
        q2 = xx.choice(data5)
        q3 = xx.choice(data5)
        q4 = xx.choice(data5)
        q5 = xx.choice(data)
    elif A == 27:
        q1 = xx.choice(data1)
        q2 = xx.choice(data5)
        q3 = xx.choice(data5)
        q4 = xx.choice(data5)
        q5 = xx.choice(data1)
    elif A == 28:
        q1 = xx.choice(data)
        q2 = xx.choice(data5)
        q3 = xx.choice(data5)
        q4 = xx.choice(data5)
        q5 = xx.choice(data)
    elif A == 29:
        q1 = xx.choice(data7)
        q2 = xx.choice(data7)
        q3 = xx.choice(data7)
        q4 = xx.choice(data7)
        q5 = xx.choice(data7)
    k = xx.randint(1,12)
    salt_bytes = os.urandom(k)
    salt_string = base64.b64encode(salt_bytes).decode('utf-8')  


    q = f'{q1}{salt_string}{q2}{q3}{q4}{q5}'
    return q

 



def hach_1():
    global e
    global p
    r = xx .randint(1,3)
    if r == 1:
        e = hashlib.sha512(q.encode()).hexdigest()
        p = 'sha512'
    elif r == 2:
        e = hashlib.sha3_512(q.encode()).hexdigest()
        p = 'sha3_512'
    elif r == 3:
        e = hashlib.blake2b(q.encode()).hexdigest()
        p = 'blake2b'
    
    return e,p




def pr():
    print(f'''{GREEN}
    [+]pw->{q}\n{RED}
    [*][{p}]hech->{e}\n
    {END}''')

try:
    while True:
        user=input('root#$>>>')
        random_pw()
        hach_1()
        pr()
except KeyboardInterrupt:
    import sys
    sys.exit(1)
