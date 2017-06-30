import sys
import heapq
from collections import deque
from math import radians, cos, sin, asin, sqrt
import random
import time

# As described in the question we considered the data set as Graph problem. Each of the citites considered as a node of the graph and each of roads is the path between them. For
#each node we expanded them based on its neighboring nodes.

# Successor function

# Sample Case: BFS
# Sample Input:
# Start CIty: Bloomington,_Indiana
# End city: Chicago,_Illinois

# Case 1: BFS segments
# Solution: Gives Solution with 13 segments
# Bloomington,_Indiana Spencer,_Indiana Terre_Haute,_Indiana Montezuma,_Indiana Covington,_Indiana Carbondale,_Indiana Gravel_Hill,_Indiana Kentland,_Indiana Schererville,_Indiana Highland,_Indiana Hammond,_Indiana Jct_I-90_&_I-94_S,_Illinois Chicago,_Illinois
# Time to run 15.56 sec

# Case 2: BFS distance
# Solution: Shortest Distance. But 15 segments
# 209 4.33632478632 Bloomington,_Indiana Spencer,_Indiana Romona,_Indiana Cloverdale,_Indiana Morton,_Indiana Crawfordsville,_Indiana Romney,_Indiana Lafayette,_Indiana Remington,_Indiana Merrillville,_Indiana Schererville,_Indiana Highland,_Indiana Hammond,_Indiana Jct_I-90_&_I-94_S,_Illinois Chicago,_Illinois
# Time to run 14.12 sec

# Case 3: BFS time
# Solution: Quickest solution
# 224 3.90034965035 Bloomington,_Indiana Martinsville,_Indiana Jct_I-465_&_IN_37_S,_Indiana Jct_I-465_&_IN_67,_Indiana Jct_I-70_&_I-465_W,_Indiana Jct_I-465_&_US_36,_Indiana Jct_I-74_&_I-465_W,_Indiana Jct_I-65_&_I-465_N,_Indiana Royalton,_Indiana Fickle,_Indiana Lafayette,_Indiana Remington,_Indiana Merrillville,_Indiana New_Chicago,_Indiana Gary,_Indiana Hammond,_Indiana Jct_I-90_&_I-94_S,_Illinois Chicago,_Illinois
# Time to run 9.68739 secs

# A star
#---------------------

#Case 1: A star segments
# Solution: Gives a quick solution comapring to BFS. Solution with 13 segments
# 261 5.60404040404 Bloomington,_Indiana Spencer,_Indiana Terre_Haute,_Indiana Montezuma,_Indiana Covington,_Indiana Danville,_Illinois Watseka,_Illinois Crescent_City,_Illinois L'Erable,_Illinois Kankakee,_Illinois Joliet,_Illinois Bolingbrook,_Illinois Willow_Springs,_Illinois Chicago,_Illinois
# Time to run: 0.1676 sec

#Case 2: A star distance
# Solution: Gives a quick solution with 15 segments
#209 4.33632478632 Bloomington,_Indiana Spencer,_Indiana Romona,_Indiana Cloverdale,_Indiana Morton,_Indiana Crawfordsville,_Indiana Romney,_Indiana Lafayette,_Indiana Remington,_Indiana Merrillville,_Indiana Schererville,_Indiana Highland,_Indiana Hammond,_Indiana Jct_I-90_&_I-94_S,_Illinois Chicago,_Illinois
#Time to run: 0.212339878082

# Case 3: A star time
# Solution: Gives the quickets solution really fast. Could have been faster in running time if we have used difference heuristics. But in that case we have to compromise the optimality of A star
#224 3.90034965035 Bloomington,_Indiana Martinsville,_Indiana Jct_I-465_&_IN_37_S,_Indiana Jct_I-465_&_IN_67,_Indiana Jct_I-70_&_I-465_W,_Indiana Jct_I-465_&_US_36,_Indiana Jct_I-74_&_I-465_W,_Indiana Jct_I-65_&_I-465_N,_Indiana Royalton,_Indiana Fickle,_Indiana Lafayette,_Indiana Remington,_Indiana Merrillville,_Indiana New_Chicago,_Indiana Gary,_Indiana Hammond,_Indiana Jct_I-90_&_I-94_S,_Illinois Chicago,_Illinois
#Time to run: 3.13794207573


