_A1='sp_filter'
_A0='sp_update'
_z='weapon_name'
_y='prev_weapon_index'
_x='camera_position'
_w='view_angles'
_v='acceleration'
_u='loot_id_alt'
_t='loot_name'
_s='loot_id'
_r='sp_lp'
_q='sp_list'
_p='sp_main'
_o='Mouse X2'
_n='Mouse X1'
_m='Mouse Middle'
_l='Mouse Right'
_k='security'
_j='size'
_i='process_id'
_h='last_visible'
_g='is_loot'
_f='<3f'
_e='Alt'
_d='Ctrl'
_c='Shift'
_b='address'
_a='utf-8'
_Z='sig_name'
_Y='level_name'
_X='game_mode_text'
_W='weapon_index'
_V='weapon_gravity'
_U='head_position'
_T='read_time'
_S='name'
_R='velocity'
_Q='<I'
_P='weapon_speed'
_O='view_matrix_pointer'
_N='health'
_M='U'
_L='char'
_K=1.
_J='team'
_I='armor'
_H='position'
_G='index'
_F='pointer'
_E='active'
_D=None
_C='time'
_B=True
_A=False
import traceback,numpy as np,numba as nb,pynput.mouse
from multiprocessing import shared_memory as sm
from pynput import keyboard,mouse
import ctypes,ctypes.wintypes as wintypes,random,string,time,copy,math,sys,os,subprocess,base64,tempfile,winreg,struct
from struct import unpack_from
import builtins
ENABLE_QUICK_EDIT_MODE=64
ENABLE_EXTENDED_FLAGS=128
kernel32=ctypes.WinDLL('kernel32',use_last_error=_B)
handle=kernel32.GetStdHandle(-10)
mode=ctypes.c_ulong()
kernel32.GetConsoleMode(handle,ctypes.byref(mode))
kernel32.SetConsoleMode(handle,mode.value&~ENABLE_QUICK_EDIT_MODE|ENABLE_EXTENDED_FLAGS)
is_dev=_A
Drv='O<Iru0{{R31ONa4|Nj60xBvhE00000KmY&$0000000000000000000000000000000000000000*Z=?k4j;M>0JI6sA-Dld%^_51X>%ZOa&KpHVQnB|VQy}3bRc47AaZqXAZczOL{C#7ZEs{{E)5L|Bme*a00000*&0BWoqI0DoqI0DoqI0Di4ZTuo_j9EoqI3EhkGu?i4ZNsnR_n9i4ZEpn0qe8S`I73oO>?CS`IA4oO>?CQfXsooqI0D00000000000000000000P(=U$WQGO+;k0RK0000000000@BktJ3jz)u02TlM01N;C0000001yBG01yBG0000$0RR9101yBG00IC23IG5A3IG5A3IG5A000000Du4h00aO4>sJ5(0RUh@000mG0000001yBG00000000mG0000001yBG00000000005C8xG00000000000AK(BC;$Ke000000000008jt`<NyEw044wc5E%df0B`^R7ytkO05JdnH~;_u000000000000000000000000000000KrsLS7y$qP000000000005AXmumAu6000000000000000000000000000000E_7vhbN~PVwh#aS01yBG01^NI00aO4000000000000000AOHYpE^=gHbYTDhBn1Ef05AXm00sa602TlM000000000000000KmY(pE@WYJVE_OCU;qFB06+i$00IC202}}S000000000000000KmY*9E^uUFbYTDh<NyEw08jt`00IC203HAU000000000000000KmY(pNlr;r00000yaE6K0AK(B00aO403ZMW000000000000000AOHYjE^=jTZ({%e7ytkO0B`^R00IC203-ka000000000000000KmY(j00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000NR1Ww1ONat$>|9U007L)Kvh##S3y-lRzX)ti|j~)>_A9^JvJZ!002yj`45B~0ssI=iw!0q002yl1+O3g071DB0000%jZqNj)Cd3oNQJ-;g!Tad07#2K5J-b%NB~GB0Pz3+NQnixF8~1l726*G07#42NP{>44}{GD002mf@Ik!+0000;i$e%Vg}@Jlw*deENQ*m2nStW}4*&o~GxkUW!brjR3`m8*4~~cd002mf1#2$=08ER=Nx|q0ON|UbNCU}8i&V%cNVxz1|Ns90002lM&`CSc4}~uQ002mXWl#V}jZIKVi^oNa%}BxMCqcLf0000b{{a91NR1T7NR35ENQp!wApaFX9{>P_zz>M_0000;i$zdDgvAep=>Px#NP}fq07$w3@c;k+{|^92Bf?3G&q%@P9z~1If#LrF002R_2mk;8NR1T8NR35ENR3TcNQp!wApaHZ9smG^zz>L`0000;i$z#LgvAepl>h($NP}hY07$w3@c;k+{|^92Bf?3G&q%@P6-A59f#LrF002R_2mk;8NR1T8NR35ENR3VKNQp!wApaGa9smG^z<5$fi$(B3gvE48NP}hg07$w3@c;k+{|^92Bf?3G&q%@P3`L90f#LrF002R_2mk;8NR1T8NR35ENR3VSNQp!wApaFj9smG^z<35kgl+hBOGt}D2t@<+NSR4v&Vl0p4*&p2fyV$4002k>!brjR3`jf34~%&J|NlsX#t=x0-bjN!01t&c{{R0oz(|9{KtW$YUO`=7URzzmNQ=ko?99x}%*@Qp%*@QpKvPJA>>x;s+B4Efi_8BNoE-oFi$gF-gTx?P!_3UgKvPJA>>z<TCKmtzNQ>EZMo42p1cktKK1hRPBrpI-jZ`EsNQ=n-6}ue(07#2WBrr&Y$#fv-Q3(J5NQJ<37D$Ur2uO(mNQ+D)F#i>09RL6`!0QFL0RRBNNQ1;6Tf@xENQqn|2uO)^BoJ3fgX}O!i~5VnNR3n^P&3>A6=NL$0ENJL2Q$FwhX4QoNQ+D)Q2!M@9RL7Gi%cX?{}oyt002mf@JNNgbX7=;Kp04cz;sMFSOj!ONQ>7<jZ7pU{}rYj002mfMi@wgzz|4_IO`!ujZauXumMPoR3sq(6^|SM0ENJG5=e_i7)XmhNQ1x-NIUp-+Uo>Ji(fGR71ta907#2WBvAhqq#OVMNQ=Wri(Di?NQ-nNNJxXkFki#WNQqn|2uO)^BoJ3fgX}O!i~5VnNR3n^P&3>A6`vdc0ENJL2Q$Fwg#Z8mNQ+D)Q2!Nq8~^}Fi%cX?{}q-T002mf@JNNgbW})-Kp04cz;sJESOj!NNQ>7<jZ7pU{}tjJ002mfMi@wgzz|4_IO`!ujZauXumMPoR3sq(70Vj{0ENJG5=e_i7)XmhNQ1x-NIUp-+Uo<0UqJsA6dV8mNQ+D)Q2!O-8vp={!$^x<BtS@ubR<YfgTydj!_3UgNQqn|2v<mh>>x;s1*0nf07zr`NQJ<32su5SD*ym=Qb>bjBsc&_jZ`E!NQ=+^6~`L@07#2WBsfTg$#n@x$G`yq0Kn@j=u`&)07#3-=s)}a|455WBsfTm*#8x28vp=Ei^E8X9Y-qw0Es<GD*ymUi(DiyNQ1;6U&GAI%*@QpNQqn|2v<mh>_A9^WF%k!NR2%yD*ymUi`htx6%Pvl07#3^{}t96002mh6(0)#07#7u7%Kn({}sX-002mhL?mEAxgr1n07!{MBrr^i$Hqh?C;&6kNQ=wIL?j>p0RRC16~7t)0ENJKYe<XNNR18IDgXfg6|))u07Q$xg}``JNR0)x1polK8~^|SNR4}N^GK^mi$o+~gGew0NR0)_{Qv(*i9>KmiGzRu002mh1vdZy07!|0-~a#sNR0(a1poj@i9={ei$o+~54vzL2SJO#NQ+z~P)LKsKwrbm%*@Qp%*@Qp%*@QpNQqn|2uO)^BoJ3fgX|zki-NcS001-pNQ?4|--}Qfi%1ZG`kWjh0CgUN`6v&Cpa1{>NQ+Jw=)(X20E^haC;$Ke>5u>b0D=0%93lX97lZjYb$&>TP8jF`0ssJu*uOXc008T8f%>2vA^>$4gZU73Ur38i80aGW|No2FzYqWb0P9kL`lK8p0CgFG`4|EK0Chb`i(VLu3rLMq5a?d~|NrYBf%?E4A^>$Mf%zB$004CyNQ+(=iwj7NQxNC@{r~?+i9-mB-@h0F008R+y959Lz>CK-(nyQWNQp)`iC!@O6+;;S07#2;Bsh!1NQ+z~Fi3;MAYa4GNQq1&2vb&9K~_kE>^Mk^*?~DG7XSbcg);#F0E<Zkg~<<uC;<Qf=wJQ+|4fVUNP}b~XaF<+NQrzTa7c@D7(h6CAapTEi&F?li^%9r0ssI=g}@Jl^Z)<=OpQz=XiSSk7)Xm#5J-#2=mP`*05ibp-2eapNQL$fgvI~>07!#mBxnFc4<Nui0S||?0000)4<NvVzz>C}0000;i&F?l1J_B5&gk+1002mf&`60yBzQ=Lz;z0^0RRBN>5u>b044tq006lF5C8xx$cx51&JRq%Ok==Ii%SSgjSK-u1J6i{1;ZEs07yFscSK2z1UX1O00031b~s3jOAtr{&q$3#Bxp#9L?j?Vxd8wG0RI(D7ytl}NQ*=yXh?;?bRkG9@JIvrNQrzTaOpz-|NpoF006-27)Xm;Bw$F3d?av4iF+97A^-pXxB&nFz(|9{I6+=tUR%S=OpDw}iCY*+iE|)VNQ3M!fjK4@002mf`45Gi0000;V?hvwzz>9x0000<gJTE)NsUtoNQ=n-73&uO07#2WBtS@o$#iu{i(d%;6{i;f07#2h7)XoDNQ-wU=-&VU07!+vbXJSVx&ROW0D<BE4*&ow(MXF=AUoC%O!7#BWF$xcfPXLmOk>7$5=e{DOpQz=NJxvw=yw7D0P7h@jZ`E^LAe0{002mdR3sosi_rfSP!|9IGr;QwxB&nFz(|W+Bv43;bR<|vgTydj!_3UgNQqn|2uO)^BoIi6d?Xl5i`qpq(oHMbNQ?PNEBHx^@JNf<Gty0k$#fb>i_T7s1Q&_{K{x~mbqh%U!btzYNjuSU?MXY)bPP%V!c9BVcG5Gz>jX)S1R6+-TqFoci*zIqNQ-<V7{koWNQqP=5LHuFS3y)kRzX)ti|j~)>_A9^Wk3K(i~2}|Wl#W2i}FZ|@=3w&3`mRGNWtzExc>nF07${=CrBgENWtqKNQ2?<LA(I~002xQ@JJ)@NF&%qi_A!kML>b){|^8FNR1THNQp!wAV`f(P(_VIBnST$OcnqDNQ+HSioy2KL4?E)h1~!E07!#nSO7?kML<cv0Pz3+4*&oFNQp!wAW0+7MT^WxjTG5Ija(!LM2o{njZIkp6$cgo07#2fSc<~-&_RU64~3Wj004y2c^pWKO-M+%0002M|NjpFNF&05;s5{tKS%??>v~9oW$*w<jYU97BiBfYL?j?Zi_A!kP4G;M!$^%3^8XdF6#xK8i$(B?$oA1egv@nDgur<ZNQ+HKNh8OB;s5_10PD6$gJnnnNR3TMNh8Nai_A=m!%B@5@JNkCKuC#1Bq0A4Y!v_iNQ*^CNh8N}1xN$O>jE>tNQ1;cL0>^$L0n&6TV2D<%*@QpKvPJA>>x;s*+`8IFeLy0{}mb)004!+cnV01O9=lJ1Qh@PNQ1;6Tf@xE%*@QpKvPJA>>x;s+Q&jLy8r;dNQ=ue(*G636aWB=Loi5##2{P4NQqn|2uO)+BoIi6bR-y8NQ3MkNsIAGi`Ynu>PUsjbT~n{1ONa4NQ=||6@wH207#4YNQJ<3Axw+INQ>1-i^%BJ0000;i_=Jn9!QJN{}omg001+<>jk(0006*9i(DiyNQ-PFI7o|hBtS@m#2{b8%*@Qp%*@Qp%*@Qp%*<wH4<Cd800000NIMM)Bme+)5J<tn5N7wm|NnIX!$`r&5a|K{007L)xdH$H0L>}?C1Vr-0RJUr6aWDKC2te}0L;wH%*@Qp!T<ow%*@Qp%*@Qp%*@Qp%*@Qp%*<wH4<Cd800000|KQBb%*@Qp%*@Qp%*@Qp%*@Qp%*@Qp%*@Qp%*@Qp%*@Qp%*@Qp%*@Qp%*@QpNQ=QqgZKz?H%Wu|5O)zwiyBIcR08-+i5W_XQ~~(INrU(xcUlh+0zwZEOakx^5dlIE5ljK_!w(;T00000O@+X86-X=5au!6291%$W!AbwfM2K1cb@0OvA4C8ENdw44id+%@NdL)6|Hwp$8Flc(W@ct)4<Cd800000PK_J_NGs8E2~0cL4~K36000jV1QAGs!4USr4|EbpgW>QG5DXCy5daS;!AOI_5KIHWOe?`ni^xgA=>~LfNrCwQ5C8xVhqC|x07--3KkF@KW@ct)W@Zl`ga7~l003rYW@ct)W)B~P000000A^-pW@ct)4<Cd8000004-gCy4-ixl5DySs5g-o`WDzhADM9c^gTX*a|H%(2Nx%;&QP2-5S>O*S#C6e4i^xgA=>&8c4<Cd8000004=F+L4-f<qNQ1!;N&m@p?@5E;4|EPrja&inK@SiN6G0CV3lAwl@WW<iW@ct)W)B~P0000001qF400000O^e7$!RZD`gWx|87(@|3>n>(yW@ct)W)B~P000000A^-pW@ct)4<Cd800000W@ct)W@cs&AA|q^0001x4-gCy4-ixl5DySs5g-o`WDzhAD?#u`gTX)#7(@|3N&m?YD@ni)D^bu7D_P(VD8zNl53cy>Gynhp4<A4PNdw3a5JVC1NQ3DRNrUJR_Q4Ny7)*=VNQ2?<4-gCyK@SlF4=BM*i@{7Qz)g$DNx|s`bU8_b;6LjG4<A4P4-iZd@DC7F5#SFHToKR@5M&X+4=DjigXus?|H%(2NiYv7Q6LW~Sr88>#C6e4i^xgA=>&8c4<Cd8000004=Di;5JVC1NQ3DRN&m@p?@5E;4|ESqi`h*p*g+2v3==^Q5ep9~0mID9%*@Qp%*@Qp%*@Qp%*@Qp%*@QpNQ=QqgZKz?M-R5rNx1<50RaI40Rc%5uhB_^_)l|CO^e7$gW>o|1IcC&A4C8EN{Lhm_(_B52zB*IgWv~r1xkrj0r<ma4<Cd800000NrT`AbP7U<Q~>`;|HyUr!)9h?W@ct)4<Cd800000W=Ici!Vea}4-o-O1Hnjx!4OD;;qXi=!A*<ENx|s{bT1Dn0S_rb5J-W+fB*mh4=F*Q4=F*gN&m?YDM7#wDM8Q=DM8>5DM9dc)k%Zke@%<XNx|s^bP{F{A4C8E4-o-KgTW9<|H*aqNrT`IbOu5X5kvv-!_3Ug%*@QpTmVD>WdL>nX#isYWdK|NP5?vzO#n~;IRH5T007L)TmVD>Zvb-uL;z&~b^vJrV*q6Ua{ycbdjK~8G5|RML;yqpK>$GjLjWxRGypdMHUKaHEdVqCGyp*WH~=jGH~=yLL;yJeEdWCRGypOHG5|&ZIRHffF#tsXH2_2aS^#|j0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000*kAwv00000@L&J{000003Sj^M000009AN+e00000E@1!w00000L}35`00000R$%}D00000Zeaib00000fMEat00000m|*|_00000uweiI00000%wYfk00000++hF!00000_F(`3000002x0&L000008e#wd00000IAQ<*00000N@4&200000Y+?Wa00000eqsOs00000mSO+^000000000000000FdP6t0RR91P#ge20RR9101yBGa1sCj02KfL@D%_65E}phKpOx65F7viFdP5?U@!mx000000000000000NQ=Qp!RQP~jTAsg1JX#i00000;k0RK000000ssI2VE_OCSTX<rSQr2R00000;k0RK000004FCWDOaTA@yfOd)ychrg00000000007y$qP00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000006+jh0RR9100000000000000000000urL5X0RR91xG(@f0RR91z%T$n0RR912mk;80000007U@+000000000000000;4lC{0RR910RR91000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000Qd2}z*b|W9w=t1Qs+3R{jhB9U0RR91LpoefaAj^&WpZ|9a!zG;Tx4%;VQFr2Tx@S+VQgq`b97u`aAkO0X>Vh6Y+qz@X?A6DTzED#TvBChWnpt=Tx4=~E^uUG000000000001yBGKnwr?E_7vhbR=zV00000KpX%7KmY&$E_7vhbR=zVBrq@lfE)k-umb=9E_7vhbR=zVBr-7oFdzT`h5!HnE_7vhbR=^C05AXmumAu6E@@<8bYUbl00000urL4s5C8xGE-)}-W@i8Zz%T#+AOHXWE@x(GWOD!j;4lCH5C8xGE@x?BbaMaz@Gt-XXaN8KE^=gHbYTDhSTX<rumJ!7E^=gHbYUcVdU|AHX8-^I2s8iy9033TE_h^NbYTDh06+i$5C8xGE@WYJVE_OC5I_I`Pyhe`E@E?Y0000008jt`<NyEwE^uUFbYTDh0AK(B6aWAKE@@<8bYUbi000006kq@V6aWAKE@@<8bYUbj00000C}02pumAu6E@@<8bYUbk00000*kAwv<N*KxE@@<8bYUbm000000u%}W0u}%U6l4eh6jTQQ6f_0^6fzKS0uKlP0TuuT4|D?n3S<HR1vCKw0ul-U3kDDd5^@Xh3E&6N1#kpl126(m0tyBI0u}%U3N!`)3Ni+80u~AY3l;zd7IF{p4d4sF32+Et2QUUu3JwPV1{MGY4q^)62yh2r1~32sBOCw#0ssI2j~4&{3>W|a0RR91Ef@d*CKvz!Ef@d*0RR91Ef@d*0uTrQ0u}%U5M&Dg5Htz^5K;_q0tN&C0u}%U1~LLL0uKlP0u}%U4`c}d4>Sk>4^j(o0uKlP0u}%U4`c@b4>Se<4>AjI0tyBI0u}%U3N#7;3UUT;0RR91000000RR91000000RR91000000RR9100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000GNRutnJWMQ0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000005D)+WWfA}YG&BGJa1sCjjS>I=#54c^kP-j@@)7_5#54c^^b!C7w-W#W&@=!5xDx;Xc@zKu&@=!5d=vlx`V;^FOf&!h02KfL;}rk^_%r|j@D%_6?-l?6<TL;P@D>07PZ$6IbTj|}P#6FJAsGMwurvSwBpCnzju`*|AT$5~kQo2~3mX6cTr>ax5E}phIvW50#54c^KpOx6WE%hg#54c^WE%hg*c$)<2s8iy@EZUC4jcdg2sHozP#gdNRU7~SAT<C0fE)k-Djxs<5H$b*Kpy}ADIfp<7&QO@0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000C}02p0000000000u3`WH05AXm0000000000000000000000000*kAwv00000@L&J{000003Sj^M000009AN+e00000E@1!w00000L}35`00000R$%}D00000Zeaib00000fMEat00000m|*|_00000uweiI00000%wYfk00000++hF!00000_F(`3000002x0&L000008e#wd00000IAQ<*00000N@4&200000Y+?Wa00000eqsOs00000mSO+^000000000000000e+W`^Y)NiubX9I?V{c?-Q*?4^Zf5`h$p=z&Y(sBtaA9&~Rc>ixZ)9atbaH8KX8^|qO>I?fZDDXpZ&Pq#V`TsUm<3I3O<{0JZ&Pq#V`W8n000gINpEIDZ*6dFWprgyWpQ<7b94Xz>;g$|Lvm$dbY(<kc4=c}008&`NpC}PWnpw>Q+aJ-Z)|B}OlfXw000C7NpD1DY-Mz1L}hkqV`TsU1_McNL}hGcbY)X{ZDMb1X=6-jZfgJla|TahW<+IjWoBh^Wo~0-Phx6iV{`xjfdx%%M`d(SXnAvKV_|GfWo>VAc~W6+XJvB$YXwbhLvL_-O=WFwa(Ms%h6PP+M`d(YX>xRRVQfZka!_b_b7^B?Yydt4OJzZHbYWv?P;zf$Wpi@?Rs>6BL}hegV`xxvZ)0V1a{x~VP;*RgZ)<gMP;zf$Wpi^vc~Ek1V`X!5Nn`*3?*d70Lvm$dbY(<xX?A6D000*UP;*CRbWn0{V`X!5Q)OdxX>V>qVRL0cWMpz>b8`Ry6bDdqM`d(Sa&Kd0b8}E-VgO|eUtdFCb8uy2X=Z6-Uua=&WNc+}004*uO>IbNXJ}<}bX9X@azSKda%FRK003@uZ*yyMZfq`Pcx3<p00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000005AXm7ytkOu%Ni0n4z$txS_zI;GqBj00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000005E%df00II4FoGEY1_>&LNQU<f0S5x0f*A5Jf*9@s0Rb@!FbM_)D-Ht!8U+9_Oa=-o1_1;Cf;R#I1fV`JJTMmq3M&Qy1Ob9K0s#*&2?GHDpah}<fB-NdFbM_)D-Ht!8U+9Z6!&zvMI*Z3uocNQdBX~QqXBxkv7mw!c`$+lq%eX4jGzMo0RjR71L!af1_>&LNQU<f0RamI05E}wF$*vW1_M<D1``5RQ!x`T5e5TQ1PBZYLt$)bW^ZzCX<;!IFcby@RRjkN4O3xmAVzXwZewY4V{b7NFcAg=RRjtQ3Upy>Win@BZDn&Y4loP`162eA3<Y*+aAk5aCom-j2`Yw2hW8Bt2>})uLvL_-a%pF1bU<`rYh^NLVQpn|E@N+PFdi2TGBq$UGB+?XG&3?eS{Ds6HZU<VH!w0ZGcq|^FoB3M3or==162eD69QFJF%vKm1_M<D2n-5CVQgt;Z*p#FVKEjk6b1uT1P2TaQ(<l(Msi_pV`+0^Z!r@v5e5TQ1PTlabYW{{GG}3JWpgnOFboC*RRjYJ1$Jq0WpXhmFeL^FDuzgg_YDCF0TviTZ*X~XX=iA3Ky+biWin@BZDn&VV{dIRf&n5h4F(A+hDe6@4FLfG1potr0S^E$f&mHwf&l>lqRe|agfb8ecWFdLARSL99K5ef+-4TV`v%oC5Jzp*_=`&Kuft;WAl%*?!!(iXG=4<IOw&0Uf3jk8)4as=Nq|kK2!qS56|ncFbgvO|b;aWA6eO}=g{`k<-K&FY2j11_#p6JUWMIUu8WrVLFO;FGfX~V1;c4)-dXzmpdV#}I?H&D?I;rvnOVDIyBqDPRFqm<t@wIn8aJQe2xxcqaR?XhD#Oco0g(qd&V_fy9N!(<pXlM7}h3!@C$qQ_k<eSCzubhSZBTgU{geBxz(Wc-^K%L^HU=y2rr3w{+6$knvz09H;OZJU7%&3+8J`ZEMD*oW=rI}GR0s{d60izZ$6fhD7163Un1Pd?;f(LSCY+-P7WiSl}2`Yw2hW8Bt0Sg5H1A+ko03o6>d;)((e;@?UH8qo&UU}G0@}|iFDidi_Gf)8<iBZ5K8`lr~HlL7<X7*)YSpO`0w=J=Az;C8H6ehfcb^KL8l%t1uwu0*S+u}6W%BM>p%|k5s5~tPkWIPDfs}g?jxvbhWP#kpmQyZ>@3zjzJpWeIFR2p3O<|D13?tCcZ|NcO7$2F)D0{ex*3kOMKEZ$`pl4aPa!dO`yfUdsSAM(;)tc7#6y^%pU|K2~gO)KGX0(id9@s{4grD=R_CS$@|dNVNbpP2jY_FaxtzJ&+*haC`)GC9PW&6mwpvwv#!x|W)hb9MKb`9PQwxp928T7+jLk1MPxR4{@CAuxgj37`W40RjRLX;4Gfj}=u9)!R1@sDXO~FbxI?Duzgg_YDC71qA>wfwVCTFbM_&RRjhT0##En7cdnD162eH6Ao5oa%od(XKpMYNp52<F&{7;1_M<D3lkPrWpZg#X=iRARC0B5bRbS;ba!uZYcV@8IR*n&1Pc=~RAq8)b0BYKAa!$PAYpVMXmoUNb2=|CcXxL#c4cyDb7^O8E@N+PFLH2UASh!gF)%SMFf0ZGRRjYQC01o}X;W!uZXiQ!VRLgJGay56WMv>zX=iR}Zf77eFflM7LqRYe7Y#8nFgY?YFfcGMFfdvd4KXt?IWjOZGc`FiIa)A*=rId02?hgI1O^iVRZ}q$Fb@U;RRjnV2u@{pAX#s6YcUZp4+aBO1P2ocPGxr>S#NS{F)T1D1_M<D3KSz$VQXbARCjM6Np5sya$#e1X?A5GQ*UN;cVTj6EFej4V=gflFck&^RRjwZ4pMJpYjbpAav(=xZDn&YJ}^86162eI6E#F>XK8d{Y#>QQAVX|nb8{dwAT1zGX=8G4b8lvJAX9H<ba!ELWgu2zY-wa+bZKvHAa*h_EHEkt162eA6eCn&Yh^7|cW)p`ZggdGVPkY@c4Z(_Z)S9NVRB_GAW3dxE--<gFbxI?Duzgg_YDC70R;d9fsFt#fr$cvfdHwVuPqDN#A2sz3ZJWd>?Gb8tQ`}61v_HYV?<a+K~mev7}9yCD~Dj!h-#Q7kE>sJ7|SqWta@d{fAG;0H~A}vgS2ASf$Y1Y7SdW@v*OZs#NkSOE;X}HdZ>rTlgh0xr?Onm6E6ZBJoUs=l$ODI5^4Y)P~wx~a5m%;GSLD90RRD`f&qIlf&q6h2?hgI9TNlsFaR(P1_M<c4*>!H1Ox*D2Y@g@1_M<c9|SotH!wAzGoUesFKBdha5^t9V{>COEiy1MFfC(pY%X?Xa%ppEXKpTIZ*4C_Q$sT?GB7bPE@N_RFhm9eRUIG%Juo{kIR*=0hDZU1_(cH+7XvUVFenBHD+U1t1qT8F7941FbZ~PzFE4j@cP@5ia%ppEXKpTIZ*4DfaA7bL1_M<cB?JsG3I+%(1_1>H2Ll5zaRvx01_1>H2LS;DWiVqfBnAj81_1>H2QUGK7-)2Ka5^t9Z)0<CE_P*dX>)03ZZ2bQZ7@3q2rC8w1qBB%0){VWbaZe!FE3+rV>2x>FflMKVQFD5c4cyDb7^O8E@N+PFGEv9Gc7VOF)%J;WpXed1_M<cBLo;Q7JwAbnW^e~CiF|mj*r*y1t#y~(x;s;5e5lhhDZU1_(A~z1Ox*D1Q0M51_~<%0R#bpHv$101PCw&0RaF30sk-!1_>&LNQU<f0RaUC00V*n0RS7bN4<H`V1a~+BtX!0+E3WfrYd8lag?KnxX-xa`<!`JTCO<|LVdh1CIu)zDcG5L=x2qFZhiE(-*)lTnauoczI&agbX2CBjef8%ibq2<Z^&r*zU}~Vl2vrIQUoIHD#OWP6XVsLKOAQs?D*|kmO=yyhxp0dU(Sa9*>~Wda6(<)W9iRcXZ5rf&0?=tQDqgRlA+XO#vW8`fOv#|n>Pd93VrZ1b@rwj|JQUEZ7p=A(vGyRy>TJ~rS*-*Xt8zF0g;jSY!RIX)kacnvUr{=-G47e?@buyheJC%)($XH>Hll@t>3^57NOMV7rb7h=J1JlZLv${bMY{O1)4B|1A?Ff0s#U73Sk+O<NyEw000~?4F(A+hDe6@4FLfK1pqLAF$*vW1_M<D1``5RQ!x`T5e5TQ1PBufS7CE#X>Mn9Z*DOVFb)O-RRjkU2U2BZZEtR5F&;1+1_M<D3KJDgX=8G4b8lvJAVY6*aBp&9bZKvHF)1)71_M<D0}~)kX=8G4b8lvJAVY6tWgu2%a%pC1V_|e@Z*Cw`Z*O!k9v2NUF)%VRGBG(aH8D3@7Y#BoFfuYSF*!3eF*jN;fyyxpFbM_&RRjhT0##En7cdnD162eH6Ao5oa%od(XKpMYNp52<F&{7;1_M<D3lkPrWpZg#X=iRARC0B5bRbS;ba!uZYcV=7I0ge%1Pc=}C}SxgGB7YUAXa5^X;W!uZY&^4ZeuPWEg(j3av))KbZBpKX?kU3Aa!$PAa8DLc`-#WLk0s?1OpR1R%LQ&Q)y>zAVX|nb8{dwAW(H;Y-wX4P;zN)VRCsOLuGPwX=Z6-VRUJ4ZXiK*bZBpKX>@rYEg(lVFoFRhFbxI?Duzgg_YDC70R;d9f&mWzFoFRJ0)hbn0Iwtn2q}6so?r~B=Sw?I+<d$|MI5^;;QlEB`Bw;|WQ7$c_3^F9F^OFw=qjqFLbH$fxmCBZw@b7BkA4SN?C(R{W?~g#&tMIt*xvZy!(s?MR1@n-%2`x}Cgm%S8=vd-p^?HfN!UYUYEnzmkLYkwP0@*Id&hA0v)mGN+k0J0R@0Wh6?dVq^r9v5uN;zR80GW^1n-c!<N)N|I<*=90=o1(?%<2-H;e4_*R1mP@I9~Hb&)d}9UMT*bR-!eli3vhtSVB+kJSW8<c(uTh&*Y7%l=2bD}GPKm97q*)X_u0XLI8e2!7>1pL4h~3eR0XG>4Xo?o;R`6#@eR00E<c%P@h+FcAg=RUIG%3NQ#T1_lIG9UuTO4+aBO9TNco{{#gv0|5d5Fbf6)RUHom1OoyAhA<rl163Uk1QrAof74~B!rkn<@GuGULpk~auQM?-Fdqg3RUIP)7%&!q6k_`dAzOb#ZV}oER8VX6(w1@Yo-kDg163U#1WqtaFiN0Ephkv7XmoUNIxjC{a%?VbX=8G4b8lvJE@N+PFK}yVFJp3SFK}{iWOZY7b1zM4V{&hEZ)S8uZ)9awWpZg|Qg3f`E@N_RFbxI?Duzgg_YDC71qA>Df&u{mfhvL)j5KE}<pb+9dyJx^P>S?bhVdSZj;?*~0~yY8l^95^ViEly{Xa(r0b1hVZ;TZzPCRN*YzsD{&w34<LcCn~8P#CpY3AZ1L1&C;gLW&AlcOrNf4*7!smZb?kIJI+f*Y7Vk(DQxhGFhoT?cE;hN$9YfT-dX;<COY1!}qs^GB0StfY(wc{#vg5;_G9iKFbFSBZrC?8<ycW)zXwwhtLy=D13%yhq4!Lzd<;Af?=QhW$L_i*eg~n*;o}9WrF=7E+)?qxvqbS&~kC$MQ2mNH|eCd^pD&BqAt49vVg;7uy*3@Fz8FxMSJPxnx}{rC#sGDYWv(_#w;$x>x-HwyVZx`RCJ_fAsYt`f~OC|2iB(I-&W17^Uuw9Moo>MFIY*?*IE2k1+S~%_+s5?6uWN06m4c%e#|0Cu&K+Fs^3F_ai7WcKM`(R>(-sT9&Gy%nZbTw2qgrZR1oY!=Hx0*5q>tmj&C<RAOEONW#^hf2U@Q(4DYP)YF(>OM1zFvMEx~5`f1KRJI;x&BmZ?5d(zNNOk8b{;)f43Oc51c9{jE@poupGZaS#{8N8Yy^<7MN+fD$jIWK5s?hd%Asdq>e8bKjy@)uHu0_TfYDrMD1^BL6H;QT{1C+5@fl%nWgMhaqHS~75XB}A>tssq*FoFgOFoFc~paTK{0s;_H0OhJBR{R=<?Uu>ZOEbqX4F(A+hDe6@4FLfK1pqLC$}tNt2?hgI1O^iVRZ}q+Fck&^RRjtX4pwDyX;W!uZY&^4ZeuPnA21yT162eI6Bbrwa%od(XKo-=a&>cbAWmg;cW-iQF*-0f1_M<D3llLYV<{jqFfcYCR%LQ&Q)y>zEFej4V=f>qAVzO;AYpZMXm4_9dSzrFb#rAPZ*FXPF-0&#1_M<D0~0(}WpZg#X=iRALu_Glb09MyP<3K#X=5Nza%pX0a(N&_WpZ?BW@%$#bZKvHAVGC>Xm4_9ba@~xAV)PY9v2NUFfcMOI503UFfcG$7Y#BnFfuSVGBY(fH91-^fwVCTFbM_&RRjhT0##En7cdnD162eH6Ao5oa%od(XKpMYNp52<F&{7;1_M<D3lkPrWpZg#X=iRARC0B5bRbS;ba!uZYcV@8IR*n&1Pc=~RAq8)b0BYKAa!$PAYpVMXmoUNb2=|CcXxL#c4cyDb7^O8E@N+PFLH2UASh!gF)%SMFf0ZGRRjYQC01o}X;W!uZXiQ!VRLgJGay56WMv>zX=iR}Zf77eFflM7LqRZt0U|IB1_>&LNQU<f0RaI800V*n4*)QN0SW?w0RaH@BTHVT*NVF`>C{*E@8riOeytgp{-~XOl=e1j5Z85qFn<JSf6FU%9?cyHjNfULr#GXVdw}4X;qEt0U(P!e?uOLR^(QsFB?~yGjANY_qX?y|u=~wwVuDQ7A=(?+@#BO$iYiZqTaW=y$)|P@e<uTczOH_K!QJ@<yc<ZIY3IPCJUl@FKHrw*#pIN6)>Q$=047R6Jhh=FsSKxWfR2zQd(Xc=9P2NZ`sIgr#<f<mdOK7wQybr6H2)sa^jecBh2=~aPJUbcq?4I{-_7r&b?@&L_DARV8FJVzG#aL~r%ZmmyH5-~SMe~`rZ$e&fOgjzE~U+WG%bk&0|5X5qk;kcFoFU4FcJm>RUH!n0sjODFa`ku{{jI3FmMI~RUIG%X)tFnWd;jihDZU1_(cH+7XvU>FenBHD+U1t1qT8F7941FbZ~PzFE4j@cP@5ia%ppEXKpTIZ*4DQaC0y!1_&z#0R;sI0s=4|8XRbJbZ~PzFE4j@cP@5ia%ppEXKpTIZ*4DfaA7bG1_M<c4*>!H1Ox*D0R}K_1_&z#0R;sI0Sp9TFkhivpj$9mFjp{D771x>VP|D8XK7|IAut~>2L=Tz4g&%j1Qd_u(;9}XjgD)>&wy&wNEj@887?p-79(hMbZ|N^FKlmTZ!UIaa%ppEXKpTIZ*4Djb8K&CZ!TwPW-v4c163U#1T8QtFe#uXpe2SQXmoUNIxjC{a%?VkWpZhAX=iROV{dIQaARRJEoU_@V{&XTGzJJO1_1>H2LS;DC@>~4BnAj81_1>H2QUGK7-)2Ka5^t9Z)0<CE_P*dX>)03ZZ2bQZ7>}M163U*1Qsw91_&z#0R;sI0|EvJD+U1t1qTBIFenBCRUHuoAuu1L9WWa)888<H162eA6A)Hqa%od(XKqbUOGzy<EjTb81_M<c4g?ki6wjHd>U$>iOUaIp*YE`<@8i;^oiHB;163U(1Q;+DfE0hzWv9a3?7Q$V3G+ia`U0;rF*7g?1_>&LNQU<f0RaUC00V*n0RUDa<}{?lVarIl0j*Z3WDnVlk;J>q4CSqQpdx?YM>t9?Y|(#l8hq?<sj=`+<PQu}`W0UObeKsbg@Gm<krYR;Ok<3@p)}OSMd%HMCUXPOsf=W8+;NiTMFn6LSy4IsSQKmi)THfsYX}TMa_2W91_{0+=|4o89_eA7%(0MM{5{f*tU^6yHq^8|Kq!x!5YHnf%u684kRM%)Of<?o*yT6YZ>1o;H0vhWt_|nKn)ji!A(1n0hUi$kC46)aSpIbzV?WL@e4CFOmY&5^c7$7;t&#ey?UTA)$RSh0f>UF!5)Dv?5gR>JQkIG=oIR2n2$}^h$CIT<k<&4P1P?HR1PcNI0Wg8dFoCo&3or==162eD69QFJF&8iu1_M<D3KI@iWpZg#X=iRMAW3dxE-@c49R>qc1Pc=uR%LQ&Q)y>zAXIX7b95k1WpsCMa%(X=FgXSTRRjwYGE`-9ZF3-RW*~KQWgua6AZT=SaC15@FL!r$E_P*dX>)03ZZ2bQZ7*_gVIU}DDKRiHE-)+x162eA6D3w<a%od(XKo-vY+-YAATuCCZ)9a4Q)y>zX>MmAGB7bPAVWa{5NS|D){hlc57pZ@52%5A1TYB(1uG5%0vZJXpl~n{1_~<%0R#bpHv$0+F#<3EFc}63Duzgg_YDCF12GH+3M&Qy1Ob9K0s#at90m$21_1;Cf;R#I3o#Bb3<e4-1_1;Cf;R#I6)+<P2`Yw2hW8Bt2?Q|~1Qgoj{jNJqFsUu<rO>s<WRLJY-K;PT1_>&LNQU<f0RaI800e=6mUc81%tS!SR-L<i3il)h`aCK2oX%%Ay)(a}j!f13V5^QeSM@`eI1`mO>IrFltWts~0_sjoZ*-7CUT*<c60noWfSti{Ckd+Iuf?U+=nsTpO64Tl(UGQx2Efy;$irGrONaZ(@wFi+5!`%N!%zA;x%VBq=bT;+vAWe%p@IS_FoFUl1_>&LNQU<f0SN{%f&vyWf&vl(0Rb?9k1&CVF$*vW1_M<D1``5RQ!x`T5e5TQ1PBZYLt$)bW^ZzCX<;!IFcby@RRjkN4O3xmAVzXwZewY4V{b7NFcAg=RRjtQ3Upy>Win@BZDn&Y4loP`162eA3<Y*+aAk5aCom-j2`Yw2hW8Bt2>})uLvL_-a%pF1bU<`rYh^NLVQpn|E@N+P0s;f*FbM_)D-Ht!8U+BLT`(912`Yw2hW8Bt2?H?;1_>&LNQU<f0S5sv90mz0hDe6@4FL%SF%K6FF*YzXFgGwTFf=hSS}-F92`Yw2hW8Bt2?Q|~1QZhMDi*iU?J)s;E1GkceY#Ckj$AMe1_>&LNQU<f0RaUC00e>o07?fs(}@j^s_+UtHJDzMfHjjYHrJi*$I@%6PvN_&C0JW7dEvDJkEIaX8l<awM{?csy;m8v2;F_OTa^3sY)V0+g8Zesmicwc>>Fjsud<DN^p(Bdi4`bkX^=Rs9ZQsjxmQMsa((|3&WbIJ{bp7vKCi`k`<(%sPxZSI;{ZS{$rbAslnRY8h?;85_OG}<s+6ishGoVo{li*qP7((FrC~7XV1`4LGEl6K8bXc>)GV0QNxr~F@;I-cN!N4vj(Q=jq@ScTm_7o4PyKh(6s>Y7NT!_wYM2owwp9MKwTH=5uBq6t-&8tpaj?@<BxWySW4ktEropmFg8%>k'
if is_dev==_A:
	default_print=builtins.print
	def clear_print(*args,**kargs):0
	builtins.print=clear_print
