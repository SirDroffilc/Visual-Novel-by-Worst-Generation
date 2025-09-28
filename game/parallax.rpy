init python:
    import pygame
    import math

    class TrackCursor(renpy.Displayable):

        def __init__(self, child, paramod, inverse=False, **kwargs):
            super(TrackCursor, self).__init__()

            # the displayable (image/layer) being tracked
            self.child = renpy.displayable(child)

            # tracked cursor positions
            self.x = 0
            self.y = 0

            # actual smoothed positions
            self.actual_x = 0
            self.actual_y = 0

            self.paramod = paramod     # strength of parallax
            self.inverse = inverse     # True = opposite (body), False = normal (eyes)
            self.last_st = 0           # last shown time for smooth movement


        def render(self, width, height, st, at):

            rv = renpy.Render(width, height)

            # speed and smoothing
            minimum_speed = 0.5
            maximum_speed = 3
            speed = 1.0

            dx = self.x - self.actual_x
            dy = self.y - self.actual_y

            st_change = st - self.last_st
            self.last_st = st

            # smooth movement (with direction preserved)
            self.actual_x = math.floor(self.actual_x + dx * speed * st_change * self.paramod)
            self.actual_y = math.floor(self.actual_y + dy * speed * st_change * self.paramod)

            # render the tracked child
            cr = renpy.render(self.child, width, height, st, at)
            rv.blit(cr, (self.actual_x, self.actual_y))

            renpy.redraw(self, 0)
            return rv


        def event(self, ev, x, y, st):
            hover = ev.type == pygame.MOUSEMOTION
            click = ev.type == pygame.MOUSEBUTTONDOWN
            if hover or click:
                if self.inverse:
                    # 👈 Opposite direction (for body)
                    self.x = -x / self.paramod
                    self.y = -y / self.paramod
                else:
                    # 👈 Normal parallax (for eyes)
                    self.x = x / self.paramod
                    self.y = y / self.paramod
