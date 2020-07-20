from gl import Render, color

r = Render()

r.glCreateWindow(800, 800)
r.glClearColor(0, 0, 0)
r.glColor(1, 0, 0.9843)
r.glClear()

r.glLine(0, 0, 1, 1)
r.glLine(0, 0, 1, 0.5)
r.glLine(0, 0, 1, 0)
r.glLine(0, 0, 1, -0.5)
r.glLine(0, 0, 1, -1)
r.glLine(0, 0, 0.5, -1)
r.glLine(0, 0, 0, -1)
r.glLine(0, 0, -0.5, -1)
r.glLine(0, 0, -1, -1)
r.glLine(0, 0, -1, -0.5)
r.glLine(0, 0, -1, 0)
r.glLine(0, 0, -1, 0.5)
r.glLine(0, 0, -1, 1)
r.glLine(0, 0, -0.5, 1)
r.glLine(0, 0, 0, 1)
r.glLine(0, 0, 0.5, 1)


r.glFinish()