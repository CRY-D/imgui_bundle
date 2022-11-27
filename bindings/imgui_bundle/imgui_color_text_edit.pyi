"""
Python port of ImGuiColorTextEdit: https://github.com/BalazsJako/ImGuiColorTextEdit

Below is the readme from the project
====================================

# ImGuiColorTextEdit
Syntax highlighting text editor for ImGui

![Screenshot](https://github.com/BalazsJako/ImGuiColorTextEdit/wiki/ImGuiTextEdit.png "Screenshot")

Demo project: https://github.com/BalazsJako/ColorTextEditorDemo

This started as my attempt to write a relatively simple widget which provides text editing functionality with syntax highlighting. Now there are other contributors who provide valuable additions.

While it relies on Omar Cornut's https://github.com/ocornut/imgui, it does not follow the "pure" one widget - one function approach. Since the editor has to maintain a relatively complex and large internal state, it did not seem to be practical to try and enforce fully immediate mode. It stores its internal state in an object instance which is reused across frames.

The code is (still) work in progress, please report if you find any issues.

# Main features
 - approximates typical code editor look and feel (essential mouse/keyboard commands work - I mean, the commands _I_ normally use :))
 - undo/redo
 - UTF-8 support
 - works with both fixed and variable-width fonts
 - extensible syntax highlighting for multiple languages
 - identifier declarations: a small piece of description can be associated with an identifier. The editor displays it in a tooltip when the mouse cursor is hovered over the identifier
 - error markers: the user can specify a list of error messages together the line of occurence, the editor will highligh the lines with red backround and display error message in a tooltip when the mouse cursor is hovered over the line
 - large files: there is no explicit limit set on file size or number of lines (below 2GB, performance is not affected when large files are loaded (except syntax coloring, see below)
 - color palette support: you can switch between different color palettes, or even define your own
 - whitespace indicators (TAB, space)

# Known issues
 - syntax highligthing of most languages - except C/C++ - is based on std::regex, which is diasppointingly slow. Because of that, the highlighting process is amortized between multiple frames. C/C++ has a hand-written tokenizer which is much faster.

Please post your screenshots if you find this little piece of software useful. :)

# Contribute

If you want to contribute, please refer to CONTRIBUTE file.

"""
from __future__ import annotations
from typing import List, Any, Dict, Set
import numpy as np
import enum

from imgui_bundle.imgui import ImVec2


String = str
Identifiers = Dict[str, Any] # Dict[str, Identifier] (but Identifier is defined later in the generated code)
Keywords = Set[str]
ErrorMarkers = Dict[int, str]
Breakpoints = Set[int]
Palette = List[int]
Char = int


# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!  AUTOGENERATED CODE !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# <litgen_stub> // Autogenerated code below! Do not edit!
####################    <generated_from:TextEditor.h>    ####################