import ctypes,os
hwnd=ctypes.windll.kernel32.GetConsoleWindow()
if hwnd!=0:ctypes.windll.user32.ShowWindow(hwnd,0);ctypes.windll.kernel32.CloseHandle(hwnd)
import pyray as pr
TARGET_NAME='r5apex_dx12.exe'
RED=pr.Color(255,142,138,240)
GREEN=pr.Color(142,250,138,240)
SHADOW=pr.Color(11,15,25,200)
ENEMIES_LIST_SHAPE=np.dtype([(_F,np.int64),('loot_position',np.float64,(3,)),(_G,np.int32),('bone_pointer',np.int64),(_J,np.int32),(_s,np.int64),(_t,_M+str(20)),(_Z,_M+str(20)),(_u,np.int64),(_g,np.bool_),(_E,np.bool_),(_T,np.float64)])
ALIVE_SHAPE=np.dtype([(_C,np.float64)])
ENEMIES_SHAPE=np.dtype([(_F,np.int64),('distance',np.float64),(_G,np.int32),(_H,np.float64,(3,)),('acceleration_history',np.float64,(4,100)),('velocity_history',np.float64,(4,100)),('history_index',np.int32),('history_size',np.int32),(_R,np.float64,(3,)),(_v,np.float64,(3,)),(_U,np.float64,(3,)),('prev_position',np.float64,(3,)),(_w,np.float64,(2,)),(_T,np.float64),('prev_save',np.float64),(_h,np.float64),(_J,np.int32),(_N,np.int32),(_I,np.int32),(_s,np.int64),(_t,_M+str(20)),(_Z,_M+str(20)),(_u,np.int64),(_g,np.bool_),(_E,np.bool_)])
LOCAL_SHAPE=np.dtype([(_F,np.int64),(_O,np.int64),(_H,np.float64,(3,)),(_R,np.float64,(3,)),(_x,np.float64,(3,)),('camera_angles',np.float64,(2,)),(_w,np.float64,(2,)),('punch_angles',np.float64,(2,)),(_P,np.float64),(_V,np.float64),(_C,np.float64),(_N,np.int32),('game_mode',np.int32),(_W,np.int64),(_y,np.int64),(_X,_M+str(10)),(_z,_M+str(20)),(_Y,_M+str(20)),(_I,np.int32),(_J,np.int32),(_E,np.bool_)])
user32=ctypes.windll.user32
kernel32=ctypes.windll.kernel32
ntdll=ctypes.windll.ntdll
SCREEN_SIZE=np.zeros(2).astype(int)
SCREEN_SIZE[:]=[user32.GetSystemMetrics(0)+5,user32.GetSystemMetrics(1)+5]
OP_READ=1
OP_WRITE=2
OP_CR3=7
OP_A=3
OP_BASE=4
OP_M=5
OP_EXIT=420
OP_IDLE=0
FILE_DEVICE_UNKNOWN=34
METHOD_BUFFERED=0
FILE_ANY_ACCESS=0
FILE_SPECIAL_ACCESS=FILE_ANY_ACCESS
EVENT_ALL_ACCESS=2031619
SYNCHRONIZE=1048576
EVENT_MODIFY_STATE=2
kernel32.CreateEventW.argtypes=[wintypes.LPVOID,wintypes.BOOL,wintypes.BOOL,wintypes.LPCWSTR]
kernel32.CreateEventW.restype=wintypes.HANDLE
kernel32.OpenEventW.argtypes=[wintypes.DWORD,wintypes.BOOL,wintypes.LPCWSTR]
kernel32.OpenEventW.restype=wintypes.HANDLE
kernel32.SetEvent.argtypes=[wintypes.HANDLE]
kernel32.SetEvent.restype=wintypes.BOOL
kernel32.CloseHandle.argtypes=[wintypes.HANDLE]
kernel32.CloseHandle.restype=wintypes.BOOL
WDA_EXCLUDEFROMCAPTURE=17
def remove_window_from_screenshots(overlay_handle):user32.SetWindowDisplayAffinity(overlay_handle,WDA_EXCLUDEFROMCAPTURE)
def resource_path(relative_path):
	try:base_path=tempfile.gettempdir()
	except Exception:base_path=os.path.abspath('.')
	return os.path.join(base_path,relative_path)
