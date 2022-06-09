import PyNewtFrac

'''
    When the program is "waiting for input", you can either:
        - press W to zoom in
        - press S to zoom out
        - press C to change the colours, in case you don't like them
'''

f = lambda x : x**4 + 5
f1 = lambda x : 4 * x  **3

x0 = - 3 + 2j

resolution = 600

PyNewtFrac.newton_roots_coloring(f, f1, x0, resolution)
