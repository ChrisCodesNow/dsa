'''
Pretend you’re selling the friendship bracelets to n customers, and the value of that product increases monotonically. This means that the product has prices {p_1, …, p_n} such that p_i ≤ p_j if customer j comes after customer i. These n customers have values {v_1, …, v_n}. A given customer i will buy a friendship bracelet at price p_i if and only if p_i ≤ v_i; otherwise the revenue obtained from that customer is 0. Assume prices are natural numbers.
'''
# Prices: actual prices of bracelets
# sorted increasing order

# Values: highest price a customer i is willing to pay for a price
# not sorted, dependent on client

