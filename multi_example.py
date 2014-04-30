import os
import sys
import pygame as pg

from textbox import TextBox


KEY_REPEAT_SETTING = (200,70)


class Control(object):
    def __init__(self):
        pg.init()
        pg.display.set_caption("Multiple Input Boxes")
        self.screen = pg.display.set_mode((500,500))
        self.clock = pg.time.Clock()
        self.fps = 60.0
        self.done = False
        screen_color = TextBox((100,100,150,30), command=self.change_color,
                               clear_on_enter=True, inactive_on_enter=False)
        text_color = TextBox((100,370,150,30), command=self.change_text_color,
                              clear_on_enter=True, inactive_on_enter=False,
                              active=False)
        self.prompts = self.make_prompts()
        self.inputs = [screen_color, text_color]
        self.color = (100,100,100)
        pg.key.set_repeat(*KEY_REPEAT_SETTING)

    def make_prompts(self, color=pg.Color("white")):
        rendered = []
        font = pg.font.SysFont("arial", 20)
        message = 'Please type a color name for background (ex. "red"):'
        rend = font.render(message, True, color)
        rendered.append((rend, rend.get_rect(topleft=(10,35))))
        message = 'Please type a color name for text (ex. "red"):'
        rend = font.render(message, True, color)
        rendered.append((rend, rend.get_rect(topleft=(10,315))))
        return rendered

    def event_loop(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.done = True
            for box in self.inputs:
                box.get_event(event)

    def change_color(self, id, color):
        try:
            self.color = pg.Color(str(color))
        except ValueError:
            print("Please input a valid color name.")

    def change_text_color(self, id, color):
        try:
            color = pg.Color(str(color))
            for box in self.inputs:
                box.font_color = color
            self.prompts = self.make_prompts(color)
        except ValueError:
            print("Please input a valid color name.")

    def render(self):
        self.screen.fill(self.color)
        for box in self.inputs:
            box.draw(self.screen)
        for prompt in self.prompts:
            self.screen.blit(*prompt)

    def main_loop(self):
        while not self.done:
            self.event_loop()
            for box in self.inputs:
                box.update()
            self.render()
            pg.display.update()
            self.clock.tick(self.fps)


if __name__ == "__main__":
    app = Control()
    app.main_loop()
    pg.quit()
    sys.exit()
