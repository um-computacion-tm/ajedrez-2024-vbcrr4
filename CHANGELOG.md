# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/).
## (0.4.4) 22/10/24
### Issue 
- error en el movimiento de un peón
### Changed
- actualizacion de codigo de las piezas
## (0.4.3) 22/10/24
### Fixed
- arreglo de actualizacion de la posicion, el metodo de traduccion de input estaba retornando de forma incorrecta las posiciones y eso me impedía realizar los movimientos correctos. :/
## (0.4.2) 22/10/24
### Added 
- cracion de cli.py t de test_cli.py
### Removed
- eliminacion de carpetas __pychache__ y de env
## (0.4.1) 21/10/24
### Fixed
- arreglo de codigo de chess.py
- arreglo de tests de chess.py
## (0.4.0) 21/10/24
### Changed
- cambio en el codigo de chess.py y de board.py
- cambio en los test de chess.py y de board.py
## (0.3.9) 21/10/24
### Changed
- cambio en el codigo de chess.py, nuevos metodos agregados para manejar el juego
### Issues
- arrgelar problemas al realizar movimientos dentro del tablero en chess.py
## (0.3.8) 21/10/24
### Added
- nuevos metodos para board.py
- nuevos tests para board.py
### Changed
- cambio en el codigo de peon.py y piece.py
## (0.3.7) 18/10/24
### Added
- nueva exepcion para un input invalido
### Changed
- arreglo en los test de las piezas
- cambio en la estructuracion de algunos metodos como los de las piezas
### Issues
- subir chess.py con el codigo nuevo, pero antes debo de terminar de testear todo de manera correcta.
## (0.3.6) 15/10/24
### Added
- nueva exepcion para un input invalido.
## (0.3.5) 15/10/24
### Changed
- arreglo en la representacion del board para que se coloquen bien las representaciones de las piezas.
- cambio en la representacion de las piezas las blancas se reprensentan con "♜" y las negras con "♖"
- cambio en los test de piece.py y de board.py 
## (0.3.4) 14/10/24
### Added
- nuevos metodos para chess.py
- nuevos test para chess.py
### Changed 
- cambio en ".coveragerc"
## (0.3.3) 11/10/24
### Changed
- cambio en el codigo de los test para alfil.py
## (0.3.2) 11/10/24
### Changed
- cambio en el codigo de rey.py
- cambio en el codigo de los test para rey.py
## (0.3.1) 11/10/24
### Changed
- cambio en el codigo de caballo.py
- cambio en el codigo de los test para caballo.py
## (0.3.0) 2/10/24
### Added
- agregado de nuevo metodo para verificar si el camino esta libre para realizar un movimiento en peon.py
- agregado de test para peon.py
## (0.2.9) 27/09/24
### Added 
- creacion de codigo para test_chess.py
## (0.2.8) 27/09/24
### Changed
- cambio en la complejidad de codigo para board.py
## (0.2.7) 26/09/24
### Changed
- cambio en el codigo de peon.py, para reducir complejidad
## (0.2.6) 26/09/24
### Changed
- cambion en el codigo de peon.py
- push de cambios en archivos varios
## (0.2.5) 22/09/24
### Changed
- cambio en la complejidad de codigo para peon.py
## (0.2.4) 19/09/24
### Changed
- cambio en el codigo de piece.py
- cambio en el codigo de test_piece.py
## (0.2.3) 17/09/24
### Changed
- cambio en la complejidad de codigo para piece.py
### Added
- nuevo metodo para verificar si el camino esta libre para realizar un movimiento en piece.py
- nuevos tests para piece.py
## (0.2.2) 13/09/24
### Changed
- cambio en el codigo de chess.py
## (0.2.1) 13/09/24
### Removed
- removed cell.py y test_cell.py
## (0.2.0) 12/09/24
- agregado de nuevas exepcones en exepciones.py
## (0.1.9) 12/09/24
### Changed
- cambio en el codigo de piece.py
## (0.1.8) 11/09/24
### Changed
- cambio en el codigo de board.py
- cambio en los test de board.py
## (0.1.7) 10/09/24
### Changed
- cambio en el codigo de peon.py
- cambio en el codigo de los test de peon
## (0.1.6) 9/09/24
### Changed
- cambio en el codigo de caballo.py
- cambio en el codigo de los test de caballo
## (0.1.5) 8/09/24
### Changed
- cambio en el codigo de alfil.py
- cambio en el codigo de los test de alfil
## (0.1.4) 7/09/24
### Changed
- cambio en el codigo de reina.py
- cambio en el codigo de los test de la reina
## (0.1.3) 3/09/24
### Changed
- cambio en el codigo de rey.py
- cambio en el codigo de los test del rey
## (0.1.2) 1/09/24
### Changed
- cambio en el codigo de piece.py
- cambio en el codigo de torre.py
- cambio en ambos test de piece y torre
## (0.1.1) 29/08/24
### Changed
- agregado de un __str__ para Piece
- agregando tests para test_piece.py
## (0.1.0) 28/08/24
### Added
- reestructuracion de de piece.py
- creacion de test_piece.py
### Issues
- crear mas seguir modificando condigo de board.py y de pieces.py
- agregar mas test para pieces.py
- modificar codigo de las piezas 
## (0.0.9) 26/08/24
### Added
- creacion de chess.py
- creacion de test_chess.py
### Issues
- agregas mas test para chess.py
- arreglar test de pieces.py y board.py
## (0.0.8) 25/08/24
### Changed
- cambio en la representacion de piezas en el tablero, ahora las celdas continenen el nombre de la pieza
- cambio en el codigo de test_board.py para implementar las celdas
### Issues
- arreglar el codigo de test_board.py
## (0.0.7) 24/08/24
### Added
- refactorizacion de codgigo de cell.py, para representar las piezas en celdas
- agregado de test para cell.py
## (0.0.6) 23/08/24
### Changed 
- cambio de codigo en board.py, el metodo para verificar 'is_clear_path'
### Issues
- arreglar codigo de board.py
- arreglar codigo de test_board.py
- arreglar la forma de representar las piezas en el tablero
## (0.0.5) 21/08/24
### Changed
- cambio en el codigo de board.py para que imprima las piezas de cell.py
- cambio en test del tablero
- cambio en el codigo de piece.py 
- reestructuracion de varias clases
### Added
- creacion de exepciones.py
- creacion de un archivo por cada pieza para cumplir con los principios SOLID
- creacion de test para cada pieza
## (0.0.4) 19/08/24
### Added
- creacion de cell.py
- creacion de test_cell.py
### Changed
- cambio en el codigo de board.py para que imprima el tablero
- cambio en test del tablero
## (0.0.3) 18/08/24
### Fixed
- arreglo en el codigo de piece.py y sus respectivos tests
### Adeded
- creacion de codigo para movimientos de piezas y sus respectivos tests
### Changed
- cambio en el codigo de board.py para que imprima el tablero
- cambio en test del tablero
## (0.0.2) 17/08/24
### Changed
- cambio en el codigo de board.py para que imprima el tablero
- cambio en test del tablero
### Issues
- modificar codigo de piezas y tests
## (0.0.1) 15/08/24
### Added
- Pawn, Rook, Knight, Bishop, Queen, King classes
- Board class
- Board.imprimir_tablero_con_piezas() method
- Piece.get_color() method
- Piece.__str__() method
-test_board.py
-test_piece.py

### Changed
- None

### Removed
- None

### Fixed
- None
