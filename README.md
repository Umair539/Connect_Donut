# Connect_Donut 
Connect Donut is a multiplayer Connect Four game built in Python. It features a client-server architecture that allows multiple pairs of two players to compete over a local network in real-time. This project showcases the implementation of modular class structures, win-condition logic, and multithreaded networking.

---

## Project Structure

The project is organized into 2 main folders:

### Client
* **`Client.py`**: The main entry point for players. Manages the Pygame window, user inputs, and visual updates.
* **`Network.py`**: A dedicated class for handling server communication.
* **`Pieces.py`**: Contains the Pieces class and is where the sprite images are accessed from.
* **`Sprites/`**: Directory containing the sprites for the game.

### Server
* **`Server.py`**: The host application that manages player connections and traffic.
* **`Game.py`**: The "Source of Truth." Contains the game state, move validation, and win-condition logic.

---

## Execution Steps

1. Install pygame
    ```bash
    pip install pygame
   ```
2. Install project in editable mode
    ```bash
    pip install -e .
   ``` 
3. Configure network details
    1. Set server IP address to the local IP address in **`Server.py`** and in **`Network.py`**
    2. Set port number in **`Server.py`** and in **`Network.py`** to an available port number

4. Launch the server
    ```
    run_server
   ```
5. Launch the clients
    ```
    run_client
   ```
Note: `run_client` must be run for each player inside its own dedicated terminal

---

## Tools and techniques

* Python
* Pygame
* Multithreading
* Networking

---

## To-do

* **Private Servers**: Add functionality so users can choose who they want to play with by inputting a code.
* **Connection Management**: Automatically close a game if a player leaves and doesn't rejoin.
* **Custom Game Modes**: Add options for custom games (e.g., an 8x8 board with 5-in-a-row to win). 
  > Note: `game.py` already supports dynamic board logic but implementing dynamic Pygame window size in `client.py` needs investigating.
