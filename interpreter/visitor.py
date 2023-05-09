from dist.logo_grammarParser import logo_grammarParser
from dist.logo_grammarVisitor import logo_grammarVisitor

class Visitor(logo_grammarVisitor):
    
    def __init__(self, log):
        self.logger = log

# Visit a parse tree produced by logo_grammarParser#program.
    def visitProgram(self, ctx:logo_grammarParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by logo_grammarParser#instrukcja.
    def visitInstrukcja(self, ctx:logo_grammarParser.InstrukcjaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by logo_grammarParser#polecenie.
    def visitPolecenie(self, ctx:logo_grammarParser.PolecenieContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by logo_grammarParser#clearscreen.
    def visitClearscreen(self, ctx:logo_grammarParser.ClearscreenContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by logo_grammarParser#penup.
    def visitPenup(self, ctx:logo_grammarParser.PenupContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by logo_grammarParser#pendown.
    def visitPendown(self, ctx:logo_grammarParser.PendownContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by logo_grammarParser#hideturtle.
    def visitHideturtle(self, ctx:logo_grammarParser.HideturtleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by logo_grammarParser#showturtle.
    def visitShowturtle(self, ctx:logo_grammarParser.ShowturtleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by logo_grammarParser#home.
    def visitHome(self, ctx:logo_grammarParser.HomeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by logo_grammarParser#setxy.
    def visitSetxy(self, ctx:logo_grammarParser.SetxyContext):
        value_1 = self.visit(ctx.wyrazenie(0))
        self.logger.log('\n\n\n\n')
        value_2 = self.visit(ctx.wyrazenie(1))
        self.logger.log(f"setxy {value_1} {value_2}")
        return self.visitChildren(ctx)


    # Visit a parse tree produced by logo_grammarParser#setpensize.
    def visitSetpensize(self, ctx:logo_grammarParser.SetpensizeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by logo_grammarParser#if.
    def visitIf(self, ctx:logo_grammarParser.IfContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by logo_grammarParser#repeat.
    def visitRepeat(self, ctx:logo_grammarParser.RepeatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by logo_grammarParser#ruch.
    def visitRuch(self, ctx:logo_grammarParser.RuchContext):
        # : forward
        # | backward
        # | rightturn
        # | leftturn
        return self.visitChildren(ctx)
    
    # Visit a parse tree produced by logo_grammarParser#forward.
    def visitForward(self, ctx:logo_grammarParser.ForwardContext):
        # : 'fd' wyrazenie 
		# | 'forward' wyrazenie
        self.log_common_move(ctx)

        return self.visitChildren(ctx)


    # Visit a parse tree produced by logo_grammarParser#backward.
    def visitBackward(self, ctx:logo_grammarParser.BackwardContext):
		# : 'bk' wyrazenie 
		# | 'backward' wyrazenie
        self.log_common_move(ctx)

        return self.visitChildren(ctx)


    # Visit a parse tree produced by logo_grammarParser#rightturn.
    def visitRightturn(self, ctx:logo_grammarParser.RightturnContext):
		# : 'rt' wyrazenie 
		# | 'rightturn' wyrazenie
        self.log_common_move(ctx)
        
        return self.visitChildren(ctx)


    # Visit a parse tree produced by logo_grammarParser#leftturn.
    def visitLeftturn(self, ctx:logo_grammarParser.LeftturnContext):
		# : 'lt' wyrazenie 
		# | 'leftturn' wyrazenie
        self.log_common_move(ctx)
        
        return self.visitChildren(ctx)


    # Visit a parse tree produced by logo_grammarParser#blok.
    def visitBlok(self, ctx:logo_grammarParser.BlokContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by logo_grammarParser#wyrazenie_logiczne.
    def visitWyrazenie_logiczne(self, ctx:logo_grammarParser.Wyrazenie_logiczneContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by logo_grammarParser#wyrazenie_porownania.
    def visitWyrazenie_porownania(self, ctx:logo_grammarParser.Wyrazenie_porownaniaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by logo_grammarParser#wartosc_logiczna.
    def visitWartosc_logiczna(self, ctx:logo_grammarParser.Wartosc_logicznaContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by logo_grammarParser#wyrazenie.
    def visitWyrazenie(self, ctx:logo_grammarParser.WyrazenieContext):
        # wyrazenie_mnozace (OPERATOR_ARYTMETYCZNY wyrazenie_mnozace )*
        self.logger.log(f"wyrażenie {ctx.getText()} a to mój operator arytmetyczny: {ctx.OPERATOR_ARYTMETYCZNY(0)}")
        self.logger.log(f"jestem w WYRAŻENIE przechodzę do wyrażenia mnożącego\n")
        result = self.visit(ctx.wyrazenie_mnozace(0))
        
        for index, i in enumerate(ctx.OPERATOR_ARYTMETYCZNY()):
            operator = str(i)
            if operator == '+':
                result = result + self.visit(ctx.wyrazenie_mnozace(index+1))
            elif operator == '-':
                result = result - self.visit(ctx.wyrazenie_mnozace(index+1))
        
        return result


    # Visit a parse tree produced by logo_grammarParser#wyrazenie_mnozace.
    def visitWyrazenie_mnozace(self, ctx:logo_grammarParser.Wyrazenie_mnozaceContext):
        # wartosc_liczbowa (OPERATOR_MNOZACY wartosc_liczbowa)*
        self.logger.log(f"wyrażenie mnożące {ctx.getText()} a to mój operator mnożący: {ctx.OPERATOR_MNOZACY(0)}")
        self.logger.log("jestem w WYRAŻENIE_MNOŻĄCE przechodzę do wartosci liczbowej \n")
        result = self.visit(ctx.wartosc_liczbowa(0))

        for index, i in enumerate(ctx.OPERATOR_MNOZACY()):
            operator = str(i)
            if operator == '*':
                result = result * self.visit(ctx.wartosc_liczbowa(index+1))
            elif operator == '/':
                if type(result) == type(1) and type(self.visit(ctx.wartosc_liczbowa(index+1))) == type(1):
                    result = result // self.visit(ctx.wartosc_liczbowa(index+1))
                else:
                    result = result / self.visit(ctx.wartosc_liczbowa(index+1))
            elif operator == '%':
                result = result % self.visit(ctx.wartosc_liczbowa(index+1))
        return result


    # Visit a parse tree produced by logo_grammarParser#wartosc_liczbowa.
    def visitWartosc_liczbowa(self, ctx:logo_grammarParser.Wartosc_liczbowaContext):
        #  OPERATOR_ZNAKU? (LICZBA | '(' wyrazenie ')')
        isNegative = ctx.OPERATOR_ZNAKU() != None and ctx.getText().startswith('-')
            
        if ctx.wyrazenie():
            self.logger.log(f"wartosc_liczbowa {ctx.getText()} znak ujemny: {isNegative} wyrazenie")
            self.logger.log(("jestem w WARTOŚĆ_LICZBOWA przechodzę do wyrażenia \n"))
            return self.visit(ctx.wyrazenie()) * (-1 if isNegative else 1)
        else:
            self.logger.log(f"wartosc_liczbowa {ctx.getText()} znak ujemny: {isNegative} wartosc")
            self.logger.log(("jestem w WARTOŚĆ_LICZBOWA zwracam wartość liczbową \n"))
            return int(ctx.getText()) * (-1 if isNegative else 1)
        
    def log_common_move(self, ctx):
        value = self.visit(ctx.wyrazenie())
        cmd = ctx.getChild(0).getText()
        self.logger.log(f"ruch {cmd} {value}")
        return value
    
del logo_grammarParser
    
