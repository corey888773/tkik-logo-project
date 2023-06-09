import time
import pygame
from dist.logo_grammarParser import logo_grammarParser
from dist.logo_grammarVisitor import logo_grammarVisitor
from drawing.vehicle import Direction

class Visitor(logo_grammarVisitor):
    
    def __init__(self, log, main_window):
        self.logger = log
        self.main_window = main_window

# Visit a parse tree produced by logo_grammarParser#program.
    def visitProgram(self, ctx:logo_grammarParser.ProgramContext):
        # (instrukcja? KONIEC_WIERSZA+)+ instrukcja? EOF

        for instrukcja in ctx.instrukcja():
            self.visit(instrukcja)


    # Visit a parse tree produced by logo_grammarParser#instrukcja.
    def visitInstrukcja(self, ctx:logo_grammarParser.InstrukcjaContext):
        # polecenie KOMENTARZ? | KOMENTARZ

        if ctx.polecenie():
            self.visit(ctx.polecenie())


    # Visit a parse tree produced by logo_grammarParser#polecenie.
    def visitPolecenie(self, ctx:logo_grammarParser.PolecenieContext):
        # ruch | clearscreen | penup | pendown | hideturtle | showturtle | home | setxy | setpensize | if | repeat

        return self.visitChildren(ctx)


    # Visit a parse tree produced by logo_grammarParser#clearscreen.
    def visitClearscreen(self, ctx:logo_grammarParser.ClearscreenContext):

        self.main_window.canvas.clear()
        return self.visitChildren(ctx)


    # Visit a parse tree produced by logo_grammarParser#penup.
    def visitPenup(self, ctx:logo_grammarParser.PenupContext):

        self.main_window.vehicle.pen.drawing_state = False
        return self.visitChildren(ctx)


    # Visit a parse tree produced by logo_grammarParser#pendown.
    def visitPendown(self, ctx:logo_grammarParser.PendownContext):

        self.main_window.vehicle.pen.drawing_state = True
        return self.visitChildren(ctx)


    # Visit a parse tree produced by logo_grammarParser#hideturtle.
    def visitHideturtle(self, ctx:logo_grammarParser.HideturtleContext):

        self.main_window.vehicle.is_turtle_visible = False
        return self.visitChildren(ctx)


    # Visit a parse tree produced by logo_grammarParser#showturtle.
    def visitShowturtle(self, ctx:logo_grammarParser.ShowturtleContext):

        self.main_window.vehicle.is_turtle_visible = True
        return self.visitChildren(ctx)


    # Visit a parse tree produced by logo_grammarParser#home.
    def visitHome(self, ctx:logo_grammarParser.HomeContext):
        
        self.main_window.vehicle.go_home()
        return self.visitChildren(ctx)


    # Visit a parse tree produced by logo_grammarParser#setxy.
    def visitSetxy(self, ctx:logo_grammarParser.SetxyContext):
        # 'setxy' wyrazenie wyrazenie

        x = self.visit(ctx.wyrazenie(0))
        y = self.visit(ctx.wyrazenie(1))
        self.logger.log(f"setxy {x} {y}")
        self.main_window.vehicle.set_position((x, y))
        return self.visitChildren(ctx)
    

    # Visit a parse tree produced by logo_grammarParser#setpensize.
    def visitSetpensize(self, ctx:logo_grammarParser.SetpensizeContext):
        # ('setps' | 'setpensize') wyrazenie

        size = self.visit(ctx.wyrazenie())
        self.main_window.vehicle.pen.set_pen_size(size)
        return self.visitChildren(ctx)


    # Visit a parse tree produced by logo_grammarParser#if.
    def visitIf(self, ctx:logo_grammarParser.IfContext):
        # 'if' '(' wyrazenie_logiczne ')' blok

        if self.visit(ctx.wyrazenie_logiczne()):
            return self.visit(ctx.blok())


    # Visit a parse tree produced by logo_grammarParser#repeat.
    def visitRepeat(self, ctx:logo_grammarParser.RepeatContext):
        # 'repeat' LICZBA blok

        try:
            count = int(ctx.LICZBA().getText())
        except ValueError:
            self.main_window.text_field.display_error_popup("Repeat number must be an integer.")
            return

        self.logger.log(f"repeat {count}")

        for i in range(count):
            self.visit(ctx.blok())


    # Visit a parse tree produced by logo_grammarParser#ruch.
    def visitRuch(self, ctx:logo_grammarParser.RuchContext):
        # forward | backward | rightturn | leftturn

        if ctx.forward():
            return self.visit(ctx.forward())
        elif ctx.backward():
           return self.visit(ctx.backward())
        elif ctx.rightturn():
            return self.visit(ctx.rightturn())
        elif ctx.leftturn():
            return self.visit(ctx.leftturn())
    

    # Visit a parse tree produced by logo_grammarParser#forward.
    def visitForward(self, ctx:logo_grammarParser.ForwardContext):
        # 'fd' wyrazenie  | 'forward' wyrazenie

        try:
            distance = self.visit(ctx.wyrazenie())
        except ValueError:
            self.main_window.text_field.display_error_popup("Distance must be an integer.")
            return

        self.log_common_move(ctx)
        self.main_window.vehicle.remaining_distance += distance
        self.main_window.vehicle.change_direction(Direction.FORWARD)
        self.main_window.run_frames(distance)


    # Visit a parse tree produced by logo_grammarParser#backward.
    def visitBackward(self, ctx:logo_grammarParser.BackwardContext):
		# 'bk' wyrazenie | 'backward' wyrazenie

        try:
            distance = self.visit(ctx.wyrazenie())
        except ValueError:
            self.main_window.text_field.display_error_popup("Distance must be an integer.")
            return

        self.log_common_move(ctx)
        self.main_window.vehicle.remaining_distance += distance
        self.main_window.vehicle.change_direction(Direction.BACKWARD)
        self.main_window.run_frames(distance)
        self.main_window.vehicle.change_direction(Direction.BACKWARD)


    # Visit a parse tree produced by logo_grammarParser#rightturn.
    def visitRightturn(self, ctx:logo_grammarParser.RightturnContext):
		# 'rt' wyrazenie  | 'rightturn' wyrazenie

        try:
            degrees = self.visit(ctx.wyrazenie())
        except ValueError:
            self.main_window.text_field.display_error_popup("Degrees must be an integer.")
            return

        self.log_common_move(ctx)
        self.main_window.vehicle.change_direction(Direction.RIGHT, degrees)


    # Visit a parse tree produced by logo_grammarParser#leftturn.
    def visitLeftturn(self, ctx:logo_grammarParser.LeftturnContext):
		# 'lt' wyrazenie | 'leftturn' wyrazenie

        try:
            degrees = self.visit(ctx.wyrazenie())
        except ValueError:
            self.main_window.text_field.display_error_popup("Degrees must be an integer.")
            return

        self.log_common_move(ctx)
        self.main_window.vehicle.change_direction(Direction.LEFT, degrees)


    # Visit a parse tree produced by logo_grammarParser#blok.
    def visitBlok(self, ctx:logo_grammarParser.BlokContext):
        # KONIEC_WIERSZA* '{' instrukcja+ '}' KONIEC_WIERSZA*

        for instrukcja in ctx.instrukcja():
            self.visit(instrukcja)


    # Visit a parse tree produced by logo_grammarParser#wyrazenie_logiczne.
    def visitWyrazenie_logiczne(self, ctx:logo_grammarParser.Wyrazenie_logiczneContext):
        # wyrazenie_porownania (OPERATOR_LOGICZNY wyrazenie_porownania)*

        result = self.visit(ctx.wyrazenie_porownania(0))

        for index, i in enumerate(ctx.OPERATOR_LOGICZNY()):
            operator = str(i)
            if operator == "&&":
                result = result and self.visit(ctx.wyrazenie_porownania(index + 1))
            elif operator == "||":
                result = result or self.visit(ctx.wyrazenie_porownania(index + 1))

        return result


    # Visit a parse tree produced by logo_grammarParser#wyrazenie_porownania.
    def visitWyrazenie_porownania(self, ctx:logo_grammarParser.Wyrazenie_porownaniaContext):
        # wartosc_logiczna (OPERATOR_POROWNANIA wartosc_logiczna)?

        result = self.visit(ctx.wartosc_logiczna(0))

        if ctx.OPERATOR_POROWNANIA():
            operator = str(ctx.OPERATOR_POROWNANIA())
            if operator == '<':
                result = result < self.visit(ctx.wartosc_logiczna(1))
            elif operator == '<=':
                result = result <= self.visit(ctx.wartosc_logiczna(1))
            elif operator == '>':
                result = result > self.visit(ctx.wartosc_logiczna(1))
            elif operator == '>=':
                result = result >= self.visit(ctx.wartosc_logiczna(1))
            elif operator == '=':
                result = result == self.visit(ctx.wartosc_logiczna(1))
            elif operator == '!=':
                result = result != self.visit(ctx.wartosc_logiczna(1))

        return result

    # Visit a parse tree produced by logo_grammarParser#wartosc_logiczna.
    def visitWartosc_logiczna(self, ctx:logo_grammarParser.Wartosc_logicznaContext):
        # wyrazenie | '(' wyrazenie_logiczne ')'

        if ctx.wyrazenie():
            return self.visit(ctx.wyrazenie())
        else:
            return self.visit(ctx.wyrazenie_logiczne())

    # Visit a parse tree produced by logo_grammarParser#wyrazenie.
    def visitWyrazenie(self, ctx:logo_grammarParser.WyrazenieContext):
        # wyrazenie_mnozace (OPERATOR_ARYTMETYCZNY wyrazenie_mnozace )*

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
            return self.visit(ctx.wyrazenie()) * (-1 if isNegative else 1)
        else:
            return int(ctx.getText()) * (-1 if isNegative else 1)
        
    def log_common_move(self, ctx):
        value = self.visit(ctx.wyrazenie())
        cmd = ctx.getChild(0).getText()
        self.logger.log(f"ruch {cmd} {value}")
        return value      
    
del logo_grammarParser