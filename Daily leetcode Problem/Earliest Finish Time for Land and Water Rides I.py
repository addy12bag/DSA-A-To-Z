def earliestFinishTime(landStartTime, landDuration, waterStartTime, waterDuration):
        res = float('inf')

        for i in range(len(landStartTime)):
            for j in range(len(waterStartTime)):
                
                
                finish_land = landStartTime[i] + landDuration[i]
                start_water = max(finish_land, waterStartTime[j])
                total1 = start_water + waterDuration[j]

               
                finish_water = waterStartTime[j] + waterDuration[j]
                start_land = max(finish_water, landStartTime[i])
                total2 = start_land + landDuration[i]

                res = min(res, total1, total2)

        return res
    
if __name__ == "__main__":
    landStartTime = [2,8]
    landDuration = [4,1]
    waterStartTime = [6]
    waterDuration = [3]
    print(earliestFinishTime(landStartTime, landDuration, waterStartTime, waterDuration))

    