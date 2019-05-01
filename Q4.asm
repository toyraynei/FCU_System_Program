BB       START   0
FIRST    WORD    16
NEXT     RESB    9
         ORG     NEXT
NAME     RESW    1
VALUE    RESW    2
         ORG
GO       LDA     #0
         END     GO 