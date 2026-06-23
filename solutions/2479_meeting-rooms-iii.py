# Problem: https://leetcode.com/problems/meeting-rooms-iii
# Runtime: 796 ms

from heapq import heappush, heappop
from collections import deque

class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        events = [] # heap
        meetingLengths = {}

        for i, (start, end) in enumerate(meetings):
            heappush(events, ((start, float('inf')), i))
            meetingLengths[i] = end - start

        meetingCountByRoom = {i : 0 for i in range(n)}
        meetingQueue = deque()
        roomQueue = [i for i in range(n)]
        heapify(roomQueue)

        while len(events) > 0:
            (time, roomVal), meetingId = heappop(events)

            isStart = roomVal == float('inf')

            if isStart:
                if len(roomQueue) > 0:
                    room = heappop(roomQueue)
                    meetingCountByRoom[room] += 1
                    heappush(events, ((time + meetingLengths[meetingId], room), meetingId))
                else:
                    meetingQueue.append(meetingId)
            else: # end event
                if len(meetingQueue) == 0:
                    heappush(roomQueue, roomVal)
                else:
                    newMeeting = meetingQueue.popleft()
                    meetingCountByRoom[roomVal] += 1
                    heappush(events, ((time + meetingLengths[newMeeting], roomVal), newMeeting))
        
        # print(meetingCountByRoom)

        results = meetingCountByRoom.items()
        maxMeetings = max([x[1] for x in results])
        for idx, val in results:
            if val == maxMeetings:
                return idx