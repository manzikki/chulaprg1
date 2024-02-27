from flask import Flask, request
import random

class thaigen:
  lastpos = -1 #indicates the consonant position in the thc list
  thc = ["กMgor gai", "ขHkho khai", "ฃHkho khuat (not used)",
    "คLkho khwai","ฅLkho khon (not used)", "ฆLkho rakhang", "งMngo ngu",
    "จHjoor jaan","ฉHcho ching","ชMcho chang", "ซLso so", "ฌLso cheer",
    "ญLyo ying", "ฎMdo chada","ฏMto patak", "ฐHtho than","ฑLtho montho",
    "ฒLtho phuthao","ณLno nen","ดMdo dek","ตMto tao","ถHtho thung",
    "ทLtho thahan","ธLtho thong","นLno nu","บMbo baimai","ปMpo pla",
    "ผHpho phueng","ฝHfo fa","พLpho phan","ฟLfo fan","ภLpho sam-phao",
    "มLmo ma","ยLyo yak","รLro rua","ลLlo ling","วLwo waen","ศHso sala",
    "ษHso rusi","สHso suea","หHho hip","ฬLlo chula","อMo ang",
    "ฮLho nokhuk"]
  as_it_was = thc

  #get just one consonant
  def get(self):
      #if the list is empty..
      if not self.thc:
          return " "
      #get a random position
      rpos = random.randint(0, len(self.thc)-1)
      self.lastpos = rpos
      #get a line from thc from that position
      line = self.thc[rpos]
      #get the consonant
      return line[0]

  def get_answer(self):
      #if the list is empty..
      if not self.thc:
          return [" "," ",""]
      #get the line of lastpos
      line = self.thc[self.lastpos]
      return [ line[0], line[1], line[2:] ]

  def howmany(self):
      #how many consonant questions left?
      return len(self.thc)

  def reset(self):
      #get all the original questions back
      self.thc = self.as_it_was

  def dont_ask_this(self):
      #removes the lastpos consonant from thc so that it won't be asked again
      line = self.thc[self.lastpos]
      self.thc.remove(line)

#code for using the class here
