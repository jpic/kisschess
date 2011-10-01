if (!window.Kisschess) {
    var Kisschess = {};
}

if (!Kisschess.Board) {
    Kisschess.Board = {}
}

Kisschess.Board.template = $('.board.template').html();
Kisschess.Board.rows = [1,2,3,4,5,6,7,8];
Kisschess.Board.columns = ['a','b','c','d','e','f','g','h'];
Kisschess.Board.start_position = 'rnbqk--r ppp--ppp -----n-- ---p--N- --P-p--- B-P---P- P--PPP-P R--QKB-R B -1 1 1 1 1 1';

Kisschess.Board.create = function(el, position, turn) {
    el.html(Kisschess.Board.template);

    position = position.split(' ')
    for(var row_key in Kisschess.Board.rows) {
        var row_num = Kisschess.Board.rows[row_key];
        for(var column_key in position[row_key]) {
            var column_letter = Kisschess.Board.columns[column_key]
            var square_key = column_letter + row_num;
            var square = el.find('.' + square_key);
            var piece_key = position[row_key][column_key];

            if (piece_key.toUpperCase() == piece_key) {
                draggable = turn == 'white';
            } else {
                draggable = turn == 'black';
            }

            if (piece_key == '-') {
                square.html('');
            } else {
                square.html('<img draggable="' + draggable + '" src="/static/pieces/' + piece_key + '" width="'+ square.width() +'" />');
            }
        }
    }
}

Kisschess.Board.create($('#main_board'), Kisschess.Board.start_position, 'white');
