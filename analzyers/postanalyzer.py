
def post_most()

def updatedict(dict, id, value, top=10):
    if len(dict) < top:
        dict[id] = value
        return

    smallest = min(dict.items(), key=lambda x: x[1])
    if value > smallest[1]:
        del dict[smallest[0]]
        dict[id] = value