# DFS
#-----------------------------------
# Worst Algorithm for this problem.   Most of the time dfs can not find solution. If they find its not optimal

#Test case:
# Start city: Austin,_Texas
# End city: Windcrest,_Texas

#BFS Solution:
# 70 1.07692307692 Austin,_Texas San_Marcos,_Texas Windcrest,_Texas
# Time to run: 0.0346310138702

# DFS Solution:
#1492 30.1933566434 Austin,_Texas Temple,_Texas Waco,_Texas Hillsboro,_Texas Waxahachie,_Texas Midlothian,_Texas Woodland_Hills,_Texas Jct_I-20_&_I-35E,_Texas Hutchins,_Texas Ennis,_Texas Kaufman,_Texas Terrell,_Texas Mesquite,_Texas Jct_I-30_&_I-635,_Texas Richardson,_Texas McKinney,_Texas Sherman,_Texas Gainesville,_Texas Saint_Jo,_Texas Ringgold,_Texas Waurika,_Oklahoma Wichita_Falls,_Texas Vernon,_Texas Seymour,_Texas Throckmorton,_Texas Jacksboro,_Texas Mineral_Wells,_Texas Weatherford,_Texas Decatur,_Texas Denton,_Texas Lewisville,_Texas Grapevine,_Texas Irving,_Texas Jct_I-35E_&_TX_183,_Texas Dallas,_Texas Cockrell_Hill,_Texas Duncanville,_Texas Webb,_Texas Forest_Hill,_Texas Jct_I-30_&_I-820,_Texas Richland_Hills,_Texas Fort_Worth,_Texas White_Settlement,_Texas Benbrook,_Texas Stephenville,_Texas Hico,_Texas Hamilton,_Texas Gatesville,_Texas Evant,_Texas Lampasas,_Texas San_Saba,_Texas Llano,_Texas Mason,_Texas Junction,_Texas Uvalde,_Texas Moore,_Texas Von_Ormy,_Texas San_Antonio,_Texas Lackland_AFB,_Texas Balcones_Heights,_Texas Jct_I-410_&_US_281,_Texas Windcrest,_Texas
# Time to run: 0.320003986359

# Considering all the above option, there is no doubt that A start search works best for finding path. A star is at least 10 times faster than BFS algorithm.
# We have used following heuristics for A star:
# segments : (shortest distance between each nodes)/ 5. We used this heuristics because Wehave tried with some known pair of cities. It needs 5 segments to find a solution from Bloomington
# To indianapolis. A random relaxed heuristic. Indianapolis is 50 mile, so it should not take more than 50/5 10 segments
# time: Total distance/ 60. As 60mph  is the average speed limit for the interstate highways.
#
# We finalized the heuristics after several trial and error. So, we are confident we picked up a good heuristics. As we relaxed the problem so the solution should be optimal.

# Design Consideration:
# There are lot of missing speed limits in the data set. For the speed limits if we found a missing speed limit we set the speed limit as 65mph by default. We assumed that the speed limit
# should be around the average speed.
# For some of the cities or road junctions, their gps data were missing. For those types of cities or road segments we picked the closest city of the missing city. If still a city detail can
#not be found then we picked a random city.





# Global Input variables
city_list = []
road_list = []

start_city =''
end_city=''
routing_algorithm=''

def find_city_list(city_name):
    city_routes = []

    for city in road_list:
        if city['1st_city'] == city_name:
            city_routes.append(city)
        if city['2nd_city'] == city_name:
            swap_cities = {'1st_city': city['2nd_city'], '2nd_city': city['1st_city'],
                       'length': city['length'], 'speed_limit': city['speed_limit'], 'highway': city['highway']}
            city_routes.append(swap_cities)

    return city_routes


def start_node(start_city,end_city,routing_option):

    h_n = calculate_heuristics(start_city,end_city)

    #heuristic for segment. A random relaxed heuristic. Indianapolis is 50 mile, so it should not take more than 50/5 1o segments
    if routing_option=='segment':
        h_n=h_n/5 # a random heuristics

    #heuristic for time . Total distance/ below average speed in interstate highways
    if routing_option=='time':
        h_n=h_n/60.0
    g_n = 0
    node = {'state': start_city, 'parent': None, 'path_cost': 0,'distance':0,'time':0,'g_n':0,'h_n':h_n,'f_n':g_n + h_n ,'path': start_city }
    return node


