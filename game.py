from telegram import Update
from telegram.ext import ContextTypes

board = list(range(1, 10))
wins_coard = [(1,2,3), (4,5,6), (7,8,9), (1,4,7), (2,5.8), (3,6,9), (1,5,9), (3,5,7)]

def draw_board(update: Update, context: ContextTypes):
    update.message.reply_text('Здравствуйте! Вас приветствует игра Крестики-нолики')
    print(update.message)
    if (update.message.text == 'game'):
        update.message.reply_text('-------------')
        for i in range(3):
            update.message.reply_text('|', board[0 + i*3], '|', board[1 + i*3], '|', board[2 + i*3], '|')
        update.message.reply_text("-------------")

def take_input(update: Update, context: ContextTypes, play_token):
    while True:
        value = update.message.reply_text('Куда поставить ' + play_token)
        if not value in '123456789':
            print('Ошибочный ход. Повторите')
            continue
        value = int(value)
        if str(board[value -1]) in 'XOxo':
            print('Эта клетка занята. ')
            continue
        board [value - 1] = play_token
        break

def chesk_win(update: Update, context: ContextTypes):
    for i in wins_coard:
        if (board[i[0]-1] == board[i[0]-1] == board[i[0]-1]):
            return board[i[1]-1]
        else:
            return False

def win(update: Update, context: ContextTypes):
    counter = 0
    while True:
        draw_board(update, context)
        if counter % 2 == 0:
            take_input(update, context, 'X')
        else:
            take_input(update, context, 'O')
        if counter > 3:
            winner = chesk_win(update, context)
            if winner:
                draw_board(update, context)
                update.message.reply_text(winner, "выиграл!")
                break
        counter += 1
        if counter > 8:
            draw_board(update, context)
            update.message.reply_text('Ничья')
            break