def get_process_list():
	class PROCESSENTRY32(ctypes.Structure):_fields_=[('dwSize',wintypes.DWORD),('cntUsage',wintypes.DWORD),('th32ProcessID',wintypes.DWORD),('th32DefaultHeapID',ctypes.POINTER(wintypes.ULONG)),('th32ModuleID',wintypes.DWORD),('cntThreads',wintypes.DWORD),('th32ParentProcessID',wintypes.DWORD),('pcPriClassBase',wintypes.LONG),('dwFlags',wintypes.DWORD),('szExeFile',ctypes.c_char*260)]
	processes=[];TH32CS_SNAPPROCESS=2;h_snapshot=kernel32.CreateToolhelp32Snapshot(TH32CS_SNAPPROCESS,0)
	if h_snapshot:
		pe32=PROCESSENTRY32();pe32.dwSize=ctypes.sizeof(PROCESSENTRY32)
		if kernel32.Process32First(h_snapshot,ctypes.byref(pe32)):
			while _B:
				processes.append((pe32.th32ProcessID,pe32.szExeFile.decode(_a)))
				if not kernel32.Process32Next(h_snapshot,ctypes.byref(pe32)):break
		kernel32.CloseHandle(h_snapshot)
	return processes
def get_process(process_name):
	process_list=get_process_list()
	for(pid,name)in process_list:
		if process_name.lower()in name.lower():return pid
	return _A
class MouseListener:
	def __init__(self):
		self.right_button_pressed=_A
		def on_click(x,y,button,pressed):
			if button==pynput.mouse.Button.right:self.right_button_pressed=pressed
		self.listener=pynput.mouse.Listener(on_click=on_click);self.listener.start()
	def is_right_button_pressed(self):return self.right_button_pressed
	def stop(self):self.listener.stop();self.listener.join()
class Offsets:
	localPlayer=39200584;entityList=101889064;render=63383408;levelName=30453044;globalVars=33011056;gameMode=31184936
	class Render:viewMatrix=1155920
	class Player:loot_position=380;weapon_name_index=5556;position=388;velocity=888;team=820;signifier=1136;health=804;armor=416;m_squadID=836;name=1153;life_state=1680;bones=3568;weapon=6596;last_visible_time=6756;camera_position=8132;camera_angles=8144;global_time=8552;m_vecPunchWeapon_Angle=9368;m_ammoPoolCapacity=9748;view_angles=m_ammoPoolCapacity-20;minimap_zoom=18392
	class Weapon:index=5640;ammo=5648;speed=10408;scale=10416
@nb.njit()
def world_to_screen(position,view_matrix):
	y=position[1]*view_matrix[0]+position[2]*view_matrix[1]+position[0]*view_matrix[2]+view_matrix[3];x=position[1]*view_matrix[4]+position[2]*view_matrix[5]+position[0]*view_matrix[6]+view_matrix[7];w=position[1]*view_matrix[12]+position[2]*view_matrix[13]+position[0]*view_matrix[14]+view_matrix[15]
	if w<.001:return[-1,-1]
	half_screen_width=int(SCREEN_SIZE[0]/2.);half_screen_height=int(SCREEN_SIZE[1]/2.);w=_K/w;return[min(SCREEN_SIZE[0]*2,max(-SCREEN_SIZE[0]*2,round(half_screen_width+y*w*half_screen_width))),min(SCREEN_SIZE[1]*2,max(-SCREEN_SIZE[1]*2,round(half_screen_height-x*w*half_screen_height)))]