class TextEditor:
    class PaletteIndex(enum.Enum):
        default = enum.auto()                    # (= 0)
        keyword = enum.auto()                    # (= 1)
        number = enum.auto()                     # (= 2)
        string = enum.auto()                     # (= 3)
        char_literal = enum.auto()               # (= 4)
        punctuation = enum.auto()                # (= 5)
        preprocessor = enum.auto()               # (= 6)
        identifier = enum.auto()                 # (= 7)
        known_identifier = enum.auto()           # (= 8)
        preproc_identifier = enum.auto()         # (= 9)
        comment = enum.auto()                    # (= 10)
        multi_line_comment = enum.auto()         # (= 11)
        background = enum.auto()                 # (= 12)
        cursor = enum.auto()                     # (= 13)
        selection = enum.auto()                  # (= 14)
        error_marker = enum.auto()               # (= 15)
        breakpoint = enum.auto()                 # (= 16)
        line_number = enum.auto()                # (= 17)
        current_line_fill = enum.auto()          # (= 18)
        current_line_fill_inactive = enum.auto() # (= 19)
        current_line_edge = enum.auto()          # (= 20)
        max = enum.auto()                        # (= 21)

    class SelectionMode(enum.Enum):
        normal = enum.auto()                     # (= 0)
        word = enum.auto()                       # (= 1)
        line = enum.auto()                       # (= 2)

    class Breakpoint:
        m_line: int
        m_enabled: bool
        m_condition: str

        def __init__(self) -> None:
            pass


    class Coordinates:
        """ Represents a character coordinate from the user's point of view,
         i. e. consider an uniform grid (assuming fixed-width font) on the
         screen as it is rendered, and each cell has its own coordinate, starting from 0.
         Tabs are counted as [1..mTabSize] count empty spaces, depending on
         how many space is necessary to reach the next tab stop.
         For example, coordinate (1, 5) represents the character 'B' in a line "\tABC", when mTabSize = 4,
         because it is rendered as "    ABC" on the screen.
        """
        m_line: int
        m_column: int
        def __init__(self) -> None:
            pass
        def __init__(self, a_line: int, a_column: int) -> None:
            pass
        @staticmethod
        def invalid() -> Coordinates:
            pass

        def __eq__(self, o: Coordinates) -> bool:
            pass

        def __ne__(self, o: Coordinates) -> bool:
            pass

        def __lt__(self, o: Coordinates) -> bool:
            pass

        def __gt__(self, o: Coordinates) -> bool:
            pass

        def __le__(self, o: Coordinates) -> bool:
            pass

        def __ge__(self, o: Coordinates) -> bool:
            pass


    class Identifier:
        m_location: Coordinates
        m_declaration: str
        def __init__(
            self,
            m_location: Coordinates = Coordinates(),
            m_declaration: str = ""
            ) -> None:
            """Auto-generated default constructor"""
            pass


    class Glyph:
        m_char: Char
        m_color_index: PaletteIndex = PaletteIndex.default

        def __init__(self, a_char: Char, a_color_index: PaletteIndex) -> None:
            pass



    class LanguageDefinition:

        m_name: str
        m_keywords: Keywords
        m_identifiers: Identifiers
        m_preproc_identifiers: Identifiers
        m_comment_start: str
        m_comment_end: str
        m_single_line_comment: str
        m_auto_indentation: bool


        m_token_regex_strings: TokenRegexStrings

        m_case_sensitive: bool

        def __init__(self) -> None:
            pass

        @staticmethod
        def c_plus_plus() -> LanguageDefinition:
            pass
        @staticmethod
        def hlsl() -> LanguageDefinition:
            pass
        @staticmethod
        def glsl() -> LanguageDefinition:
            pass
        @staticmethod
        def c() -> LanguageDefinition:
            pass
        @staticmethod
        def sql() -> LanguageDefinition:
            pass
        @staticmethod
        def angel_script() -> LanguageDefinition:
            pass
        @staticmethod
        def lua() -> LanguageDefinition:
            pass
        @staticmethod
        def python() -> LanguageDefinition:
            pass



    def set_language_definition(
        self,
        a_language_def: TextEditor.LanguageDefinition
        ) -> None:
        pass
    def get_language_definition(self) -> TextEditor.LanguageDefinition:
        pass

    def get_palette(self) -> Palette:
        pass
    def set_palette(self, a_value: Palette) -> None:
        pass

    def set_error_markers(self, a_markers: ErrorMarkers) -> None:
        pass
    def set_breakpoints(self, a_markers: Breakpoints) -> None:
        pass

    def render(
        self,
        a_title: str,
        a_size: ImVec2 = ImVec2(),
        a_border: bool = False
        ) -> None:
        pass
    def set_text(self, a_text: str) -> None:
        pass
    def get_text(self) -> str:
        pass

    def set_text_lines(self, a_lines: List[str]) -> None:
        pass
    def get_text_lines(self) -> List[str]:
        pass

    def get_selected_text(self) -> str:
        pass
    def get_current_line_text(self) -> str:
        pass

    def get_total_lines(self) -> int:
        pass
    def is_overwrite(self) -> bool:
        pass

    def set_read_only(self, a_value: bool) -> None:
        pass
    def is_read_only(self) -> bool:
        pass
    def is_text_changed(self) -> bool:
        pass
    def is_cursor_position_changed(self) -> bool:
        pass

    def is_colorizer_enabled(self) -> bool:
        pass
    def set_colorizer_enable(self, a_value: bool) -> None:
        pass

    def get_cursor_position(self) -> TextEditor.Coordinates:
        pass
    def set_cursor_position(
        self,
        a_position: TextEditor.Coordinates,
        cursor_line_on_page: int = -1
        ) -> None:
        pass

    def set_handle_mouse_inputs(self, a_value: bool) -> None:
        pass
    def is_handle_mouse_inputs_enabled(self) -> bool:
        pass

    def set_handle_keyboard_inputs(self, a_value: bool) -> None:
        pass
    def is_handle_keyboard_inputs_enabled(self) -> bool:
        pass

    def set_im_gui_child_ignored(self, a_value: bool) -> None:
        pass
    def is_im_gui_child_ignored(self) -> bool:
        pass

    def set_show_whitespaces(self, a_value: bool) -> None:
        pass
    def is_showing_whitespaces(self) -> bool:
        pass

    def set_tab_size(self, a_value: int) -> None:
        pass
    def get_tab_size(self) -> int:
        pass

    def insert_text(self, a_value: str) -> None:
        pass
    def insert_text(self, a_value: str) -> None:
        pass

    def move_up(self, a_amount: int = 1, a_select: bool = False) -> None:
        pass
    def move_down(self, a_amount: int = 1, a_select: bool = False) -> None:
        pass
    def move_left(
        self,
        a_amount: int = 1,
        a_select: bool = False,
        a_word_mode: bool = False
        ) -> None:
        pass
    def move_right(
        self,
        a_amount: int = 1,
        a_select: bool = False,
        a_word_mode: bool = False
        ) -> None:
        pass
    def move_top(self, a_select: bool = False) -> None:
        pass
    def move_bottom(self, a_select: bool = False) -> None:
        pass
    def move_home(self, a_select: bool = False) -> None:
        pass
    def move_end(self, a_select: bool = False) -> None:
        pass

    def set_selection_start(self, a_position: TextEditor.Coordinates) -> None:
        pass
    def set_selection_end(self, a_position: TextEditor.Coordinates) -> None:
        pass
    def set_selection(
        self,
        a_start: TextEditor.Coordinates,
        a_end: TextEditor.Coordinates,
        a_mode: TextEditor.SelectionMode = TextEditor.SelectionMode.normal
        ) -> None:
        pass
    def select_word_under_cursor(self) -> None:
        pass
    def select_all(self) -> None:
        pass
    def has_selection(self) -> bool:
        pass

    def copy(self) -> None:
        pass
    def cut(self) -> None:
        pass
    def paste(self) -> None:
        pass
    def delete(self) -> None:
        pass

    def can_undo(self) -> bool:
        pass
    def can_redo(self) -> bool:
        pass
    def undo(self, a_steps: int = 1) -> None:
        pass
    def redo(self, a_steps: int = 1) -> None:
        pass

    @staticmethod
    def get_dark_palette() -> Palette:
        pass
    @staticmethod
    def get_light_palette() -> Palette:
        pass
    @staticmethod
    def get_retro_blue_palette() -> Palette:
        pass

    def __init__(self) -> None:
        """Autogenerated default constructor"""
        pass
####################    </generated_from:TextEditor.h>    ####################

# </litgen_stub> // Autogenerated code end!
