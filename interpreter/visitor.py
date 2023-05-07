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
        return self.visitChildren(ctx)


    # Visit a parse tree produced by logo_grammarParser#wyrazenie_mnozace.
    def visitWyrazenie_mnozace(self, ctx:logo_grammarParser.Wyrazenie_mnozaceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by logo_grammarParser#wartosc_liczbowa.
    def visitWartosc_liczbowa(self, ctx:logo_grammarParser.Wartosc_liczbowaContext):
        return int(ctx.getText())

del logo_grammarParser