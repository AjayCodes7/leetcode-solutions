class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        # # preprocessing
        # meetings.sort()
        # i = 1
        # while i < len(meetings):
        #     if meetings[i][0] <= meetings[i-1][1]:
        #         meetings[i-1][1] = max(meetings[i-1][1],meetings[i][1])
        #         meetings.pop(i)
        #         continue
        #     i += 1
        # print(meetings)
        # sheduled = 0
        # for meeting in meetings:
        #     print(meeting)
        #     print((meeting[1]-meeting[0]+1))
        #     sheduled += (meeting[1]-meeting[0]+1)
        # return days - sheduled
        meetings.sort()
        free = meetings[0][0] - 1
        prev_day = meetings[0][1]
        i = 1
        while i < len(meetings):
            if prev_day < meetings[i][0]:
                free += meetings[i][0] - prev_day -1
            prev_day = max(meetings[i][1],prev_day)
            i += 1
        free += days - prev_day
        return free