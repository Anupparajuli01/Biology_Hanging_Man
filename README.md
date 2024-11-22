# Biology Hanging Man

Hangman is a classic word-guessing game. The game is typically played by two or more players, where one player thinks of a secret word, and the other player(s) tries to guess the word by suggesting letters one at a time. In this project, the computer (Bot) will ask a user to guess the word. This version of the game has been designed to make learning biology vocabulary enjoyable.

# Specification of the Game
The game is played between a Computer and a Human. The human is required to guess the word that the computer has masked. The computer will select the random line from a text file “fnl.txt.” The text file is derived from the glossary of the biology book from OpenStax. graphics.py from Python Programming: An Introduction to Computer
Science is used for the graphics of the game.
For this version, the game is only mouse-based. The user must click the letters shown in the display and win the game before they fail because of multiple incorrect entries.
The game ends when the word is correctly guessed, or the stick figure is fully drawn. For this model of the game, the stick figure is fully drawn at four incorrect attempts regardless of the word length.
A hint would be available before the final chance to make the user focus more on the words and their spelling to enrich their vocabulary.
No statistics will be revealed in the game. The game would only prompt you if you won the game for that round or not.

# Rules of the Game
The game proceeds as follows:
- The user will be displayed with a graphical user interface for the game. Initially, the
guessing word is masked, gallows, and the keyboard is displayed.
- The user is supposed to guess the word and is allowed to click a letter.
- If the user guesses the correct letter, then the correct letter is unmasked from the masked
letter.
- There are four chances given to guess the masked word correctly. A hint will be provided
on the third failed attempt to guess the word correctly. Please get the word in four accurate shots to avoid a loss for the game. And it will pop you a button either to try again or quit.
- If the user clicks the try button again, then the user will be given a chance to play again.

# Visuals
<img width="602" alt="Screenshot 2024-11-21 at 11 20 55 PM" src="https://github.com/user-attachments/assets/9011b0c3-59e7-42e0-bee0-6a7300010693">
<img width="602" alt="Screenshot 2024-11-21 at 11 21 18 PM" src="https://github.com/user-attachments/assets/66a955c0-095e-470f-bc61-8f82cfc89d2f">
<img width="602" alt="Screenshot 2024-11-21 at 11 22 52 PM" src="https://github.com/user-attachments/assets/792366df-f451-483d-903a-326434b48a83">
<img width="600" alt="Screenshot 2024-11-21 at 11 24 05 PM" src="https://github.com/user-attachments/assets/4cee840b-3a6f-421d-bcc6-979684f3896f">


# Acknowledgment
I would like to thank Professor Aana Varvak for her invaluable guidance. I would also like to thank the authors of "Python Programming: An Introduction to Computer
Science ISBN: 9781590282755 and OpenStax for their valuable contributions to my project.

Note: This project was submitted for the Introduction to Computer Science(MATH121)(2023), Soka University of America.

<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Hangman Game</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            display: flex;
            flex-direction: column;
            align-items: center;
            background-color: #f0f0f0;
            min-height: 100vh;
            margin: 0;
            padding: 20px;
        }

        .game-container {
            background-color: white;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 0 10px rgba(0,0,0,0.1);
            max-width: 800px;
            width: 100%;
            display: flex;
            flex-direction: column;
            align-items: center;
        }

        .word-display {
            font-size: 2em;
            letter-spacing: 5px;
            margin: 20px 0;
            text-align: center;
            min-height: 50px;
        }

        .hint-display {
            color: red;
            margin: 20px 0;
            text-align: center;
            font-size: 0.9em;
            max-width: 600px;
            min-height: 60px;
            padding: 10px;
        }

        .keyboard {
            display: grid;
            grid-template-rows: repeat(3, 1fr);
            gap: 5px;
            margin: 20px 0;
        }

        .keyboard-row {
            display: flex;
            justify-content: center;
            gap: 5px;
        }

        .key {
            width: 40px;
            height: 40px;
            border: 1px solid #ccc;
            border-radius: 5px;
            display: flex;
            align-items: center;
            justify-content: center;
            cursor: pointer;
            background-color: white;
            font-weight: bold;
        }

        .key.disabled {
            background-color: #ddd;
            cursor: not-allowed;
            color: #999;
        }

        .hangman-container {
            border: 1px solid #ccc;
            padding: 20px;
            margin: 20px 0;
            width: 400px;
            height: 400px;
            position: relative;
        }

        #game-over {
            position: fixed;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            background-color: white;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 0 10px rgba(0,0,0,0.2);
            display: none;
            text-align: center;
            z-index: 1000;
        }

        .button {
            padding: 10px 20px;
            margin: 10px;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            background-color: #4CAF50;
            color: white;
            font-size: 1em;
        }

        .button:hover {
            background-color: #45a049;
        }
    </style>
