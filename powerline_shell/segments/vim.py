from ..utils import BasicSegment
import os


class Segment(BasicSegment):
    def add_to_powerline(self):
        mode = os.getenv('VIMODE')
        if mode is None:
            return
        bg = self.powerline.theme.AWS_PROFILE_FG
        fg = self.powerline.theme.AWS_PROFILE_BG
        self.powerline.append(" " + mode + " ", fg, bg)