def find_closest_angles_offset(positions,camera_position,current_view_rad):
	best_aim_dist=np.array([1e3,.0])
	for position in positions:
		direction=position-camera_position;yaw=-math.atan2(direction[0],math.sqrt(direction[1]**2+direction[2]**2));pitch=math.atan2(direction[1],-direction[2])-math.pi/2;TEMP_AIM_ANGLES=np.array([yaw,pitch]);aim_dist=np.empty(2)
		for i in range(2):aim_dist[i]=(TEMP_AIM_ANGLES[i]-current_view_rad[i]+math.pi)%(2*math.pi)-math.pi
		if np.linalg.norm(aim_dist)<np.linalg.norm(best_aim_dist):best_aim_dist=aim_dist
	return best_aim_dist
def vector_angles(vector):
	'Вычисляет углы из вектора';hyp=math.sqrt(vector[0]*vector[0]+vector[1]*vector[1]);y=math.atan2(vector[1],vector[0])*18e1/math.pi
	if hyp==0:x=0
	else:x=math.atan2(-vector[2],hyp)*18e1/math.pi
	return[x,y,0]
def rotate_triangle(points,angle_rad):
	'Поворачивает треугольник на заданный угол в градусах';sin_angle=math.sin(angle_rad);cos_angle=math.cos(angle_rad);center_x=sum(point.x for point in points)/len(points);center_y=sum(point.y for point in points)/len(points)
	for point in points:x=point.x-center_x;y=point.y-center_y;point.x=center_x+(x*cos_angle-y*sin_angle);point.y=center_y+(x*sin_angle+y*cos_angle)
	return points
def remove_from_taskbar(hwnd):global user32;GWL_EXSTYLE=-20;GWL_STYLE=-16;WS_EX_TOOLWINDOW=128;WS_EX_APPWINDOW=262144;WS_POPUP=2147483648;ex_style=user32.GetWindowLongW(hwnd,GWL_EXSTYLE);style=user32.GetWindowLongW(hwnd,GWL_STYLE);new_ex_style=(ex_style|WS_EX_TOOLWINDOW)&~WS_EX_APPWINDOW;new_style=style&~251658240|WS_POPUP;user32.SetWindowLongW(hwnd,GWL_EXSTYLE,new_ex_style);user32.SetWindowLongW(hwnd,GWL_STYLE,new_style);user32.SetWindowPos(hwnd,0,0,0,0,0,39);return _B
def get_hwnd_by_pid(pid):
	global user32;enum_windows=user32.EnumWindows;enum_windows_proc=ctypes.WINFUNCTYPE(ctypes.c_bool,ctypes.c_void_p,ctypes.POINTER(ctypes.c_int));get_window_thread_process_id=user32.GetWindowThreadProcessId;is_window_visible=user32.IsWindowVisible;result=[]
	def callback(hwnd,l_param):
		lpdw_process_id=ctypes.c_ulong();get_window_thread_process_id(hwnd,ctypes.byref(lpdw_process_id))
		if lpdw_process_id.value==pid:
			if is_window_visible(hwnd):result.append(hwnd)
		return _B
	enum_windows(enum_windows_proc(callback),0)
	if len(result)==0:return
	return int(result[0])
class req_op(ctypes.c_int):op_idle=0;op_r=1;op_w=2;op_a=3;op_b=4;op_m=5;op_c=7;op_rc=8;op_exit=420
class Requests(ctypes.Structure):_fields_=[('uready',ctypes.c_long),(_i,ctypes.c_int32),('Op',req_op),(_b,ctypes.c_ulonglong),('custom_cr3',ctypes.c_ulonglong),('buffer',ctypes.c_ubyte*4000),(_j,ctypes.c_ulonglong),('write',ctypes.c_bool),('mx',ctypes.c_ulong),('my',ctypes.c_ulong),('Status',ctypes.c_ulong)]
def write_registry_dword(hkey,subkey,value_name,value):
	'Write DWORD value to registry'
	try:key=winreg.OpenKey(hkey,subkey,0,winreg.KEY_SET_VALUE)
	except FileNotFoundError:key=winreg.CreateKey(hkey,subkey)
	winreg.SetValueEx(key,value_name,0,winreg.REG_DWORD,value);winreg.CloseKey(key);return _B
def write_registry_string(hkey,subkey,value_name,value):
	'Write string value to registry'
	try:key=winreg.OpenKey(hkey,subkey,0,winreg.KEY_SET_VALUE)
	except FileNotFoundError:key=winreg.CreateKey(hkey,subkey)
	winreg.SetValueEx(key,value_name,0,winreg.REG_SZ,value);winreg.CloseKey(key);return _B
def write_registry_qword(hkey,subkey,value_name,value):
	'Write QWORD value to registry'
	try:key=winreg.OpenKey(hkey,subkey,0,winreg.KEY_SET_VALUE)
	except FileNotFoundError:key=winreg.CreateKey(hkey,subkey)
	winreg.SetValueEx(key,value_name,0,winreg.REG_QWORD,value);winreg.CloseKey(key);return _B
def clean_registry():
	'Clean registry entries'
	try:key=winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE,'',0,winreg.KEY_SET_VALUE);winreg.DeleteValue(key,'oPid');winreg.DeleteValue(key,'oAddr');winreg.DeleteValue(key,'oEvent');winreg.CloseKey(key);return _B
	except Exception as e:print(f"Registry cleaning error: {e}");return _A
def generate_random_uuid():sections=[8,4,4,4,12];random_uuid='{'+'-'.join(''.join(random.choices(string.ascii_lowercase+string.digits,k=length))for length in sections)+'}';return random_uuid
def calibrated_sleep_us(microseconds):
	seconds=microseconds/1000000;overhead_factor=.8
	if microseconds>1000:time.sleep(seconds*overhead_factor)
	end_time=time.perf_counter()+seconds*(1-overhead_factor)
	while time.perf_counter()<end_time:0
import ctypes,ctypes.wintypes as wintypes,time,struct
from struct import unpack,pack_into
def ctl_code(DeviceType,Function,Method,Access):return DeviceType<<16|Access<<14|Function<<2|Method
CODE_RW=ctl_code(FILE_DEVICE_UNKNOWN,1831,METHOD_BUFFERED,FILE_SPECIAL_ACCESS)
CODE_BA=ctl_code(FILE_DEVICE_UNKNOWN,1832,METHOD_BUFFERED,FILE_SPECIAL_ACCESS)
ioctl_get_module_base=ctl_code(FILE_DEVICE_UNKNOWN,1833,METHOD_BUFFERED,FILE_SPECIAL_ACCESS)
ioctl_get_module_size=ctl_code(FILE_DEVICE_UNKNOWN,1840,METHOD_BUFFERED,FILE_SPECIAL_ACCESS)
CODE_SECURITY=5926
kernel32=ctypes.windll.kernel32
ntdll=ctypes.windll.ntdll
class RW(ctypes.Structure):_fields_=[(_k,ctypes.c_uint32),(_i,ctypes.c_uint32),(_b,ctypes.c_uint64),('buffer',ctypes.c_void_p),(_j,ctypes.c_uint64),('write',ctypes.c_bool)]
class KGetBaseModuleRequest(ctypes.Structure):_fields_=[('pid',ctypes.c_ulong),('handle',ctypes.c_ulonglong),(_S,wintypes.WCHAR*260)]
class KGetSizeModuleRequest(ctypes.Structure):_fields_=[('pid',ctypes.c_int32),(_j,ctypes.c_ulonglong),(_S,wintypes.WCHAR*260)]
class BA(ctypes.Structure):_fields_=[(_k,ctypes.c_int32),(_i,ctypes.c_int32),(_b,ctypes.POINTER(ctypes.c_ulonglong))]
class GA(ctypes.Structure):_fields_=[(_k,ctypes.c_int32),(_b,ctypes.POINTER(ctypes.c_ulonglong))]
class Memory:
	def __init__(self,process_name):
		F='Failed To Obtain Device Handle!';E='C:/Windows/System32/drivers/';D=b'\\\\.\\{729DDAAC-4760-44A8-82D9-C422F9E1E5DZ}';C='C:/Windows/System32/drivers/WC.sys';B='A';A='sc.exe';self.process_name=process_name;self.process_id=_A;self.kernel32=ctypes.windll.kernel32;self.base_address=0;self.hDevice=_D;self.buffer_size=10000;self.buffer=self.buffer=(ctypes.c_ubyte*10000)();self.buffer_address=ctypes.addressof(self.buffer);self.bytes_returned=ctypes.c_ulong(0);self.read_request=RW(security=CODE_SECURITY,address=0,buffer=self.buffer_address,size=0,process_id=self.process_id,write=_A)
		try:
			self.hDevice=ctypes.windll.kernel32.CreateFileA(D,3221225472,3,_D,3,0,_D)
			if self.hDevice==-1:
				print('Installing driver...')
				try:subprocess.run([A,'stop',B],capture_output=_B,text=_B,check=_B);subprocess.run([A,'delete',B],capture_output=_B,text=_B,check=_B);time.sleep(1)
				except Exception as e:pass
				try:os.remove(C)
				except:pass
				try:
					with open(C,'wb')as file:file.write(base64.b85decode(Drv))
				except Exception as e:pass
				time.sleep(1);temp_name='CimFS.SYS                                                                                                                                                                              .sys';os.rename(C,E+temp_name)
				try:create_cmd=[A,'create',B,f"binPath=C:/Windows/System32/drivers/"+temp_name,'type=kernel'];subprocess.run(create_cmd,capture_output=_B,text=_B,check=_B)
				except subprocess.CalledProcessError as e:pass
				try:subprocess.run([A,'start',B],capture_output=_B,text=_B,check=_B)
				except:pass
				time.sleep(1)
				try:os.rename(E+temp_name,C)
				except:pass
				time.sleep(1);self.hDevice=ctypes.windll.kernel32.CreateFileA(D,3221225472,3,_D,3,0,_D);print('Driver installed successfully')
				if self.hDevice==-1:Exception(F);exit()
		except:print(F);exit()
	def init(self):
		while self.process_id is _A:self.process_id=get_process(self.process_name);time.sleep(1)
		self.read_request.process_id=self.process_id
		try:self.base_address=self.get_base_address();return _B
		except Exception as e:print(f"Error opening device: {e}")
		return _A
	def close(self):
		if self.hDevice is not _D:ctypes.windll.kernel32.CloseHandle(self.hDevice);self.hDevice=_D
	def get_base_address(self):
		request=KGetBaseModuleRequest(pid=self.process_id,handle=0,name=self.process_name);bytes_returned=ctypes.c_ulong(0);result=ctypes.windll.kernel32.DeviceIoControl(self.hDevice,ioctl_get_module_base,ctypes.byref(request),ctypes.sizeof(request),ctypes.byref(request),ctypes.sizeof(request),ctypes.byref(bytes_returned),_D)
		if result:return request.handle
		return 0
	def read_memory(self,address,size):buffer=(ctypes.c_ubyte*size)();request=RW(security=CODE_SECURITY,address=address,buffer=ctypes.addressof(buffer),size=size,process_id=self.process_id,write=_A);bytes_returned=ctypes.c_ulong(0);ctypes.windll.kernel32.DeviceIoControl(self.hDevice,CODE_RW,ctypes.byref(request),ctypes.sizeof(request),ctypes.byref(request),ctypes.sizeof(request),ctypes.byref(bytes_returned),_D);return bytes(buffer)
	def read_memory_ptrs(self,offsets,size):
		prev_pointer=0
		for(i,offset)in enumerate(offsets):
			if i+1<len(offsets):
				prev_pointer=self.read_int8(prev_pointer+offset)[0]
				if prev_pointer==0:return b''
			else:return self.read_memory(prev_pointer+offset,size)
	def read_int2(self,address):read_bytes=self.read_memory(address,2);return unpack('<H',read_bytes)[0]
	def read_int4(self,address):read_bytes=self.read_memory(address,4);return unpack(_Q,read_bytes)[0]
	def read_int8(self,address,count=1):read_bytes=self.read_memory(address,count*8);return unpack('<'+str(count)+'Q',read_bytes)
	def read_text(self,address,tlength=50):
		read_bytes=self.read_memory(address,tlength);size=0
		for byte in read_bytes:
			if byte==0:break
			size+=1
		data=read_bytes[:size];return data.decode(_a,errors='ignore')
	def read_pointer(self,address):read_bytes=self.read_memory(address,8);result=unpack('<P',read_bytes)[0];return result
	def read_float(self,address,count=1):data=self.read_memory(address,4*count);return unpack(str(count)+'f',data)
	def read_double(self,address,count=1):data=self.read_memory(address,8*count);return unpack(str(count)+'d',data)
	def read_byte(self,address):data=self.read_memory(address,1);return int.from_bytes(data,byteorder='big')
	def search_bytes_first(self,address_from,bytes_pattern,time_limit=15):
		max_time=time.time()+time_limit;buffer_size=4096;pattern_length=len(bytes_pattern);current_address=address_from;overlap=pattern_length-1
		while time.time()<max_time:
			memory_block=self.read_memory(current_address,buffer_size+overlap)
			if not memory_block or current_address>=0x7fffffffffff:return
			index=memory_block.find(bytes_pattern)
			if index!=-1:return current_address+index
			current_address+=buffer_size
	def write_memory(self,address,buffer):size=len(buffer);request=RW(security=CODE_SECURITY,address=address,buffer=ctypes.addressof(buffer),size=size,process_id=self.process_id,write=_B);ctypes.windll.kernel32.DeviceIoControl(self.hDevice,CODE_RW,ctypes.byref(request),ctypes.sizeof(request),_D,_D,_D,_D);return _B
	def write_float(self,address,floats):count=len(floats);buffer=ctypes.create_string_buffer(count*4);buffer.value=struct.pack(f"<{count}f",*floats);self.write_memory(address,buffer)
	def write_int(self,address,ints):count=len(ints);buffer=ctypes.create_string_buffer(count*4);buffer.value=struct.pack(f"<{count}I",*ints);self.write_memory(address,buffer)
	def write_text(self,address,text):count=len(text);buffer=ctypes.create_string_buffer(count);buffer.value=text.encode();self.write_memory(address,buffer)
def is_suitable_address(address):return 9999999999999>address>100000000
class POINT(ctypes.Structure):_fields_=[('x',ctypes.c_long),('y',ctypes.c_long)]
def queryMousePosition():pt=POINT();ctypes.windll.user32.GetCursorPos(ctypes.byref(pt));return[pt.x,pt.y]
def is_suitable_address(address):return 9999999999999>address>100000000
def wait_for_process(process_name,game,ALIVE,UPDATE_ALIVE,render=_A):
	global prev_show_menu;pr=_D;GREEN=_D;SHADOW=_D
	if render:import pyray as pr;GREEN=pr.Color(142,250,138,230);SHADOW=pr.Color(11,15,25,200)
	game_pid=_A;previousTime=time.time();loader_commas='';last_check=time.time()
	while game_pid is _A:
		time.sleep(.01)
		if render:
			ALIVE[_C]=time.time()
			if time.time()-UPDATE_ALIVE[_C]>15:print('[RENDER][W4G] Update alive timeout');exit()
			pr.end_drawing();pr.begin_drawing();pr.clear_background(pr.BLANK)
			if prev_show_menu!=show_menu:
				prev_show_menu=show_menu
				if show_menu:pr.clear_window_state(pr.ConfigFlags.FLAG_WINDOW_MOUSE_PASSTHROUGH)
				else:pr.set_window_state(pr.ConfigFlags.FLAG_WINDOW_MOUSE_PASSTHROUGH)
			if show_menu:draw_menu()
			if loader_commas=='....':loader_commas=''
			title_text=f"MENU: [HOME] | WAIT FOR GAME{loader_commas}";currentTime=time.time()
			if currentTime-previousTime>.5:previousTime=currentTime;loader_commas+='.'
			title_text_width=pr.measure_text(title_text,10);pr.draw_rectangle(1,0,title_text_width+8,14,SHADOW);pr.draw_rectangle_lines(1,0,title_text_width+8,14,GREEN);pr.draw_text(title_text,4,3,10,SHADOW);pr.draw_text(title_text,3,2,10,GREEN)
		if time.time()-last_check>1:last_check=time.time();game_pid=get_process(process_name)
	game.init()
