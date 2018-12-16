class Solution:
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        def all_s1_sort(s):
            if len(s) == 1:
                return [s]
            res = []
            for each in range(len(s)):
                list_without_i = all_s1_sort(s[:each]+s[each+1:])
                if list_without_i:
                    for each_sub in list_without_i:
                        res.append(s[each]+each_sub)
                else:
                    res.append(s[each])
            return res

        if len(s1)>len(s2):
            return False
        if len(s1) == len(s2):
            if set(s1) == set(s2):
                return True
            else:
                return False

        if not s1:
            return True
        s1_list = all_s1_sort(s1)
        print(s1_list)
        for each in s1_list:
            if each in s2:
                return True
        return False


    def checkInclusion2(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if len(s1)>len(s2):
            return False

        dict_s1 = {}
        dict_s2 = {}
        for each in "abcdefghijklmnopqrstuvwxyz":
            dict_s1[each] = 0
            dict_s2[each] = 0

        for each in s1:
            dict_s1[each] += 1

        for each in s2[:len(s1)]:
            dict_s2[each] += 1

        if dict_s1 == dict_s2:
            return True


        for i in range(1, len(s2)-len(s1)+1):
            dict_s2[s2[i-1]] -= 1
            dict_s2[s2[i+len(s1)-1]] += 1
            if dict_s1 == dict_s2:
                return True
        return False


    def checkInclusion3(self, s1, s2):
        if len(s1)>len(s2):
            return False

        dict_s1 = {}
        for each in s1:
            if each not in dict_s1:
                dict_s1[each] = 1
            else:
                dict_s1[each] += 1


        for i in range(len(s2)-len(s1)+1):
            dict_s2 = {}
            for each in s2[i:i+len(s1)]:
                if each not in dict_s2:
                    dict_s2[each] = 1
                else:
                    dict_s2[each] += 1

            if dict_s1 == dict_s2:
                return True

        return False



s1 = "adc"
s2 = "dcda"
# s1 = "trinitrophenylmethylnitramine"
# s2 = "dinitrophenylhydrazinetrinitrophenylmethylnitramine"
# s1 = "hello"
# s2 = "ooolleoooleh"

# s1 = "cgzvjlgigiosbizrtoyxexeijhqzzgbwxnmyhmanpaagjblooflawusyjiayocqhpxkybgkkybkostijmntcaxpjrfrvirvwdvlcrnrdsceldnhihrftexsdykkzcbelecdjhnwfuvnwwyxvowugdhpxfbigotfajpitxuvvcmbiipjzctrrlyxswgcvkaklfkocmathfdsgddmtstzqedazztmutaqgyiywsufcgejubzsuwcawpxwwdnzfvkpbdjuvhkrifzdtzpssbvqetzejjpdfzxczfnfoucfkvyspmpscpljmchrsfdtfcyvhfyqiaxfqdmewxtwavbxreeogxeelvrashuelrkrmxmdxriayxfmhfmxelwbydycfornyqpuhjrbgbukotgtgbtlnqljjxktnysnayiutkxuzdimbaocjymgledptwavfhlnauiafqiaoyngspnmttcxkgzufpvfvfulclgqekmehwqmfqtcrtvkfnjifrhmrsbcixlopgxkrgwnqjdhrftrwqmnfgjhwmbbmbnuawyjliarjgafybqvcigmpiyqguiwzvthtwqjvwmgfxvfwcyxizavpwwwuoqzhjyjxnjxyzpdmajxtckzdkklipdldzobgjnhyrcexggtjbilqrnfgvmtwrvhxsuysxyuumnxaucvkuafpbegihgcsuhfqqljrxrquaqpjmsegzisqogtvxcqfhnrxedovyjgyknqlfmdlpfbcyfrdokvlzlgbsnajwgnybmutvljqwovppctbadmkmujpwnggqbrcqmjbdaodixjsozzrmgoycpfkhwomujbuxqdyjmrqbchhfpwgbigboxseknxdptgoejsgewykoszssnnwaocaodqsghprzqbtnfosgotvdwxzwhjdlqhlwgidlrdudgwkgrtzdxjlhbkdjkjxjvmkvdimdeejvsmqjkagffrfsdspstowzcablbtcbpdovfinpyatkgcrzotmtztiyqnxycsawmdpfdeubekhzktgnqabfhqkfrszwpaylarurklzrfjeruqpjhhjibojcovcbccbscgwwjkixhufvbmrbbcbjiaxhhryqgbbpbzwbbbyxukrervckfislgwunqbyzandfqlsturgrssnzneqtgbsrfugstirqholqmftjacnqapjdxzrcpqfnkiuaqeyawhobemdnkshevtkywueowgekedmjdledcddtoomnkkzgvyqbonynqlakhcxynsfoxjlkevqscltkyroiiymzcxvmvhtojspzwezdxabuxuhhrgeynczmnujzglzhgywtpbyygwvazmqbcnlbjwcyzkurnsrvuxltsymrvoonasiquqvtgcffaphsfklonlsdvrmmobdafchuyntcciugpfgkuszgwrcfkbpfztiwpcczlnjoabxvtkldmtyjlbhorvhiuvzqidypyzwxqjefdhztbgcunthxzimaszfvzzfbnydxsmnplqgtrkcbadmvbqlonrxdgxpunwptatdvgxnybmviiwdrkcplezholphdenmvywilaqfujnmbeydvovytlmzpjalkekwbljwvrmemfcthyickamqdszdglrsapjjhehbiqoxhgynfyypljxhpfjxlckfxvhetcylewtnbhvgvhbpsmftgzsrzawwcunjdarwdgsqrihyshnraiizbsavcdqmjvezehjjgaxnmffdtapkzbhimygljaimqncsrynjzvkdcenndicaxnorrcbhvkgrouchpzqxtchmqabktglnjbpxhuroxjxskfppkyzbsvkenecglzbgvkxdpkjoykcsobkjnzwhbyycvkxwdwqbfzjeoakbadlaekmqgdxbojwpvkftckuparzpeyytdowcxrupeoidlirdqseqhkpfxcvfuuyqybgosfppscdtwetliojdztckjarmlkmtpuhqfhshdwummaphq"
# s2 = "vnndchsddonunovgxxlrrdtnfjidmocdrdcnousrajalpsgvxolzhujffwszxhqhojtmdluwdrzwqwqvbebztgghadtdroxujmzwmftiwamymwmpysqwffjuxtdebqoglbqobxfixdlircftggnezxyxrjzytffudihaespkhdpeqnalqohjqtypsobhrxtovxskqvtdqulgaeozlxazpubdveorkytajakzagxmhrlcvfwyuteboazjnecgrggpmmxplndhbvkhmkaozlqpgxenkchjjtaegwfcbquxlsldlbxzyfwahdpybheugrysnbjizbpgpwzwfdnriscqlrndkvibkqczjbiwkahypuujuexwtbtiqpnixwcslojlowxxjhpxvmxssciyhxpbmfpoeiizuhlkswctwkzguwyvyqvtemnerodalfuocyaduvyjwcgyxtcdhggskcdazjsqnowkkklmnocgrjpgrwdwjbhvvwtgfuialbafnycigyhnphhvnibinvadcoprwdnreuwukosnlatsymuqxtgdvsrvmercfpfaaeszkhknurpqxhyyxclzvzjqkztoqrpszcmhbcdvxwbdokmflzcsepejdemzvtzhtkmhhjhducxxijvgjidjaemzwkeyggircxivxyxcogasotyfnuamfavpkcjbnvxddhyiiybwkqobmzuzmegdiqvzjptiwhujpndvxzlaclqsemhtqwufeonsdjgnbkkjjsyxtpdytfsgpmknjibjyxctwmprbcyjhlfiyaofvjryiicpoaxeonayvztnkvzpoprnbdtwllozlqyedvnezxxxuspenwxjekkgaeajhxriahqcutakhifqkzgcjldlkbxapqrwvwshpyvnbukblgcdyyhikloslaxrsfrkwexzbrndopgnwejltpdiiwykwfymmwtsbjcvtmnakjyeqcbcbdtcuxuueaxzurixojxqdfcsdmfejajqlissfkkowchuyabccuazveqmegrtdnsoqsqxgmilxnyewpkiheajdvcnyjuuuvhonjumnshoinriazaxrqizrkuhyadjmkwdizkuamgseqibgnhgovccxmgtcywroxctticxbmvvqenvmuzdobfcxqffzgcojdhvvvkgajmuelevryxxjcvfbgpztrpzjpmttwjalllbltzmfqiwoodlvnnoviwiotmpjkjwfdnjfcsylhtioszxytvkkhrunwqxuivzukynbrdjryxkivngsecgskxhtpffrvfpwrpcythjbjdjocxcaemznunyhhrvcchmubozsqnfbgwrtzhhaprjkiwwrxzggkamvzdeidbckwyctuspdmfjhhrujobvvzuhhimutzlqfleimwechdemrztldrqwtevkbmttsdxcpmkzogegytvtrwevzbvszsxpohqqndstnstnaltilpeqdixpokcgzvjlgigiosbizrtoyxexeijkqzzgbwxnmyhmanpmagjblooflawusyjiayocqhpxkpbgkkybkostijmntcaxpjrfrvirvwdvlcrnrdsceldnhihrfyexsdykkzcbelecdjhnqcuvnwwyxvowugdhpxfbigotfajpitxuvvcmbiipjzctrrlyxswgcvkahlfkocmathfdsgddmtstzqedazztmutaqgyitwsufcgejufzsuwcawpxwwdnzfvkpbdjuvhkrifzdtzpssbvqetzejjpdfzxczfnfoucfkvyspmpscpljmchrsfdqfcyvhfyqiaxfqdmewxtwavbxreeogxeelvrashuelrkrmxmdxriayxfmhfmxelwbydycfornyqpuhjrbgbukotgtgbtlnqljjxktnysnayiutkxuzdimbsocjyagledptwavfhlnauiafqiaoyngspnmttcxkgzubpvfvfulclgqekmehwqmfqtcrtxkfnjifrhmrsbcixlougxkrgwnqjdhrftrwqmnfgjhwmbbmbnuawyjliarjgafylqvcigmpiyqguiwzvthtwqjvwmgfxvfwcyvizavpwwwuoqzhjyjxnjxyzpdmajxtckzdkklipdldzobgjnhyrcexggtjbilqrnfgvmtwrvhxsuysxyuumnxaucvkuafpbegihgcsuhfqqljrxrquaqpjmsegzisqogtvxcqfhnrxedovyjgykntlfmdlpfbcyfrdokvlzlgbsnajwgnybmutvljqwovppctbadmkmujpwnggqbrcqmjbdaodixjsozzrmgoyfpfkhwomajbuxqdyjmrqbchhfpwgbigboxseknxdptgoejsgewykoszssnywaocaodqsghprzqbtnfosgotvdwxuwhjdlqhlwgidbrdudgwkgrtzdxjlhbkdjkjxjvmkvdimdeejvsmqjkagffrfsdspstowzcablbtcbpdovfinpyutkgcrzotmtztiyqnxycsawmdpfdezbekhzktgnqabfhqkfrszwpaylarurklzrfjeruqpjhhjibojcovcbccbscgwwjkixhpfvbmrbbcbjiaxhhryqgbbpbzwbbbyxukrervckfislgwunqbyzandfqlsturgrssnzneqtgbsrfugstirqholqmftjacnqapjdxzrcpqfnkiuaqeyawhobemdnkshevtkywueowgekedmjdledcddtoomnkkzgvnqbonynqlakkcxynsfoxjlkevqsyltkyroiiymzcxvmvhtojspzwezdxabuxuhhrgecnczmnujzglzhgywtpbyygwvazmqbcnlbjwcyzkurnsrvuxltsymrvoonasiquqvtgcffaphsfklonlsdvrmmobdafchuyntcciugpfgkuszgwrcfkbpfztiwpcczlnjoabxvtkldmtyjlbhorvhiuvzqidypyzwxqjefdhztbgcunthxzimaszfvzzfbnydxsmnplqgtrkcbadmvbqlonrxdgxpunwptatdvgxnybmviiwdrkcplezholphdenmvywilaqfujnmbeydvovytlmzpjalkekwbljwvrmemfcthyickamqdszdglrsapjjhehbiqoxhgynfyypljxhpfjxlckfxvhetcylewtnbhvgvhbpsmftgzsrzawwcunjdarwdgaqrihyshnraiizbsavcdqmjvezehjjgaxnmrfdtapkzbhimygljaimqncsrynjzvkdcenndicaxnorrcbhvkgrouchpzqxtchmqabktglnjbpxhuroxjxskfppkyzbsvkenecglzbgvkxdykjoykcsobkjnzwhbyycvkxwdwqbfzjeoakbadlaehmwgdxbojwpvkftckuparzpeyytdowcxrupeoidlirdqseqhkpfxcvfuuyqybgosfppscdtwetliojdztckjafmlkmtpuhqfhshdwummaphqccfbvtdzgqhgxefzzpggjsilrfchvpzmkmmdxncnqiauqkpxldmynhhqceijcmucekiqtojnotkaqrjpdhxdpxhtabmxnszocainqyzuciyktazyksdvrcerptpjrbkszgehypijcqmvpezufyhscxgowkuhexfikfqdkxemkkowkfofxskwyumvmfvpparszcldalecfmkltqmxubmbmbnanciofqaxxz"
s = Solution()
print(s.checkInclusion2(s1, s2))
print(s.checkInclusion3(s1, s2))