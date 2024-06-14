import React, { useState, useEffect } from 'react';
import Board from './Board';

const HUMAN = 'O';
const AI = 'X';
const EMPTY = ' ';

const Game = () => {
  const [board, setBoard] = useState(Array(9).fill(EMPTY));
  const [isHumanTurn, setIsHumanTurn] = useState(true);
  const [winner, setWinner] = useState(null);

  useEffect(() => {
    if (!isHumanTurn && !winner) {
      const aiMove = bestMove(board);
      makeMove(aiMove, AI);
      setIsHumanTurn(true);
    }
  }, [isHumanTurn, winner]);

  const makeMove = (index, player) => {
    const newBoard = [...board];
    if (newBoard[index] === EMPTY) {
      newBoard[index] = player;
      setBoard(newBoard);
      if (checkWinner(newBoard, player)) {
        setWinner(player);
      } else if (isBoardFull(newBoard)) {
        setWinner('draw');
      }
    }
  };

  const handleClick = (index) => {
    if (isHumanTurn && board[index] === EMPTY && !winner) {
      makeMove(index, HUMAN);
      setIsHumanTurn(false);
    }
  };

  const checkWinner = (board, player) => {
    const winConditions = [
      [0, 1, 2], [3, 4, 5], [6, 7, 8], // Horizontal
      [0, 3, 6], [1, 4, 7], [2, 5, 8], // Vertical
      [0, 4, 8], [2, 4, 6] // Diagonal
    ];
    return winConditions.some(condition => condition.every(index => board[index] === player));
  };

  const isBoardFull = (board) => {
    return !board.includes(EMPTY);
  };

  const minimax = (board, depth, isMaximizing) => {
    if (checkWinner(board, AI)) return 1;
    if (checkWinner(board, HUMAN)) return -1;
    if (isBoardFull(board)) return 0;

    if (isMaximizing) {
      let bestScore = -Infinity;
      getAvailableMoves(board).forEach(move => {
        board[move] = AI;
        const score = minimax(board, depth + 1, false);
        board[move] = EMPTY;
        bestScore = Math.max(score, bestScore);
      });
      return bestScore;
    } else {
      let bestScore = Infinity;
      getAvailableMoves(board).forEach(move => {
        board[move] = HUMAN;
        const score = minimax(board, depth + 1, true);
        board[move] = EMPTY;
        bestScore = Math.min(score, bestScore);
      });
      return bestScore;
    }
  };

  const bestMove = (board) => {
    let bestScore = -Infinity;
    let move = -1;
    getAvailableMoves(board).forEach(possibleMove => {
      board[possibleMove] = AI;
      const score = minimax(board, 0, false);
      board[possibleMove] = EMPTY;
      if (score > bestScore) {
        bestScore = score;
        move = possibleMove;
      }
    });
    return move;
  };

  const getAvailableMoves = (board) => {
    return board.map((value, index) => value === EMPTY ? index : null).filter(value => value !== null);
  };

  return (
    <div>
      <h1>Tic-Tac-Toe</h1>
      <Board board={board} onClick={handleClick} />
      {winner && (
        <div>
          {winner === 'draw' ? <p>It's a draw!</p> : <p>{winner} wins!</p>}
        </div>
      )}
    </div>
  );
};

export default Game;
