from room import Room
from player import Player
from world import World

import random
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph = literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']

# sequential travel directions
traversal_path = []
# visited rooms
visited = set()
# map of maze up to current point: {0: [(1, 'n'), (5, 's'), (7, 'w'), (3, 'e')], 1: [(2, 'n'), (0, 's')], 2: [(1, 's')]}
adj_list = {}
# simpler map
simple_list = {}
# list of known rooms that are known to exist but have not been visited. Idea is that last element will be nearest empty room
unvisited_rooms = []
# a set of unvisited rooms to use as a look up table. BFT wi
unvis_rooms = set()
count = 0


# Find shortest path to an unexplored room
def find_path_to_unexplored(starting_vert=0, des_set=1):
    print('search started')
    queue = [[starting_vert]]
    seen = {}
    seen[starting_vert] = True
    while len(queue) > 0:
        current_path = queue.pop(0)
        if current_path[-1] in des_set:
            print('need to find', current_path[-1])
            return current_path
        for i in simple_list[current_path[-1]]:
            if i not in seen:
                seen[i] = True
                new_path = current_path + [i]
                queue.append(new_path)


def navigate_to(path_list=[]):
    if player.current_room.id == path_list[-1]:
        unvis_rooms.remove(path_list[-1])
    while player.current_room.id != path_list[-1]:
        print('navigate loop started')
        c_room = player.current_room
        a_exits = c_room.get_exits()
        path_list.pop(0)
        for i in a_exits:
            a_room = c_room.get_room_in_direction(i).id
            if a_room == path_list[0]:
                traversal_path.append(i)
                player.travel(i)


while len(visited) < len(room_graph):
    print('main loop started', 'visited length: ', len(visited))
    print('current room', player.current_room.id)
    print('traversal path', traversal_path, '\n')
    explored = False
    current_room = player.current_room
    exits = current_room.get_exits()
    # If current room has not been previously visited
    if current_room.id not in visited:
        visited.add(current_room.id)
        adj_list[current_room.id] = []
        simple_list[current_room.id] = []
        for i in exits:
            adj_room_id = current_room.get_room_in_direction(i).id
            adj_list[current_room.id].append((adj_room_id, i))
            simple_list[current_room.id].append(adj_room_id)
            if adj_room_id not in visited and adj_room_id not in unvis_rooms:
                unvisited_rooms.append(adj_room_id)
                unvis_rooms.add(adj_room_id)

    # make list of unexplored exits by checking if adjacent rooms are on the visited list
    unexplored_exits = []
    for exit in exits:
        adj_room_id = current_room.get_room_in_direction(exit).id
        if adj_room_id not in visited:
            unexplored_exits.append((adj_room_id, exit))

    # if unexplored exit exists, choose one at random and travel to it
    if len(unexplored_exits) > 0:
        travel_index = random.randint(0, len(unexplored_exits)-1)
        next_room_id = unexplored_exits[travel_index][0]
        next_room_dir = unexplored_exits[travel_index][1]
        # add to the traversal path
        traversal_path.append(next_room_dir)
        # travel to next room
        player.travel(next_room_dir)
        # remove from the unvisited list and set
        unvisited_rooms.remove(next_room_id)
        unvis_rooms.remove(next_room_id)

    # if no unexplored exits start the breadth-first search to
    elif len(unexplored_exits) == 0:
        explored = True

    # if no unexplored exits start the breadth-first search to
    if explored is True:
        # unvisited_rooms.remove(player.current_room.id)
        # print('dead end', current_room.id)

        # print('simple list', simple_list)
        xer = find_path_to_unexplored(player.current_room.id, unvis_rooms)

        navigate_to(xer)

        explored = False
        print('length of visited: ', len(visited))
        print(len(traversal_path))


# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(
        f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")


#######
# UNCOMMENT TO WALK AROUND
#######
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")
