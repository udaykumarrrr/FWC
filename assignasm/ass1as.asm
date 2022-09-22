.include "/sdcard/Download/assembly1/m328Pdef.inc"
  
   ldi r16, 0b00100000 ;identifying output pins 2,3,4,5
   out DDRB,r16            ;declaring pins as output
  
  
  
   ldi r16,0b00000001      ;initializing A
   ldi r17,0b00000000      ;initializing C
                
  ;logical XOR
   eor r16,r17                     ;A XOR C
 
   ;following code is for displaying output
   ;shifting LSB in r16 to 13th position
   ldi r20, 0b00000101     ;counter = 5
 
   rcall loopw             ;calling the loopw routine
 
   out PORTB,r16           ;writing output to pin 13
    Start:
    rjmp Start
 
  ;loop for bit shifting
   loopw:  lsl r16                 ;left shift
           dec r20                 ;counter --
           brne    loopw   ;if counter != 0
           ret

