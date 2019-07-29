
class KataBowling:

    def __init__(self):
        self.current_roll = 0
        self.rolls = []

    def roll(self, pins):
        self.rolls.append(pins)

    @property
    def score(self):
        score_ = 0
        rolls = self.rolls

        frame_index = 0
        for i in range(0, 10):
            if self._is_strike(frame_index):
                score_ += 10 + self._strike_bonus(frame_index)
                frame_index += 1
            elif self._is_spare(frame_index):
                score_ += 10 + rolls[frame_index+2]
                frame_index += 2
            else:
                score_ += rolls[frame_index] + rolls[frame_index+1]
                frame_index += 2

        return score_

    def _is_spare(self, frame_index):
        return self.rolls[frame_index] + self.rolls[frame_index+1] == 10

    def _is_strike(self, frame_index):
        return self.rolls[frame_index] == 10

    def _strike_bonus(self, frame_index):
        return self.rolls[frame_index+1] + self.rolls[frame_index+2]
