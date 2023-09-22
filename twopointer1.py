'''
투포인터 이동 원칙
sum > N : sum = sum - start_index; start_index++;
sum < N : end_index++; sum = sum + end_index;
sum == N : end_index++; sum = sum+ end_index; count++; 
'''

n = int(input())
count = 1           # 갯수
start_index = 1     
end_index = 1
sum = 1

while end_index != n:
    if sum == n:         
        count += 1
        end_index += 1
        sum+= end_index
    elif sum > n :
        sum -= start_index
        start_index +=1 
    else :
        end_index +=1
        sum+=end_index
