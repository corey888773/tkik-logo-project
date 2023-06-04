import sys, os, pygame
from antlr4 import *
from dist.logo_grammarLexer import logo_grammarLexer
from dist.logo_grammarParser import logo_grammarParser
from dist.logo_grammarListener import logo_grammarListener
# from interpreter.listener import Listener
from interpreter.logger import Logger
from interpreter.visitor import Visitor


from drawing.main_window import MainWindow


if __name__ == "__main__":
    program = None
    if len(sys.argv) < 2:
        program = input('>>> ')
    else:
        program = open(sys.argv[1]).read()

    if os.system == 'Windows':  
        outfile = sys.argv[1].split('\\')[-1].split('.')[0]
    else:
        outfile = sys.argv[1].split('/')[-1].split('.')[0]

    logger = Logger()
    main_window = MainWindow(program)

    data =  InputStream(program)
    lexer = logo_grammarLexer(data)
    stream = CommonTokenStream(lexer)
    parser = logo_grammarParser(stream)
    tree = parser.program()

        # First run
    # output = ParseTreeWalker().walk(logo_grammarListener(), tree)

    output = Visitor(logger, main_window).visit(tree)

    logger.log(f"Output: {output}")

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: #or event.type == pygame.MOUSEBUTTONDOWN
                running = False
            else:
                main_window.nextFrame(event=event)

                
    main_window.save(outfile)
    pygame.quit()
