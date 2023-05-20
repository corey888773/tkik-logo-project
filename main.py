import sys
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
        
    logger = Logger()
    main_window = MainWindow()
        
    data =  InputStream(program)
    lexer = logo_grammarLexer(data)
    stream = CommonTokenStream(lexer)
    parser = logo_grammarParser(stream)
    tree = parser.program()

        # First run
    # output = ParseTreeWalker().walk(logo_grammarListener(), tree)
    
    output = Visitor(logger, main_window).visit(tree)
    
    logger.log(f"Output: {output}")
    
    