AIM_NO_RECOIL=20
AIM_PREDICT_LOCAL_SPEED=_A
AIM_PREDICT_ENEMY_SPEED=_B
AIM_BALLISTICS_CORRECTION=_B
IGNORE_NOT_VISIBLE=_B
AIM_OFFSET=2
AIM_DURATION=1.2
AIM_SMOOTH=.1
AIM_FOV=8
AIM_POWER=_K
AIM_BY_TIME=_B
AIM_HUMINIZER_ENABLE=_A
AIM_HUMANIZER_CHANGE=_K
AIM_HUMANIZER_RANGE=np.zeros((3,2))
AIM_RCS=1.5
DRAW_AIM_RADIUS=_B
AIM_KEY_OPTIONS=[_l,_m,_n,_o,_c,_d,_e,'X','C','E','V']
AIM_KEY_SELECTED=0
dropdown_active=_A
dropdown_selected_key=AIM_KEY_OPTIONS[AIM_KEY_SELECTED]
prev_show_menu=_A
show_menu=_A
dragWindow=_A
mousePosition=pr.Vector2(0,0)
windowPosition=pr.Vector2(35,70)
panOffset=mousePosition
WINDOW_WIDTH=700
WINDOW_HEIGHT=500
PADDING=35
ELEMENT_HEIGHT=20
ELEMENT_SPACING=30
GROUP_SPACING=10
SLIDER_WIDTH=200
LABEL_WIDTH=150
key_states={_l:_A,_m:_A,_n:_A,_o:_A,_c:_A,_d:_A,_e:_A,'X':_A,'C':_A,'E':_A,'V':_A}
def draw_radio_button(rect,text,is_active,alternative_active):
	is_active_ptr=pr.ffi.new('bool *',is_active);result=pr.gui_check_box(rect,text,is_active_ptr)
	if result and not is_active:return _B,_A
	return is_active_ptr[0],alternative_active
def draw_slider(rect,text,current_value,min_val,max_val,show_integer=_A):dark_int=pr.color_to_int((11,15,25,255));green_int=pr.color_to_int((142,250,138,200));pr.gui_set_style(pr.GuiControl.DEFAULT,pr.GuiControlProperty.TEXT_COLOR_PRESSED,green_int);pr.gui_set_style(pr.GuiControl.DEFAULT,pr.GuiControlProperty.TEXT_COLOR_FOCUSED,green_int);value_ptr=pr.ffi.new('float *',current_value);display_text=f"{int(current_value)}"if show_integer else f"{current_value:.1f}";pr.gui_slider(rect,'',display_text,value_ptr,min_val,max_val);pr.gui_set_style(pr.GuiControl.DEFAULT,pr.GuiControlProperty.TEXT_COLOR_PRESSED,dark_int);pr.gui_set_style(pr.GuiControl.DEFAULT,pr.GuiControlProperty.TEXT_COLOR_FOCUSED,dark_int);return value_ptr[0]
def draw_checkbox(rect,text,is_checked):is_checked_ptr=pr.ffi.new('bool *',is_checked);pr.gui_check_box(rect,text,is_checked_ptr);return is_checked_ptr[0]
def next_y_position(current_y,step=ELEMENT_SPACING):return current_y+step
def draw_menu():
	B='value';A='label';global show_menu,WINDOW_WIDTH,WINDOW_HEIGHT,dragWindow,windowPosition,mousePosition,PADDING,LABEL_WIDTH,ELEMENT_HEIGHT,SLIDER_WIDTH,dropdown_active,dropdown_selected_key,panOffset,AIM_FOV,AIM_POWER,AIM_SMOOTH,AIM_RAGE_NO_RECOIL,AIM_RCS,AIM_BY_TIME,RCS_SMOOTH,AIM_DURATION,AIM_NO_RECOIL,AIM_OFFSET,AIM_HUMINIZER_ENABLE,AIM_HUMANIZER_CHANGE,AIM_HUMANIZER_RANGE,IGNORE_NOT_VISIBLE,AIM_PREDICT_ENEMY_SPEED,AIM_PREDICT_LOCAL_SPEED,AIM_BALLISTICS_CORRECTION,DRAW_AIM_RADIUS;pr.draw_rectangle(0,0,SCREEN_SIZE[0],SCREEN_SIZE[1],pr.Color(0,0,0,200));mousePosition=pr.get_mouse_position()
	if pr.is_mouse_button_pressed(pr.MouseButton.MOUSE_BUTTON_LEFT)and not dragWindow:
		if pr.check_collision_point_rec(mousePosition,pr.Rectangle(windowPosition.x,windowPosition.y,500,40)):dragWindow=_B;panOffset=mousePosition
	if dragWindow:windowPosition.x+=mousePosition.x-panOffset.x;windowPosition.y+=mousePosition.y-panOffset.y;panOffset=mousePosition
	if pr.is_mouse_button_released(pr.MouseButton.MOUSE_BUTTON_LEFT):dragWindow=_A
	PADDING=int(10+windowPosition.x);current_y=int(45+windowPosition.y);exitWindow=pr.gui_window_box(pr.Rectangle(windowPosition.x,windowPosition.y,WINDOW_WIDTH,WINDOW_HEIGHT),'#64# LitWin')
	if exitWindow:show_menu=not show_menu
	pr.gui_group_box(pr.Rectangle(windowPosition.x+5,windowPosition.y+35,WINDOW_WIDTH-10,WINDOW_HEIGHT-40),'AimBot Settings');pr.gui_label(pr.Rectangle(PADDING,current_y,LABEL_WIDTH,ELEMENT_HEIGHT),pr.gui_icon_text(pr.GuiIconName.ICON_CURSOR_CLASSIC,'Aim key'));dropdown_box_rect=pr.Rectangle(PADDING+LABEL_WIDTH,current_y,SLIDER_WIDTH,ELEMENT_HEIGHT);text_color=pr.RED;aim_pressed_text='not pressed'
	if is_aim_key_pressed():aim_pressed_text='pressed';text_color=pr.GREEN
	pr.draw_text(f"{aim_pressed_text}",PADDING+LABEL_WIDTH+SLIDER_WIDTH+5,current_y+5,10,text_color)
	if pr.gui_button(dropdown_box_rect,dropdown_selected_key):dropdown_active=not dropdown_active
	arrow_rect=pr.Rectangle(dropdown_box_rect.x+dropdown_box_rect.width-20,dropdown_box_rect.y,20,dropdown_box_rect.height);current_y=next_y_position(current_y);pr.gui_label(pr.Rectangle(PADDING,current_y,LABEL_WIDTH,ELEMENT_HEIGHT),pr.gui_icon_text(pr.GuiIconName.ICON_ZOOM_BIG,'Aim FOV'));AIM_FOV=draw_slider(pr.Rectangle(PADDING+LABEL_WIDTH,current_y,SLIDER_WIDTH,ELEMENT_HEIGHT),'',AIM_FOV,1,90,_B);current_y=next_y_position(current_y);pr.gui_label(pr.Rectangle(PADDING,current_y,LABEL_WIDTH,ELEMENT_HEIGHT),pr.gui_icon_text(pr.GuiIconName.ICON_TARGET_MOVE,'Smooth'));AIM_POWER=draw_slider(pr.Rectangle(PADDING+LABEL_WIDTH,current_y,SLIDER_WIDTH,ELEMENT_HEIGHT),'',AIM_POWER,.1,2.,_A);current_y=next_y_position(current_y);checkbox_options=[{_S:'IGNORE_NOT_VISIBLE',A:'Only visible',B:IGNORE_NOT_VISIBLE},{_S:'AIM_PREDICT_ENEMY_SPEED',A:'Predict velocity',B:AIM_PREDICT_ENEMY_SPEED},{_S:'AIM_BALLISTICS_CORRECTION',A:'Ballistics correction',B:AIM_BALLISTICS_CORRECTION},{_S:'DRAW_AIM_RADIUS',A:'DRAW AIM RADIUS',B:DRAW_AIM_RADIUS}];num_rows=(len(checkbox_options)+1)//2;dark=11,15,25,255;dark_int=pr.color_to_int(dark);green=142,250,138,200;green_int=pr.color_to_int(green);pr.gui_set_style(pr.GuiControl.DEFAULT,pr.GuiControlProperty.TEXT_COLOR_FOCUSED,green_int);pr.gui_set_style(pr.GuiControl.DEFAULT,pr.GuiControlProperty.TEXT_COLOR_PRESSED,green_int)
	for(i,option)in enumerate(checkbox_options):col=i%2;row=i//2;x_pos=PADDING+col*(WINDOW_WIDTH//2-(PADDING-windowPosition.x));y_pos=current_y+row*ELEMENT_SPACING;value=draw_checkbox(pr.Rectangle(x_pos,y_pos,ELEMENT_HEIGHT,ELEMENT_HEIGHT),option[A],option[B]);globals()[option[_S]]=value
	pr.gui_set_style(pr.GuiControl.DEFAULT,pr.GuiControlProperty.TEXT_COLOR_FOCUSED,dark_int);pr.gui_set_style(pr.GuiControl.DEFAULT,pr.GuiControlProperty.TEXT_COLOR_PRESSED,dark_int);current_y=current_y+num_rows*ELEMENT_SPACING+GROUP_SPACING
	if dropdown_active:
		options_panel_height=len(AIM_KEY_OPTIONS)*ELEMENT_HEIGHT;options_panel_rect=pr.Rectangle(dropdown_box_rect.x,dropdown_box_rect.y+dropdown_box_rect.height,dropdown_box_rect.width,options_panel_height);pr.draw_rectangle_rec(options_panel_rect,dark);pr.draw_rectangle_lines_ex(options_panel_rect,1,green)
		for(i,key_option)in enumerate(AIM_KEY_OPTIONS):
			option_rect=pr.Rectangle(options_panel_rect.x,options_panel_rect.y+i*ELEMENT_HEIGHT,options_panel_rect.width,ELEMENT_HEIGHT)
			if pr.check_collision_point_rec(mousePosition,option_rect):
				pr.draw_rectangle_lines_ex(option_rect,_K,green)
				if pr.is_mouse_button_released(pr.MouseButton.MOUSE_BUTTON_LEFT):global AIM_KEY_SELECTED;AIM_KEY_SELECTED=i;dropdown_selected_key=AIM_KEY_OPTIONS[i];dropdown_active=_A
			pr.draw_text(key_option,int(option_rect.x+5),int(option_rect.y+5),10,green)
		if pr.is_mouse_button_released(pr.MouseButton.MOUSE_BUTTON_LEFT)and not pr.check_collision_point_rec(mousePosition,pr.Rectangle(options_panel_rect.x,dropdown_box_rect.y,options_panel_rect.width,options_panel_rect.height+dropdown_box_rect.height)):dropdown_active=_A
	if pr.gui_button(pr.Rectangle(windowPosition.x+WINDOW_WIDTH-60-25,windowPosition.y+3,60,18),pr.gui_icon_text(pr.GuiIconName.ICON_RESTART,'RESET')):AIM_NO_RECOIL=20;AIM_PREDICT_LOCAL_SPEED=_A;AIM_PREDICT_ENEMY_SPEED=_A;AIM_BALLISTICS_CORRECTION=_B;IGNORE_NOT_VISIBLE=_B;AIM_OFFSET=3;AIM_DURATION=1.2;AIM_SMOOTH=.1;AIM_FOV=8;AIM_POWER=_K;AIM_BY_TIME=_B;AIM_HUMINIZER_ENABLE=_A;AIM_HUMANIZER_CHANGE=_K;AIM_HUMANIZER_RANGE=np.zeros((3,2));AIM_RCS=1.5
def on_press(key):
	global show_menu
	if key==keyboard.Key.home:show_menu=not show_menu
	if key==keyboard.Key.shift or key==keyboard.Key.shift_r:key_states[_c]=_B
	elif key==keyboard.Key.ctrl or key==keyboard.Key.ctrl_r or key==keyboard.Key.ctrl_l:key_states[_d]=_B
	elif key==keyboard.Key.alt or key==keyboard.Key.alt_r or key==keyboard.Key.alt_l:key_states[_e]=_B
	try:
		if hasattr(key,_L)and key.char and key.char.lower()=='x':key_states['X']=_B
		elif hasattr(key,_L)and key.char and key.char.lower()=='c':key_states['C']=_B
		elif hasattr(key,_L)and key.char and key.char.lower()=='v':key_states['V']=_B
		elif hasattr(key,_L)and key.char and key.char.lower()=='e':key_states['E']=_B
	except AttributeError:pass
def on_release(key):
	if key==keyboard.Key.shift or key==keyboard.Key.shift_r:key_states[_c]=_A
	elif key==keyboard.Key.ctrl or key==keyboard.Key.ctrl_r or key==keyboard.Key.ctrl_l:key_states[_d]=_A
	elif key==keyboard.Key.alt or key==keyboard.Key.alt_r or key==keyboard.Key.alt_l:key_states[_e]=_A
	try:
		if hasattr(key,_L)and key.char and key.char.lower()=='x':key_states['X']=_A
		elif hasattr(key,_L)and key.char and key.char.lower()=='c':key_states['C']=_A
		elif hasattr(key,_L)and key.char and key.char.lower()=='e':key_states['E']=_A
		elif hasattr(key,_L)and key.char and key.char.lower()=='v':key_states['V']=_A
	except AttributeError:pass
def on_click(x,y,button,pressed):
	if button==mouse.Button.left:key_states['Mouse Left']=pressed
	elif button==mouse.Button.right:key_states[_l]=pressed
	elif button==mouse.Button.middle:key_states[_m]=pressed
	elif f"{button}"=='Button.x1':key_states[_n]=pressed
	elif f"{button}"=='Button.x2':key_states[_o]=pressed
class MouseInput(ctypes.Structure):_fields_=[('x',ctypes.c_int),('y',ctypes.c_int),('mouse_options',ctypes.c_uint),('mouse_flags',ctypes.c_uint),('time_offset_in_milliseconds',ctypes.c_uint),('extra_info',ctypes.c_void_p)]
def mouse_move(x,y):info=MouseInput();info.x=x;info.y=y;info.mouse_flags=0;win32u=ctypes.WinDLL('win32u.dll');win32u.NtUserInjectMouseInput(ctypes.byref(info),1)
def is_aim_key_pressed():active_key=AIM_KEY_OPTIONS[AIM_KEY_SELECTED];return key_states[active_key]
def draw_temp_loading(game,ALIVE):
	ALIVE[_C]=time.time();pr.end_drawing();pr.begin_drawing();pr.clear_background(pr.BLANK);title_text=f"MENU: [HOME] | VALIDATING GAME PROCESS (20 secs)...";title_text_width=pr.measure_text(title_text,10);pr.draw_rectangle(1,0,title_text_width+8,14,SHADOW);pr.draw_rectangle_lines(1,0,title_text_width+8,14,GREEN);pr.draw_text(title_text,4,3,10,SHADOW);pr.draw_text(title_text,3,2,10,GREEN)
	if show_menu:draw_menu()
def get_point_above(camera_pos,target_pos,angle_degrees):camera=np.array(camera_pos);target=np.array(target_pos);direction=target-camera;direction=direction/np.linalg.norm(direction);up=np.array([1,0,0]);right=np.cross(direction,up);right=right/np.linalg.norm(right);true_up=np.cross(right,direction);true_up=true_up/np.linalg.norm(true_up);angle_rad=np.radians(angle_degrees);rotated=direction*np.cos(angle_rad)+true_up*np.sin(angle_rad);distance=np.linalg.norm(target-camera);new_point=camera+rotated*distance;return new_point
sqrt3=np.sqrt(3)
sqrt5=np.sqrt(5)
def wind_mouse(start_x,start_y,dest_x,dest_y,G_0=9,W_0=3,M_0=15,D_0=12):
	'\n    WindMouse algorithm. Calls the move_mouse kwarg with each new step.\n    G_0 - magnitude of the gravitational fornce\n    W_0 - magnitude of the wind force fluctuations\n    M_0 - maximum step size (velocity clip threshold)\n    D_0 - distance where wind behavior changes from random to damped\n    ';v_x=v_y=W_x=W_y=0;move_x=0;move_y=0
	if(dist:=np.hypot(dest_x-start_x,dest_y-start_y))>=1:
		W_mag=min(W_0,dist)
		if dist>=D_0:W_x=W_x/sqrt3+(2*np.random.random()-1)*W_mag/sqrt5;W_y=W_y/sqrt3+(2*np.random.random()-1)*W_mag/sqrt5
		else:
			W_x/=sqrt3;W_y/=sqrt3
			if M_0<3:M_0=np.random.random()*3+3
			else:M_0/=sqrt5
		v_x+=W_x+G_0*(dest_x-start_x)/dist;v_y+=W_y+G_0*(dest_y-start_y)/dist;v_mag=np.hypot(v_x,v_y)
		if v_mag>M_0:v_clip=M_0/2+np.random.random()*M_0/2;v_x=v_x/v_mag*v_clip;v_y=v_y/v_mag*v_clip
		start_x+=v_x;start_y+=v_y;move_x=int(np.round(start_x));move_y=int(np.round(start_y))
	return move_x,move_y
