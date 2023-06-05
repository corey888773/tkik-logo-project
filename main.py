import sys, os, pygame
from antlr4 import *
from dist.logo_grammarLexer import logo_grammarLexer
from dist.logo_grammarParser import logo_grammarParser
from dist.logo_grammarListener import logo_grammarListener
# from interpreter.listener import Listener
from interpreter.logger import Logger
from interpreter.visitor import Visitor
from typing import Tuple


from drawing.main_window import MainWindow

def execute_script(script: str) -> None:
    data =  InputStream(script)
    lexer = logo_grammarLexer(data)
    stream = CommonTokenStream(lexer)
    parser = logo_grammarParser(stream)
    tree = parser.program()

    _ = Visitor(logger, main_window).visit(tree)

def load_file() -> Tuple[str, str]:
    script = None
    if len(sys.argv) < 2:
        script = input('>>> ')
    else:
        script = open(sys.argv[1]).read()

    if os.system == 'Windows':  
        outfile = sys.argv[1].split('\\')[-1].split('.')[0]
    else:
        outfile = sys.argv[1].split('/')[-1].split('.')[0]
        
    return script, outfile


if __name__ == "__main__":
    script, outfile = load_file()

    logger = Logger()
    main_window = MainWindow(script, outfile)

    running = True
    while running:
        if main_window.text_field.execution_script:
            execute_script(main_window.text_field.execution_script)
            main_window.text_field.execution_script = None
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            else:
                is_still_running = main_window.nextFrame(event=event)

    pygame.quit()

