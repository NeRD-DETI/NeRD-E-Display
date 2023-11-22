import random
from time import sleep
import vlc


neutral_eyes="gifs/look.png"

class NerdE():

    def __init__(self):
        print("Starting")
        #self.gifs = ["gifs/Accept_oneshot.gif", "gifs/Accept_Squint_oneshot.gif", "gifs/Angrier_oneshot.gif", "gifs/Blink_oneshot.gif", "gifs/Deny_oneshot.gif","gifs/look_oneshot.gif","gifs/owo_oneshot.gif","gifs/uwu_oneshot.gif"]
        self.gifs = ["webm/accept.webm", "webm/accept_squint.webm", "webm/angrier.webm", "webm/blink.webm", "webm/deny.webm","webm/look.webm","webm/owo.webm","webm/uwu.webm"]
        self.player = vlc.MediaPlayer("webp/look.jpg")
        self.player.set_fullscreen(True)

        self.player.play()
        self.is_playing = False
        
        self.next = []


    def random_gif_loop(self):
        # [HUGO] My suggestion is to have a list with the actions and randomly pick, way faster :D
        if self.player.get_state() == vlc.State.Ended:  
                self.back_to_neutral()
        else:
            if not self.is_playing:
                self.play_gif(random.choice(self.gifs))



    def play_gif(self,gifname):
        if not isinstance(gifname, str):
            gifname=None
            return
        if self.is_playing:
            self.next+=[gifname]
        else:
            self.is_playing = True
            if len(self.next)>0:
                print("next gif!")
                self.next+=[gifname]
                self.player.set_mrl(self.next.pop(0))
                self.player.play()
            else:
                print("next gif!")

                self.player.set_mrl(gifname)
                self.player.play()

    def set_not_playing(self):
        self.is_playing=False

    def back_to_neutral(self,something=None):
        self.is_playing = False
        self.player.set_mrl("webm/look.webm")
        self.player.next_frame()
        self.player.pause()
        sleep(3)

        
        


#def on_mouse_press(x, y, button,modifiers):
#    if button == mouse.LEFT:
#        if nerde.is_playing:
#            if not nerde.next:
#                nerde.next='owo_oneshot.gif'
#            else:
#                print("Already queued, discarding...")
#            pyglet.clock.schedule_once(nerde.play_gif, nerde.animation.get_duration())
#        else:
#            nerde.play_gif('owo_oneshot.gif')
#        
#        print('The left mouse button was pressed.')
        

#def on_draw():
#    window.clear()
#    nerde.sprite.draw()
#


def main():
    nerde=NerdE()
    try:
        while True:
            nerde.random_gif_loop()
    except KeyboardInterrupt:
        print("Exiting...")
        nerde.player.stop()
        exit(0)



if __name__ == '__main__':
    main()