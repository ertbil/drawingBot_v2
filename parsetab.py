
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'COLOR FORWARD KIRMIZI LEFTBRACKET LOOP MAVI NUMBER PEN RIGHTBRACKET ROTATE SIYAH YESIL\n    result : expression\n           | empty\n    \n    expression : expression FORWARD NUMBER\n         | expression ROTATE NUMBER\n         | expression COLOR KIRMIZI\n         | expression COLOR YESIL\n         | expression COLOR MAVI\n         | expression COLOR SIYAH\n         | expression PEN NUMBER\n    \n     expression : loop\n                | loop_with_loop\n                | empty\n\n    \n    empty :\n    \n    loop : LOOP NUMBER LEFTBRACKET expression RIGHTBRACKET\n         | LOOP NUMBER LEFTBRACKET loop RIGHTBRACKET\n         | empty\n    \n    loop_with_loop : LOOP NUMBER LEFTBRACKET loop expression RIGHTBRACKET\n    '
    
_lr_action_items = {'$end':([0,1,2,3,4,5,12,13,14,15,16,17,18,23,24,26,],[-13,0,-1,-2,-10,-11,-3,-4,-5,-6,-7,-8,-9,-14,-15,-17,]),'FORWARD':([0,2,3,4,5,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,],[-13,7,-12,-10,-11,-3,-4,-5,-6,-7,-8,-9,-13,7,-10,-12,-14,-15,7,-17,]),'ROTATE':([0,2,3,4,5,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,],[-13,8,-12,-10,-11,-3,-4,-5,-6,-7,-8,-9,-13,8,-10,-12,-14,-15,8,-17,]),'COLOR':([0,2,3,4,5,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,],[-13,9,-12,-10,-11,-3,-4,-5,-6,-7,-8,-9,-13,9,-10,-12,-14,-15,9,-17,]),'PEN':([0,2,3,4,5,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,],[-13,10,-12,-10,-11,-3,-4,-5,-6,-7,-8,-9,-13,10,-10,-12,-14,-15,10,-17,]),'LOOP':([0,19,21,22,23,24,],[6,6,6,-16,-14,-15,]),'RIGHTBRACKET':([4,5,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,],[-10,-11,-3,-4,-5,-6,-7,-8,-9,-13,23,24,-12,-14,-15,26,-17,]),'NUMBER':([6,7,8,10,],[11,12,13,18,]),'KIRMIZI':([9,],[14,]),'YESIL':([9,],[15,]),'MAVI':([9,],[16,]),'SIYAH':([9,],[17,]),'LEFTBRACKET':([11,],[19,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'result':([0,],[1,]),'expression':([0,19,21,],[2,20,25,]),'empty':([0,19,21,],[3,22,22,]),'loop':([0,19,21,],[4,21,4,]),'loop_with_loop':([0,19,21,],[5,5,5,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> result","S'",1,None,None,None),
  ('result -> expression','result',1,'p_result','parserFile.py',59),
  ('result -> empty','result',1,'p_result','parserFile.py',60),
  ('expression -> expression FORWARD NUMBER','expression',3,'p_expression','parserFile.py',67),
  ('expression -> expression ROTATE NUMBER','expression',3,'p_expression','parserFile.py',68),
  ('expression -> expression COLOR KIRMIZI','expression',3,'p_expression','parserFile.py',69),
  ('expression -> expression COLOR YESIL','expression',3,'p_expression','parserFile.py',70),
  ('expression -> expression COLOR MAVI','expression',3,'p_expression','parserFile.py',71),
  ('expression -> expression COLOR SIYAH','expression',3,'p_expression','parserFile.py',72),
  ('expression -> expression PEN NUMBER','expression',3,'p_expression','parserFile.py',73),
  ('expression -> loop','expression',1,'p_expression1','parserFile.py',79),
  ('expression -> loop_with_loop','expression',1,'p_expression1','parserFile.py',80),
  ('expression -> empty','expression',1,'p_expression1','parserFile.py',81),
  ('empty -> <empty>','empty',0,'p_empty','parserFile.py',89),
  ('loop -> LOOP NUMBER LEFTBRACKET expression RIGHTBRACKET','loop',5,'p_loop','parserFile.py',95),
  ('loop -> LOOP NUMBER LEFTBRACKET loop RIGHTBRACKET','loop',5,'p_loop','parserFile.py',96),
  ('loop -> empty','loop',1,'p_loop','parserFile.py',97),
  ('loop_with_loop -> LOOP NUMBER LEFTBRACKET loop expression RIGHTBRACKET','loop_with_loop',6,'p_loop_with_loop','parserFile.py',104),
]