def child_node(state,end_city, parent_node,routing_option,edge):
    h_n = calculate_heuristics(state, end_city)
    distance=parent_node['distance']+edge['length']
    cost=1
    #heuristic for segment. A random relaxed heuristic. Indianapolis is 50 mile, so it should not take more than 50/5 10 segments
    if routing_option=='segment':
        cost=1
        h_n=h_n/15

    #heuristic for distance. A general one
    if routing_option=='distance':
        cost=edge['length']
    #heuristic for time. A random one distance/ 40mph which is below avg in the US. Found a good number after several try
    if routing_option=='time':
        if edge['speed_limit']!=0:
            cost=(edge['length']/(float(edge['speed_limit'])))
        else:
            cost=(edge['length']/65.0)
        h_n=h_n/60.0
   # print edge
  #  print distance
    g_n=parent_node['path_cost'] + cost


    if(edge['speed_limit']!=0):
        time=parent_node['time']+(edge['length']/(float(edge['speed_limit'])))
    else:
        time=parent_node['time']+(edge['length']/65.0) # US average speed limit 65mph in interstate highways

    node = {'state': state, 'path_cost': parent_node['path_cost'] + cost,'distance':distance,'time':time, 'f_n':g_n + h_n,'g_n':g_n,
            'path': parent_node['path'] + ' ' + state}
    return node



# http://stackoverflow.com/questions/4913349/haversine-formula-in-python-bearing-and-distance-between-two-gps-points
def haversine(lon1, lat1, lon2, lat2):
    """
    Calculate the great circle distance between two points
    on the earth (specified in decimal degrees)
    """
    # convert decimal degrees to radians

    #print lon1
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])
    # haversine formula
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a))
    r = 3956 # Radius of earth in kilometers. Use 3956 for miles
    return c * r


def check_city_exists(city_name):
    for city in city_list:
        if city['city']==city_name:
            return True
    return False
def find_closest_city(city_name):
    closest_city=list()

    for city in road_list:
        if city['1st_city'] == city_name:
            if check_city_exists(city['1st_city']) or check_city_exists(city['2nd_city']):
                heapq.heappush(closest_city, (int(city['length']), city))
        if city['2nd_city'] == city_name:
            if check_city_exists(city['1st_city']) or check_city_exists(city['2nd_city']):
                swap_cities = {'1st_city': city['2nd_city'], '2nd_city': city['1st_city'],
                       'length': city['length'], 'speed_limit': city['speed_limit'], 'highway': city['highway']}
                heapq.heappush(closest_city, (int(swap_cities['length']), swap_cities))

   # print city_name
    try:
        valid_closest_city=heapq.heappop(closest_city)
        return valid_closest_city[1]
    except IndexError:
        random.seed()
        return road_list[random.randint(0,len(city_list))]



# Get the details of the city name. If no city is found, we picked the closest ones
def find_city_details(city_name):
    city_details=dict()
    for city in city_list:
        if city['city']==city_name:
            city_details=city
            return city_details

    if len(city_details)==0:
        city_details=find_closest_city(city_name)
        #print city_details
        if city_details['1st_city'] == city_name:
            return find_city_details(city_details['2nd_city'])
        elif city_details['2nd_city'] == city_name:
            return find_city_details(city_details['1st_city'])
        else:
            return find_city_details(city_details['1st_city'])


def calculate_heuristics(first_city,end_city):

    end_city_gps=dict()

    first_city_gps=find_city_details(first_city)
    end_city_gps=find_city_details(end_city)
    return haversine(float(first_city_gps['longitude']),float(first_city_gps['latitude']),float(end_city_gps['longitude']),float(end_city_gps['latitude']))

def bfs(start_city, end_city,routing_option):

    node = start_node(start_city,end_city,routing_option)
    frontier = list()
    heapq.heappush(frontier,(node['path_cost'],node))

    explored = list()
    while True:
        if len(frontier) == 0:
            print "No Solutions Found"
            return
        pop=heapq.heappop(frontier)
        node=pop[1]
        if(routing_option=='distance' or routing_option=='time'):
            if node['state']==end_city:
                print str(node['distance'])+' '+str(node['time'])+' ' + node['path']
                return

        explored.append(node['state'])
        action_list = find_city_list(node['state'])

        for action in action_list:
            child = child_node(action['2nd_city'],end_city, node, routing_option,action)
            #  print child
            if child['state'] not in explored:
                if(routing_option=='segment'):
                    if child['state'] == end_city:
                        print str(child['distance'])+' '+str(child['time'])+' ' + child['path']
                        return
                heapq.heappush(frontier,(child['path_cost'],child))



