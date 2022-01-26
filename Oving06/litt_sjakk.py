# PROGRAM RULES:
# None in list = no piece in pos
# Whites are capital
# Blacks are lower case
# king = k, queen = q, rook = r, bishop = b, knight = n, pawn = p
# . = empty space
# board is 5x5
boardWidth = 5

# oppgave a
def make_board(board_string):
    board = [[]]
    rowIndx = 0
    for counter,piece in enumerate(board_string):
        if piece == '.':
            piece = None
        if counter % boardWidth == 0 and counter != 0:
            board.append([])
            rowIndx += 1
            board[rowIndx].append(piece)
        else:
            board[rowIndx].append(piece)
    return board

# oppgave b
def get_piece(board,x,y):
    colIndx = x-1
    rowIndx = boardWidth-y
    return board[rowIndx][colIndx]

# oppgave c, only pawn movements
# one step forward if not obsturcted
# can capture on forward diagonal
# possible to move to spaces from start position
# disregard promotion and en passant
# ord for p = 112, ord for P is 80
def get_legal_moves(board,x,y):
    legal_moves = []
    if get_piece(board,x,y) not in ['P','p']: # check if piece is a pawn
        return []
    else:
        movement = 1
        if get_piece(board,x,y) == 'p': # black or white pieces
            movement = -1
        if get_piece(board,x,y+movement) == None: # unobstructed move forward
            legal_moves.append((x,y+movement))
        if y == 2 or y == 5 + movement: # on starting row for pawn
            if get_piece(board,x,y+(2*movement)) == None: # two moves forward is unobstructed
                legal_moves.append((x,y+(2*movement)))
        if get_piece(board,x+1,y+movement) != None: # diagonal right
            if movement != 1 and get_piece(board,x+1,y+movement).isupper(): # target is white, attacker is black
                legal_moves.append((x+1,y+movement))
            elif movement == 1 and get_piece(board,x+1,y+movement).isupper() == False: # target is black, attacker is white
                legal_moves.append((x+1,y+movement))
        if get_piece(board,x-1,y+movement) != None: # diagonal left
            if movement != 1 and get_piece(board,x-1,y+movement).isupper(): # target is white, attacker is black
                legal_moves.append((x-1,y+movement))
            if movement == 1 and get_piece(board,x-1,y+movement).isupper() == False: # target is black, attacker is white
                legal_moves.append((x-1,y+movement))
    return legal_moves

#testkode
board_string_1 = 'rkn.r.p.....P..PP.PPB.K..'
board = make_board(board_string_1)
print(board)
#oppg b
print('\nget_piece()')
print(get_piece(board, 2, 1)) # bot left, one in
print(get_piece(board, 5, 2)) # one up, far right
print(get_piece(board, 1, 5)) # top left
#oppg c
print('\nget_legal_moves()')
print(get_legal_moves(board, 4, 2))
print(get_legal_moves(board, 2, 4))
print(get_legal_moves(board, 3, 3))

