__author__ = 'fhca'

from turtle import Turtle, mainloop
from random import random


class Lsystem(Turtle):
    Lsystems = []

    def __init__(self, lsys="", ops=""):
        Turtle.__init__(self, shape="turtle")
        if lsys == "":
            lsys = {"axiom": "0", "rules": {"1": "11", "0": "1[0]0"},
                    "langle": 45, "rangle": 45, "startpos": (0, -300),
                    "startheading": 90}
        # if ops == "":
        #     ops = {"1":self.segment, "0": self.leaf_segment,
        #            "[": self.push_left, "]": self.pop_right}
        if ops == "":
            ops = {"1": "segment", "0": "leaf_segment", "[": "push_left",
                   "]": "pop_right", "(": "push_pos_angle",
                   ")": "pop_pos_angle"}
        self.shapesize(1, 1, 2)
        self.speed(0)
        self.screen.colormode(1)
        self.ht()
        self.screen.tracer(0, 0)  # no animation
        self.pencolor(lsys.get("color", (random(), random(), random())))
        self.setheading(lsys.get("startheading", 90))
        self.pu()
        self.setpos(lsys.get("startpos", (0, 0)))
        # add constants to rules
        lsys["const"] = lsys.get("const", ("[", "]", "+", "-"))
        for c in lsys["const"]:
            lsys["rules"][c] = c
        lsys["scale"] = lsys.get("scale", 10)
        lsys["depth"] = lsys.get("depth", 5)
        lsys["angle"] = lsys.get("angle", 45)
        lsys["rangle"] = lsys.get("rangle", lsys["angle"])
        lsys["langle"] = lsys.get("langle", lsys["angle"])
        ops["+"] = ops.get("+", "tright")
        ops["-"] = ops.get("-", "tleft")
        ops["F"] = ops.get("F", "segment")
        ops["C"] = ops.get("C", "switchcolor")
        self.lsys = lsys
        self.ops = ops
        self.LIFO = []
        self.str = self.iterate(self.lsys["depth"])
        Lsystem.Lsystems.append(self)

    def iterate(self, n):
        str = self.lsys["axiom"]
        for i in range(n):
            str = self._iterate(str)
        return str

    def _iterate(self, str):
        rules = self.lsys["rules"]
        # si no encuentra el símbolo, lo deja ahí
        return "".join(rules.get(x, x) for x in str)

    def draw(self):
        for c in list(self.str):
            res = self.ops.get(c, "None")
            if hasattr(self, res):
                eval("self.%s()" % res)
            yield
        self.hideturtle()

    def segment(self):
        self.pd()
        self.fd(self.lsys["scale"])
        self.pu()

    def leaf_segment(self):
        self.pd()
        self.fd(self.lsys["scale"])
        self.pu()

    def push_pos_angle(self):  # "("
        self.LIFO.append((self.pos(), self.heading()))

    def pop_pos_angle(self):  # ")"
        pos, heading = self.LIFO.pop()
        self.setheading(heading)
        self.setpos(*pos)

    def push_left(self):  # "["
        self.push_pos_angle()
        self.lt(self.lsys["langle"])

    def pop_right(self):  # "]"
        self.pop_pos_angle()
        self.rt(self.lsys["rangle"])

    def tright(self):  # "+"
        self.rt(self.lsys["rangle"])

    def tleft(self):  # "-"
        self.lt(self.lsys["langle"])

    def switchcolor(self):
        self.pencolor(random(), random(), random())


class GatherLsystems:
    def __init__(self, *l):
        self.done = dict()
        if len(l) > 0:
            for t in l:
                self.add(t)
        else:  # añade todos los Lsystems por default
            for t in Lsystem.Lsystems:
                self.add(t)

    def add(self, t):
        self.done[t] = False

    def draw(self):
        mylist = [(t, t.draw()) for t in self.done.keys()]
        done = False
        while not done:
            for turtle, turtle_draw in mylist:
                try:
                    next(turtle_draw)
                except StopIteration:
                    self.done[turtle] = True
            done = all(self.done.values())
        mainloop()


"branch large"
Lsystem({"axiom": "0", "rules": {"1": "11", "0": "1[0]0"}, "langle": 3,
         "rangle": 7, "startpos": (0, -300), "scale": 8})

"branch small"
Lsystem({"axiom": "0", "rules": {"1": "11", "0": "1[0]0"}, "langle": 15,
         "rangle": 8, "startpos": (-100, -300), "depth": 6})

"square koch"
Lsystem({"axiom": "F", "rules": {"F": "F+F-F-F+F"}, "angle": 90, "scale": 1.3,
         "color": "red"})

"tepee"
Lsystem({"axiom": "G", "rules": {"G": "GFX(+G)(-G)", "X": "X(-FFF)(+FFF)FX"},
         "startpos": (-200, -280)})

"sierp"
Lsystem({"axiom": "A", "rules": {"A": "C+B-A-B+", "B": "C-A+B+A-"},
         "angle": 60, "startpos": (100, -300), "scale": 1.3, "depth": 8,
         "color": "brown"}, {"A": "segment", "B": "segment"})

"plant"
Lsystem({"axiom": "X", "rules": {"X": "F-((X)+X)+F(+FX)-X", "F": "FF"},
         "angle": 20, "startpos": (250, -100), "scale": 3, "depth": 6,
         "color": "darkblue"})

"dragon"
Lsystem({"axiom": "X", "rules": {"X": "X+YF+", "Y": "-FX-Y"}, "angle": 90,
         "startpos": (-250, -300), "scale": 3, "depth": 8,
         "color": "darkblue"})

GatherLsystems().draw()
