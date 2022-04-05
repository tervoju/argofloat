# Import the main fetcher:
from argopy import DataFetcher as ArgoDataFetcher
# Define what you want to fetch... 


# a region:
# baltic sea area E 14.35, 29.5
# N 54.1, 65.8
ArgoSet = ArgoDataFetcher().region([14.3,29.5,54,65.8,0,10.])

# floats in baltic sea:
# 6903706, 6903708, 6903709,  6903710, 6903711, 6904116
# 7900579, 7900586, 7900587
# 3902110,3902115 

ArgoSet = ArgoDataFetcher().float([6903706, 6903708, 6903709,  6903710, 6903711, 6904116])
# or specific profiles:
ArgoSet = ArgoDataFetcher().profile(6902746, 34)
# then fetch and get data as xarray datasets:
ds = ArgoSet.load().data
# or
ds = ArgoSet.to_xarray()
# you can even plot some information:
ArgoSet.plot('trajectory')    