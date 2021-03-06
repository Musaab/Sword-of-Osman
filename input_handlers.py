# Possible commands in the game
from game_states import GameStates

MoveUp = {'move': (0, -1)}
MoveDown = {'move': (0, 1)}
MoveLeft = {'move': (-1, 0)}
MoveRight = {'move': (1, 0)}
MoveUpLeft = {'move': (-1, -1)}
MoveUpRight = {'move': (1, -1)}
MoveDownLeft = {'move': (-1, 1)}
MoveDownRight = {'move': (1, 1)}
Wait = {'wait': True}
Pickup = {'pickup': True}
ShowInventory = {'show_inventory': True}
DropInventory = {'drop_inventory': True}
TakeStairs = {'take_stairs': True}
ShowCharacterScreen = {'show_character_screen': True}

FullScreen = {'fullscreen': True}
Exit = {'exit': True}

NewGame = {'new_game': True}
LoadGame = {'load_game': True}

# Keybindings tied to commands.  Will eventually be able to be changed by user.
keybindings = {
    'UP': MoveUp,
    'DOWN': MoveDown,
    'LEFT': MoveLeft,
    'RIGHT': MoveRight,
    'h': MoveLeft,
    'j': MoveDown,
    'k': MoveUp,
    'l': MoveRight,
    'y': MoveUpLeft,
    'u': MoveUpRight,
    'b': MoveDownLeft,
    'n': MoveDownRight,
    'g': Pickup,
    'i': ShowInventory,
    'd': DropInventory,
    'c': ShowCharacterScreen,
    'z': Wait
}


def handle_keys(user_input, game_state):
    if user_input:
        if game_state == GameStates.PLAYERS_TURN:
            return handle_player_turn_keys(user_input)
        elif game_state == GameStates.PLAYER_DEAD:
            return handle_player_dead_keys(user_input)
        elif game_state == GameStates.TARGETING:
            return handle_targeting_keys(user_input)
        elif game_state in (GameStates.SHOW_INVENTORY, GameStates.DROP_INVENTORY):
            return handle_inventory_keys(user_input)
        elif game_state == GameStates.LEVEL_UP:
            return handle_level_up_menu(user_input)
        elif game_state == GameStates.CHARACTER_SCREEN:
            return handle_character_screen(user_input)

    return {}


def handle_player_turn_keys(user_input):
    key_char = user_input.char

    if user_input.key in keybindings:
        return keybindings[user_input.key]
    elif key_char in keybindings:
        return keybindings[key_char]
    elif key_char == '.' and user_input.shift:
        return TakeStairs

    if user_input.key == 'ENTER' and user_input.alt:
        # Alt+Enter: toggle full screen
        return FullScreen
    elif user_input.key == 'ESCAPE':
        # Exit the game
        return Exit

    # No key was pressed
    return {}


def handle_targeting_keys(user_input):
    if user_input.key == 'ESCAPE':
        return Exit

    return {}


def handle_player_dead_keys(user_input):
    key_char = user_input.char

    if key_char == 'i':
        return ShowInventory

    if user_input.key == 'ENTER' and user_input.alt:
        # Alt+Enter: toggle full screen
        return FullScreen
    elif user_input.key == 'ESCAPE':
        # Exit the game
        return Exit

    # No key was pressed
    return {}


def handle_main_menu(user_input):
    if user_input:
        key_char = user_input.char

        if key_char == 'a':
            return NewGame
        elif key_char == 'b':
            return LoadGame
        elif key_char == 'c' or user_input.key == 'ESCAPE':
            return Exit

    return {}


def handle_level_up_menu(user_input):
    if user_input:
        key_char = user_input.char

        if key_char == 'a':
            return {'level_up': 'hp'}
        elif key_char == 'b':
            return {'level_up': 'str'}
        elif key_char == 'c':
            return {'level_up': 'def'}

    return {}


def handle_character_screen(user_input):
    if user_input.key == 'ESCAPE':
        return {'exit': True}

    return {}


def handle_mouse(mouse_event):
    if mouse_event:
        (x, y) = mouse_event.cell

        if mouse_event.button == 'LEFT':
            return {'left_click': (x, y)}
        elif mouse_event.button == 'RIGHT':
            return {'right_click': (x, y)}

    return {}


def handle_inventory_keys(user_input):
    if not user_input.char:
        return {}

    index = ord(user_input.char) - ord('a')

    if index >= 0:
        return {'inventory_index': index}

    if user_input.key == 'ENTER' and user_input.alt:
        # Alt+Enter: toggle full screen
        return FullScreen
    elif user_input.key == 'ESCAPE':
        # Exit the game
        return Exit

    return {}
