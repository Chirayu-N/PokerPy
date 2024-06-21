# PokerPy
Python implementation of standard No Limit Texas Hold'em and a bot to play against.

## Project Components
A clean implementation of the poker game itself:
- `cards.py`: useful functions for managing and dealing a standard 52-card deck
- `hand_eval.py`: evaluate two-card poker hand and determine which hand wins
- `simulation.py`: client for simulating a heads-up (2-player) poker round, showing the hand evaluation after the flop, turn, and river

(WIP) A implementation of a poker bot to play against:
- Planned to use reinforcement learning/counterfactual regret minimization