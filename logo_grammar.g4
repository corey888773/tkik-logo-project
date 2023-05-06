grammar logo_grammar;

program
	: (instrukcja? koniec_wiersza+)+ instrukcja? koniec_pliku
    ;

instrukcja
	: polecenie komentarz?
	| komentarz
	;

polecenie
	: repeat
	| ruch
	| ('cs' | 'clearscreen')
	| ('pu' | 'penup')
	| ('pd' | 'pendown')
	| ('ht' | 'hideturtle')
	| ('st' | 'showturtle')
	| 'home'
	| 'setxy' wyrazenie wyrazenie
	| 'setpensize' wyrazenie
	| 'if' '(' wyrazenie_logiczne ')' blok
	| 'repeat' liczba blok
	;

ruch
	: ( ('fd' | 'forward')
    | ('bk' | 'backward')
    | ('rt' | 'rightturn')
    | 'lt' | 'leftturn')
    | wyrazenie
	;

blok
	: koniec_wiersza* '{' instrukcja+ '}' koniec_wiersza*
	;

liczba
	: [0-9] +
	;

komentarz
	: '#' ~ [\r\n]*
	;

koniec_wiersza
	: '\r'? '\n'
	;

wyrazenie_logiczne
	: wyrazenie operator_porównania wyrazenie
	;

operator_porownania
	: '<'
	| '<='
	| '>'
	| '>='
	| '='
	| '!='
	;

operator_logiczny
	: '||'
	| '&&'
	;

wyrazenie
	:  wyrazenie_mnozace (operator_arytmetyczny wyrazenie_mnozace )*
	;

wyrazenie_mnozace
    : wartosc_liczbowa (operator_mnozacy wartosc_liczbowa)*
    ;

wartosc_liczbowa
    : operator_znaku? (liczba | '(' wyrazenie ')')
    ;

operator_znaku
    : '-'
    | '+'
    ;

operator_arytmetyczny
    : '-'
    | '+'
    ;

operator_mnozacy
    : '/'
    | '*'
    | '%'
    ;

WS
    : [ \t\r\n]+ -> skip
    ;
