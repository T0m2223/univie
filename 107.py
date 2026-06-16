testmat = np.array([
    [0,0,1,0,1],
    [0,0,1,1,1],
    [1,1,0,1,0],
    [0,1,1,0,1],
    [1,1,0,1,0]
])


def nachbarn(amat, v):
    """Hilfsfunktion: Finde in einem Graphen G (gegeben durch
    seine Adjazenzmatrix amat (np.array)) die Nachbarn (also die adjazenten
    Knoten) eines Knotens v (int, wobei die Nummerierung der Knoten mit 0 beginnt)."""
    return np.nonzero(amat[v])[0]


# Am einfachsten wird die Programmierung _rekursiv_:
# Die Funktion übernimmt den "bisher beschrittenen"
# Weg "path", den gesuchten Endknoten e und die Liste
# der bereits "durchlaufenen" (gerichteten!) Kanten und
# versucht, den Weg fortzusetzen; oder einen Schritt zurück
# zu machen:
def schritt_weiter(amat,path,e,used_edges):
    """Hilfsfunktion: Angenommen, wir haben bereits einen Teil-Weg "path"
    absolviert und eine Menge schon benutzter Kanten (dargestellt in Form
    einer Liste "used_edges") angesammelt, dann machen wir jetzt rekursiv weiter."""
    # Ab hier bitte Code einfügen bzw. verändern!
    # ...
    # Richtiges Ergebnis zurückgeben:
    v = path[-1]
    if v == e: return path

    for v_next in nachbarn(amat, v):
        # Don't walk an already used edge
        if (v, v_next) in used_edges: continue

        # Append walked edge
        used_edges.append((v, v_next))
        used_edges.append((v_next, v))

        # Recursion (return early if path to e found)
        ret = schritt_weiter(amat, path + [v_next.item()], e, used_edges)
        if ret != None: return ret

    return None


"""
DFS isnt guaranteed to find a shortest path
"""

def theseus(amat,s,e):
    """Finde in einem einfach zusammenhängenden Graphen (gegeben durch
    seine Adjazenzmatrix amat) einen Weg von Knoten s nach Knoten e, sodaß
    in dem Algorithmus keine Kante öfter als zweimal betrachtet wird.
    Der Ausgabewert soll eine Liste von Knoten sein, in der Reihenfolge, in welcher diese durchlaufen werden."""
    # Jede Kante wird höchstens "einmal hin und einmal zurück" durchlaufen:
    ausweg = [s]
    used_edges = []
    # Ab hier bitte Code einfügen bzw. verändern!
    # ...
    # Richtiges Ergebnis zurückgeben:
    return schritt_weiter(amat, ausweg, e, used_edges)



# Kleiner Test
theseus(testmat,0,3) # => [0, 2, 1, 3]