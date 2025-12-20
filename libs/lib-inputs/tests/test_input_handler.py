from lib_inputs import InputHandler
from .conftest import test_handler
import pygame

from unittest.mock import MagicMock


def _write_instructions_text(instructions, ih, south_just_pressed_count = 0, west_just_pressed_count = 0):
    instruction_text = test_handler.font.render(instructions, 1, pygame.Color("RED"))

    pos_y = 0
    test_handler.screen.blit(instruction_text,(0,0))

    pos_y += 20
    test_handler.screen.blit(
        test_handler.font.render(f"Mouse pos: {str(ih.get_mouse_pos())}", 1, pygame.Color("RED"))
        ,(0,pos_y))
    
    pos_y += 20
    test_handler.screen.blit(
        test_handler.font.render(f"south: {str(ih.south)}", 1, pygame.Color("RED"))
        ,(0,pos_y))
    pos_y += 20
    test_handler.screen.blit(
        test_handler.font.render(f"just pressed south: {str(ih.south_just_pressed)}", 1, pygame.Color("RED"))
        ,(0,pos_y))
    pos_y += 20
    test_handler.screen.blit(
        test_handler.font.render(f"just pressed south: {str(south_just_pressed_count)}", 1, pygame.Color("RED"))
        ,(0,pos_y))
    
    pos_y += 20
    test_handler.screen.blit(
        test_handler.font.render(f"primary: {str(ih.primary)}", 1, pygame.Color("RED"))
        ,(0,pos_y))
    
    pos_y += 20
    test_handler.screen.blit(
        test_handler.font.render(f"west: {str(ih.west)}", 1, pygame.Color("RED"))
        ,(0,pos_y))
    
    pos_y += 20
    test_handler.screen.blit(
        test_handler.font.render(f"just pressed west: {str(ih.west_just_pressed)}", 1, pygame.Color("RED"))
        ,(0,pos_y))
    
    pos_y += 20
    test_handler.screen.blit(
        test_handler.font.render(f"just pressed west: {str(west_just_pressed_count)}", 1, pygame.Color("RED"))
        ,(0,pos_y))
    pass

def _mock_mouse_input_event(ih, button, down = True):
    event = MagicMock()
    event.button = button
    if down:
        event.type = pygame.MOUSEBUTTONDOWN
    else:
        event.type = pygame.MOUSEBUTTONUP

    print("mock input", event.type, event.button)
    ih.handle_event(event)


# lib-sprites\tests\test_mouse.py
def test_mouse_primary_click():

    event = MagicMock()
    event.type = pygame.MOUSEBUTTONDOWN
    event.button = 1

    print(event)
    print(event.type)
    print(event.button)

    ih = InputHandler(pygame)

    mouse_pos = (0,0)

    south_just_pressed_count = 0
    west_just_pressed_count = 0

    instructions = "Update"
    def callback():
        _write_instructions_text(instructions, ih, south_just_pressed_count, west_just_pressed_count)
        return

    # feed the input handler events.
    # It also should have access to things like fetching the mouse position.


    is_first_loop = True
    while(test_handler.do_iteration(ih, callback)):
        instructions = "Left Click Press And Hold"
        mouse_pos = ih.get_mouse_pos()
        assert mouse_pos is not None
        assert len(mouse_pos) == 2

        if is_first_loop:
            # fire event is being pressed
            assert ih.south is False
            assert ih.primary is False

        if test_handler.is_ci_test:
            _mock_mouse_input_event(ih, 1)

        if ih.south is True:
            break
        # default bindings
        is_first_loop = False

        if ih.south_just_pressed:
            south_just_pressed += 1
        if ih.west_just_pressed:
            west_just_pressed_count += 1
        pass
    is_first_loop = True

    while(test_handler.do_iteration(ih, callback)):
        instructions = "Left Click Release"

        mouse_pos = ih.get_mouse_pos()
        assert mouse_pos is not None
        assert len(mouse_pos) == 2

        if is_first_loop:
            # fire event is being pressed
            assert ih.south is True
            assert ih.primary is True

        if test_handler.is_ci_test:
            _mock_mouse_input_event(ih, 1, False)

        if ih.south is False:
            break
        # default bindings
        is_first_loop = False
        pass

    assert ih.south is False
    assert ih.primary is False


    pass


def test_mouse_right_click():

    ih = InputHandler(pygame)

    mouse_pos = (0,0)

    instructions = "Update"
    def callback():
        _write_instructions_text(instructions, ih)
        return

    # feed the input handler events.
    # It also should have access to things like fetching the mouse position.

    is_first_loop = True
    while(test_handler.do_iteration(ih, callback)):
        instructions = "Right Click Press And Hold"
        mouse_pos = ih.get_mouse_pos()
        assert mouse_pos is not None
        assert len(mouse_pos) == 2

        if is_first_loop:
            # fire event is being pressed
            assert ih.west is False

        if test_handler.is_ci_test:
            _mock_mouse_input_event(ih, 3)

        if ih.west is True:
            break
        # default bindings
        is_first_loop = False
        pass
    is_first_loop = True

    while(test_handler.do_iteration(ih, callback)):
        instructions = "Right Click Release"

        mouse_pos = ih.get_mouse_pos()
        assert mouse_pos is not None
        assert len(mouse_pos) == 2

        if is_first_loop:
            # fire event is being pressed
            assert ih.west is True

        if test_handler.is_ci_test:
            _mock_mouse_input_event(ih, 3, False)

        if ih.west is False:
            break
        # default bindings
        is_first_loop = False
        pass

    assert ih.west is False


    pass