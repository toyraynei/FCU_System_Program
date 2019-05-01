HW3      START   0000
LOAD     LDX	 #0
         LDA     #15
         STA     NUM, X
         LDX	 #3
         LDA     #30
         STA     NUM, X
         LDX	 #6
         LDA     #34
         STA     NUM, X
         LDX	 #9
         LDA     #51
         STA     NUM, X
         LDX	 #12
         LDA     #60
         STA     NUM, X
         LDX	 #15
         LDA     #21
         STA     NUM, X
         LDX	 #18
         LDA     #199
         STA     NUM, X
         LDX	 #21
         LDA     #99
         STA     NUM, X
         LDX	 #24
         LDA     #63
         STA     NUM, X
         LDX	 #27
         LDA     #63
         STA     NUM, X
........ 第一組
         LDX     #0
         LDS     NUM, X
	 STS     TMP3
         LDX     #3
         LDT     NUM, X
	 STT     TMP4
	 JSUB    LCM
	 LDA     TMP1
         LDX     #0
         STA     ANS, X
         LDA     TMP2
         LDX     #3
         STA     ANS, X
........ 第二組
         LDX     #6
         LDS     NUM, X
	 STS     TMP3
         LDX     #9
         LDT     NUM, X
	 STT     TMP4
	 JSUB    LCM
	 LDA     TMP1
         LDX     #6
         STA     ANS, X
         LDA     TMP2
         LDX     #9
         STA     ANS, X
........ 第三組
         LDX     #12
         LDS     NUM, X
	 STS     TMP3
         LDX     #15
         LDT     NUM, X
	 STT     TMP4
	 JSUB    LCM
	 LDA     TMP1
         LDX     #12
         STA     ANS, X
         LDA     TMP2
         LDX     #15
         STA     ANS, X
........ 第四組
         LDX     #18
         LDS     NUM, X
	 STS     TMP3
         LDX     #21
         LDT     NUM, X
	 STT     TMP4
	 JSUB    LCM
	 LDA     TMP1
         LDX     #18
         STA     ANS, X
         LDA     TMP2
         LDX     #21
         STA     ANS, X
........ 第五組
         LDX     #24
         LDS     NUM, X
	 STS     TMP3
         LDX     #27
         LDT     NUM, X
	 STT     TMP4
	 JSUB    LCM
	 LDA     TMP1
         LDX     #24
         STA     ANS, X
         LDA     TMP2
         LDX     #27
         STA     ANS, X
	 J       ENDDD
GCD      COMPR	 S, T
         JEQ     RET
         JLT     CHANGE
         STT     TMP2
         LDA     TMP2
         COMP	 #0
         JEQ     GCDIS1
         STS     TMP1
         DIVR    T, S
         STS     Q
         LDA     Q
         LDS     TMP1
CAL      COMP    #0
         JEQ     AFTCAL
         SUB	 #1
         SUBR    T, S
         J       CAL
AFTCAL   STS     TMP1
         LDS     TMP2
         LDT     TMP1
         LDA     TMP1
         COMP    #0
         JGT     GCD
         JEQ     RET
GCDIS1   LDA     #1
         RSUB
RET      STS     TMP1
         LDA     TMP1
         RSUB
CHANGE   STS     TMP1
         STT     TMP2
         LDS     TMP2
         LDT     TMP1
         J	 GCD
LCM      STL     TMPL
         JSUB    GCD
	 STA     TMP1
	 LDS     TMP3
	 LDT     TMP4
	 MULR    S, T
	 DIVR    A, T
	 STT     TMP2
	 LDL     TMPL
	 RSUB
TMP1     RESW    1
TMP2     RESW    1
TMP3     RESW    1
TMP4     RESW    1
TMPL     RESW    1
Q        RESW    1
NUM      RESW    10
ANS      RESW    10
ENDDD    END     LOAD