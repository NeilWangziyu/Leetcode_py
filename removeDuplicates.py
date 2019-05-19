class Solution:
    def removeDuplicates(self, S: str) -> str:
        if not S:
            return ""
        if len(S) == 1:
            return S
        for i in range(len(S)-1):
            if S[i] == S[i+1]:
                return self.removeDuplicates(S[:i]+S[i+2:])
        return S

    def removeDuplicates2(self, S: str) -> str:
        if not S:
            return ""
        if len(S) == 1:
            return S
        while(True):
            i = 0
            found = False
            while(True):
                if i >= len(S)-1:
                    break
                else:

                    if S[i] == S[i + 1]:
                        S = S[:i] + S[i + 2:]
                        found = True
                    else:
                        i += 1
            if found == False:
                return S







S = "tmrejigdbnmhatkmidsrsgtfhugftkistfifofraffrtirostceuojgccmokeumapprjrdceigudnmsjtcmlntfekubnblbhtjbdktskoqrnhohbimtahlehuispgpejrcmuonephgpkjuigeemttoiallejtdjoqjaoeiqnqdbbgsnpcoqmematgpbcdqalkqrkgklbouomgaeslfdbnerjpecdtrhanohofqgjmsksslfiiqjcmhummmjhdeefummbnlkmmejjjoolcgqjddlcmhtgtaqumbjusgpkeikhjseshbhuksjiokmmjiobfblrdfglopedpmnhqiosmhepksajafgotnifntsqrkoejkjfmhjpmalrnpnrhhjbsnmcaqiiemhhoauqondhouudqcbapiocdmfktjtdciuareqjpdsjkqftgnnbebjcrjdaslrtmprlsuepenmtrqdfpbbenftebntegpsfkhbphoosladeplkratssdhiijfcrqbdbjefmokgujudfaakigedtufrdaatfogeakasnfutnelkmtinkksgnbtuojfkjliououfsaninejdncluejiatkunjumdjchhkaofpkmhsrgqmmrfefejnuaselrerdfnkctnqscegrogspceambnhcdchmrkjpcmdulredgmlqjnpuleulggqftapjoumgpkshqceuqakjjuaqdpmagljkfaskgngolbutnakpifnporuclcupdbrckcfobgrrinladcsrghsjruqmkculjnmntjgdtaunfbmgjcmucadmbpusmfhkhrfnstgsiqleaefpeqfkflamuhfplgehhrrkklaidthlmqmppoqqrdmklgcngnqsukjikelrqkfcgcrtfsogceejbhkojlbioclclgtdheqlpalgsgbbamklcjldheincnhhsiiefrmpngbhlthqlmcddbqseqgudoookppsabmgnjaufqdocbqjkotgjeilierjcaqubkdhrhsuqdkomnpigmtklbmouulrkifjrkddnhbatjriftbspoujaniqkfmncppitnhnkumqmnelpmkdrrlhmjdgcqrsrotlgldqtifslairmrithfkdsdnnddrjukspujinlkrjjdicgntubcgifcpfpcbbdjekrjnjksltchtbsijoukttosltarpctlfnbnhmcdilbehidhbhljeeschshkhifapmstgfmlsttnfbjcqsckafdetunpbnjqajsennuuqoachhocdfdtniuttpiunlgaefiipsiuajmepfdcoetciicmotiropkukfnfnpldsklbfsurlpfacitdeieulhthcatfjnnjsmlidgmsjohpbembjuinqjmmqdsiufkhdlrofiphmrqdioeljlohckprhpgfegkikofndjisgojjakpjrnbclpacmjrfsihfupcuiqcbjhhuchebftgroefodqagdprqhdacnbnttqftpmmddfpktmldtadsrunidaqlslbdkldirrajkbssgicrncngpfutnqjauoneqqgcueahanbikoiqkhdludfifuhkrahmcuaijequnidcbkprnhuqlbpeahefucsguahkoahkmjndlgglgnmojdbufercpgrultojdokfebfoddbhetenshqedaqisssdptafninukbrrjpogpnuspbjultprhdiskmlerlfpsfradalgkdouennqmrcqumdrufcjsrgeajubtmatnrdgebspppeudblqeqcspriinlcnidfmnqcrdkuccjkaunaudaspbniknjeamceafmnprkihjcttohdqhhlkeomajfsrcifqbjeadoktrbppfcutjpubngafratmshrgcbapaeilpmpetscaqdaeelusdgceqgsljhpftiikgkpiitleoaobkreilbkbqogsotqmlossjbdfrbplucucfnfngcfuadsdndosgbjpodfbtctmoaafmcjaifredpmogkmcpklkgosqjmqcofrrnejtikaqnqgfucqobmogudiegorkbatphtkrjphhosrnulkaesjcqurjkfendduqdurrjukfshiibfjkggoldbndqpkgmskolfugtkrgkogadomfsgpkbqidppcugcglekagftuejjbbrkgsjjereudronnjflmghqekgkluractfdauklftfiultnirbqqfadfcakhoeqljspgflaigdqsptebqajbbiakkgucdcffkatfjmohakraabqrtbonfcdarbpodupokhcebkmshsfaoddjajfgpcinnalujcouocbctcfprpmikobmdneoojhpqdebdfctootjstqhjlnqdsfpmfheifamuohratqtqidlajpfkqamhgulgdfcptsoftfkctffbibsetheguruqdeugruomlfabajqmjjtjipkcpeeaeriaqhigkdckldmrbjphutdqioltrmmqqkummpgoedaqehgbbptnhjebcokeunkjgciikdjenfginqojhkafinbnfugfhbifbuamsaqnsubuleekiiaaakfdukhpchatmjfuhrmcfieoqhblnradpibfioujcrkokqldhehihfcuhlbdbsdulnmnsorrpruohmdsadhdcncrceeratjmusdnjjsklfajhpamntjmpuotptaldgarnmepthibsktntaijscereqejjhmhmchiflsfcfdteqgklongihpckkonkgpgsjqrrtahofjnqcqjfqrunbbmfaijehjbdjcgqksustijqkumhhsfsrbupnjlrfhfkbkojgreejumpjabupbubrmgdgckqgjrqngkbonaosrpperiqnkqijbitogbltgsduspfcuqkmfpkifqeahopehuafadabsrafoofomlptcdotmhdmciccotqeaibpcfgkoqbdkmudsfokiemcnqohcoonktjcokgijlndhacjeplikqmalsselmggpstjidbjdguofgfdqfrqemcudagertcotlijtrdotignkjgmhkuikgiddudbaorkhdrjignfucfbncccfqubocusutkbamobrgjahlefieuelbnekmtnbmnqsnmqinjpituqdkcdoikcfgitcticlnpmkhbkonjkrrqfbnbptetijnbguinkkkkqrqppjglfgistnicsccduqihnmpgjcjqngkgsrhrqgrqhebbeefehunmrphbpbbdhrbdomhjukllpocgbceindqskagirrbltlbrlcmutktghbgnrlaellqhgonsshbpfbefjnlbaqkmkpglbuucqjpismlunffieslnqpiqsgtlaojrghqnenridpfkutibcejdhtrjfandrgrhshlnoqoqnnmoilkjcrjepnhffgcqndhjlainafcqqggqmhrirstecctfpkqdbrbdgkpiraajqeetsjhmugcgoteqrdobnoeejftmifqdthtnmuleatatdsfnehcskrqtfpucaoafqliqhoscbhglmlgrahsftqadbdpodmnpbtgnrimlaugasilmmeprugbaamrklpklmkrigcncmeckjdkjkhpjkcptnnmnldtipbntpeqtmiaojplkpmucftuectcqscaqonekhahodbhdgksrhmdlatjdcsuoopfinitjkmsppjjlptdrjbirjpdmukkrlrcbrnfgmdcoudninehiirkrbrohukhccjnredblrckkmrsdcasujgfrgaesookijlpprchtukonrrmuiqcfchkiuipqqqhbqugrlliheskmcuslosnhqgchhjbdjuuqlqlfmstpuoaqkbpmhhamppfebldaljqgtpimadpoqdrmbqfukepithlesgkenshtpbqntlhpaddtjtfjnphpbogkljgbpjgacsdqkuuuouksrdrildgrtnitafkbfttkcinondobmfcabekkqnbqnrqgkaaolmelmcoroqqkodeaanmeksflmibqhuuqkkdtnhhpqjtoiotnpltsejqdbbcdbjunaqqrpfuqaffdqknildjaplgcrggkrjtpusbbbkgejpudfutkrghctfldoncldridphsnpjibrkaipmiidaundegefppcjndssqhqkuckuonrquhkpfbsargdubnnkqiskmgaeehsnffsjoecreunbaaiddiduqmbnbtgiubcccfpbnuehffplfjjocnahbukbnrfflineuntaarglckffkjnbhjfrklqbksnecqrlaegogqrigrgulcrmeqgknqmgdggtsjqhejfljllinreslubglctrhqbrohjeoqdhepqlpnpcftccagqqaomougnojgribpcpoerjqjggghndslapgkalkeaaofcermolcrhgacncemtqnlmtqkmafignfbrclokfbjkjfrjipdakfdlmatbcesgteqpmhkuubefoqohiprkpeejckmimrjmegehsiqatocmockrshsmlqrtrregobeoursqstfntqfguctpltqinblbamuhenukkdffgilkfbhogfsulalgjcggtrmtccpfsudngoqoprmetbemmcqekoifpdohdtodqlieapunaulejabrodeelpojrcpfmocluoreillpamtgirjrjtlsttlerhsnnqdngjnqhmirugtdnpnkdrmbbtopfabiakomghfgpcmhusimtteqjblbtrnbqsnmrtianpafiucbcinulelgtqbumlmuihskurknpdpskjtnmmimtkcqslcnbctbofodjemaubbejfnosttpcsckpimcicrjuhdlretrmnqdrreajhedfhdmcpkpmsbukemkstpnlnpakfjjgbojjpaoklsfnnjoiqcssnpffhfmbqjpugbrdidgrnfaqobcbdhrsajglemipdkgtrcjpmmomkokeklipechktgtncogtolqjnjitsuqgrsjqjdeqliaihseuqnecothcrnrpoubsjjpudlnlgkneuudkhpepfcnacsuamnqkftiguljhdhrndtjjfntatdlclkljquolcpionqpalgemiabkpipebtlnnlqctdmohgrtueqgpaenaglglqplljtgfnbedbsqrjujbelupubomgdeidarrqiilegbgmjibtkhsdihbulfbfjlnieguaadkgnrrufrmosgmdeusihuelamenshbuhcjierhgldmrelroaimsccabbtkdsrquhkqslcbucknlnhhettnctdlaegmjoqiuithgthfidcibnpbreumajchahftrcttcllqpgkssqfaaamgbgoebocrrogscjpdcoanoernafmchfumorjbhfqhrmimsaolqqtrnofjigcrhcqlaqogglsmlnqtmqspccodskhcsijqtdkqkbiibdokldcounmmpohbmgkokusuhohpsupsnmlggfpshaecdsdteabkeefjksrirdheqrjpdotohldcibuqtairncntrqmdrcommteaamniaaecsimkgbcugirjifistorngemsjqgjspmphidhpftllshmfmcscpnjharopddlbkaijsotiejeahbnhkrekpbqidkhkackrcgefndgiuhpkkgkorcenospbjlmdoqicgafcgrokegqtngpqsbndtiepftkmckmfieuccojarsbjkofsiaefqscuenkjpsdeiujtiuneujhkerimjnacrjqtmkqmplsranomuhegqocrqnjaupfbicshoseqlqhoeirbqfclartobrchjpagblounmkjsmcaolskdtganrhdllbpbdociitmsgrdlaugondgjaufluqiihkcocceiamlbegqepmdthfircqeotugbmmarlimepbuuggmtmenjhgdqtkprkeeehmkjbuiurclobajhggigcohltdlsibmeucdjpffmgelagffuatiprjirjljoqhiifnsqlmshaodntfqahmmrkcejotbosisaarqfafkjifmnbgnaqlljadceanccrtupebemdfqesaoeakokqltarpbdfrfllnlhtuirddsgpglujckjhdptehiisikgnjojalapqulkmfkqilaskneatulteplhtgnslarbttqpsdeeadjnfimirrduolaonodjeoigcibpjfhcdglepcqbrmnjpesofhbeebpdktnaursahogcjudhdbmktrnnfcjgcjjdkgnoioftcdhppimarnbibdpaopnbsstcqjgtedfkfldnjfuelehlddskllrnjiiihiocrgjpqqoletbpjrebfcaigapkchomfoudctttnumbssfrhocqkipqaprohknbeadqfinoqjdikdtforqisgdqokfsbcmcnsuqemadsknjobrmpcmmukknalqlfhussjkcblspkfifhftoqfqmesmsbbogtijtuajhnbqblrsammnnlercuqdbjjgprjtupblehdfoaqnnacgumaocpmcuagciiucnnmeojbfhtpbjfaplsbcsljdupuaipfpiknmrstsqtqhlfrmdblssmkikokmurhoucfkegcucrrjienspumlnkugqtfnabpoecghkcdssunjcrtuledbnlojlalqkcnuuuqmgkbgolhlciomrcuhflrumkltngtgpuaelufamghjretpualjugehbpoiagnttmlajjffnngucbatjjlcfqtrbpbpuafutuhsnquphdktkpecbhfkrbkgrqeepfsjegjpqaecugspdfrbmggcbtcchugajnoetduqsjqrmjjiaapmhmmaksqrsolaggatfjsimtubtmsupkueqoisisnitgonuqgptpjpjalmttocbrkmuqkrqcbtnibsflslunoprtrnlbspipbmhhbuuppnsbctucaiqudglojhbbkgcsfbaocbdijoopeuoiqijhcoadjkfdsmhrfusgeptscigcfsbhnsmmhpebupkomlrujotobdmriuositrgnqoqlahskucoioeglosakocgjfprbqdnhgqhmmcniuaqirhtedrudbrajjbpesuqemdcksutkpltcnfutdgisftcalpiaahjmbbtmhpomkdmeojdpsenctlkmnhjthqbhfaequmbejhnoidncajmkjefaqbclbnihbaiofjtntljlsbfqatgnrnmjnfgblfabipcebftlbkgplhucrmuisitetisjfeqltidsuintajijrgfmabsmafkpbutteuusckbhrrquubssumbppikqidbhcmgketionnhsbdiagkeonnapbrnskknebfupceiqirdojlriceedsluhgsuqbtbubfujpilekskootkkcnesludelqmkespjbtpoqhtcoksqrodftodfrjoclchmmbdgossoiucrtojttssahiagskqlbupsqiniojqalltkhrggscndrllfkfqaiesutsgkfndqcjahcfpgngisjhpmnrnicbtkfcdnsqtiriskmjjdlrrjsrbhsnpbqdtcbianhoemsemjgadjioicjieabbptrulchmegpsstipamprbhmmkieqtrdaftgkgojeqlqligkuhuijdumsmkaunkjhprcjiucatltqqcpsmjsdmmenstarmdoiiqbepteibtsjhdhphmheldnqphnmnrgikunhcmopchmpfhdtratrsptegurnpfrcmkkasjuqpjtbqfirdtgtnnmffsusmmfqikelqsqtokejourprqiojgjstgdfptarijtrrebpjnqqhuagbjlnuqktdfhblnckshfnkinlokcckbncgchhtoanosjdkingmfqmlmaobuidudmjkjdnsqhcudahmrtdofltobcmlcjthktbbdqfnmstjsheiiefqrgiigharsauielidqpgssakdsfqdbddnjkhsjegtdkseqqpthonnoiraferbqaegksfpenkfmcmjnffdctmblkepfjfpuoanaundlinhoecadptckobmpdbduetrjiolfmfmkgnqkjgubmkmqemookjrbmhoiiqpnnnsgcbnutkerhsttsnqdodcgmfqegfbjfkmmrfqrumnmfjisltunrjirkmcoutuiqbouufsbbrqktlkkhklpffoqgujbphmiaipspaorrdfntrpndpqlhbtoibocngtkmlocnnppefmjmslljjfdktuhoejddppsjteeclfqhmfuotfepjcgajhdnnjinoniqsojhjgifhmrntmutmqkgihucqkkfsqroltdggccgletjdgqcccasikfhuokeificniufciiofchotdkcutcmurnjmaftotndlmgkriqecdmfhcfoidtruibhhdbfqidhophbfogsnnicdhcnsaufnqacgsutcjaofmrkiiifsggjeeshnbranffjkfbtdrgtgqhdgadjntttbotacmcicbgsjfdjdckoudfacnfeomkfpjcrfnprkdtmggldcdtokihfrbqefhifcalhucirupckbimlbeckhcestrsodpeuqblpjbrnfqobpiadbnjcftdhdsanolbuagbpjrmtblefschjjojtmpfhkpprquegsrfebppcjdmumbuacqjfunhobpubalmcflaucrsntmuotdmaukechbskdsofdkhmkucccbkubnnpgfcgttmtcgrqfqdnodeqnecdknfsoldblhsoqonialcmancmqcmnsellnsigoadbodhgflekflhangbifulftpejfmdjhelbilabekbuhbcttsgrjghfieokehbgukeutsfrtkkhloemimhdilbcqjbscgjeoejkhocerapsmbmbaaumeephftqnhhjktpbdhskdnuuksfmogtqgruikbgjibshpkjnougmlroankgobkakbijuoslcaokmlejlottphlkmcrtgfnlolsrplpaotirimmhijuaimntncnitnmtaetktnasrjmhkriqecnqiegmfqlbdkbnkhmerkefjotkfsatubsdphdibfoencmaefiekijqsmjmulpkajoiiagbfqijmocrllmoopkimheuqpsmjqmjdqqsngcadqsoogssordtbepehjtakmsgpalnsqlafsshnoqjsniejfikplobanalueeoqrrljbkejrhnmreitjdienpujksttjudabaojtcngfbpjdemrenhagltamgmjrapgedqqgpjmdnqhngutnddoqnnsjlbrtlhaodoriiasfqrkluqapamgsptbnsupcbasdulphlhjlohgrbcqtribniitrgeakgtifopniclunsmsicunfnscggokdosmjpgjirtplttkiemlesdjfbnfkfmnqfirqcjbdbitpickpuiiusbcbadkpduuppjrgfqsumtipicuepeqmluoicjefmeansohhtufolrtdhaderflbrfbbaumdnebhuibseaohnnjmqrohginolshhpsifpbqbngifeqobrqaehjmguobdhkbdqkjkhlhnhdpkafeoaojobhhibphunnojohpcbmhkimgdpgtaotaddbrklupqfqcmhfcqjjcrqfnfumtkaaqmjaiodrebugckdmlcirmkggbuhaoqaknqcobebiquqacbgcqllsbtndbdoabnldcficcnqbkksclurjddfrsfmcbrbmaffrkephmgqlttqgescgeeclgsedgrntcqfdnonqnlfqeosjjgqfolmuruqhhbjktkgqrauelgpjnaruapeturaltlhcdsjtkirlgrprbqkopsfqhqkpmeibjnhfsdillnjjbfskjsaobkkbcpgkgdiqgetsaedialqpipmrbrmoompctudniptpkhgjmsisifjifqendgcugtgriqaetdqfsrfafqngossagotmlobslrdlcbkagegiauctblquspenrpgqonpanfdqokmjesichiiarctscsomjoskrmipebsedhgoblebtufslkomdenrucmlqkfppodddfmbrfskerookunhahutascflpingigbdgrbgdeuosepbmurfoftcnhupisbdtbdfmeutoophusqpbmhtqankkoiaabcepmeickgihdglcgqujrqpsbprbrilnriohdgmtkipducoconajiaserkekfnpfcbehhcsbjrfrcdgulalninhsfiombdpfigkqsoekbhnoubnlknlkoincnecskqnjhfheqbbsqushhsbuatcndqbcpsmrotfjfhfrfkmknefglfckcsmccjmbcskruufeijmaqenjjmobdqjhptpoaksrhlresnfqldiuqcfrdpfntfaclttnigccpbsquhmasobusknlpauildbiqelajbjpfdsaguqejgajbkitjoerjporjdonfghjbmaqokrhupsqjnqpjgptdgppukgackfdlilbqbpnkbgohmpubnehmpnejnmtnhphkdhhbidlllecasfgrfuodrfucjkqapdbmidfgutuqcluekfjonqkjgkjegnpjfgkmeroohmleanssrfdhltcuuintjerpmgheplkfntelfaogqlmnfilbgdulbigumkjjssduqjkcrttbtlfhhbofshqduoolftnoamgkdrgidtoubbndisekfqbebcgmadcqehtqcrurraigfiuhtjopghkqmrraaekgohnultkpbprrcblcksmdjfmdmhbqqucoupjqadqgfpiumpolcshtasulmpfbgfelfbjklmhmlinjbibecesglugqsemhcgrnhkndmkdarofsrrlrdrstpttcmnhjikfftnrcsshfdfaattknthbsbcajaqknkapnipnpujhookigjkjqiahmmadfacantatskndmdcqbggegtfqftotpbukfhfnstfuensetkiicqhjpbbddceqadjtnmchstsrqcocunfksonijpujmqijsjsqjqpmrorigukjfhusmbbqtgaemmldleaqjndketomlknqpkhftjulnmjhkeucdldiqsubqeisctdndrqleaalqacbeisnndfpkffrcpjtbhllblucgieucejpmruapmospeilcmerokgmemqjcbnjddnunofgkgmcmbgjufcrrnfmqdfocfriggueoqrfaeunesugqeggcqoemfqsqbbkocragdfdeufuurptipdogdehanbrmsicqmslubadodtpshsogoofekpqolbgeqiadceijeunjadiiafetjlbbkeasqsrhjcsmrlldapmbgfqtshkjnhublqugarghmtfpiglbidrgsoiknissudbdcrkirkrbpbgkrnhdkrhpsqmousfqnhmksfkhunfthoinhqoodkgcoohjbunnpgbacqhsmaiqgbhuortetabdceqclqhbuspgaediecsorrgbqegaemlgeehnurukapdgkobsouttsrdiqjckmhuhqjaumapukhmefgmsherlsgldfgukujggtorochnahesibhussdkddnihjbralmkfhokcthrmrhpabkslbsghhlnubkfhagihlmgrgnihsrgistibgefhlofkfnkaimhobsjmqroonqmdgbmcnomfjnrfdeocacbfjcmmaqajmbgqkkjpupaqbniasmpndbfgacsfutamqgkigrnabbacqgbngnmbjjlgfofolatfdkdeuolhndtjmdcmftdmllgconbeicqkopluonmcocaamhiqbnhjuskgafubnculdqgutdeerpubhhkibrhndqhfrjcpiciecohmbpjorpkinfjjcahucqnshmrekbadmhpijcruihikpekoijjolqfrgkbjnloiqimilrhtilcsqehdtbrafgftqqmkdlrgbglpiuqmttogrbprgjpjqltphtnjolaefodsghdubebnmqqffpficgnejjjsikkerdglbuatqircibcbrnaigoubhgupjbqamkutictebtclrjkrrltubtnsejreduptipciofbjgjnkmakbabmbhgomeithtjomnfgujebntbrtolhfpjtelihajckmqmprrtmabtessnublftaffilnnjkopbijgqbkqerljigrgcnoucqeducalgqrluepbmqnnqdrlacfdbftojohecotaasepprdmgukorobtccprqbmtcpbigstpinnpspfckmdnpadehacskndpqmqubeebosfcmuldkcdqmfeoiobbubgkjaeohkkqufiaiepldbmapdookkadranfrgkisjshjuofeelqoecunjupamtbjljiligkphbaoqlclouilqrmchbpldnckosadelrnbcjpdldighbjnhlsshnaujamtfaabipdpugsogimlfhkkddpapjqbbsbprtoetrukdofiifiamagcfetebpdainglonitiotscebmjrfigeneqqnhfukljesrakdmrrpaghhqqnptegnkdseamdehbcuciqiullarsjplrrmteladaiitaelomhotunaaormpgghkqmspsrphabqqrkmfirohmjebcpkefjeekdlapmodbnrdkboashjauujrqatktdqksfkqrqajeahortsrmetrgankeuauckeuumbpugkmuklncbdogifmscnkfsosgurapklredpaehgdrgbndjmdqaakqnquiodipcshlpacqoghmcrmckmoukrfuhebehdqfimmrfltdnmdjcdponhbiooongfpcgqrarkrnqoqdtukntolbnkdfqdkfpjesepdqsjrpmimkcpcosetofchkdbbpiliosaajhqmahhclbmpfeinijioouceimfjrrnkcdrpnpoodbriudjipi"
s = Solution()
A = s.removeDuplicates(S)
B = s.removeDuplicates2(S)
print(len(A), len(B))
print(B)
assert A==B
