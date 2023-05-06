# Generated from logo_grammar.g4 by ANTLR 4.12.0
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .logo_grammarParser import logo_grammarParser
else:
    from logo_grammarParser import logo_grammarParser

# This class defines a complete listener for a parse tree produced by logo_grammarParser.
class logo_grammarListener(ParseTreeListener):

    # Enter a parse tree produced by logo_grammarParser#program.
    def enterProgram(self, ctx:logo_grammarParser.ProgramContext):
        pass

    # Exit a parse tree produced by logo_grammarParser#program.
    def exitProgram(self, ctx:logo_grammarParser.ProgramContext):
        pass


    # Enter a parse tree produced by logo_grammarParser#instrukcja.
    def enterInstrukcja(self, ctx:logo_grammarParser.InstrukcjaContext):
        pass

    # Exit a parse tree produced by logo_grammarParser#instrukcja.
    def exitInstrukcja(self, ctx:logo_grammarParser.InstrukcjaContext):
        pass


    # Enter a parse tree produced by logo_grammarParser#polecenie.
    def enterPolecenie(self, ctx:logo_grammarParser.PolecenieContext):
        pass

    # Exit a parse tree produced by logo_grammarParser#polecenie.
    def exitPolecenie(self, ctx:logo_grammarParser.PolecenieContext):
        pass


    # Enter a parse tree produced by logo_grammarParser#ruch.
    def enterRuch(self, ctx:logo_grammarParser.RuchContext):
        pass

    # Exit a parse tree produced by logo_grammarParser#ruch.
    def exitRuch(self, ctx:logo_grammarParser.RuchContext):
        pass


    # Enter a parse tree produced by logo_grammarParser#blok.
    def enterBlok(self, ctx:logo_grammarParser.BlokContext):
        pass

    # Exit a parse tree produced by logo_grammarParser#blok.
    def exitBlok(self, ctx:logo_grammarParser.BlokContext):
        pass


    # Enter a parse tree produced by logo_grammarParser#wyrazenie_logiczne.
    def enterWyrazenie_logiczne(self, ctx:logo_grammarParser.Wyrazenie_logiczneContext):
        pass

    # Exit a parse tree produced by logo_grammarParser#wyrazenie_logiczne.
    def exitWyrazenie_logiczne(self, ctx:logo_grammarParser.Wyrazenie_logiczneContext):
        pass


    # Enter a parse tree produced by logo_grammarParser#wyrazenie_porownania.
    def enterWyrazenie_porownania(self, ctx:logo_grammarParser.Wyrazenie_porownaniaContext):
        pass

    # Exit a parse tree produced by logo_grammarParser#wyrazenie_porownania.
    def exitWyrazenie_porownania(self, ctx:logo_grammarParser.Wyrazenie_porownaniaContext):
        pass


    # Enter a parse tree produced by logo_grammarParser#wartosc_logiczna.
    def enterWartosc_logiczna(self, ctx:logo_grammarParser.Wartosc_logicznaContext):
        pass

    # Exit a parse tree produced by logo_grammarParser#wartosc_logiczna.
    def exitWartosc_logiczna(self, ctx:logo_grammarParser.Wartosc_logicznaContext):
        pass


    # Enter a parse tree produced by logo_grammarParser#wyrazenie.
    def enterWyrazenie(self, ctx:logo_grammarParser.WyrazenieContext):
        pass

    # Exit a parse tree produced by logo_grammarParser#wyrazenie.
    def exitWyrazenie(self, ctx:logo_grammarParser.WyrazenieContext):
        pass


    # Enter a parse tree produced by logo_grammarParser#wyrazenie_mnozace.
    def enterWyrazenie_mnozace(self, ctx:logo_grammarParser.Wyrazenie_mnozaceContext):
        pass

    # Exit a parse tree produced by logo_grammarParser#wyrazenie_mnozace.
    def exitWyrazenie_mnozace(self, ctx:logo_grammarParser.Wyrazenie_mnozaceContext):
        pass


    # Enter a parse tree produced by logo_grammarParser#wartosc_liczbowa.
    def enterWartosc_liczbowa(self, ctx:logo_grammarParser.Wartosc_liczbowaContext):
        pass

    # Exit a parse tree produced by logo_grammarParser#wartosc_liczbowa.
    def exitWartosc_liczbowa(self, ctx:logo_grammarParser.Wartosc_liczbowaContext):
        pass



del logo_grammarParser