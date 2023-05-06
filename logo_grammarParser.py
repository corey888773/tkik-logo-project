# Generated from logo_grammar.g4 by ANTLR 4.12.0
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,36,146,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,1,0,3,0,24,8,0,1,0,4,0,27,8,
        0,11,0,12,0,28,4,0,31,8,0,11,0,12,0,32,1,0,3,0,36,8,0,1,0,1,0,1,
        1,1,1,3,1,42,8,1,1,1,3,1,45,8,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,
        1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,3,2,69,8,
        2,1,3,1,3,1,3,1,3,1,3,3,3,76,8,3,1,3,3,3,79,8,3,1,4,5,4,82,8,4,10,
        4,12,4,85,9,4,1,4,1,4,4,4,89,8,4,11,4,12,4,90,1,4,1,4,5,4,95,8,4,
        10,4,12,4,98,9,4,1,5,1,5,1,5,5,5,103,8,5,10,5,12,5,106,9,5,1,6,1,
        6,1,6,3,6,111,8,6,1,7,1,7,1,7,1,7,1,7,3,7,118,8,7,1,8,1,8,1,8,5,
        8,123,8,8,10,8,12,8,126,9,8,1,9,1,9,1,9,5,9,131,8,9,10,9,12,9,134,
        9,9,1,10,3,10,137,8,10,1,10,1,10,1,10,1,10,1,10,3,10,144,8,10,1,
        10,0,0,11,0,2,4,6,8,10,12,14,16,18,20,0,8,1,0,1,2,1,0,3,4,1,0,5,
        6,1,0,7,8,1,0,9,10,1,0,18,19,1,0,20,21,1,0,22,23,165,0,30,1,0,0,
        0,2,44,1,0,0,0,4,68,1,0,0,0,6,78,1,0,0,0,8,83,1,0,0,0,10,99,1,0,
        0,0,12,107,1,0,0,0,14,117,1,0,0,0,16,119,1,0,0,0,18,127,1,0,0,0,
        20,136,1,0,0,0,22,24,3,2,1,0,23,22,1,0,0,0,23,24,1,0,0,0,24,26,1,
        0,0,0,25,27,5,30,0,0,26,25,1,0,0,0,27,28,1,0,0,0,28,26,1,0,0,0,28,
        29,1,0,0,0,29,31,1,0,0,0,30,23,1,0,0,0,31,32,1,0,0,0,32,30,1,0,0,
        0,32,33,1,0,0,0,33,35,1,0,0,0,34,36,3,2,1,0,35,34,1,0,0,0,35,36,
        1,0,0,0,36,37,1,0,0,0,37,38,5,0,0,1,38,1,1,0,0,0,39,41,3,4,2,0,40,
        42,5,29,0,0,41,40,1,0,0,0,41,42,1,0,0,0,42,45,1,0,0,0,43,45,5,29,
        0,0,44,39,1,0,0,0,44,43,1,0,0,0,45,3,1,0,0,0,46,69,3,6,3,0,47,69,
        7,0,0,0,48,69,7,1,0,0,49,69,7,2,0,0,50,69,7,3,0,0,51,69,7,4,0,0,
        52,69,5,11,0,0,53,54,5,12,0,0,54,55,3,16,8,0,55,56,3,16,8,0,56,69,
        1,0,0,0,57,58,5,13,0,0,58,69,3,16,8,0,59,60,5,14,0,0,60,61,5,15,
        0,0,61,62,3,10,5,0,62,63,5,16,0,0,63,64,3,8,4,0,64,69,1,0,0,0,65,
        66,5,17,0,0,66,67,5,28,0,0,67,69,3,8,4,0,68,46,1,0,0,0,68,47,1,0,
        0,0,68,48,1,0,0,0,68,49,1,0,0,0,68,50,1,0,0,0,68,51,1,0,0,0,68,52,
        1,0,0,0,68,53,1,0,0,0,68,57,1,0,0,0,68,59,1,0,0,0,68,65,1,0,0,0,
        69,5,1,0,0,0,70,76,7,5,0,0,71,76,7,6,0,0,72,76,7,7,0,0,73,76,5,24,
        0,0,74,76,5,25,0,0,75,70,1,0,0,0,75,71,1,0,0,0,75,72,1,0,0,0,75,
        73,1,0,0,0,75,74,1,0,0,0,76,79,1,0,0,0,77,79,3,16,8,0,78,75,1,0,
        0,0,78,77,1,0,0,0,79,7,1,0,0,0,80,82,5,30,0,0,81,80,1,0,0,0,82,85,
        1,0,0,0,83,81,1,0,0,0,83,84,1,0,0,0,84,86,1,0,0,0,85,83,1,0,0,0,
        86,88,5,26,0,0,87,89,3,2,1,0,88,87,1,0,0,0,89,90,1,0,0,0,90,88,1,
        0,0,0,90,91,1,0,0,0,91,92,1,0,0,0,92,96,5,27,0,0,93,95,5,30,0,0,
        94,93,1,0,0,0,95,98,1,0,0,0,96,94,1,0,0,0,96,97,1,0,0,0,97,9,1,0,
        0,0,98,96,1,0,0,0,99,104,3,12,6,0,100,101,5,32,0,0,101,103,3,12,
        6,0,102,100,1,0,0,0,103,106,1,0,0,0,104,102,1,0,0,0,104,105,1,0,
        0,0,105,11,1,0,0,0,106,104,1,0,0,0,107,110,3,14,7,0,108,109,5,31,
        0,0,109,111,3,14,7,0,110,108,1,0,0,0,110,111,1,0,0,0,111,13,1,0,
        0,0,112,118,3,16,8,0,113,114,5,15,0,0,114,115,3,10,5,0,115,116,5,
        16,0,0,116,118,1,0,0,0,117,112,1,0,0,0,117,113,1,0,0,0,118,15,1,
        0,0,0,119,124,3,18,9,0,120,121,5,34,0,0,121,123,3,18,9,0,122,120,
        1,0,0,0,123,126,1,0,0,0,124,122,1,0,0,0,124,125,1,0,0,0,125,17,1,
        0,0,0,126,124,1,0,0,0,127,132,3,20,10,0,128,129,5,35,0,0,129,131,
        3,20,10,0,130,128,1,0,0,0,131,134,1,0,0,0,132,130,1,0,0,0,132,133,
        1,0,0,0,133,19,1,0,0,0,134,132,1,0,0,0,135,137,5,33,0,0,136,135,
        1,0,0,0,136,137,1,0,0,0,137,143,1,0,0,0,138,144,5,28,0,0,139,140,
        5,15,0,0,140,141,3,16,8,0,141,142,5,16,0,0,142,144,1,0,0,0,143,138,
        1,0,0,0,143,139,1,0,0,0,144,21,1,0,0,0,19,23,28,32,35,41,44,68,75,
        78,83,90,96,104,110,117,124,132,136,143
    ]

