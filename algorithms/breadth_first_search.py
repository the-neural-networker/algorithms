from collections import deque

def person_is_seller(person):
    return person[-1] == "m"

def breadth_first_search(name):
    search_queue = deque()
    search_queue += graph[name]
    searched = []

    while search_queue:
        person = search_queue.popleft()
        if person not in searched:
            if person_is_seller(person):
                print(f"{person} is a mango seller!")
                return True
            else:
                search_queue += graph[person]
                searched.append(person)

    return False


if __name__ == "__main__":
    # directed graph
    graph = {} 
    graph["you"] = ["alice", "bob", "claire"]
    graph["alice"] = ["peggy"]
    graph["bob"] = ["anuj", "peggy"]
    graph["claire"] = ["thom", "jonny"]
    graph["anuj"] = []
    graph["peggy"] = []
    graph["thom"] = []
    graph["jonny"] = []

    breadth_first_search("you")
