def isPalindrome(s):
    """
    :type s: str
    :rtype: bool
    """
    # print(list(filter(str.isalnum, s.lower())))
    s_list = list(s)
    print(s_list)
    flag1 = True
    changable1 = True
    flag2 = True
    changable2 = True
    i = 0
    j = -1
    while (i - j < len(s_list)):
        if s_list[i] != s_list[j]:
            print("not equal at",i,j)
            if changable1 == False:
                flag1 = False
                break
            else:
                if s_list[i + 1] == s_list[j]:
                    changable1 = False
                    i = i + 1
                    print("i+1")
                # elif s_list[i] == s_list[j - 1]:
                #     changable1 = False
                #     j = j - 1
                #     print("j-1")
                else:
                    print("no way")
                    flag1 = False
                    break
        else:
            # equal
            pass
        i += 1
        j -= 1
        print(i,j)

    if flag1 == True:
        return True
    else:
        i = 0
        j = -1
        while (i - j < len(s_list)):
            if s_list[i] != s_list[j]:
                print("not equal at", i, j)
                if changable2 == False:
                    flag2 = False
                    break
                else:
                    if s_list[i] == s_list[j - 1]:
                        changable2 = False
                        j = j - 1
                        print("i+1")

                    else:
                        print("no way")
                        flag2 = False
                        break
            else:
                # equal
                pass
            i += 1
            j -= 1

    if flag2 == True:
        return True
    else:
        return False

    # return flag




# print(isPalindrome("cupuufxoohdfpgjdmysgvhmvffcnqxjjxqncffvmhvgsymdjgpfdhooxfuupucu"))
print(isPalindrome("kalrggkgbqyiwuqeqvkvggeaejigtztdwyqrsserhyjqplauvuckmshpeyxacpcrtdaufaqfcspllfiirnxphsllrgkujfvgejcqrrewwgdzzmyzovswtgordbvogffiysscnqmccnknaubiqlzdijygksqnfrvylzbfyeujdzeygefviujwfgmmshfigzsrdhtmltdfynxlvggkoxpfbitncjitqauwpqkfjwhxfvdihznlqwdvuzvdzovyursfeozqbjhqmmzhorqsoruwmuipshwpmkzzjcolfxvehzpgqsevjpqnjchglmacbdddgeshpksncgohjhtexojkfjwebbdzdfvzlsfhuyvtttiljmydrkgpuyttktvnixvhxdbhomkjpctkqdceakjlqphrvsnkahcivuemeqxtleeomlzxjvfiqdebgzxutjkmgznwvxrgtxczlovndkmduoptbvpzvvymlzlphkgqddgsdgcgfmegmjqpciknjbzopxbpovkvtamxbrjbjvxtivepwgezrfraaxynhzptytzitqiblbleculrcjlfqczhfdtdeqqcnyqtkeydtgzgbetxlqaqzkpzclygmtyeabsgsnpcwwdvexdjymkxjvslgxiodcdeasmidbfencwqipwrdjyrnzoeqnapttppqvrkcqratkwfgetxklgaksrzutyoslveckymqdoktsexdlrvwvovlgrknqkbaeofjdenvfxfwzarkaxtamxukbyigbeggdlqscxkpmxwrxnjubynvzcpemldeqwuorveflbovgmxrtddscurdudxbdtovopcnicljeqzzjumhviwghjyxmilvwkrqogddkrsusymxigozzuurqhofemnaoemppzorperpnvtlnuvbcjjbuihnwlpkonovjzjihboyhrdkjwlotdczlwgwdpozistldzdsnrocafthydiwgiurewvsrszmbwhnzsprcxwggwxcrpsznhwbmzsrsvweruigwidyhtfacornsdzdltsizopdwgwlzcdtolwjkdrhyobhijzjvonokplwnhiubjjcbvunltvnpreprozppmeoanmefohqruuzzogixmysusrkddgoqrkwvlimxyjhgwivhmujzzqejlcincpovotdbxdudrucsddtrxmgvoblfevrouwqedlmepczvnybujnxrwxmpkxcsqldggebgiybkuxmatxakrazwfxfvnedjfoeabkqnkrglvovwvrldxestkodqmykcevlsoytuzrskaglkxtegfwktarqckrvqppttpanqeoznryjdrwpiqwcnefbdimsaedcdoixglsvjxkmyjdxevdwwcpnsgsbaeytmgylczpkzqaqlxtebgzgtdyektqyncqqedtdfhzcqfljcrlucelblbiqtiztytpzhnyxaarfrzegwpevitxvjbjrbxmatvkvopbxpozbjnkicpqjmgemfgcgdsgddqgkhplzlmyvvzpvbtpoudmkdnvolzcxtgrxvwnzgmkjtuxzgbedqifvjxzlmoeeltxqemeuvichaknsvrhpqljkaecdqktcpjkmohbdxhvxinvtkttyupgkrdymjlitttvyuhfslzvfdzdbbewjfkjoxethjhogcnskphsegdddbcamlghcjnqpjvesqgpzhevxflocjzzkmpwhspiumwurosqrohzmmqhjbqzoefsruyvozdvzuvdwqlnzhidvfxhwjfkqpwuaqtijcntibfpxokggvlxnyfdtlmthdrszgifhsmmgfwjuivfegyezdjueyfbzlyvrfnqskgyjidzlqibuanknccmqncssyiffgovbdrogtwsvozymzzdgwwerrqcjegvfjukgrllshpxnriifllpscfqafuadtrcpcaxyephsmkcuvualpqjyhressrqywdtztgijeaeggvkvqequwiyqbgkggrla"))

