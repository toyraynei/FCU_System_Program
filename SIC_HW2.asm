QQ       START   2000              
FIRST    LDA     NUM1                
         AND     ONE
	 COMP    ZERO
	 LDA     NUM1
	 JEQ     EVEN
ODD	 COMP    NUM2
	 JEQ     END1
	 JGT     END1
	 ADD     SUM
	 STA     SUM
	 LDA     NUM1
	 ADD     THREE
	 STA     NUM1
	 J       ODD
EVEN     COMP    NUM2
	 JEQ     END1
	 JGT     END1
	 ADD     SUM
	 STA     SUM
	 LDA     NUM1
	 ADD     TWO
	 STA     NUM1
	 J       EVEN
NUM1     WORD    20
NUM2     WORD    36
ZERO     WORD    0
ONE      WORD    1
TWO      WORD    2
THREE    WORD    3
SUM      RESW    1
END1     END     FIRST