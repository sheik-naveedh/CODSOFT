import React from 'react';

const Board = ({ board, onClick }) => {
  return (
    <div className="board">
      {board.map((value, index) => (
        <div key={index} className="cell" onClick={() => onClick(index)}>
          {value}
        </div>
      ))}
    </div>
  );
};

export default Board;
