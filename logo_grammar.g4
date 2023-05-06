grammar logo_grammar;

program
	: (instrukcja? KONIEC_WIERSZA+)+ instrukcja? EOF
    ;

instrukcja
	: polecenie KOMENTARZ?
	| KOMENTARZ
	;

polecenie
	: ruch
	| ('cs' | 'clearscreen')
	| ('pu' | 'penup')
	| ('pd' | 'pendown')
	| ('ht' | 'hideturtle')
	| ('st' | 'showturtle')
	| 'home'
	| 'setxy' wyrazenie wyrazenie
	| 'setpensize' wyrazenie
	| 'if' '(' wyrazenie_logiczne ')' blok
	| 'repeat' LICZBA blok
	;

ruch
	: ( ('fd' | 'forward')
    | ('bk' | 'backward')
    | ('rt' | 'rightturn')
    | 'lt' | 'leftturn')
    | wyrazenie
	;

blok
	: KONIEC_WIERSZA* '{' instrukcja+ '}' KONIEC_WIERSZA*
	;

LICZBA
	: [0-9]+
	;

KOMENTARZ
	: '#' ~[\r\n]*
	;

KONIEC_WIERSZA
	: '\r'? '\n'
	;

wyrazenie_logiczne
	: wyrazenie_porownania (OPERATOR_LOGICZNY wyrazenie_porownania)*
	;

wyrazenie_porownania
	: wartosc_logiczna (OPERATOR_POROWNANIA wartosc_logiczna)?
	;

wartosc_logiczna
	: wyrazenie
	| '(' wyrazenie_logiczne ')'
	;
OPERATOR_POROWNANIA
	: '<'
	| '<='
	| '>'
	| '>='
	| '='
	| '!='
	;

OPERATOR_LOGICZNY
	: '||'
	| '&&'
	;

wyrazenie
	:  wyrazenie_mnozace (OPERATOR_ARYTMETYCZNY wyrazenie_mnozace )*
	;

wyrazenie_mnozace
    : wartosc_liczbowa (OPERATOR_MNOZACY wartosc_liczbowa)*
    ;

wartosc_liczbowa
    : OPERATOR_ZNAKU? (LICZBA | '(' wyrazenie ')')
    ;

OPERATOR_ZNAKU
    : '-'
    | '+'
    ;

OPERATOR_ARYTMETYCZNY
    : '-'
    | '+'
    ;

OPERATOR_MNOZACY
    : '/'
    | '*'
    | '%'
    ;

WS
    : [\t\r\n]+ -> skip
    ;
