def Profit_max(k,prices):
    # if not prices:
    #     return 0
    
    # n = len(prices)
    # if k >= n // 2:
    #     return sum(max(prices[i+1] - prices[i], 0) for i in range(n-1))
    
    # # Khởi tạo mảng lưu lợi nhuận của k giao dịch gần nhất
    # profits = [0] * k
    # for i in range(n):
    #     # Tính lợi nhuận cho từng giao dịch tại ngày i
    #     for j in range(k-1, -1, -1):
    #         profits[j] = max(profits[j], prices[i] - (prices[j-1] if j > 0 else 0) + (profits[j-1] if j > 0 else 0))
    
    # return profits[-1]
    if not prices:
        return 0

    # Khởi tạo một danh sách các khoảng cách giữa các điểm mua và bán.
    transactions = []

    # Tìm tất cả các khoảng cách giữa các điểm mua và bán.
    for i in range(len(prices) - 1):
        if prices[i + 1] > prices[i]:
            transactions.append(prices[i + 1] - prices[i])

    # Sắp xếp danh sách các khoảng cách giảm dần.
    transactions.sort(reverse=True)

    # Lấy tổng của k khoảng cách có giá trị lớn nhất.
    max_profit = 0
    for i in range(k):
        if i < len(transactions):
            max_profit += transactions[i]

    return max_profit


k = int(input())
a = []*0
prices = [int(x) for x in input().split()]
print(Profit_max(k,prices))
