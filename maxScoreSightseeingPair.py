class Solution:
    def maxScoreSightseeingPair(self, A):
        if not A:
            return 0
        if len(A)<2:
            return 0
        res = 0
        for i in range(len(A)):
            for j in range(i+1, len(A)):
                score = A[i] + A[j] + i - j

                if score > res:
                    res = score
                    print(score, i, j,A[i], A[j])
        return res

    def maxScoreSightseeingPair2(self, A):
        """
        双指针
        :param A:
        :return:
        """
        if not A:
            return 0
        if len(A)<2:
            return 0
        ans = A[0] + A[1] - 1
        s = max(A[0], A[1] + 1)
        for j in range(2, len(A)):
            ans = max(ans, s + A[j] - j)
            s = max(s, A[j] + j)
        return ans

    def maxScoreSightseeingPair3(self, A):
        """
        双指针
        :param A:
        :return:
        """
        if not A:
            return 0
        if len(A)<2:
            return 0
        low = A[0]
        res = 0
        for i in range(1, len(A)):
            if low + A[i] - i > res:
                res = low + A[i] - i
            if A[i] + i > low:
                low = A[i] + i
        return res



if __name__ == "__main__":
    A = [509,614,349,955,828,259,470,418,934,630,243,91,426,687,495,48,203,321,805,835,4,915,723,799,869,49,596,974,534,787,835,853,622,46,459,954,348,391,136,406,597,48,113,434,855,523,576,962,19,132,446,965,238,894,280,238,416,742,713,833,429,191,289,292,649,725,584,953,576,894,251,222,472,129,922,201,856,685,259,836,87,690,778,123,975,116,576,197,740,997,573,356,203,281,334,651,521,287,410,175,977,853,336,813,148,298,667,829,235,764,62,133,551,125,106,512,439,998,200,32,472,761,135,284,284,495,313,406,768,226,945,215,513,207,739,721,834,213,66,226,496,381,72,853,310,346,724,858,826,110,650,902,357,325,904,655,954,181,778,143,322,930,655,584,146,879,633,520,649,767,65,240,893,899,499,884,646,568,308,343,357,98,883,549,590,781,756,673,769,495,176,380,156,116,122,149,888,877,50,899,82,618,977,402,782,309,221,75,699,570,977,408,501,390,19,70,345,713,38,199,399,709,983,501,408,633,40,901,968,676,731,70,267,76,159,733,855,35,698,529,937,722,330,461,892,596,903,775,307,110,52,254,598,649,319,572,420,916,267,804,40,852,370,483,858,617,859,302,979,390,889,595,610,844,920,350,284,113,271,119,645,599,425,432,560,476,44,785,50,452,225,870,583,790,141,444,976,191,314,622,481,503,350,56,946,597,726,116,105,156,30,397,105,259,703,754,573,949,937,571,459,311,254,952,47,815,258,157,141,41,439,683,658,834,921,515,474,22,921,268,319,298,297,87,651,482,481,226,548,266,748,995,37,1,585,983,182,681,142,506,3,299,84,902,514,67,243,788,962,852,517,639,698,39,235,772,543,90,948,683,800,339,359,696,396,441,893,358,547,519,469,875,457,655,717,370,326,622,944,315,226,665,424,414,462,486,57,78,525,627,90,671,793,608,554,861,674,301,249,376,77,418,866,237,275,130,659,955,168,53,595,309,23,759,540,478,600,696,311,948,946,429,845,813,921,147,685,419,467,240,538,801,919,578,516,503,709,367,210,64,785,634,384,497,575,62,381,153,208,603,131,787,289,291,310,187,814,515,811,583,950,139,509,840,126,301,8,995,800,186,413,133,598,50,322,584,642,297,924,284,151,403,54,921,944,132,819,441,749,524,825,397,589,470,440,64,49,174,490,531,512,443,838,974,463,832,800,703,368,521,194,699,246,924,428,899,228,139,172,766,29,403,110,113,58,50,874,751,208,724,596,626,619,727,552,94,78,143,259,696,819,330,275,267,9,43,804,756,648,697,150,795,893,810,944,469,181,665,775,739,841,278,879,531,929,322,434,369,245,936,421,803,136,521,1000,226,601,560,840,457,179,309,10,62,445,619,431,152,757,576,981,560,279,221,874,996,681,282,229,829,410,677,62,623,320,570,22,326,817,40,866,380,667,955,621,654,397,315,193,916,539,344,455,128,337,636,254,622,525,142,20,838,889,192,244,695,635,670,203,362,559,443,604,92,297,140,460,926,871,790,115,293,401,120,319,299,867,907,259,706,357,670,626,718,608,412,699,27,36,155,453,103,105,882,21,460,585,214,490,577,180,424,99,245,784,19,630,511,398,430,301,403,803,947,606,910,742,517,539,165,832,174,97,178,925,639,277,672,142,901,142,705,425,38,473,570,519,236,847,304,314,633,332,518,572,267,533,297,72,763,903,790,281,15,13,503,122,784,257,263,444,255,303,263,226,320,536,841,777,754,295,953,7,287,173,638,229,106,632,870,622,531,851,115,939,116,5,956,655,172,981,699,182,463,546,225,631,944,31,854,883,23,365,954,634,39,171,230,677,76,672,824,191,571,306,561,548,687,794,637,800,458,776,842,229,235,935,707,706,624,991,887,837,172,832,712,133,281,734,317,291,655,138,224,207,716,290,609,162,825,848,985,116,779,774,258,487,776,177,360,483,698,856,595,649,744,637,770,927,890,124,35,917,141,70,457,257,796,418,792,181,751,347,610,695,857,135,615,121,745,838,351,424,553,635,380,731,88,182,650,468,213,390,36,741,299,844,214,460,318,78,765,650,160,838,349,237,499,716,483,656,835,305,2,992,733,326,469,272,97,504,911,83,355,284,586,246,346,246,10,711,91,124,671,902,540,943,384,776,203,365,645,421,735,519,60,114,958,723,461,251,380,600,852,696,343,364,171,110,918,296,157,357,615,373,788,236,285,8,275,623,249,340,402,442,331,270,717,287,12,564,372,743,31,938,787,824,203,343,988,625,554,9,639,694,635,503,753,867,367,544,572,11,753,216,914,33,251,469,467,559,736,485,49,320,440,850,56,989,810,24,303,625,58,206,1000,720,653,183,728,810,218,723,447,558,342,788,380,529,859,474,989,950,199,171,368,847,126,116,976,176,394,228,858,565,420,563,661,419,603,694,804,827,475,360,902,364,652,958,663,304,588,417,201,608,37,377,816,14,333,28,1,459,555,647,887,948,164,592,736,932,319,383,365,788,401,590,415,903,279,337,830,134,567,469,581,61,556,528,16,991,890,577,319,225,510,555,76,923,284,190,862,777,375,718,19,43,992,640,642,596,925,1000,25,54,573,15,594,309,21,959,793,441,290,60,950,730,608,361,407,66,731,639,149,685,502,213,30,830,701,232,683,816,542,325,4,147,352,259,530,515,20,534,246,490,386,72,651,419,99,208,306,875,616,132,21,966,868,102,968,120,601,266,626,846,663,72,705,310,326,846,371,89,216,393,999,145,800,329,485,332,801,801,435,765,753,319,719,750,825,749,552,33,750,999,538,195,621,523,118,172,827,4,197,75,357,416,878,52,902,622,710,73,145,492,833,485,477,960,776,386,508,402,754,321,775,328,330,467,614,443,33,903,499,631,338,761,796,229,519,765,997,978,558,149,609,743,625,219,331,522,769,30,69,569,726,280,603,422,613,876,92,931,768,839,735,51,183,480,910,469,365,949,365,392,263,41,167,648,610,212,322,575,391,616,218,174,867,883,569,718,352,91,168,337,948,386,449,868,229,624,816,815,909,555,52,863,246,682,124,415,305,160,982,623,955,645,283,220,331,609,973,534,839,89,943,747,927,860,293,794,699,418,803,294,988,380,852,258,928,227,896,885,284,106,378,266,957,830,473,548,686,263,500,921,203,75,6,642,692,332,428,541,371,21,850,926,191,675,716,775,887,361,932,948,52,144,859,866,531,34,443,772,62,809,899,754,135,265,788,579,682,780,543,355,690,163,534,352,882,527,759,407,944,469,845,427,14,819,920,619,968,94,175,432,284,530,468,935,800,584,228,164,556,470,770,887,581,538,960,378,126,152,326,34,169,964,489,454,642,757,162,574,880,977,77,425,499,868,176,239,85,423,2,578,441,850,354,588,570,746,638,139,732,740,575,291,736,706,743,892,633,717,278,407,489,605,306,23,718,716,198,651,521,170,87,676,997,572,870,864,725,544,765,125,699,76,382,355,258,308,391,15,24,146,575,106,671,726,932,336,436,893,63,446,766,849,854,903,292,377,84,269,636,672,172,123,508,15,198,858,972,135,872,140,343,950,248,401,387,116,331,370,525,902,466,664,842,479,438,633,90,511,507,926,845,496,688,355,658,795,254,52,664,286,52,960,986,990,839,502,506,295,720,847,720,629,789,55,650,427,64,938,338,670,165,704,363,192,880,153,45,906,543,850,473,835,829,409,961,91,314,968,542,93,243,854,74,712,351,521,959,138,983,516,865,876,906,280,38,971,500,53,659,769,525,276,213,172,735,725,36,969,759,830,565,433,552,513,160,116,212,179,449,256,429,479,716,397,404,757,20,961,510,197,902,575,777,956,393,512,750,485,375,269,520,622,74,890,438,872,277,335,491,776,770,429,560,794,191,840,910,799,166,721,86,55,192,673,401,645,429,225,660,730,561,74,806,759,51,263,310,842,249,520,943,306,468,80,864,668,708,930,731,208,645,486,260,686,536,713,649,276,460,909,736,459,775,88,359,804,999,574,951,45,228,442,509,409,840,750,55,217,28,631,683,784,593,202,887,391,229,660,353,559,219,809,577,245,281,706,161,940,669,512,122,729,10,332,630,80,445,664,27,971,323,517,405,414,910,347,827,806,98,250,207,174,545,708,690,598,263,479,854,484,994,727,577,862,351,197,307,35,183,600,794,789,416,776,757,406,31,826,446,119,843,819,620,818,589,611,460,833,763,758,610,549,442,740,345,655,192,900,103,702,499,243,661,34,406,151,768,273,62,791,765,974,134,424,396,481,43,170,505,56,184,419,587,888,318,763,104,553,289,449,119,280,395,919,709,132,162,739,298,293,621,670,889,962,160,739,663,349,16,16,548,853,173,534,29,178,269,558,636,245,564,508,604,914,989,504,249,815,860,356,636,821,648,197,117,623,991,639,152,890,746,763,207,30,211,237,758,591,171,490,519,829,385,28,672,693,161,868,933,310,944,633,129,822,279,147,312,865,129,451,831,966,821,429,935,893,27,749,274,607,172,19,174,612,324,851,699,214,387,99,17,960,688,311,628,775,344,411,228,362,24,310,810,930,666,627,447,741,827,845,163,985,256,924,793,255,14,251,147,785,211,131,229,370,890,507,523,366,383,444,831,16,206,16,872,697,751,976,154,297,920,653,774,170,699,143,686,299,105,820,66,45,423,136,311,637,76,782,560,439,164,234,225,917,208,610,769,659,569,496,181,626,110,983,394,71,527,665,51,383,211,161,617,413,696,268,216,650,812,280,82,733,653,803,864,838,907,671,918,98,235,578,353,321,498,589,909,503,775,327,607,929,567,807,326,46,503,119,84,942,397,103,383,801,226,856,851,907,217,221,726,304,166,574,8,61,250,371,273,730,538,833,699,584,770,744,559,485,939,930,670,388,701,638,998,657,428,280,700,695,165,748,288,5,236,642,516,391,603,614,797,244,973,221,959,409,211,540,346,159,555,504,599,254,246,125,343,261,710,445,481,98,594,646,145,776,760,293,333,125,973,639,279,171,629,924,850,925,342,666,620,872,896,151,955,489,357,899,111,647,183,801,966,641,265,38,800,524,147,121,625,536,552,674,706,235,883,467,712,748,166,119,637,710,483,177,591,357,645,66,787,820,130,396,791,476,927,516,928,556,120,632,596,281,68,304,392,204,247,884,982,911,68,825,468,965,763,384,99,179,60,429,253,927,22,805,88,323,431,259,798,524,476,429,12,966,524,98,560,758,469,210,622,967,339,979,176,799,462,821,993,786,819,519,730,402,135,717,640,883,379,961,553,818,173,934,829,892,448,828,206,818,130,268,641,977,439,620,73,564,787,234,283,823,733,660,731,70,92,239,395,409,793,395,712,727,996,238,392,544,575,137,660,772,608,471,637,802,813,338,225,936,824,565,963,83,469,491,688,769,337,428,582,758,938,340,639,390,478,695,589,738,84,676,616,201,871,181,270,624,287,89,683,690,919,564,874,971,981,219,415,629,834,335,946,97,809,547,18,789,118,981,697,803,47,657,118,607,780,270,935,59,974,386,403,354,716,394,542,888,511,23,192,584,286,795,630,811,12,886,802,156,444,678,533,539,862,279,236,631,514,42,316,113,305,463,264,540,368,709,274,293,204,330,226,272,574,530,855,633,937,182,401,465,615,542,804,169,741,276,276,696,157,412,484,711,623,404,585,748,489,211,906,903,958,412,484,804,977,800,395,538,623,467,504,351,912,404,379,841,474,999,71,838,362,563,48,661,488,861,835,261,762,699,269,196,215,42,470,565,742,951,362,380,75,861,128,97,196,876,354,109,82,253,758,906,717,181,334,134,790,219,950,974,781,631,452,620,140,813,861,562,67,143,616,460,905,475,551,948,150,216,692,870,400,804,966,519,202,805,859,817,952,261,143,637,281,848,157,467,57,66,696,498,524,145,89,702,378,318,195,787,208,450,550,574,139,437,592,743,878,854,819,244,132,696,130,239,649,420,68,860,310,776,555,673,630,338,86,847,57,791,917,98,405,643,979,161,465,233,141,159,307,61,740,591,481,752,184,232,762,794,340,145,888,8,766,517,804,469,917,878,420,872,124,107,199,279,577,861,496,234,402,49,49,820,793,847,655,165,818,983,634,222,844,281,282,20,212,477,354,172,13,700,818,369,667,433,214,39,157,592,561,464,507,749,337,523,854,686,51,105,777,759,133,23,401,141,499,295,196,400,266,946,881,912,559,530,986,831,776,320,754,405,738,460,83,445,658,501,540,950,332,875,70,648,732,50,145,213,795,32,590,309,534,270,2,2,958,264,806,141,288,581,887,340,979,328,183,383,336,95,903,587,252,990,120,739,242,325,944,322,411,561,312,304,671,605,712,355,101,555,754,659,527,827,483,745,596,441,34,475,863,877,802,328,289,426,942,879,653,594,324,449,762,225,565,420,139,158,919,230,163,804,37,735,944,439,651,526,704,717,673,675,77,683,227,84,453,159,505,128,907,297,20,500,957,362,249,854,486,573,292,987,464,22,340,98,238,724,749,440,56,423,517,471,834,770,631,283,657,716,907,745,426,903,653,686,539,307,903,434,366,230,571,824,208,312,283,583,669,882,434,878,860,421,935,474,647,642,326,557,758,888,374,572,395,384,832,837,123,540,181,125,671,331,331,634,188,589,595,576,50,743,578,584,601,194,605,683,626,633,503,916,116,407,281,756,320,508,297,549,250,12,26,615,472,263,236,401,829,694,630,322,176,170,323,367,843,226,474,162,868,324,605,742,188,350,578,344,244,943,595,820,29,372,82,450,577,648,140,746,203,469,497,560,192,696,278,496,642,112,264,61,578,66,157,636,560,199,424,320,367,376,871,514,327,596,774,950,861,224,903,916,642,762,195,584,129,270,655,726,390,759,165,644,625,53,974,335,102,999,569,256,718,149,995,322,581,582,503,895,287,331,945,46,604,280,174,862,763,612,830,655,875,813,763,841,201,691,358,843,697,60,615,279,385,706,306,48,951,245,253,681,686,625,218,48,931,49,461,201,828,269,641,712,334,168,657,204,489,524,192,320,22,283,38,884,522,94,327,637,414,596,537,982,357,808,646,733,869,877,438,983,805,644,900,148,142,31,832,117,584,366,353,883,486,770,229,792,297,571,162,946,911,186,314,677,851,645,302,109,266,624,640,122,697,837,636,627,440,490,578,841,246,187,70,151,211,531,850,561,805,983,548,245,271,997,835,337,423,883,227,660,814,825,473,892,621,751,517,208,451,722,185,679,450,336,266,996,580,957,603,532,131,284,40,449,60,462,626,624,763,40,668,575,18,311,990,872,990,340,389,88,299,313,806,141,895,115,293,137,533,430,828,573,528,502,159,633,686,32,669,940,570,780,812,752,519,488,489,157,847,337,696,592,837,83,380,94,926,492,71,678,564,94,655,375,784,762,577,95,518,61,813,288,842,864,620,325,207,182,592,481,86,37,749,45,134,356,455,229,410,483,120,471,178,430,124,139,249,962,31,120,482,26,352,883,348,710,755,161,290,246,812,319,38,210,965,643,958,307,352,951,750,229,443,463,819,722,247,820,534,302,156,921,399,217,186,828,133,938,160,681,490,292,606,641,625,785,79,531,574,946,930,258,405,589,122,192,21,433,905,173,198,504,406,466,658,501,19,430,44,595,227,599,513,917,985,369,360,840,422,251,530,4,843,163,448,642,793,60,153,44,275,735,61,292,984,2,451,501,982,363,368,211,32,892,702,44,472,383,524,723,584,245,797,993,113,567,825,203,698,13,347,834,788,314,100,823,669,981,850,587,598,890,608,698,843,327,870,158,782,622,601,389,797,403,615,156,582,175,718,206,587,679,429,447,934,876,683,687,233,389,767,923,192,228,361,705,457,774,384,466,161,69,41,488,833,3,356,766,57,476,509,2,921,460,96,46,844,32,837,478,334,362,697,109,693,883,447,859,417,663,882,728,99,209,838,663,459,786,213,778,948,908,323,899,278,516,633,513,753,950,706,854,743,508,435,1,925,71,345,139,474,21,850,526,660,722,587,822,316,139,386,820,699,48,604,171,130,292,106,170,797,779,247,215,641,1000,823,870,143,741,302,531,264,897,530,320,416,937,148,34,459,303,659,269,241,353,213,754,823,133,875,580,594,165,255,844,802,947,4,539,652,873,421,304,58,515,545,169,215,674,968,380,43,396,814,336,498,647,804,902,792,245,488,448,387,839,545,227,873,933,335,202,657,874,270,92,832,465,193,672,376,689,263,710,960,727,512,42,693,276,338,114,114,173,550,945,876,934,146,275,375,273,682,842,97,606,843,469,224,146,622,818,281,671,63,163,541,466,119,726,266,493,196,869,327,31,922,268,941,251,843,689,637,407,271,820,7,486,325,409,813,860,294,99,926,919,101,56,419,754,887,422,252,327,219,92,72,787,519,451,599,712,343,595,388,309,675,333,37,275,838,185,16,630,88,445,230,47,860,736,791,551,617,602,421,1000,519,587,87,328,773,442,976,860,307,402,720,793,911,996,512,57,482,159,557,436,519,189,875,6,359,942,526,308,678,621,811,535,897,546,808,784,572,921,734,157,799,381,499,103,453,140,606,221,226,957,274,927,6,427,976,798,775,172,613,658,48,710,235,457,307,601,652,168,203,912,789,645,697,559,70,804,349,169,887,439,600,457,936,494,368,2,607,793,38,106,385,993,913,875,270,843,402,968,51,731,278,441,199,907,272,980,672,839,497,766,530,210,882,555,288,854,778,432,170,97,551,646,692,479,385,848,846,478,703,946,238,778,410,874,443,410,681,634,77,553,100,820,413,519,109,265,621,826,88,661,417,915,94,547,520,672,549,423,138,213,870,867,236,447,725,958,37,278,14,805,112,189,671,468,708,954,679,829,697,863,239,65,985,450,353,459,417,851,602,124,63,79,99,60,178,17,532,857,419,951,515,978,699,131,635,767,906,635,994,252,677,655,982,48,587,21,365,155,75,271,999,964,141,844,994,872,535,99,529,295,793,310,402,236,473,997,106,421,946,780,107,104,37,182,476,184,995,332,500,208,737,612,355,992,788,824,747,820,188,433,422,880,368,541,60,957,673,881,181,386,585,954,369,412,259,374,412,873,487,3,652,217,376,345,308,435,876,838,583,6,173,20,237,29,556,330,997,790,162,540,902,591,463,907,814,948,532,625,618,156,130,150,57,785,916,624,732,392,488,93,483,358,881,748,142,882,772,534,690,594,235,964,588,399,293,647,544,259,412,918,535,945,61,154,81,131,491,367,430,65,779,782,522,758,685,533,427,294,802,379,128,718,431,104,554,902,834,864,872,118,324,118,547,612,556,965,333,525,890,899,505,501,968,781,603,109,565,232,907,594,10,405,533,413,693,405,914,978,170,128,483,770,981,479,886,173,843,573,587,208,566,339,469,243,866,866,806,373,193,944,856,610,326,199,126,452,587,234,259,114,894,109,813,634,921,171,379,511,428,293,210,797,458,532,714,334,445,243,193,110,965,112,321,101,385,144,714,23,375,800,744,260,717,770,555,564,906,865,587,390,456,421,90,615,530,912,685,36,287,527,548,374,70,159,246,449,678,882,807,45,997,566,816,920,998,649,939,750,220,228,750,784,885,301,573,377,540,68,747,566,726,259,174,178,470,55,91,840,72,378,512,860,935,845,782,289,342,770,156,290,603,500,483,906,719,920,333,281,939,959,650,831,897,163,553,425,460,67,316,257,757,207,763,607,122,661,130,934,944,789,749,266,569,818,681,84,784,790,257,427,24,181,663,4,59,877,399,105,324,532,684,52,642,433,660,580,61,342,209,700,466,248,994,344,7,4,474,404,793,911,144,792,206,748,834,778,880,831,268,421,8,66,365,896,456,724,705,290,818,362,825,781,822,637,389,686,152,328,132,158,560,314,515,122,851,3,596,484,157,425,355,987,419,597,206,688,486,308,198,373,469,138,103,704,110,711,669,988,163,983,552,423,960,395,996,128,507,130,803,702,792,21,483,36,329,340,967,797,786,224,415,524,915,609,301,756,502,196,811,624,343,220,11,228,22,44,997,253,827,534,731,616,235,295,80,148,788,264,399,546,381,681,593,609,111,779,311,763,452,140,554,45,948,277,104,998,12,77,725,411,319,426,222,639,488,446,774,588,822,588,407,288,692,654,120,942,497,19,624,25,374,669,849,102,454,19,295,714,978,908,971,169,389,800,975,295,54,330,624,325,877,370,270,401,816,294,273,472,46,542,289,964,233,899,37,705,408,812,828,732,751,486,423,730,361,4,369,121,37,593,777,820,678,762,8,476,129,47,316,888,258,45,287,540,394,51,176,227,604,434,989,689,961,823,232,120,356,252,577,478,608,586,178,584,775,869,723,890,439,601,95,143,515,596,436,37,750,603,165,585,710,991,670,239,79,302,231,960,326,551,866,547,500,778,301,501,283,489,249,335,709,817,177,958,887,709,698,705,919,633,888,207,381,707,735,379,826,495,428,660,387,53,57,311,587,91,123,717,943,683,738,437,768,820,398,364,867,480,647,593,132,708,589,820,693,645,727,576,286,564,546,306,270,44,954,384,226,814,697,440,477,896,306,105,579,114,954,873,272,624,593,852,583,342,199,178,382,31,834,724,865,945,749,510,594,336,351,570,268,834,169,796,54,210,216,315,571,611,549,94,430,908,938,298,629,802,931,827,681,961,428,21,383,487,839,213,189,212,129,908,11,251,534,357,934,474,896,388,109,184,20,197,483,748,38,91,185,434,420,701,376,637,57,772,415,393,831,631,914,655,852,173,200,159,203,229,640,934,695,932,941,662,314,549,652,157,455,647,661,945,998,808,862,632,199,150,947,333,768,257,62,797,7,889,683,990,530,872,973,50,941,610,347,259,823,556,547,34,583,377,378,110,563,461,73,41,501,606,329,680,788,967,875,908,549,911,217,742,843,670,269,621,497,406,261,94,29,231,926,947,50,761,186,751,935,1000,738,337,881,116,388,72,916,691,71,85,619,342,760,449,147,544,353,94,826,895,687,972,509,927,971,222,871,935,740,364,44,454,848,126,746,83,684,374,341,963,936,186,100,978,431,566,462,301,799,571,360,990,498,332,755,615,870,78,765,811,165,897,651,389,703,965,210,190,325,107,609,120,4,309,279,577,252,714,350,721,366,776,153,101,833,508,738,726,745,199,481,55,55,920,266,463,811,805,604,656,969,697,602,987,138,731,182,196,157,281,80,619,913,37,469,262,125,403,957,360,225,619,410,458,653,83,4,941,751,320,476,835,165,602,51,334,355,766,883,404,837,249,352,295,610,953,537,131,688,307,856,530,866,750,717,924,547,868,354,365,307,469,643,915,413,293,951,844,792,517,200,962,309,398,116,534,561,97,6,966,561,472,91,994,345,424,499,217,5,503,770,407,732,521,697,186,691,76,601,807,733,379,134,137,587,58,480,745,856,87,939,678,557,999,150,677,273,131,555,733,21,909,723,842,377,930,364,338,626,71,952,552,811,537,220,688,930,809,360,348,577,418,4,198,976,802,896,887,67,436,206,107,809,677,177,723,162,384,201,187,248,669,846,218,452,667,294,512,349,48,158,42,61,696,94,785,969,753,467,36,363,552,640,370,470,734,541,847,109,403,792,674,766,120,318,878,106,790,573,968,493,66,220,777,391,197,979,36,292,600,677,313,448,242,891,54,186,986,666,91,841,221,18,213,815,924,504,423,420,542,139,679,17,893,338,451,811,956,928,769,402,315,159,992,684,215,185,223,779,505,163,531,363,3,517,362,524,458,55,910,968,666,889,877,594,892,930,58,268,44,993,27,644,884,798,66,470,528,202,461,159,60,693,926,460,607,826,825,202,961,908,330,813,388,992,726,607,988,50,357,772,419,872,119,276,467,370,204,15,518,456,573,447,717,856,872,141,438,485,450,526,310,327,201,839,841,747,17,245,852,139,829,561,321,184,929,814,763,526,310,785,35,39,11,480,570,191,182,162,116,666,878,996,117,274,292,263,675,485,829,190,291,230,464,244,742,979,474,954,622,914,285,606,265,663,128,883,569,974,206,281,888,739,691,295,594,32,48,488,481,184,348,129,793,8,352,367,491,330,993,717,93,73,866,444,573,740,741,662,704,342,516,979,481,509,530,747,269,18,19,688,956,767,491,646,31,202,693,590,285,774,530,98,913,190,757,491,227,654,747,695,845,366,172,752,172,775,877,1,551,113,481,132,204,134,912,176,916,139,453,521,393,748,623,759,302,900,567,76,712,742,700,727,883,308,677,878,190,206,876,726,976,245,683,6,206,387,653,931,595,111,244,681,599,602,926,768,479,690,592,979,292,963,700,567,327,759,33,520,621,128,585,799,681,116,656,806,875,794,984,471,666,846,676,894,545,942,592,751,228,658,230,597,813,19,879,79,82,386,450,325,88,217,687,530,901,972,172,334,760,557,981,481,993,638,928,360,199,151,718,870,373,964,888,524,397,181,139,126,976,538,152,896,375,31,113,439,349,660,218,273,779,93,221,226,885,210,230,885,937,902,688,685,443,389,73,290,357,603,106,821,664,960,806,595,746,82,127,668,698,654,133,735,199,303,196,671,717,177,324,237,357,771,827,49,561,520,678,412,380,560,219,847,272,115,295,266,46,920,296,331,90,205,891,251,367,723,474,268,798,796,632,432,952,900,191,924,33,450,1,898,425,773,307,56,663,180,461,722,613,18,659,18,564,120,879,70,19,522,69,388,288,957,647,629,942,39,420,751,144,327,69,852,680,665,52,515,813,294,89,508,215,147,71,98,879,889,271,478,52,769,912,987,696,217,768,663,391,240,568,584,816,266,405,837,500,552,236,293,374,532,29,51,495,217,846,86,986,169,812,127,847,231,850,129,166,594,12,476,684,622,533,841,912,28,983,211,694,944,248,448,504,490,192,78,483,683,97,697,304,911,12,49,542,369,947,969,800,626,805,239,328,322,153,215,348,995,179,432,380,598,269,763,240,187,765,174,419,252,196,60,328,415,79,467,523,479,559,715,231,97,68,666,585,648,741,906,32,832,400,48,18,332,459,73,8,145,51,53,481,650,961,703,586,92,251,654,119,667,281,898,484,231,298,15,396,484,463,991,360,317,435,602,939,557,522,422,931,313,976,440,678,454,903,114,90,325,364,89,834,39,113,337,774,55,721,197,963,61,839,131,92,825,667,511,66,308,382,830,782,760,243,426,850,417,70,381,984,601,984,747,405,502,34,876,189,260,577,256,828,248,707,269,329,420,300,942,228,879,765,570,718,251,610,594,1000,457,801,775,900,329,546,988,54,469,752,957,973,898,171,158,709,580,358,273,919,969,339,727,449,273,816,264,401,562,933,982,975,374,97,172,813,115,43,768,616,388,76,485,872,170,566,421,569,144,111,575,513,758,972,967,35,308,442,664,309,314,818,611,984,803,994,629,681,79,626,972,672,15,89,441,481,444,693,549,830,99,747,714,236,619,714,130,429,578,259,153,343,54,113,460,493,793,175,828,741,957,357,411,12,197,863,199,997,390,555,463,371,399,330,443,107,9,863,534,665,75,307,741,602,346,770,577,970,938,315,79,511,34,980,756,865,5,167,107,968,901,839,805,319,738,263,321,57,86,607,27,920,838,32,576,793,876,743,580,980,673,909,915,258,514,462,461,159,451,171,937,682,859,716,370,406,952,978,352,780,440,35,487,478,374,360,803,23,915,545,586,995,957,397,200,562,257,543,321,81,9,122,682,278,429,875,979,384,156,798,719,724,828,668,59,660,899,403,72,225,655,370,62,128,116,263,741,479,649,375,30,486,599,685,423,471,171,60,219,224,316,492,71,988,881,881,590,640,542,431,233,145,380,672,802,694,381,917,772,638,716,45,194,562,425,1000,765,212,699,170,361,412,901,564,300,80,521,926,157,60,629,483,252,166,378,665,680,473,775,53,69,325,380,834,222,660,488,932,791,338,626,366,30,754,79,564,787,141,79,75,232,288,119,573,575,406,290,868,160,479,892,91,107,340,592,463,688,606,174,23,725,132,846,488,784,967,877,471,905,880,584,991,930,921,192,112,103,869,862,410,909,248,418,915,343,566,544,94,375,419,334,347,179,794,928,413,748,416,786,752,957,845,841,481,746,900,645,924,355,34,33,850,53,37,451,144,959,396,89,874,277,121,492,579,33,243,480,377,508,218,630,197,409,629,632,444,322,1000,762,881,373,768,822,106,480,676,752,928,534,141,331,619,69,186,672,420,437,947,671,498,397,811,509,396,81,610,408,897,208,714,843,866,901,38,233,786,787,971,512,455,803,796,582,831,478,142,994,338,846,17,697,258,409,811,244,749,88,714,985,200,967,54,350,800,48,638,447,685,171,115,410,353,770,884,930,784,630,433,508,714,581,250,164,756,347,469,464,501,429,70,728,700,778,547,382,486,255,781,794,129,178,75,481,10,460,15,294,14,257,295,115,981,811,450,611,526,22,382,530,726,37,182,160,271,743,995,637,694,809,336,11,749,108,688,376,720,229,47,375,62,567,973,571,857,574,77,209,362,851,3,131,309,197,442,33,495,422,532,952,888,75,49,317,867,636,319,648,845,803,774,27,949,690,218,111,611,772,284,529,349,759,808,262,929,980,579,445,893,286,834,52,890,318,967,583,796,602,524,477,776,1,170,438,621,267,712,611,889,335,664,968,103,720,311,829,682,787,580,991,149,409,58,908,705,366,506,73,407,198,877,525,848,233,925,44,474,96,731,812,8,922,949,618,415,77,178,27,674,67,519,990,123,978,979,716,11,332,1000,71,888,296,770,673,508,845,701,407,782,398,750,574,85,842,839,42,600,555,197,869,905,456,37,747,450,641,930,626,567,243,823,386,799,709,191,446,348,659,222,788,49,678,590,547,210,796,252,974,933,13,394,717,167,781,770,919,518,884,898,57,696,453,954,293,798,105,644,916,58,141,13,320,910,300,154,385,861,606,370,519,314,501,19,185,700,475,459,230,802,11,296,967,328,10,780,55,969,865,512,38,564,731,184,510,153,362,67,387,353,190,692,184,372,373,486,363,761,993,126,197,144,340,140,111,189,598,723,272,840,353,532,233,158,851,836,923,645,391,200,978,977,166,59,934,929,604,493,717,277,113,617,595,87,828,138,936,911,261,127,898,645,33,895,915,332,905,24,1,647,139,514,124,509,273,961,493,182,72,797,952,218,778,358,522,15,228,624,148,690,597,812,517,468,209,385,312,654,261,593,407,554,865,922,740,234,218,963,809,49,806,493,400,728,21,462,16,704,820,744,468,734,871,29,422,335,988,511,497,137,456,987,234,425,887,152,839,391,741,810,867,892,680,165,829,398,386,730,787,498,977,374,462,122,966,237,632,937,700,349,511,807,93,878,908,859,471,831,124,109,57,868,857,171,457,212,161,924,882,621,11,346,465,908,49,804,144,928,721,83,556,108,180,943,16,513,320,941,27,720,333,782,365,583,832,49,505,415,326,995,969,313,630,904,677,762,262,566,595,542,219,949,423,392,655,934,430,564,508,176,410,48,754,538,602,193,258,598,174,566,290,958,810,641,314,842,24,380,955,735,600,947,927,128,658,794,254,379,710,300,757,673,69,829,424,576,303,861,981,683,223,105,163,262,977,510,39,454,715,239,250,622,309,321,852,617,42,734,20,474,796,507,498,856,246,212,562,826,459,51,855,737,844,971,279,686,599,26,796,281,430,81,377,417,867,504,522,482,518,896,428,618,233,891,2,694,412,426,17,855,425,644,770,48,352,606,370,91,491,7,522,240,350,189,35]

    # A = [3,7,2,3]
    s = Solution()

    print(s.maxScoreSightseeingPair2(A))
    print(s.maxScoreSightseeingPair3(A))
