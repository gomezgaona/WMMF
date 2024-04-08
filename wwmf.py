def weighted_max_min_fairness(tputs, weights, max_capacity):
    capacity_remaining = max_capacity
    output = []
    
    for i, (tput, weight) in enumerate(zip(tputs, weights)):
        share = capacity_remaining / (len(tputs) - i)
        weighted_tput = tput * weight
        allocation = min(share, weighted_tput)
        
        if i == len(tputs) - 1:
            allocation = max(share, capacity_remaining)
        
        output.append(allocation)
        capacity_remaining -= allocation
    
    return output

def main():
    tputs = [800, 400, 100, 300]
    weights = [0.5, 0.9, 0.5, 0.1]
    max_capacity = 1000
    
    result = weighted_max_min_fairness(tputs, weights, max_capacity)
    print(result)
 
if __name__ == "__main__":
    main()