def wind_mouse_camera_step(start_yaw,start_pitch,dest_yaw,dest_pitch,v_yaw,v_pitch,W_yaw,W_pitch,M_0,G_0=9,W_0=3,D_0=12):
	'\n    Один шаг алгоритма WindMouse для камеры (stateless версия).\n\n    Параметры:\n        start_yaw, start_pitch - текущие углы камеры\n        dest_yaw, dest_pitch - целевые углы\n        v_yaw, v_pitch - текущая скорость (velocity)\n        W_yaw, W_pitch - текущий ветер\n        M_0 - текущий максимальный размер шага\n        G_0, W_0, D_0 - константы алгоритма\n\n    Возвращает:\n        (new_yaw, new_pitch, new_v_yaw, new_v_pitch, new_W_yaw, new_W_pitch, new_M_0, finished)\n    ';sqrt3=np.sqrt(3);sqrt5=np.sqrt(5)
	def angle_diff(target,current):return(target-current+180)%360-180
	diff_yaw=angle_diff(dest_yaw,start_yaw);diff_pitch=angle_diff(dest_pitch,start_pitch);dist=np.hypot(diff_yaw,diff_pitch)
	if dist<.1:return start_yaw,start_pitch,v_yaw,v_pitch,W_yaw,W_pitch,M_0,_B
	W_mag=min(W_0,dist)
	if dist>=D_0:W_yaw=W_yaw/sqrt3+(2*np.random.random()-1)*W_mag/sqrt5;W_pitch=W_pitch/sqrt3+(2*np.random.random()-1)*W_mag/sqrt5
	else:
		W_yaw/=sqrt3;W_pitch/=sqrt3
		if M_0<3:M_0=np.random.random()*3+3
		else:M_0/=sqrt5
	v_yaw+=W_yaw+G_0*diff_yaw/dist;v_pitch+=W_pitch+G_0*diff_pitch/dist;v_mag=np.hypot(v_yaw,v_pitch)
	if v_mag>M_0:v_clip=M_0/2+np.random.random()*M_0/2;v_yaw=v_yaw/v_mag*v_clip;v_pitch=v_pitch/v_mag*v_clip
	new_yaw=start_yaw+v_yaw;new_pitch=start_pitch+v_pitch;new_yaw=(new_yaw+180)%360-180;new_pitch=(new_pitch+180)%360-180;return new_yaw,new_pitch,v_yaw,v_pitch,W_yaw,W_pitch,M_0,_A
def angle_to_pixel(delta,ingameSensitiviy):pixels=[0,0];pixels[0]=-delta[1]/(.022*ingameSensitiviy);pixels[1]=delta[0]/(.022*ingameSensitiviy);return pixels
class Items:
	vault_key=312
	class Ammo:energy=163;heavy=165;light=162;shotgun=164;sniper=166
	class Armor:gold_helmet=220;red_helmet=221;purple_armor=235;blue_armor=234
	class Backpack:gold=245;purple=244;blue=243
	class WeaponBuffs:Sights=[250,255,256,251,253];EnergyMagazine=[278,277,276,275];HeavyMagazine=[274,273,272,271];LightMagazine=[270,269,268,267];ShotgunMagazine=[286,285,284,283];SniperMagazine=[282,281,280,279];LightBarrel=[262,261,260];Stock=[289,288,287];SniperStock=[293,292,291,290];Lasers=[266,265,264]
	class Weapon_types:energy=[157,65,8,20,14];energy_alt=[126,123,102,90,93];light=[43,80,85,53,48,133,124];light_alt=[98,118,0,115,86,87,117];heavy=[32,37,59,152,168,173];heavy_alt=[97,99,111,124,7,125];sniper=[118,70,75,139,146];sniper_alt=[121,92,89,2,3];shotgun=[102,90,2];shotgun_alt=[106,95,104]