def print_frontier(frontier):
    print "Frontier"
    print '.......................................................'
    for f in frontier:
        print 'state ' + f['state'], 'path '+ str(f['path'])
    print '.......................................................'
    return


#If we dont have the solution, DFS runs forever. Distance and time might not work for DFS. That is why we did not consider those parameteres.
def dfs(start_city, end_city,routing_option):

    node = start_node(start_city,end_city,routing_option)
    frontier = list()
    frontier.append(node)
    i = 0

    while True:   # loop can not be greater than the number of cities
        if len(frontier) == 0:
            print "No Solutions Found"
            return
        node = frontier.pop()
        #print node

        if node['state']==end_city:
            print str(node['distance'])+' '+str(node['time'])+' ' + node['path']
            return
        action_list = find_city_list(node['state'])
        #print action_list
        for action in action_list:
            #print child
            if action['2nd_city'] not in node['path']:

                child = child_node(action['2nd_city'], end_city,node, routing_option,action)
                frontier.append(child)
              #  print_frontier(frontier)
        i+=1
    return



def a_star(start_city, end_city,routing_option):
    node = start_node(start_city,end_city,routing_option)
    frontier = list()
    heapq.heappush(frontier,(node['f_n'],node))

    while True:
        if len(frontier) == 0:
            print "No Solutions Found"
            return
        pop = heapq.heappop(frontier)
        node=pop[1]
        #explored.append(node['state'])
        if node['state'] == end_city:
            print str(node['distance'])+' '+str(node['time'])+' ' + node['path']
            return
        action_list = find_city_list(node['state'])

        for action in action_list:
            child = child_node(action['2nd_city'],end_city, node,routing_option,action)
            #  print child

            heapq.heappush(frontier,(child['f_n'],child))


def read_data():
    cities = open('city-gps.txt', 'r')
    roads = open('road-segments.txt', 'r')

    for city in cities:
        row = city.strip().split(' ')
        city_dictionary = {'city': row[0], 'latitude': row[1], 'longitude': row[2]}
        city_list.append(city_dictionary)

    for road in roads:
        # print road.strip()
        road_col1 = road.strip().split(' ')
        length=0
        speed_limit=0
        #print type(road_col1[2])
        if len(road_col1[2])>0:
            length=int(road_col1[2])

        if len(road_col1[3])>0:
            speed_limit=int(road_col1[3])

        road_dict = {'1st_city': road_col1[0], '2nd_city': road_col1[1], 'length':length ,
                     'speed_limit': speed_limit, 'highway': road_col1[4]}
        #if road_col1[1]=='Bloomington,_Indiana':

        road_list.append(road_dict)

    cities.close()
    roads.close()

def main(argv):
    start_city = ''
    end_city = ''
    routing_option = 'segments'  # default Segments
    routing_algorithm = 'bfs'  # default bfs
    if (len(argv) < 2):
        print "Start City and End City required"
        return

    else:
        if len(argv) == 2:
            start_city = argv[0]
            end_city = argv[1]
        elif len(argv) == 3:
            start_city = argv[0]
            end_city = argv[1]
            routing_option = argv[2]
        elif len(argv) == 4:
            start_city = argv[0]
            end_city = argv[1]
            routing_option = argv[2]
            routing_algorithm = argv[3]
        else:
            print "More Than four arguments"
            return

    # print start_city+ end_city+routing_algorithm+routing_option
    read_data()
    end_city=end_city
    if routing_algorithm == 'dfs':
        start=time.time()
        dfs(start_city, end_city,routing_option)
        end=time.time()
        print 'Time to run: '+str(end-start)
    elif routing_algorithm == 'astar':
        start=time.time()
        a_star(start_city,end_city,routing_option)
        end=time.time()
        print 'Time to run: '+str(end-start)
    else:
        start=time.time()
        bfs(start_city,end_city,routing_option)
        end=time.time()
        print 'Time to run: '+str(end-start)
    # dfs(start_city, end_city)


if __name__ == "__main__":
    main(sys.argv[1:])
