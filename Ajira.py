from collections import defaultdict as dd

graph = dd(list)
ID = dd(int)
Added = dd(bool)
Connected = dd(tuple)
nodes = []
c = []
r = []
error = "Error:"
success = "Successfully"
max_id = 0
strength = []
rslt = None

def solve(graph, root, dest, visited, ID, lst = []):
    if root == dest:
        global rslt
        rslt = lst
        return True
    if visited[root]: return False
    visited[root] = True
    # lst.append(root)
    for x in graph[root]:
        # print(x, end = ' ')
        if not visited[x]:
            lst.append(x)
            if solve(graph, x, dest, visited, ID, lst): 
                return True
            lst.pop()
            # visited[ID[x]] = False
    return False

try:
    while 1:
        command = input().strip().split()
        if len(command) != 3: 
            if len(command) != 2:
                print(error, "Invalid command syntax.")
            else:
                if command[0] == "SET_DEVICE_STRENGTH":
                    if not Added[command[1]]:
                        print(error, "Node not found")
                    else:
                        strength[ID[command[1]]] = 5
        elif command[0] == "ADD":
            if command[1] == "COMPUTER" or command[1] == "REPEATER":
                if not Added[command[2]]:
                    nodes.append(command[2])
                    strength.append(0)
                    ID[command[2]] = max_id
                    max_id += 1
                    Added[nodes[-1]] = True
                    if command[1] == "REPEATER":
                        r.append(command[0])
                    print(success, "added", command[2])
                else:
                    print(error, "That name already exists.")
            else:
                print(error, "Invalid command syntax.")
        elif command[0] == "SET_DEVICE_STRENGTH":
            if not Added[command[1]]:
                print(error, "Node not found")
            elif command[2].isdigit():
                strength[ID[command[1]]] = command[2]
                print(success, "defined strength")
            else:
                print(error, "Invalid command syntax.")
        elif command[0] == "CONNECT":
            if not Added[command[1]]:
                print(error, "Node not found")
            elif command[1] == command[2]:
                print(error, "Cannot connect device to itself.")
            elif Connected[(command[1], command[2])]:
                print(error, "Devices are already connected.")
            elif not Added[command[1]] or not Added[command[2]]:
                print(error, "Node not found")
            else:
                graph[command[1]].append(command[2])
                graph[command[2]].append(command[1])
                Connected[(command[1], command[2])] = True
                Connected[(command[2], command[1])] = True
                print(success, "conencted")
        elif command[0] == "INFO_ROUTE":
            if not Added[command[1]]:
                print(error, "Node not found")
            elif command[1] == command[2]:
                print(command[1], "->", command[2])
            elif not Added[command[1]] or not Added[command[2]]:
                print(error, "Node not found")
            elif command[1] in r or command[2] in r:
                print(error, "Rout cannot be calculated with a repeater.")
            else:
                visited = dd(bool)
                solve(graph, command[1], command[2], visited, ID, [])
                if rslt:
                    print(command[1], "->", end = " ")
                    print(*rslt, sep = " -> ")
                else:
                    print(error, "Route not found!")
                rslt = None
        else:
            print(error, "Invalid command syntax.")
            
except:
    pass

# for x in graph:
#     print(x, graph[x])

# print(*strength)

# print("678".isdigit())


# ADD COMPUTER A1
# ADD COMPUTER A2
# ADD COMPUTER A3
# ADD
# ADD PHONE A1
# ADD COMPUTER A1
# ADD COMPUTER A4
# ADD COMPUTER A5
# ADD COMPUTER A6
# ADD REPEATER R1
# SET_DEVICE_STRENGTH A1 HELLO
# SET_DEVICE_STRENGTH A1 2
# CONNECT A1 A2
# CONNECT A1 A3
# CONNECT A1 A1
# CONNECT A1 A2
# CONNECT A5 A4
# CONNECT R1 A2
# CONNECT R1 A5
# CONNECT A1
# CONNECT
# CONNECT A8 A1
# CONNECT A2 A4
# INFO_ROUTE A1 A4
# INFO_ROUTE A1 A5
# INFO_ROUTE A4 A3
# INFO_ROUTE A1 A1
# INFO_ROUTE A1 A6
# INFO_ROUTE A1 R1
# INFO_ROUTE A3
# INFO_ROUTE
# INFO_ROUTE A1 A10