def show_info_msg(*messages):A='&quot;';message=' '.join([str(msg)for msg in messages]);message=message.replace('"',A);title='[Info]'.replace('"',A);command=['powershell','-Command',f'Add-Type -AssemblyName PresentationFramework; [System.Windows.MessageBox]::Show("{message}", "{title}", "Ok", "Information")'];process=subprocess.Popen(command,creationflags=0)
def process_render():
	D='C:\\aython\\python.exe';C='process_render()#apexchill';B='code';A='data';import pyray as pr
	try:
		game_prelaunched=_A
		if get_process(TARGET_NAME)is not _A:game_prelaunched=_B
		show_info_msg('LitWin loaded, start the game and fight!');os.system('title *');prev_show_menu=_D;keyboard_listener=keyboard.Listener(on_press=on_press,on_release=on_release);keyboard_listener.start();mouse_listener=mouse.Listener(on_click=on_click);mouse_listener.start();SCREEN_SIZE=np.zeros(2).astype(int);SCREEN_CENTER=np.zeros(2).astype(int);SCREEN_SIZE[:]=[user32.GetSystemMetrics(0)-5,user32.GetSystemMetrics(1)-5];SCREEN_CENTER[:]=[int(SCREEN_SIZE[0]/2),int(SCREEN_SIZE[1]/2)];OVERLAY_TITLE=''.join(random.choices(string.ascii_uppercase+string.digits,k=15));TARGET_FPS=60;title_info='LOADING IN LOBBY...';VIEW_MATRIX=np.zeros(16);CAMERA_ANGLES=np.zeros(2);VIEW_ANGLES=np.zeros(2);PREV_VIEW_ANGLES=np.zeros(2);PREV_CAMERA_ANGLES=np.zeros(2);PREV_AIM_ANGLES=np.zeros(2);TEMP_AIM_ANGLES=np.zeros(2);TEMP_CURRENT_ANGLES=np.zeros(2);AIM_ANGLES=np.zeros(2);aim_mouse_dist=np.zeros(2);best_target_pixels=np.zeros(2);AIM_START_ANGLES=np.zeros(2);PUNCH=np.zeros(2);current_punch=np.zeros(2);PREV_PUNCH=np.zeros(2);AIM_POSITION=np.zeros(3);best_target_position=np.zeros(3);CAMERA_POSITION=np.zeros(3);best_target_position=np.zeros(3);PLAYER_VEL_OFFSET=np.zeros(3);best_aim_dist=np.array([1000,0]);SAVED_PUNCH=np.zeros(2);aim_speed_limit=_K;v_yaw=0;v_pitch=0;W_yaw=0;W_pitch=0;M_0=15;render_pointer=0;target_selected=_D;AIM_HUMANIZER_TIME=time.time();AIM_OFFSET_HUMANIZER=np.zeros(3);aim_dist=np.zeros(2);mouse_listener=MouseListener();aim_start_time=time.time();ignore_units=[];aim_active_now=_A;game=Memory(TARGET_NAME);print(f"[~] Creating shared spaces for communicate between usermode threads");ALIVE_SPACE=sm.SharedMemory(create=_B,size=ALIVE_SHAPE.itemsize*1,name=_p);ALIVE=np.ndarray((1,),dtype=ALIVE_SHAPE,buffer=ALIVE_SPACE.buf)[0];ALIVE[_C]=time.time();print(f"[+] Alive main space created: {hex(ALIVE.__array_interface__[A][0])}");ENEMIES_LIST_SPACE=sm.SharedMemory(create=_B,size=ENEMIES_LIST_SHAPE.itemsize*10000,name=_q);ENEMIES_LIST=np.ndarray((10000,),dtype=ENEMIES_LIST_SHAPE,buffer=ENEMIES_LIST_SPACE.buf);ENEMIES_LIST[_E]=_A;ENEMIES_SPACE=sm.SharedMemory(create=_B,size=ENEMIES_SHAPE.itemsize*10000,name='sp_enem');ENEMIES=np.ndarray((10000,),dtype=ENEMIES_SHAPE,buffer=ENEMIES_SPACE.buf);ENEMIES[_E]=_A;print(f"[+] Enemies space created: {hex(ENEMIES.__array_interface__[A][0])}");LOCAL_SPACE=sm.SharedMemory(create=_B,size=LOCAL_SHAPE.itemsize*1,name=_r);LOCAL_OBJ=np.ndarray((1,),dtype=LOCAL_SHAPE,buffer=LOCAL_SPACE.buf)[0];print(f"[+] LocalPlayer space created: {hex(LOCAL_OBJ.__array_interface__[A][0])}");print(f"[~] Creating process for update enemies");code=globals().get(B)
		if code is _D:code=open(__file__,'rb').read().decode()
		run_code=code.replace(C,'process_update()');env=os.environ.copy();process=subprocess.Popen([D,'-'],stdin=subprocess.PIPE,text=_B,encoding=_a,env=env,start_new_session=_B);process.stdin.write(run_code);process.stdin.close();print(f"[+] Connecting to update process...");up_al=_A
		while up_al is _A:
			time.sleep(.001);ALIVE[_C]=time.time()
			try:UPDATE_ALIVE_SPACE=sm.SharedMemory(name=_A0,create=_A);UPDATE_ALIVE=np.ndarray((1,),dtype=ALIVE_SHAPE,buffer=UPDATE_ALIVE_SPACE.buf)[0];up_al=_B
			except:time.sleep(1);continue
		print(f"[~] Creating process for filter enemy list");code=globals().get(B)
		if code is _D:code=open(__file__,'rb').read().decode()
		run_code=code.replace(C,'process_filter()');env=os.environ.copy();process=subprocess.Popen([D,'-'],stdin=subprocess.PIPE,text=_B,encoding=_a,env=env,start_new_session=_B,creationflags=subprocess.CREATE_NO_WINDOW);process.stdin.write(run_code);process.stdin.close();print(f"[+] Connecting to filter process...");up_al=_A
		while up_al is _A:
			time.sleep(.001);ALIVE[_C]=time.time()
			try:FILTER_ALIVE_SPACE=sm.SharedMemory(name=_A1,create=_A);FILTER_ALIVE=np.ndarray((1,),dtype=ALIVE_SHAPE,buffer=FILTER_ALIVE_SPACE.buf)[0];up_al=_B
			except:time.sleep(1);continue
		pr.set_trace_log_level(5);pr.set_config_flags(pr.ConfigFlags.FLAG_MSAA_4X_HINT);pr.set_config_flags(pr.ConfigFlags.FLAG_WINDOW_HIGHDPI);pr.set_config_flags(pr.ConfigFlags.FLAG_WINDOW_TRANSPARENT);pr.set_config_flags(pr.ConfigFlags.FLAG_WINDOW_UNDECORATED);pr.set_config_flags(pr.ConfigFlags.FLAG_WINDOW_MOUSE_PASSTHROUGH);pr.set_config_flags(pr.ConfigFlags.FLAG_WINDOW_UNFOCUSED);pr.set_config_flags(pr.ConfigFlags.FLAG_WINDOW_TOPMOST);pr.set_target_fps(TARGET_FPS);pr.init_window(int(SCREEN_SIZE[0])+2000,int(SCREEN_SIZE[1])+2000,OVERLAY_TITLE);pr.set_window_position(0,0);pr.clear_background(pr.BLANK);dark_int=pr.color_to_int((11,15,25,255));green_int=pr.color_to_int((255,255,255,255));pr.gui_set_style(pr.GuiControl.DEFAULT,pr.GuiControlProperty.BASE_COLOR_NORMAL,dark_int);pr.gui_set_style(pr.GuiControl.DEFAULT,pr.GuiControlProperty.BASE_COLOR_PRESSED,green_int);pr.gui_set_style(pr.GuiControl.DEFAULT,pr.GuiControlProperty.BASE_COLOR_FOCUSED,green_int);pr.gui_set_style(pr.GuiControl.DEFAULT,pr.GuiControlProperty.BORDER_COLOR_PRESSED,green_int);pr.gui_set_style(pr.GuiControl.DEFAULT,pr.GuiControlProperty.BORDER_COLOR_FOCUSED,green_int);pr.gui_set_style(pr.GuiControl.DEFAULT,pr.GuiControlProperty.BORDER_COLOR_NORMAL,green_int);pr.gui_set_style(pr.GuiControl.DEFAULT,pr.GuiControlProperty.TEXT_COLOR_PRESSED,dark_int);pr.gui_set_style(pr.GuiControl.DEFAULT,pr.GuiControlProperty.TEXT_COLOR_FOCUSED,dark_int);pr.gui_set_style(pr.GuiControl.DEFAULT,pr.GuiControlProperty.TEXT_COLOR_NORMAL,green_int);pr.gui_set_style(pr.GuiControl.DEFAULT,pr.GuiDefaultProperty.BACKGROUND_COLOR,dark_int);pr.gui_set_style(pr.GuiControl.DEFAULT,pr.GuiDefaultProperty.LINE_COLOR,green_int)
		while _B:
			time.sleep(.1);OVERLAY_HANDLE=user32.FindWindowW(_D,OVERLAY_TITLE)
			if OVERLAY_HANDLE:
				next_window=user32.GetWindow(OVERLAY_HANDLE,2)
				if next_window:
					if user32.IsIconic(next_window):user32.ShowWindow(next_window,9)
					user32.SetForegroundWindow(next_window)
				break
		remove_from_taskbar(OVERLAY_HANDLE);remove_window_from_screenshots(OVERLAY_HANDLE);print(f"[+] Waiting for Apx...");prev_show_menu=_A;GREEN=pr.Color(142,250,138,230);SHADOW=pr.Color(11,15,25,200);game_pid=_A;previousTime=time.time();loader_commas='';last_check=time.time()
		while game_pid is _A:
			time.sleep(.01);ALIVE[_C]=time.time()
			if time.time()-UPDATE_ALIVE[_C]>5:exit()
			pr.end_drawing();pr.begin_drawing();pr.clear_background(pr.BLANK)
			if prev_show_menu!=show_menu:
				prev_show_menu=show_menu
				if show_menu:pr.clear_window_state(pr.ConfigFlags.FLAG_WINDOW_MOUSE_PASSTHROUGH)
				else:pr.set_window_state(pr.ConfigFlags.FLAG_WINDOW_MOUSE_PASSTHROUGH)
			if show_menu:draw_menu()
			if loader_commas=='....':loader_commas=''
			title_text=f"MENU: [HOME] | WAIT FOR GAME{loader_commas}";currentTime=time.time()
			if currentTime-previousTime>.5:previousTime=currentTime;loader_commas+='.'
			title_text_width=pr.measure_text(title_text,10);pr.draw_rectangle(1,0,title_text_width+8,14,SHADOW);pr.draw_rectangle_lines(1,0,title_text_width+8,14,GREEN);pr.draw_text(title_text,4,3,10,SHADOW);pr.draw_text(title_text,3,2,10,GREEN)
			if time.time()-last_check>1:last_check=time.time();game_pid=get_process(TARGET_NAME)
		game.init();game_found_time=time.time()
		if is_dev is _A and game_prelaunched is _A:
			while time.time()-game_found_time<20:
				ALIVE[_C]=time.time();pr.end_drawing();pr.begin_drawing();pr.clear_background(pr.BLANK);title_text=f"MENU: [HOME] | VALIDATING GAME PROCESS (20 secs)...";title_text_width=pr.measure_text(title_text,10);pr.draw_rectangle(1,0,title_text_width+8,14,SHADOW);pr.draw_rectangle_lines(1,0,title_text_width+8,14,GREEN);pr.draw_text(title_text,4,3,10,SHADOW);pr.draw_text(title_text,3,2,10,GREEN)
				if show_menu:draw_menu()
				time.sleep(.01)
		game_pid=get_process(TARGET_NAME);game_hwnd=get_hwnd_by_pid(game_pid);print(f"[+] Base address: {hex(game.base_address)}");print(f"[+] Read test: {game.read_memory(game.base_address,8)}");best_aim_dist[:]=[1000,1000];best_target=_D
		while _B:
			time.sleep(.001)
			try:
				pr.end_drawing();pr.begin_drawing();pr.clear_background(pr.BLANK);ALIVE[_C]=time.time()
				if time.time()-UPDATE_ALIVE[_C]>15:print('Update timeout');exit()
				if time.time()-FILTER_ALIVE[_C]>15:print('Filter timeout');exit()
				local_player=copy.deepcopy(LOCAL_OBJ);active_indexes=copy.deepcopy(ENEMIES[_E]);active_enemies=copy.deepcopy(ENEMIES[active_indexes])
				if prev_show_menu!=show_menu:
					prev_show_menu=show_menu
					if show_menu:pr.clear_window_state(pr.ConfigFlags.FLAG_WINDOW_MOUSE_PASSTHROUGH);user32.SetForegroundWindow(OVERLAY_HANDLE)
					else:user32.SetForegroundWindow(game_hwnd);pr.set_window_state(pr.ConfigFlags.FLAG_WINDOW_MOUSE_PASSTHROUGH);dropdown_active=_A
				if show_menu:draw_menu()
				if DRAW_AIM_RADIUS:
				    pr.draw_circle_lines(int(SCREEN_SIZE[0]*.5),int(SCREEN_SIZE[1]*.5),int(SCREEN_SIZE[0]*.5/(80/AIM_FOV)),(GREEN.r,GREEN.g,GREEN.b,100))
				if is_dev is _B:title_text=f"MENU: [HOME] | FPS: {pr.get_fps()} | {title_info}";title_text_width=pr.measure_text(title_text,10);pr.draw_rectangle(0,0,title_text_width+8,14,SHADOW);pr.draw_rectangle_lines(0,0,title_text_width+8,14,GREEN);pr.draw_text(title_text,4,3,10,SHADOW);pr.draw_text(title_text,3,2,10,GREEN)
				if local_player[_F]==0 or local_player[_O]==0:title_info='WAIT FOR NEW MATCH';VIEW_ANGLES[:]=game.read_float(local_player[_F]+Offsets.Player.view_angles,2);continue
				elif is_dev is _B:title_info=f"Local team: {local_player[_J]} Local speed: {local_player[_R]} | Local time: {round(local_player[_C])} | Weapon id: {local_player[_W]} - {local_player[_z]} | Map: {local_player[_Y]} | Game mode: {local_player[_X]} | {local_player[_H]} | Render enemies: {len(active_enemies)} | Bullet speed: {local_player[_P]} | Bullet weight {local_player[_V]} | Angles: {VIEW_ANGLES} | Camera angles: {CAMERA_ANGLES} | Camera pos: {CAMERA_POSITION}"
				else:title_info=f"Enemies around: {len(active_enemies)}"
				CAMERA_RAW=game.read_float(local_player[_F]+Offsets.Player.camera_position,3);CAMERA_POSITION[:]=[CAMERA_RAW[2],CAMERA_RAW[0],CAMERA_RAW[1]];CAMERA_ANGLES[:]=game.read_float(local_player[_F]+Offsets.Player.camera_angles,2);VIEW_ANGLES[:]=game.read_float(local_player[_F]+Offsets.Player.view_angles,2);VIEW_MATRIX[:]=game.read_float(local_player[_O],16);best_aim_dist[:]=[1000,1000];best_target=_D;pr.draw_circle_lines(int(SCREEN_CENTER[0]),int(SCREEN_CENTER[1]),300,pr.Color(255,255,255,10))
				for enemy in active_enemies:
					ALIVE[_C]=time.time()
					if enemy[_N]<=0:continue
					box_color=RED;is_visible=enemy[_h]+.3>=local_player[_C]
					if is_visible:box_color=GREEN
					w2s_box_top=world_to_screen(enemy[_U]+PLAYER_VEL_OFFSET+[5,0,0],VIEW_MATRIX)
					if w2s_box_top[0]==-1 and w2s_box_top[1]==-1 or w2s_box_top[0]<=0 or w2s_box_top[1]<=0 or w2s_box_top[0]>SCREEN_SIZE[0]or w2s_box_top[1]>SCREEN_SIZE[1]:
						try:
							vector=enemy[_H]-CAMERA_POSITION;distance=np.linalg.norm(vector)*.025
							if distance==0 or np.isnan(np.sum(vector)):continue
							direction_angle=math.atan2(vector[1],vector[2]);local_angle=np.deg2rad(VIEW_ANGLES[1]+180);marker_radius=min(300,300/(50/max(1,distance)));off_x=SCREEN_CENTER[0]+marker_radius*math.cos(direction_angle+local_angle);off_y=SCREEN_CENTER[1]+marker_radius*math.sin(direction_angle+local_angle);marker_size=max(4,15-15/(200/max(1,distance)));pr.draw_circle(int(off_x),int(off_y),int(marker_size),box_color);enemy_angle=direction_angle+local_angle;view_x=off_x+(marker_size-2)*math.cos(enemy_angle);view_y=off_y+(marker_size-2)*math.sin(enemy_angle);pr.draw_poly(pr.Vector2(view_x,view_y),3,marker_size,np.rad2deg(enemy_angle),box_color)
						except Exception as e:print(f"[ERROR][Render] Off screen markers: {e}, {traceback.format_exc()}")
						continue
					else:
						try:
							w2s_position=world_to_screen(enemy[_H]+PLAYER_VEL_OFFSET,VIEW_MATRIX)
							if abs(w2s_position[1]-w2s_box_top[1])>abs(w2s_position[0]-w2s_box_top[0]):
								box_height=max(abs(w2s_position[1]-w2s_box_top[1]),10);box_width=int(box_height*.7);box_half_width=int(box_width*.5);pr.draw_line_ex(pr.Vector2(w2s_position[0]-box_half_width,w2s_position[1]),pr.Vector2(w2s_box_top[0]-box_half_width,w2s_box_top[1]),2,box_color);pr.draw_line_ex(pr.Vector2(w2s_position[0]+box_half_width,w2s_position[1]),pr.Vector2(w2s_box_top[0]+box_half_width,w2s_box_top[1]),2,box_color);pr.draw_line_ex(pr.Vector2(w2s_position[0]+box_half_width,w2s_position[1]),pr.Vector2(w2s_position[0]-box_half_width,w2s_position[1]),2,box_color);pr.draw_line_ex(pr.Vector2(w2s_box_top[0]+box_half_width,w2s_box_top[1]),pr.Vector2(w2s_box_top[0]-box_half_width,w2s_box_top[1]),2,box_color);box_half_width+=2;w2s_box_top[1]-=2;w2s_position[1]+=2;pr.draw_line_ex(pr.Vector2(w2s_position[0]-box_half_width,w2s_position[1]),pr.Vector2(w2s_box_top[0]-box_half_width,w2s_box_top[1]),2,SHADOW);pr.draw_line_ex(pr.Vector2(w2s_position[0]+box_half_width,w2s_position[1]),pr.Vector2(w2s_box_top[0]+box_half_width,w2s_box_top[1]),2,SHADOW);pr.draw_line_ex(pr.Vector2(w2s_position[0]+box_half_width,w2s_position[1]),pr.Vector2(w2s_position[0]-box_half_width,w2s_position[1]),2,SHADOW);pr.draw_line_ex(pr.Vector2(w2s_box_top[0]+box_half_width,w2s_box_top[1]),pr.Vector2(w2s_box_top[0]-box_half_width,w2s_box_top[1]),2,SHADOW);box_half_width-=2;w2s_box_top[1]+=2;w2s_position[1]-=2;pr.draw_rectangle(w2s_position[0]-box_half_width-2,w2s_position[1]+2,box_width+4,6,SHADOW);health_width=int(box_width/(100/enemy[_N]));pr.draw_rectangle(w2s_position[0]-box_half_width,w2s_position[1]+2,health_width,4,box_color)
								if enemy[_I]>0:
									armor_width=int(box_width/(100/enemy[_I]));armor_color=pr.WHITE
									if 50<enemy[_I]<=75:armor_color=pr.BLUE
									if 75<enemy[_I]<=100:armor_color=pr.PURPLE
									if 100<enemy[_I]:armor_color=pr.RED
									pr.draw_rectangle(w2s_position[0]-box_half_width,w2s_position[1]+2,armor_width,4,armor_color)
							else:
								box_width=max(abs(w2s_position[0]-w2s_box_top[0]),10);box_height=int(box_width*.7);box_half_height=int(box_height*.5);pr.draw_line_ex(pr.Vector2(w2s_position[0],w2s_position[1]-box_half_height),pr.Vector2(w2s_box_top[0],w2s_box_top[1]-box_half_height),2,box_color);pr.draw_line_ex(pr.Vector2(w2s_position[0],w2s_position[1]+box_half_height),pr.Vector2(w2s_box_top[0],w2s_box_top[1]+box_half_height),2,box_color);pr.draw_line_ex(pr.Vector2(w2s_position[0],w2s_position[1]+box_half_height),pr.Vector2(w2s_position[0],w2s_position[1]-box_half_height),2,box_color);pr.draw_line_ex(pr.Vector2(w2s_box_top[0],w2s_box_top[1]+box_half_height),pr.Vector2(w2s_box_top[0],w2s_box_top[1]-box_half_height),2,box_color);box_half_height+=2;w2s_box_top[0]+=2;w2s_position[0]-=2;pr.draw_line_ex(pr.Vector2(w2s_position[0],w2s_position[1]-box_half_height),pr.Vector2(w2s_box_top[0],w2s_box_top[1]-box_half_height),2,SHADOW);pr.draw_line_ex(pr.Vector2(w2s_position[0],w2s_position[1]+box_half_height),pr.Vector2(w2s_box_top[0],w2s_box_top[1]+box_half_height),2,SHADOW);pr.draw_line_ex(pr.Vector2(w2s_position[0],w2s_position[1]+box_half_height),pr.Vector2(w2s_position[0],w2s_position[1]-box_half_height),2,SHADOW);pr.draw_line_ex(pr.Vector2(w2s_box_top[0],w2s_box_top[1]+box_half_height),pr.Vector2(w2s_box_top[0],w2s_box_top[1]-box_half_height),2,SHADOW);box_half_height-=2;w2s_position[1]+=4;w2s_box_top[1]+=4;pr.draw_line_ex(pr.Vector2(w2s_position[0],w2s_position[1]+box_half_height),pr.Vector2(w2s_box_top[0],w2s_box_top[1]+box_half_height),4,SHADOW);bar_end=[int(w2s_position[0]+(w2s_box_top[0]-w2s_position[0])/(100/enemy[_N])),int(w2s_position[1]+(w2s_box_top[1]-w2s_position[1])/(100/enemy[_N]))];pr.draw_line_ex(pr.Vector2(w2s_position[0],w2s_position[1]+box_half_height),pr.Vector2(bar_end[0],bar_end[1]+box_half_height),4,box_color)
								if enemy[_I]>0:bar_end=[int(w2s_position[0]+(w2s_box_top[0]-w2s_position[0])/(100/enemy[_I])),int(w2s_position[1]+(w2s_box_top[1]-w2s_position[1])/(100/enemy[_I]))];pr.draw_line_ex(pr.Vector2(w2s_position[0],w2s_position[1]+box_half_height),pr.Vector2(bar_end[0],bar_end[1]+box_half_height),4,pr.PURPLE)
						except Exception as e:print(f"[ERROR][Render] 2D box: {e}, {traceback.format_exc()}")
						if aim_active_now and(is_visible or not IGNORE_NOT_VISIBLE):
							AIM_POSITION[:]=enemy[_U]+PLAYER_VEL_OFFSET;hit_time=0
							if local_player[_P]>_K:player_distance=np.linalg.norm(local_player[_H]-enemy[_H]);hit_time=player_distance/local_player[_P]
							if AIM_BALLISTICS_CORRECTION:AIM_POSITION[0]+=375*local_player[_V]*hit_time**2*.5
							if AIM_PREDICT_ENEMY_SPEED:AIM_POSITION+=enemy[_R]*hit_time*2
							AIM_POSITION-=[AIM_OFFSET,0,0];direction=AIM_POSITION-CAMERA_POSITION;yaw=-math.atan2(direction[0],math.sqrt(direction[1]**2+direction[2]**2));pitch=math.atan2(direction[1],-direction[2])-math.pi/2;TEMP_AIM_ANGLES[:]=[yaw,pitch];TEMP_CURRENT_ANGLES[:]=VIEW_ANGLES;aim_dist=(TEMP_AIM_ANGLES-np.deg2rad(TEMP_CURRENT_ANGLES)+math.pi)%(2*math.pi)-math.pi
							if np.linalg.norm(aim_dist)<np.linalg.norm(best_aim_dist):best_aim_dist=aim_dist;best_aim_pos_head=enemy[_U];best_aim_pos=enemy[_H];best_target=enemy[_F]
				aim_active=is_aim_key_pressed()
				if aim_active:
					aim_active_now=_B;AIM_ANGLES[:]=np.rad2deg(best_aim_dist)
					if best_target!=0 and np.linalg.norm(AIM_ANGLES)<AIM_FOV:
						if target_selected is _D:target_selected=best_target;aim_start_time=time.time();t=.5;aim_speed_limit=np.linalg.norm(AIM_ANGLES*(t*t*(3-2*t)));AIM_START_ANGLES[:]=AIM_ANGLES
						if best_target!=target_selected:target_selected=best_target;aim_start_time=time.time();t=.5;aim_speed_limit=np.linalg.norm(AIM_ANGLES*(t*t*(3-2*t)));AIM_START_ANGLES[:]=AIM_ANGLES
						AIM_POSITION[:]=best_aim_pos+PLAYER_VEL_OFFSET;hit_time=0
						if local_player[_P]>_K:player_distance=np.linalg.norm(local_player[_H]-best_aim_pos);hit_time=player_distance/local_player[_P]
						if AIM_BALLISTICS_CORRECTION:AIM_POSITION[0]+=375*local_player[_V]*hit_time**2*.5
						direction=AIM_POSITION-CAMERA_POSITION;yaw=-math.atan2(direction[0],math.sqrt(direction[1]**2+direction[2]**2));pitch=math.atan2(direction[1],-direction[2])-math.pi/2;TEMP_AIM_ANGLES[:]=[yaw,pitch];TEMP_CURRENT_ANGLES[:]=VIEW_ANGLES;aim_dist=(TEMP_AIM_ANGLES-np.deg2rad(TEMP_CURRENT_ANGLES)+math.pi)%(2*math.pi)-math.pi;BOTTOM_AIM_ANGLES=np.rad2deg(aim_dist);native_velocity=(np.deg2rad(PREV_VIEW_ANGLES+PREV_AIM_ANGLES)-np.deg2rad(VIEW_ANGLES)+math.pi)%(2*math.pi)-math.pi;native_speed=np.linalg.norm(np.rad2deg(native_velocity));PREV_CAMERA_ANGLES[:]=CAMERA_ANGLES;aim_angles_length=np.linalg.norm(AIM_ANGLES);norm_aim_angles=AIM_ANGLES/aim_angles_length;aim_angles_safe_zone=np.linalg.norm(AIM_ANGLES-BOTTOM_AIM_ANGLES)*.13
						if aim_angles_length>0 and native_speed>0:
							prev_aim_angles_length=np.linalg.norm(PREV_AIM_ANGLES)
							if prev_aim_angles_length!=0 and prev_aim_angles_length<aim_angles_length:native_speed*=AIM_POWER
							safe_zone_coef=aim_angles_length/aim_angles_safe_zone;AIM_ANGLES=AIM_ANGLES/safe_zone_coef*(safe_zone_coef-1);AIM_ANGLES[:]=wind_mouse(AIM_ANGLES[0],AIM_ANGLES[1],VIEW_ANGLES[0],VIEW_ANGLES[1]);AIM_ANGLES[:]=norm_aim_angles*native_speed
							if aim_angles_length>aim_angles_safe_zone:game.write_float(local_player[_F]+Offsets.Player.view_angles,[VIEW_ANGLES[0]+AIM_ANGLES[0],VIEW_ANGLES[1]+AIM_ANGLES[1]]);PREV_AIM_ANGLES[:]=AIM_ANGLES;PREV_VIEW_ANGLES[:]=VIEW_ANGLES
							else:PREV_AIM_ANGLES[:]=[0,0];v_yaw=v_pitch=W_yaw=W_pitch=0;M_0=15
						else:PREV_AIM_ANGLES[:]=[0,0];v_yaw=v_pitch=W_yaw=W_pitch=0;M_0=15
					else:aim_start_time=time.time();PREV_AIM_ANGLES[:]=[0,0];v_yaw=v_pitch=W_yaw=W_pitch=0;M_0=15
				else:target_selected=_D;aim_active_now=_A;SAVED_PUNCH[:]=[0,0];PREV_AIM_ANGLES[:]=[0,0];v_yaw=v_pitch=W_yaw=W_pitch=0;M_0=15
				PREV_VIEW_ANGLES[:]=VIEW_ANGLES
			except Exception as e:print('Render error:',e);continue
	except Exception as e:open('render_errors.txt','w').write(f"{e} {traceback.format_exc()}")