class logo_grammarParser ( Parser ):

    grammarFileName = "logo_grammar.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'cs'", "'clearscreen'", "'pu'", "'penup'", 
                     "'pd'", "'pendown'", "'ht'", "'hideturtle'", "'st'", 
                     "'showturtle'", "'home'", "'setxy'", "'setpensize'", 
                     "'if'", "'('", "')'", "'repeat'", "'fd'", "'forward'", 
                     "'bk'", "'backward'", "'rt'", "'rightturn'", "'lt'", 
                     "'leftturn'", "'{'", "'}'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "LICZBA", "KOMENTARZ", "KONIEC_WIERSZA", "OPERATOR_POROWNANIA", 
                      "OPERATOR_LOGICZNY", "OPERATOR_ZNAKU", "OPERATOR_ARYTMETYCZNY", 
                      "OPERATOR_MNOZACY", "WS" ]

    RULE_program = 0
    RULE_instrukcja = 1
    RULE_polecenie = 2
    RULE_ruch = 3
    RULE_blok = 4
    RULE_wyrazenie_logiczne = 5
    RULE_wyrazenie_porownania = 6
    RULE_wartosc_logiczna = 7
    RULE_wyrazenie = 8
    RULE_wyrazenie_mnozace = 9
    RULE_wartosc_liczbowa = 10

    ruleNames =  [ "program", "instrukcja", "polecenie", "ruch", "blok", 
                   "wyrazenie_logiczne", "wyrazenie_porownania", "wartosc_logiczna", 
                   "wyrazenie", "wyrazenie_mnozace", "wartosc_liczbowa" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    T__16=17
    T__17=18
    T__18=19
    T__19=20
    T__20=21
    T__21=22
    T__22=23
    T__23=24
    T__24=25
    T__25=26
    T__26=27
    LICZBA=28
    KOMENTARZ=29
    KONIEC_WIERSZA=30
    OPERATOR_POROWNANIA=31
    OPERATOR_LOGICZNY=32
    OPERATOR_ZNAKU=33
    OPERATOR_ARYTMETYCZNY=34
    OPERATOR_MNOZACY=35
    WS=36

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.12.0")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(logo_grammarParser.EOF, 0)

        def instrukcja(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(logo_grammarParser.InstrukcjaContext)
            else:
                return self.getTypedRuleContext(logo_grammarParser.InstrukcjaContext,i)


        def KONIEC_WIERSZA(self, i:int=None):
            if i is None:
                return self.getTokens(logo_grammarParser.KONIEC_WIERSZA)
            else:
                return self.getToken(logo_grammarParser.KONIEC_WIERSZA, i)

        def getRuleIndex(self):
            return logo_grammarParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)




    def program(self):

        localctx = logo_grammarParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 30 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 23
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if (((_la) & ~0x3f) == 0 and ((1 << _la) & 9462284286) != 0):
                        self.state = 22
                        self.instrukcja()


                    self.state = 26 
                    self._errHandler.sync(self)
                    _alt = 1
                    while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                        if _alt == 1:
                            self.state = 25
                            self.match(logo_grammarParser.KONIEC_WIERSZA)

                        else:
                            raise NoViableAltException(self)
                        self.state = 28 
                        self._errHandler.sync(self)
                        _alt = self._interp.adaptivePredict(self._input,1,self._ctx)


                else:
                    raise NoViableAltException(self)
                self.state = 32 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

            self.state = 35
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 9462284286) != 0):
                self.state = 34
                self.instrukcja()


            self.state = 37
            self.match(logo_grammarParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InstrukcjaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def polecenie(self):
            return self.getTypedRuleContext(logo_grammarParser.PolecenieContext,0)


        def KOMENTARZ(self):
            return self.getToken(logo_grammarParser.KOMENTARZ, 0)

        def getRuleIndex(self):
            return logo_grammarParser.RULE_instrukcja

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInstrukcja" ):
                listener.enterInstrukcja(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInstrukcja" ):
                listener.exitInstrukcja(self)




    def instrukcja(self):

        localctx = logo_grammarParser.InstrukcjaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_instrukcja)
        try:
            self.state = 44
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 17, 18, 19, 20, 21, 22, 23, 24, 25, 28, 33]:
                self.enterOuterAlt(localctx, 1)
                self.state = 39
                self.polecenie()
                self.state = 41
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
                if la_ == 1:
                    self.state = 40
                    self.match(logo_grammarParser.KOMENTARZ)


                pass
            elif token in [29]:
                self.enterOuterAlt(localctx, 2)
                self.state = 43
                self.match(logo_grammarParser.KOMENTARZ)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PolecenieContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ruch(self):
            return self.getTypedRuleContext(logo_grammarParser.RuchContext,0)


        def wyrazenie(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(logo_grammarParser.WyrazenieContext)
            else:
                return self.getTypedRuleContext(logo_grammarParser.WyrazenieContext,i)


        def wyrazenie_logiczne(self):
            return self.getTypedRuleContext(logo_grammarParser.Wyrazenie_logiczneContext,0)


        def blok(self):
            return self.getTypedRuleContext(logo_grammarParser.BlokContext,0)


        def LICZBA(self):
            return self.getToken(logo_grammarParser.LICZBA, 0)

        def getRuleIndex(self):
            return logo_grammarParser.RULE_polecenie

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPolecenie" ):
                listener.enterPolecenie(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPolecenie" ):
                listener.exitPolecenie(self)




    def polecenie(self):

        localctx = logo_grammarParser.PolecenieContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_polecenie)
        self._la = 0 # Token type
        try:
            self.state = 68
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [15, 18, 19, 20, 21, 22, 23, 24, 25, 28, 33]:
                self.enterOuterAlt(localctx, 1)
                self.state = 46
                self.ruch()
                pass
            elif token in [1, 2]:
                self.enterOuterAlt(localctx, 2)
                self.state = 47
                _la = self._input.LA(1)
                if not(_la==1 or _la==2):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                pass
            elif token in [3, 4]:
                self.enterOuterAlt(localctx, 3)
                self.state = 48
                _la = self._input.LA(1)
                if not(_la==3 or _la==4):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                pass
            elif token in [5, 6]:
                self.enterOuterAlt(localctx, 4)
                self.state = 49
                _la = self._input.LA(1)
                if not(_la==5 or _la==6):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                pass
            elif token in [7, 8]:
                self.enterOuterAlt(localctx, 5)
                self.state = 50
                _la = self._input.LA(1)
                if not(_la==7 or _la==8):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                pass
            elif token in [9, 10]:
                self.enterOuterAlt(localctx, 6)
                self.state = 51
                _la = self._input.LA(1)
                if not(_la==9 or _la==10):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                pass
            elif token in [11]:
                self.enterOuterAlt(localctx, 7)
                self.state = 52
                self.match(logo_grammarParser.T__10)
                pass
            elif token in [12]:
                self.enterOuterAlt(localctx, 8)
                self.state = 53
                self.match(logo_grammarParser.T__11)
                self.state = 54
                self.wyrazenie()
                self.state = 55
                self.wyrazenie()
                pass
            elif token in [13]:
                self.enterOuterAlt(localctx, 9)
                self.state = 57
                self.match(logo_grammarParser.T__12)
                self.state = 58
                self.wyrazenie()
                pass
            elif token in [14]:
                self.enterOuterAlt(localctx, 10)
                self.state = 59
                self.match(logo_grammarParser.T__13)
                self.state = 60
                self.match(logo_grammarParser.T__14)
                self.state = 61
                self.wyrazenie_logiczne()
                self.state = 62
                self.match(logo_grammarParser.T__15)
                self.state = 63
                self.blok()
                pass
            elif token in [17]:
                self.enterOuterAlt(localctx, 11)
                self.state = 65
                self.match(logo_grammarParser.T__16)
                self.state = 66
                self.match(logo_grammarParser.LICZBA)
                self.state = 67
                self.blok()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RuchContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def wyrazenie(self):
            return self.getTypedRuleContext(logo_grammarParser.WyrazenieContext,0)


        def getRuleIndex(self):
            return logo_grammarParser.RULE_ruch

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRuch" ):
                listener.enterRuch(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRuch" ):
                listener.exitRuch(self)




    def ruch(self):

        localctx = logo_grammarParser.RuchContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_ruch)
        self._la = 0 # Token type
        try:
            self.state = 78
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [18, 19, 20, 21, 22, 23, 24, 25]:
                self.enterOuterAlt(localctx, 1)
                self.state = 75
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [18, 19]:
                    self.state = 70
                    _la = self._input.LA(1)
                    if not(_la==18 or _la==19):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    pass
                elif token in [20, 21]:
                    self.state = 71
                    _la = self._input.LA(1)
                    if not(_la==20 or _la==21):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    pass
                elif token in [22, 23]:
                    self.state = 72
                    _la = self._input.LA(1)
                    if not(_la==22 or _la==23):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    pass
                elif token in [24]:
                    self.state = 73
                    self.match(logo_grammarParser.T__23)
                    pass
                elif token in [25]:
                    self.state = 74
                    self.match(logo_grammarParser.T__24)
                    pass
                else:
                    raise NoViableAltException(self)

                pass
            elif token in [15, 28, 33]:
                self.enterOuterAlt(localctx, 2)
                self.state = 77
                self.wyrazenie()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlokContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KONIEC_WIERSZA(self, i:int=None):
            if i is None:
                return self.getTokens(logo_grammarParser.KONIEC_WIERSZA)
            else:
                return self.getToken(logo_grammarParser.KONIEC_WIERSZA, i)

        def instrukcja(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(logo_grammarParser.InstrukcjaContext)
            else:
                return self.getTypedRuleContext(logo_grammarParser.InstrukcjaContext,i)


        def getRuleIndex(self):
            return logo_grammarParser.RULE_blok

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlok" ):
                listener.enterBlok(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlok" ):
                listener.exitBlok(self)




    def blok(self):

        localctx = logo_grammarParser.BlokContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_blok)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 83
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==30:
                self.state = 80
                self.match(logo_grammarParser.KONIEC_WIERSZA)
                self.state = 85
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 86
            self.match(logo_grammarParser.T__25)
            self.state = 88 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 87
                self.instrukcja()
                self.state = 90 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 9462284286) != 0)):
                    break

            self.state = 92
            self.match(logo_grammarParser.T__26)
            self.state = 96
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,11,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 93
                    self.match(logo_grammarParser.KONIEC_WIERSZA) 
                self.state = 98
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,11,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Wyrazenie_logiczneContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def wyrazenie_porownania(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(logo_grammarParser.Wyrazenie_porownaniaContext)
            else:
                return self.getTypedRuleContext(logo_grammarParser.Wyrazenie_porownaniaContext,i)


        def OPERATOR_LOGICZNY(self, i:int=None):
            if i is None:
                return self.getTokens(logo_grammarParser.OPERATOR_LOGICZNY)
            else:
                return self.getToken(logo_grammarParser.OPERATOR_LOGICZNY, i)

        def getRuleIndex(self):
            return logo_grammarParser.RULE_wyrazenie_logiczne

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWyrazenie_logiczne" ):
                listener.enterWyrazenie_logiczne(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWyrazenie_logiczne" ):
                listener.exitWyrazenie_logiczne(self)




    def wyrazenie_logiczne(self):

        localctx = logo_grammarParser.Wyrazenie_logiczneContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_wyrazenie_logiczne)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 99
            self.wyrazenie_porownania()
            self.state = 104
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==32:
                self.state = 100
                self.match(logo_grammarParser.OPERATOR_LOGICZNY)
                self.state = 101
                self.wyrazenie_porownania()
                self.state = 106
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Wyrazenie_porownaniaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def wartosc_logiczna(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(logo_grammarParser.Wartosc_logicznaContext)
            else:
                return self.getTypedRuleContext(logo_grammarParser.Wartosc_logicznaContext,i)


        def OPERATOR_POROWNANIA(self):
            return self.getToken(logo_grammarParser.OPERATOR_POROWNANIA, 0)

        def getRuleIndex(self):
            return logo_grammarParser.RULE_wyrazenie_porownania

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWyrazenie_porownania" ):
                listener.enterWyrazenie_porownania(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWyrazenie_porownania" ):
                listener.exitWyrazenie_porownania(self)




    def wyrazenie_porownania(self):

        localctx = logo_grammarParser.Wyrazenie_porownaniaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_wyrazenie_porownania)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 107
            self.wartosc_logiczna()
            self.state = 110
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==31:
                self.state = 108
                self.match(logo_grammarParser.OPERATOR_POROWNANIA)
                self.state = 109
                self.wartosc_logiczna()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Wartosc_logicznaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def wyrazenie(self):
            return self.getTypedRuleContext(logo_grammarParser.WyrazenieContext,0)


        def wyrazenie_logiczne(self):
            return self.getTypedRuleContext(logo_grammarParser.Wyrazenie_logiczneContext,0)


        def getRuleIndex(self):
            return logo_grammarParser.RULE_wartosc_logiczna

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWartosc_logiczna" ):
                listener.enterWartosc_logiczna(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWartosc_logiczna" ):
                listener.exitWartosc_logiczna(self)




    def wartosc_logiczna(self):

        localctx = logo_grammarParser.Wartosc_logicznaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_wartosc_logiczna)
        try:
            self.state = 117
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 112
                self.wyrazenie()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 113
                self.match(logo_grammarParser.T__14)
                self.state = 114
                self.wyrazenie_logiczne()
                self.state = 115
                self.match(logo_grammarParser.T__15)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WyrazenieContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def wyrazenie_mnozace(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(logo_grammarParser.Wyrazenie_mnozaceContext)
            else:
                return self.getTypedRuleContext(logo_grammarParser.Wyrazenie_mnozaceContext,i)


        def OPERATOR_ARYTMETYCZNY(self, i:int=None):
            if i is None:
                return self.getTokens(logo_grammarParser.OPERATOR_ARYTMETYCZNY)
            else:
                return self.getToken(logo_grammarParser.OPERATOR_ARYTMETYCZNY, i)

        def getRuleIndex(self):
            return logo_grammarParser.RULE_wyrazenie

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWyrazenie" ):
                listener.enterWyrazenie(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWyrazenie" ):
                listener.exitWyrazenie(self)




    def wyrazenie(self):

        localctx = logo_grammarParser.WyrazenieContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_wyrazenie)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 119
            self.wyrazenie_mnozace()
            self.state = 124
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==34:
                self.state = 120
                self.match(logo_grammarParser.OPERATOR_ARYTMETYCZNY)
                self.state = 121
                self.wyrazenie_mnozace()
                self.state = 126
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Wyrazenie_mnozaceContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def wartosc_liczbowa(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(logo_grammarParser.Wartosc_liczbowaContext)
            else:
                return self.getTypedRuleContext(logo_grammarParser.Wartosc_liczbowaContext,i)


        def OPERATOR_MNOZACY(self, i:int=None):
            if i is None:
                return self.getTokens(logo_grammarParser.OPERATOR_MNOZACY)
            else:
                return self.getToken(logo_grammarParser.OPERATOR_MNOZACY, i)

        def getRuleIndex(self):
            return logo_grammarParser.RULE_wyrazenie_mnozace

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWyrazenie_mnozace" ):
                listener.enterWyrazenie_mnozace(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWyrazenie_mnozace" ):
                listener.exitWyrazenie_mnozace(self)




    def wyrazenie_mnozace(self):

        localctx = logo_grammarParser.Wyrazenie_mnozaceContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_wyrazenie_mnozace)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 127
            self.wartosc_liczbowa()
            self.state = 132
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==35:
                self.state = 128
                self.match(logo_grammarParser.OPERATOR_MNOZACY)
                self.state = 129
                self.wartosc_liczbowa()
                self.state = 134
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Wartosc_liczbowaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LICZBA(self):
            return self.getToken(logo_grammarParser.LICZBA, 0)

        def wyrazenie(self):
            return self.getTypedRuleContext(logo_grammarParser.WyrazenieContext,0)


        def OPERATOR_ZNAKU(self):
            return self.getToken(logo_grammarParser.OPERATOR_ZNAKU, 0)

        def getRuleIndex(self):
            return logo_grammarParser.RULE_wartosc_liczbowa

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWartosc_liczbowa" ):
                listener.enterWartosc_liczbowa(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWartosc_liczbowa" ):
                listener.exitWartosc_liczbowa(self)




    def wartosc_liczbowa(self):

        localctx = logo_grammarParser.Wartosc_liczbowaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_wartosc_liczbowa)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 136
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==33:
                self.state = 135
                self.match(logo_grammarParser.OPERATOR_ZNAKU)


            self.state = 143
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [28]:
                self.state = 138
                self.match(logo_grammarParser.LICZBA)
                pass
            elif token in [15]:
                self.state = 139
                self.match(logo_grammarParser.T__14)
                self.state = 140
                self.wyrazenie()
                self.state = 141
                self.match(logo_grammarParser.T__15)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





