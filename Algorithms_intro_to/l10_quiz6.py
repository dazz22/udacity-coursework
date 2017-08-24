def make_link(movie):
    for actorp in movies[movie]:
        if actorp not in Network:
            Network[actorp]={}

        for actor in movies[movie]:
            if actor not in Network[actorp] and actorp != actor:
                (Network[actorp])[actor] = []
            if actorp != actor:            
                (Network[actorp])[actor].append(movie)
    return

def centrality(actor):
    linklen= {}
    open_list = [actor]
    linklen[actor] = 0
    while len(open_list) > 0:
        current = open_list.pop(0)
        for actors in Network[current].keys():
            if actors not in linklen:
                linklen[actors] = linklen[current] + 1
                open_list.append(actors)
    print(linklen)
    return (sum(linklen.values())+0.0)/len(linklen)

#with open('l10_quiz6_actors.tsv','rb') as lines:
with open('test.tsv','rb') as lines:
    Network={}
    movies={}
    for line in lines:
        A = line.split('\t')
        mov = A[1] + A[2]
        if mov not in movies:
            movies[mov] = []
        movies[mov].append(A[0])
    for movie in movies.keys():
        make_link(movie)
    print(Network) 
    print(len(Network))
    central=[]
    with open("central.txt", 'a') as out:

        for actor in Network.keys():
            print(actor)
            print(centrality(actor))
            #out.write(str(centrality(actor))+"\t"+ actor+'\n' )