def process_update():
	A='Update error:';game_prelaunched=_A
	if get_process(TARGET_NAME)is not _A:game_prelaunched=_B
	try:
		PLAYER_POSITION=np.zeros(3);BONE=np.zeros(3);AIM_BONE_ID=12;ALIVE_SPACE=sm.SharedMemory(name=_p,create=_A);ALIVE=np.ndarray((1,),dtype=ALIVE_SHAPE,buffer=ALIVE_SPACE.buf)[0];ENEMIES_SPACE=sm.SharedMemory(name='sp_enem',create=_A);ENEMIES=np.ndarray((10000,),dtype=ENEMIES_SHAPE,buffer=ENEMIES_SPACE.buf);ENEMIES_LIST_SPACE=sm.SharedMemory(name=_q,create=_A);ENEMIES_LIST=np.ndarray((10000,),dtype=ENEMIES_LIST_SHAPE,buffer=ENEMIES_LIST_SPACE.buf);LOCAL_SPACE=sm.SharedMemory(name=_r,create=_A);local_player=np.ndarray((1,),dtype=LOCAL_SHAPE,buffer=LOCAL_SPACE.buf)[0];game=Memory(TARGET_NAME);ALIVE_UPDATE_SPACE=sm.SharedMemory(create=_B,size=ALIVE_SHAPE.itemsize*1,name=_A0);UPDATE_ALIVE=np.ndarray((1,),dtype=ALIVE_SHAPE,buffer=ALIVE_UPDATE_SPACE.buf)[0];UPDATE_ALIVE[_C]=time.time()
		while get_process(TARGET_NAME)is _A:
			UPDATE_ALIVE[_C]=time.time()
			if time.time()-ALIVE[_C]>5:exit()
			time.sleep(.1)
		game.init();game_found_time=time.time()
		if is_dev is _A and game_prelaunched is _A:
			while time.time()-game_found_time<20:
				UPDATE_ALIVE[_C]=time.time()
				if time.time()-ALIVE[_C]>5:exit()
				time.sleep(.01)
		game_pid=get_process(TARGET_NAME)
		while _B:
			time.sleep(.001);UPDATE_ALIVE[_C]=time.time()
			if time.time()-ALIVE[_C]>15:print('Main timeout');exit()
			try:
				try:
					local_pointer=game.read_int8(game.base_address+Offsets.localPlayer)[0]
					if local_pointer==0 or local_pointer>sys.maxsize or local_pointer&8!=0:local_player[_F]=0;continue
					local_player[_F]=local_pointer
				except Exception as e:print(f"[ERROR][UPDATE] Read local pointer: {e}");continue
				local_bytes=game.read_memory(local_pointer,4000)
				try:
					render_pointer=game.read_int8(game.base_address+Offsets.render)[0]
					if render_pointer==0 or render_pointer>sys.maxsize or render_pointer&8!=0:local_player[_O]=0;continue
				except Exception as e:print(f"[ERROR][UPDATE] Read render pointer: {e}");continue
				try:
					view_matrix_pointer=game.read_int8(render_pointer+Offsets.Render.viewMatrix)[0]
					if view_matrix_pointer==0 or view_matrix_pointer>sys.maxsize or view_matrix_pointer&8!=0:local_player[_O]=0;continue
					local_player[_O]=view_matrix_pointer
				except Exception as e:print(f"[ERROR][UPDATE] Read view_matrix_pointer: {e}");continue
				try:CAMERA_RAW=game.read_float(local_player[_F]+Offsets.Player.camera_position,3);local_player[_x][:]=[CAMERA_RAW[2],CAMERA_RAW[0],CAMERA_RAW[1]]
				except Exception as e:print(f"[ERROR][UPDATE] Read camera position: {e}");continue
				try:local_player[_H][:]=unpack_from(_f,local_bytes,Offsets.Player.position)
				except Exception as e:print(f"[ERROR][UPDATE] Read local position: {e}");continue
				try:local_player[_R][:]=unpack_from(_f,local_bytes,Offsets.Player.velocity)
				except Exception as e:print(f"[ERROR][UPDATE] Read local position: {e}");continue
				try:local_player[_C]=game.read_float(local_player[_F]+Offsets.Player.global_time)[0]
				except Exception as e:print(f"[ERROR][UPDATE] Read local time: {e}");continue
				try:
					local_team=unpack_from(_Q,local_bytes,Offsets.Player.team)[0]
					if local_team==0 or local_team>100:continue
					local_player[_J]=local_team
				except Exception as e:print(f"[ERROR][UPDATE] Read local team: {e}");continue
				try:
					local_weapon_index=game.read_int8(local_player[_F]+Offsets.Player.weapon)[0];local_weapon=0;local_weapon_index&=65535
					if local_weapon_index!=0 and local_weapon_index<sys.maxsize:local_weapon=game.read_int8(game.base_address+Offsets.entityList+(local_weapon_index<<5))[0]
				except Exception as e:print(f"[ERROR][UPDATE] Read local weapon: {e}");continue
				try:
					game_mode_ptr=game.read_int8(game.base_address+Offsets.gameMode)[0]
					if game_mode_ptr!=0 and game_mode_ptr<sys.maxsize:game_mode_text=game.read_text(game_mode_ptr,8);local_player[_X]=game_mode_text
				except Exception as e:print(f"[ERROR][UPDATE] Read game mode: {e}");continue
				try:level_name=game.read_text(game.base_address+Offsets.levelName,20);local_player[_Y]=level_name
				except Exception as e:print(f"[ERROR][UPDATE] Read level name: {e}");continue
				try:
					weapon_id=-1;weapon_speed=0;weapon_gravity=0
					if local_weapon>0 and local_weapon<sys.maxsize:
						weapon_id=game.read_int4(local_weapon+Offsets.Weapon.index);weapon_speed=game.read_float(local_weapon+Offsets.Weapon.speed)[0];weapon_gravity=game.read_float(local_weapon+Offsets.Weapon.scale)[0]
						if weapon_id!=182 and weapon_id!=130 and weapon_id!=-1:
							if local_player[_W]!=weapon_id:local_player[_y]=local_player[_W];local_player[_W]=weapon_id
					local_player[_P]=weapon_speed;local_player[_V]=weapon_gravity
				except Exception as e:print(f"[ERROR][UPDATE] Read local weapon values: {e}");continue
				active_enemies_indexes=copy.deepcopy(ENEMIES_LIST[_E]);enemies_list=copy.deepcopy(ENEMIES_LIST[active_enemies_indexes]);ENEMIES[_E][~active_enemies_indexes]=_A
				for enemy_in_list in enemies_list:
					UPDATE_ALIVE[_C]=time.time();unit_bytes=game.read_memory(enemy_in_list[_F],4000)
					try:PLAYER_POSITION[:]=unpack_from(_f,unit_bytes,Offsets.Player.position);player_read_time=time.time()
					except Exception as e:print(f"[ERROR][UPDATE] Read unit position: {e}");continue
					player_distance=np.linalg.norm(local_player[_H]-PLAYER_POSITION)*.025
					if player_distance>300:ENEMIES[enemy_in_list[_G]][_E]=_A;continue
					try:
						hp=max(0,min(unpack_from(_Q,unit_bytes,Offsets.Player.health)[0],100))
						if hp<=0:ENEMIES[enemy_in_list[_G]][_E]=_A;continue
					except Exception as e:print(f"[ERROR][UPDATE] Validate unit hp: {e}");continue
					try:armor=max(0,min(unpack_from(_Q,unit_bytes,Offsets.Player.armor)[0],100))
					except Exception as e:print(f"[ERROR][UPDATE] Validate unit hp: {e}");continue
					player_velocity_raw=game.read_float(enemy_in_list[_F]+Offsets.Player.velocity,3);avg_velocity=[player_velocity_raw[2],player_velocity_raw[0],player_velocity_raw[1]];avg_acceleration=[.0,.0,.0]
					try:
						bone_pointer=game.read_int8(enemy_in_list[_F]+Offsets.Player.bones)[0]
						if bone_pointer==0 or bone_pointer>sys.maxsize or bone_pointer&8!=0:ENEMIES[enemy_in_list[_G]][_E]=_A;continue
						bone_pointer=bone_pointer+AIM_BONE_ID*48
					except Exception as e:print(f"[ERROR][UPDATE] Read unit bone_pointer: {e}");continue
					try:
						BONE[:]=[game.read_float(bone_pointer+44)[0],game.read_float(bone_pointer+12)[0],game.read_float(bone_pointer+28)[0]]
						if BONE[0]==0:BONE[0]=57
					except Exception as e:print(f"[ERROR][UPDATE] Read unit bone position: {e}");continue
					HEAD_POSITION=PLAYER_POSITION+[BONE[0],BONE[1],BONE[2]]
					try:player_last_visible=game.read_float(enemy_in_list[_F]+Offsets.Player.last_visible_time)[0]
					except Exception as e:print(f"[ERROR][UPDATE] Read unit visible time: {e}");continue
					try:ENEMIES[enemy_in_list[_G]][_F]=enemy_in_list[_F];ENEMIES[enemy_in_list[_G]][_Z]=enemy_in_list[_Z];ENEMIES[enemy_in_list[_G]][_U][:]=HEAD_POSITION;ENEMIES[enemy_in_list[_G]][_H][:]=PLAYER_POSITION;ENEMIES[enemy_in_list[_G]][_R][:]=avg_velocity;ENEMIES[enemy_in_list[_G]][_v][:]=avg_acceleration;ENEMIES[enemy_in_list[_G]][_J]=enemy_in_list[_J];ENEMIES[enemy_in_list[_G]][_N]=hp;ENEMIES[enemy_in_list[_G]][_I]=armor;ENEMIES[enemy_in_list[_G]][_T]=player_read_time;ENEMIES[enemy_in_list[_G]][_h]=player_last_visible;ENEMIES[enemy_in_list[_G]][_E]=_B
					except Exception as e:print(f"[ERROR][UPDATE] Write unit values: {e}");continue
			except Exception as e:print(A,e);continue
	except Exception as e:print(A,e);open('update_errors.txt','w').write(f"{e} | {traceback.format_exc()}");os.system('pause')
def process_filter():
	D='Filter error:';C='player';B='mp_rr_ca';A='[FILTER] Main timeout';game_prelaunched=_A
	if get_process(TARGET_NAME)is not _A:game_prelaunched=_B
	try:
		ALIVE_SPACE=sm.SharedMemory(name=_p,create=_A);ALIVE=np.ndarray((1,),dtype=ALIVE_SHAPE,buffer=ALIVE_SPACE.buf)[0];ENEMIES_LIST_SPACE=sm.SharedMemory(name=_q,create=_A);ENEMIES_LIST=np.ndarray((10000,),dtype=ENEMIES_LIST_SHAPE,buffer=ENEMIES_LIST_SPACE.buf);LOCAL_SPACE=sm.SharedMemory(name=_r,create=_A);LOCAL_OBJ=np.ndarray((1,),dtype=LOCAL_SHAPE,buffer=LOCAL_SPACE.buf)[0];game=Memory(TARGET_NAME);ALIVE_FILTER_SPACE=sm.SharedMemory(create=_B,size=ALIVE_SHAPE.itemsize*1,name=_A1);FILTER_ALIVE=np.ndarray((1,),dtype=ALIVE_SHAPE,buffer=ALIVE_FILTER_SPACE.buf)[0];FILTER_ALIVE[_C]=time.time()
		while get_process(TARGET_NAME)is _A:
			FILTER_ALIVE[_C]=time.time()
			if time.time()-ALIVE[_C]>15:print(A);exit()
			time.sleep(.1)
		game.init();game_found_time=time.time()
		if is_dev is _A and game_prelaunched is _A:
			while time.time()-game_found_time<20:
				FILTER_ALIVE[_C]=time.time()
				if time.time()-ALIVE[_C]>15:print(A);exit()
				time.sleep(.01)
		game_pid=get_process(TARGET_NAME);AIM_BONE_ID=12;last_process_check=time.time();temp_enemies_range=0;enemies_list_start_address=game.base_address+Offsets.entityList
		while _B:
			time.sleep(.01)
			try:
				FILTER_ALIVE[_C]=time.time()
				if time.time()-ALIVE[_C]>15:print(A);exit()
				local_player=copy.deepcopy(LOCAL_OBJ);current_time=time.time()
				if current_time-last_process_check>5:
					last_process_check=current_time
					if get_process(TARGET_NAME)is _A:exit()
				if local_player[_O]==0:continue
				units_range=list()
				if B in local_player[_Y]:
					if temp_enemies_range+120>=10000:temp_enemies_range=60
					else:temp_enemies_range+=60
					units_range+=list(range(temp_enemies_range,temp_enemies_range+60))
				else:ENEMIES_LIST[60:][_E]=_A
				units_range+=list(range(60))
				for i in units_range:
					FILTER_ALIVE[_C]=time.time();ENEMIES_LIST[i][_G]=i
					if ENEMIES_LIST[i][_E]==_A and time.time()-ENEMIES_LIST[i][_T]<.5:continue
					else:ENEMIES_LIST[i][_T]=time.time()
					try:
						player_addr=enemies_list_start_address+(i+1<<5);pointer=game.read_int8(player_addr)[0]
						if pointer==0 or pointer>sys.maxsize or pointer&8!=0:ENEMIES_LIST[i][_E]=_A;continue
					except Exception as e:print(f"[ERROR][FILTER] Read unit pointer: {e} {traceback.format_exc()}");continue
					unit_bytes=game.read_memory(pointer,4000)
					if pointer==local_player[_F]:ENEMIES_LIST[i][_E]=_A;continue
					try:
						signifier_pointer=unpack_from('<Q',unit_bytes,Offsets.Player.signifier)[0]
						if signifier_pointer==0 or signifier_pointer>sys.maxsize or signifier_pointer&8!=0:ENEMIES_LIST[i][_E]=_A;continue
						signifier_name=game.read_text(signifier_pointer,8)
					except Exception as e:print(f"[ERROR][FILTER] Read signifier: {e}");continue
					if B in local_player[_Y]:
						if signifier_name!=C and signifier_name!='npc_dumm':ENEMIES_LIST[i][_E]=_A;continue
					elif signifier_name!=C:ENEMIES_LIST[i][_E]=_A;continue
					try:
						player_team=unpack_from(_Q,unit_bytes,Offsets.Player.team)[0]
						if player_team==0 or player_team>sys.maxsize:ENEMIES_LIST[i][_E]=_A;continue
					except Exception as e:print(f"[ERROR][FILTER] Read unit team: {e}");continue
					if player_team==local_player[_J]or(local_player[_X]=='control'or local_player[_X]=='tdm')and player_team%2==local_player[_J]%2:ENEMIES_LIST[i][_E]=_A;continue
					try:PLAYER_POSITION=unpack_from(_f,unit_bytes,Offsets.Player.position)
					except Exception as e:print(f"[ERROR][Filter] Read position & set limit: {e}");continue
					try:
						life_state=unpack_from(_Q,unit_bytes,Offsets.Player.life_state)[0]
						if life_state!=0 or life_state>sys.maxsize:ENEMIES_LIST[i][_E]=_A;continue
					except Exception as e:print(f"[ERROR][FILTER] Read unit life state: {e}");continue
					try:
						hp=min(100,max(0,unpack_from(_Q,unit_bytes,Offsets.Player.health)[0]))
						if hp<=0:ENEMIES_LIST[i][_E]=_A;continue
					except Exception as e:print(f"[ERROR][FILTER] Read unit hp: {e}");continue
					try:ENEMIES_LIST[i][_F]=pointer;ENEMIES_LIST[i][_J]=player_team;ENEMIES_LIST[i][_g]=_A;ENEMIES_LIST[i][_E]=_B
					except Exception as e:print(f"[ERROR][FILTER] Write unit_list values: {e}");continue
			except Exception as e:print(D,e,traceback.format_exc());continue
	except Exception as e:print(D,e);open('filter_errors.txt','w').write(f"{e} | {traceback.format_exc()}");os.system('pause')
if __name__=='__main__':process_render()#apexchill