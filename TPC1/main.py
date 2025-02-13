from enum import Enum

#region Token

class tokenType_t ( Enum ):
    NUMBER = 1
    ON     = 2
    OFF    = 3
    EQUAL  = 4
    EOL    = 5

class Token:
    def __init__( self , token_type , data ):
        self.type = token_type
        self.data = data

    def __str__( self ):
        return f"Token( { self.type } , \" { self.data } \")"

#endregion

#region Lexer

class Lexer:
    def __init__( self , line ):
        self.line = line
        self.position = 0
    
    def current_char( self ) -> str:
        return self.line[self.position] if self.position < len( self.line ) else '\0'

    def next_token( self ) -> Token:
        
        while self.position < len( self.line ):
            char = self.current_char()

            ## get number
            if char.isdigit():
                number = 0
                #isNegative = False
                isDecimal = False
                exp = 1

                while ( self.position < len( self.line ) and char.isdigit() ) or ( char == '.' and self.line[self.position + 1].isdigit() ):
                    if char == '.':
                        isDecimal = True
                        self.position += 1
                        char = self.current_char()
                        
                    if isDecimal:
                        number = number + 10**( -exp ) * int( char )
                        exp += 1
                    else:
                        number = number * 10 + int( char )
                    
                    self.position += 1
                    char = self.current_char()
                return Token( tokenType_t.NUMBER , number )
            
            ## on/off
            if char in "oO":
                ## verify if is not part of other words
                if self.position > 0:
                    if self.line[self.position - 1].isalpha():
                        self.position += 1
                        continue 
                    
                start = self.position
                while ( self.position < len( self.line ) and char in "onONfF"):
                    self.position += 1
                    char = self.current_char()
                    
                ## verify if is not part of other words
                if self.position < len( self.line ):
                    if self.line[self.position].isalpha():
                        self.position += 1
                        continue
        
                word = self.line[start : self.position]
                lower_word = word.lower()
                
                if lower_word == "on":
                    return Token( tokenType_t.ON , None )
                elif lower_word == "off":
                    return Token( tokenType_t.OFF , None )
                else:
                    continue

            if char == '=':
                self.position += 1
                return Token( tokenType_t.EQUAL , None )
            
            ## skip char
            self.position += 1
        
        return Token( tokenType_t.EOL , None )

#endregion

#region Parser

class Parser: 
    def __init__( self , filename ):
        self.filename = filename
        self.total = 0
        self.isCounting = True
        
    def start( self ):
        currentToken = None
        with open( self.filename , "r" ) as file:
            while True:
                line = file.readline()
                
                # EOF
                if not line:  
                    break
                
                lexer = Lexer( line )
                while line:
                    currentToken = lexer.next_token()
                    
                    if currentToken.type == tokenType_t.NUMBER and self.isCounting:
                        self.total += currentToken.data
                    elif currentToken.type == tokenType_t.EQUAL:
                        print( self.total )
                    elif currentToken.type == tokenType_t.ON:
                        self.isCounting = True
                    elif currentToken.type == tokenType_t.OFF:
                        self.isCounting = False
                    elif currentToken.type == tokenType_t.EOL:
                        break
                    else:
                        continue
        print( f"TOTAL: { self.total }" )
                
#endregion

if __name__ == '__main__' :
    filename = "TPC1/tv.txt"
    parser = Parser( filename )
    parser.start()