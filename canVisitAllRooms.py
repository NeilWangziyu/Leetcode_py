class Solution:
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        room_list = [False for _ in range(len(rooms))]
        room_list[0] = True
        key_list = []
        check = 1
        for each in rooms[0]:
            key_list.append(each)

        while(key_list):
            check_this_room = key_list.pop(0)
            if room_list[check_this_room] == True:
                continue
            else:
                room_list[check_this_room] = True
                check += 1
                if rooms[check_this_room]:
                    for each in rooms[check_this_room]:
                        key_list.append(each)
        # print(room_list)
        # if False in room_list:
        #     return False
        # else:
        #     return True
        if check == len(rooms):
            return True
        else:
            return False







rooms = [[1,3],[3,0,1],[2],[0]]
s = Solution()
print(s.canVisitAllRooms(rooms))