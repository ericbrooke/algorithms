from collections import deque

def person_is_target(name):
    return name[0] == 'A'


def search(name):
    search_queue = deque()
    search_queue += graph[name]
    searched = []
    while search_queue:
        person = search_queue.popleft()
        if person not in searched:
            if person_is_target(person):
                print(person + " is the target for assination")
                return True
            else:
                search_queue += graph[person]
                searched.append(person)
        return False


graph = {}
graph["you"] = ["Steph", "Bill", "Carl", "Adrian", "Will"]
graph["Bill"] = ["Jill"]
graph["Carl"] = ["Eric"]
graph["Steph"] = ["Francis"]
graph["Adian"] = []
graph["Will"] = ["Gwen"]

search("you")
