# GUI-based-Connect-4-game-vs-AI
A GUI based connect 4 game that uses voice as input

The speech recognition works by using two packages, pyaudio and speechRecognition. 
Pyaudio allows the microphone to be accepted as input, speechRecognition then discerns what the audio input is and a big if chain does the rest. We have to use a button to start the voice recognition so the gui can update. 

*GUI:*

![image](https://user-images.githubusercontent.com/97651215/193509274-a547dca5-319f-4adb-a9a5-b902b3394b31.png)

Here the GUI is booted up and shows the Connect 4 board. Here the two players decide who is first. When Player 1 is chosen, then they will click the, “Take Turn,” button to start.

![image](https://user-images.githubusercontent.com/97651215/193509367-ebb1fdd6-a882-42c3-a1dd-399054677850.png)

Here, Player 1 clicked the button and now they will have to say which column they want to place their ‘chip.’

![image](https://user-images.githubusercontent.com/97651215/193509403-66a0069c-aa84-4085-bdf6-257128d2041d.png)

Here the user placed their ‘chip’ into column one. After that it will give the prompt for Player 2 to take their turn. This will continue until a player has won, or there is a tie. 

![image](https://user-images.githubusercontent.com/97651215/193509444-def3f8ff-a2c6-4ca7-b57d-71e6e080df65.png)
![image](https://user-images.githubusercontent.com/97651215/193509452-85b7da69-e08d-4145-a1dc-85bd770c4dac.png)

Here is a depiction of each player winning, as well as a win for horizontal placement as well as diagonal placement. After there is a winner, or tie, the, “Reset Game,” button will appear for them to reset the game and play again. 