</head>
<body>
    <div class="game-container">
        <div class="hangman-container">
            <canvas id="hangmanCanvas" width="400" height="400"></canvas>
        </div>
        <div class="word-display" id="wordDisplay"></div>
        <div class="hint-display" id="hintDisplay"></div>
        <div class="keyboard">
            <div class="keyboard-row" id="row1">
                <button class="key">Q</button>
                <button class="key">W</button>
                <button class="key">E</button>
                <button class="key">R</button>
                <button class="key">T</button>
                <button class="key">Y</button>
                <button class="key">U</button>
                <button class="key">I</button>
                <button class="key">O</button>
                <button class="key">P</button>
            </div>
            <div class="keyboard-row" id="row2">
                <button class="key">A</button>
                <button class="key">S</button>
                <button class="key">D</button>
                <button class="key">F</button>
                <button class="key">G</button>
                <button class="key">H</button>
                <button class="key">J</button>
                <button class="key">K</button>
                <button class="key">L</button>
            </div>
            <div class="keyboard-row" id="row3">
                <button class="key">Z</button>
                <button class="key">X</button>
                <button class="key">C</button>
                <button class="key">V</button>
                <button class="key">B</button>
                <button class="key">N</button>
                <button class="key">M</button>
            </div>
        </div>
    </div>

    <div id="game-over">
        <h2 id="result-text"></h2>
        <button class="button" id="playAgain">Play Again</button>
        <button class="button" id="quit">Quit</button>
    </div>

    <script>
        class HangmanGame {
            constructor() {
                // Sample data format from fnl.txt (will be loaded from file in production)
                this.gameData = [
                    "word1: This is hint 1",
                    "complex word or phrase: This is a longer hint that explains the word",
                    // ... more entries would be loaded from fnl.txt
                ];
                
                this.canvas = document.getElementById('hangmanCanvas');
                this.ctx = this.canvas.getContext('2d');
                this.wordDisplay = document.getElementById('wordDisplay');
                this.hintDisplay = document.getElementById('hintDisplay');
                this.errorCount = 0;
                this.maxErrors = 4;
                
                // Load the game data
                this.loadGameData().then(() => {
                    this.initGame();
                    this.setupKeyboard();
                    this.setupKeyboardInput();
                });
            }

            async loadGameData() {
                try {
                    const response = await fetch('fnl.txt');
                    const text = await response.text();
                    this.gameData = text.split('\n').filter(line => line.trim());
                } catch (error) {
                    console.error('Error loading game data:', error);
                    // Keep using sample data if file load fails
                }
            }

            initGame() {
                const randomIndex = Math.floor(Math.random() * this.gameData.length);
                const line = this.gameData[randomIndex];
                const [word, hint] = line.split(':').map(str => str.trim());
                
                this.currentWord = word.toUpperCase();
                this.currentHint = hint;
                this.maskedWord = this.maskWord(word);
                this.hintDisplay.textContent = '';  // Start with no hint
                this.wordDisplay.textContent = this.maskedWord;
                this.errorCount = 0;
                this.drawGallows();
                this.enableAllKeys();
            }

            maskWord(word) {
                return word.split('').map(char => {
                    if (char === ' ' || char === '-' || char === ',' || char === "'" || 
                        char === '.' || char === ';' || char === '(' || char === ')') {
                        return char;
                    }
                    return '~';
                }).join('');
            }

            setupKeyboard() {
                document.querySelectorAll('.key').forEach(key => {
                    key.addEventListener('click', () => this.handleKeyClick(key));
                });

                document.getElementById('playAgain').addEventListener('click', () => {
                    document.getElementById('game-over').style.display = 'none';
                    this.initGame();
                });

                document.getElementById('quit').addEventListener('click', () => {
                    window.close();
                });
            }

            setupKeyboardInput() {
                document.addEventListener('keydown', (event) => {
                    const key = event.key.toUpperCase();
                    if (/^[A-Z]$/.test(key)) {
                        const keyElement = Array.from(document.querySelectorAll('.key'))
                            .find(k => k.textContent === key && !k.classList.contains('disabled'));
                        if (keyElement) {
                            this.handleKeyClick(keyElement);
                        }
                    }
                });
            }

            handleKeyClick(key) {
                if (key.classList.contains('disabled')) return;
                
                const letter = key.textContent;
                key.classList.add('disabled');
                
                if (this.currentWord.includes(letter)) {
                    this.updateMaskedWord(letter);
                } else {
                    this.errorCount++;
                    this.drawHangman();
                    
                    // Show hint after 3 incorrect attempts
                    if (this.errorCount === 3) {
                        this.hintDisplay.textContent = `Hint: ${this.currentHint}`;
                    }
                }

                this.checkGameEnd();
            }

            updateMaskedWord(letter) {
                let newMasked = '';
                for (let i = 0; i < this.currentWord.length; i++) {
                    if (this.currentWord[i] === letter) {
                        newMasked += letter;
                    } else {
                        newMasked += this.maskedWord[i];
                    }
                }
                this.maskedWord = newMasked;
                this.wordDisplay.textContent = this.maskedWord;
            }

            enableAllKeys() {
                document.querySelectorAll('.key').forEach(key => {
                    key.classList.remove('disabled');
                });
            }

            checkGameEnd() {
                if (this.errorCount >= this.maxErrors || !this.maskedWord.includes('~')) {
                    const gameOver = document.getElementById('game-over');
                    const resultText = document.getElementById('result-text');
                    
                    if (this.errorCount >= this.maxErrors) {
                        resultText.textContent = 'You Lost!';
                    } else {
                        resultText.textContent = 'You Won!';
                    }
                    
                    this.wordDisplay.textContent = this.currentWord;
                    gameOver.style.display = 'block';
                }
            }

            drawGallows() {
                this.ctx.clearRect(0, 0, 400, 400);
                this.ctx.strokeStyle = 'black';
                this.ctx.lineWidth = 2;
                
                // Base
                this.ctx.beginPath();
                this.ctx.moveTo(100, 350);
                this.ctx.lineTo(300, 350);
                this.ctx.stroke();
                
                // Vertical pole
                this.ctx.beginPath();
                this.ctx.moveTo(200, 350);
                this.ctx.lineTo(200, 100);
                this.ctx.stroke();
                
                // Horizontal beam
                this.ctx.beginPath();
                this.ctx.moveTo(200, 100);
                this.ctx.lineTo(300, 100);
                this.ctx.stroke();
                
                // Rope
                this.ctx.beginPath();
                this.ctx.moveTo(300, 100);
                this.ctx.lineTo(300, 120);
                this.ctx.stroke();
            }

            drawHangman() {
                switch(this.errorCount) {
                    case 1: // Head
                        this.ctx.beginPath();
                        this.ctx.arc(300, 140, 20, 0, Math.PI * 2);
                        this.ctx.stroke();
                        break;
                    case 2: // Body
                        this.ctx.beginPath();
                        this.ctx.moveTo(300, 160);
                        this.ctx.lineTo(300, 240);
                        this.ctx.stroke();
                        break;
                    case 3: // Arms
                        this.ctx.beginPath();
                        this.ctx.moveTo(300, 180);
                        this.ctx.lineTo(270, 200);
                        this.ctx.moveTo(300, 180);
                        this.ctx.lineTo(330, 200);
                        this.ctx.stroke();
                        break;
                    case 4: // Legs
                        this.ctx.beginPath();
                        this.ctx.moveTo(300, 240);
                        this.ctx.lineTo(270, 280);
                        this.ctx.moveTo(300, 240);
                        this.ctx.lineTo(330, 280);
                        this.ctx.stroke();
                        break;
                }
            }
        }

        // Start the game
        new HangmanGame();
    </script>
</body>
</html>

