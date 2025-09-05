independence_stages = ["Inicio", "Organizacion", "Resistencia", "Consumacion"]
print(independence_stages[0])
print(len(independence_stages))

#List Methods
leaders = []
leaders.append("Miguel Hidalgo")
leaders.append("Vicente Guerrero")
#leaders.extend(independence_stages) //Mix lists togheter
leaders.insert(1, "Jose Maria Morelos")
#leaders.remove("Vicente Guerrero") // Delete first match of specific items
leaders.append("Augustin de Iturbide")
#leaders.pop(1) //Delete an index
#leaders.clear()
print(leaders.index("Miguel Hidalgo"))
print(leaders.count("Vicente Guerrero"))
#leaders.sort()
#leaders.reverse()
new_leaders = leaders.copy()


print(leaders)
print(new_leaders)

