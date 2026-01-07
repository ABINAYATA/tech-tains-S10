name=["abi","vijay","kumar","sat"]
dept=["cse","ece","mech","civil"]

seat=1
for name,dept in zip(name,dept):
     print(f"seat{seat}-{name} {dept}")
     seat=seat+1