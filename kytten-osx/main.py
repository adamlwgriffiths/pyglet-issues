import os
import kytten
import pyglet

window = pyglet.window.Window(
    640,
    480,
    caption='Kytten Test',
    resizable = True,
    vsync = False
    )
batch = pyglet.graphics.Batch()

window.register_event_type('on_update')
theme = kytten.Theme( os.path.join(os.getcwd(), 'theme') )

dialog = kytten.Dialog(
    kytten.TitleFrame(
        "Kytten Demo",
        kytten.VerticalLayout(
        [
            kytten.Label("Drag Me!"),
            ]
        ),
    ),
    window = window,
    batch = batch,
    anchor = kytten.ANCHOR_TOP_LEFT,
    theme = theme
    )

@window.event
def on_draw():
    global window
    global batch
    window.clear()
    batch.draw()

def update(dt):
    global window
    window.dispatch_event('on_update', dt)

pyglet.clock.schedule(update)
pyglet.app.run()

