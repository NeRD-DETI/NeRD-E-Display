import pyglet
from pyglet.window import mouse
import random

window = pyglet.window.Window(fullscreen=True)

class NerdE(pyglet.sprite.Sprite):

    def __init__(self):
        self.is_playing = False
        self.to_play = None
        self.animation=pyglet.image.load_animation('gifs/look_oneshot.gif')
        self.back_to_neutral()
        pyglet.clock.schedule_interval(self.random_gif_loop,3)

    def random_gif_loop(self,something=None):
        # [HUGO] My suggestion is to have a list with the actions and randomly pick, way faster :D
        gifs = ["Accept_oneshot.gif", "Accept_Squint_oneshot.gif", "Angrier_oneshot.gif", "Blink_oneshot.gif", "Deny_oneshot.gif","look_oneshot.gif","owo_oneshot.gif","uwu_oneshot.gif"]
        self.play_gif(random.choice(gifs))
        # rand = random.randint(0,7)
        # match rand:
        #     case 0:
        #         self.play_gif("Accept_oneshot.gif")
                
        #     case 1:
        #         self.play_gif("Accept_Squint_oneshot.gif")
                
        #     case 2:
        #         self.play_gif("Angrier_oneshot.gif")
                
        #     case 3:
        #         self.play_gif("Blink_oneshot.gif")
                
        #     case 4:
        #         self.play_gif("Deny_oneshot.gif")
                
        #     case 5:
        #         self.play_gif("look_oneshot.gif")
                
        #     case 6:
        #         self.play_gif("owo_oneshot.gif")
                
        #     case 7:
        #         self.play_gif("uwu_oneshot.gif")
            
            


    def play_gif(self,gifname=None,something=None):
        if not isinstance(gifname, str):
            gifname=None
        if self.is_playing:
            if not self.to_play:
                self.to_play=gifname
        else:
            self.is_playing = True
            if self.to_play:
                self.animation = pyglet.image.load_animation('gifs/'+self.to_play)
                self.to_play = None
            else:
                self.animation = pyglet.image.load_animation('gifs/'+gifname)
            bin = pyglet.image.atlas.TextureBin()
            self.animation.add_to_texture_bin(bin)

            self.sprite = pyglet.sprite.Sprite(img=self.animation)
            self.sprite.x = self.sprite.width // 2 ##this line is new
            window.clear()
            self.sprite.draw()
            pyglet.clock.schedule_once(self.back_to_neutral, self.animation.get_duration())

    def set_not_playing(self):
        self.is_playing=False

    def back_to_neutral(self,something=None):
        self.is_playing = False
        test= pyglet.image.load_animation('gifs/owo_oneshot.gif')
        eyes=test.frames[0]
        
        self.sprite = pyglet.sprite.Sprite(img=eyes.image)

        self.sprite.x =( window.width // 4 )+19

        window.clear()
        self.sprite.draw()


@window.event
def on_mouse_press(x, y, button,modifiers):
    if button == mouse.LEFT:
        if nerde.is_playing:
            if not nerde.to_play:
                nerde.to_play='owo_oneshot.gif'
            else:
                print("Already queued, discarding...")
            pyglet.clock.schedule_once(nerde.play_gif, nerde.animation.get_duration())
        else:
            nerde.play_gif('owo_oneshot.gif')
        
        print('The left mouse button was pressed.')
        

@window.event
def on_draw():
    window.clear()
    nerde.sprite.draw()


nerde=NerdE()

if __name__ == '__main__':
    pyglet.app.run()