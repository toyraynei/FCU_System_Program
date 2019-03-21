QQ       START   1000              
FIRST    LDA     NUM1                
         AND     #1
	 COMP    #0
	 LDA     NUM1
	 LDT     NUM2
	 LDS     SUM
	 JEQ     EVEN
ODD	 COMPR   A, T
	 JEQ     END1
	 JGT     END1
	 ADDR    A, S
	 ADD     #3
	 J       ODD
EVEN     COMPR   A, T
	 JEQ     END1
	 JGT     END1
	 ADDR    A, S
	 ADD     #2
	 J       EVEN	 
NUM1     WORD    15
NUM2     WORD    36
SUM      RESW    1
END1     STS     SUM
	 END     FIRST