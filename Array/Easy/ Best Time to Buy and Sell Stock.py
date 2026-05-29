class best_time_to_buy_and_sell_stock:
    def maxprofit(self,nums):
        buy = nums[0]
        profit = 0

        for i in range(1,len(nums)):
            if nums[i]<buy:
                buy = nums[i]
            else:
                profit = max(profit,nums[i]-buy)
        return profit
    
if __name__ == "__main__":
    nums = [7,6,5,4,3,2,1]
    print(best_time_to_buy_and_sell_stock().maxprofit(nums))
                