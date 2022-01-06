class Solution:
    def carPooling(self, trips, capacity: int) -> bool:
        passagerIn,passagerOut=dict(),dict()
        for i,from_i,to_i in trips:
            if passagerIn.get(from_i) is None:
                passagerIn[from_i]=i
            else:
                passagerIn[from_i]+=i
            if passagerOut.get(to_i) is None:
                passagerOut[to_i]=i
            else:
                passagerOut[to_i]+=i
        check_points=list(set(passagerIn.keys()).union(set(passagerOut.keys())))
        check_points.sort()
        for point in check_points:
            capacity+=passagerOut[point] if passagerOut.get(point) is not None else 0
            capacity-=passagerIn[point] if passagerIn.get(point) is not None else 0
            if capacity<0:
                return False
        return True

