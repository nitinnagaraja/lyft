# This is to solve the Lyft Programming Challenge
import math

def delta(p1, p2):
    return math.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)


def find_shorter_detour(pA, pB, pC, pD):    
    diff = delta(pC, pD) - delta(pA, pB)
    if diff >= 0:
        route = 'C -> A -> B -> D'
        detour = 'Driver two (at C) has to take the detour!'
    else:
        route = 'A -> C -> D -> B'
        detour = 'Driver one (at A) has to take the detour!'
    return abs(diff), detour, route

a = map(int, list(raw_input().split()))
b = map(int, list(raw_input().split()))
c = map(int, list(raw_input().split()))
d = map(int, list(raw_input().split()))

diff, detour, route = find_shorter_detour(a, b, c, d)
print "Detour diff = %f" % diff
print detour
print "Route is %s" % route
