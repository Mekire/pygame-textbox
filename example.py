import os
import sys
import pygame as pg

from textbox import TextBox


KEY_REPEAT_SETTING = (200,70)


class Control(object):
    def __init__(self):
        pg.init()
        pg.display.set_caption("Input Box")
        self.screen = pg.display.set_mode((500,500))
        self.clock = pg.time.Clock()
        self.fps = 60.0
        self.done = False
        self.input = TextBox((100,100,150,30),command=self.change_color,
                              clear_on_enter=True,inactive_on_enter=False)
        self.color = (100,100,100)
        self.prompt = self.make_prompt()
        pg.key.set_repeat(*KEY_REPEAT_SETTING)

    def make_prompt(self):
        font = pg.font.SysFont("arial", 20)
        message = 'Please type a color name for background (ex. "red"):'
        rend = font.render(message, True, pg.Color("white"))
        return (rend, rend.get_rect(topleft=(10,35)))

    def event_loop(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.done = True
            self.input.get_event(event)

    def change_color(self,id,color):
        try:
            self.color = pg.Color(str(color))
        except ValueError:
            print("Please input a valid color name.")

    def main_loop(self):
        while not self.done:
            self.event_loop()
            self.input.update()
            self.screen.fill(self.color)
            self.input.draw(self.screen)
            self.screen.blit(*self.prompt)
            pg.display.update()
            self.clock.tick(self.fps)


if __name__ == "__main__":
    app = Control()
    app.main_loop()
    pg.quit()
    sys.exit()
