# ==========================================
# TAREA #1: ESTRUCTURAS DE DATOS BÁSICAS
# Alfredo Emir Puente Medrano - A00837999
# ==========================================

# 1. 

class Stack:
    """LIFO: Last-In, First-Out (Pila)"""
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if self.is_empty():
            return "Error: Stack vacío"
        return self.stack.pop()

    def is_empty(self):
        return len(self.stack) == 0

    def __str__(self):
        return f"Contenido del Stack: {self.stack}"


class Queue:
    """FIFO: First-In, First-Out (Cola)"""
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if self.is_empty():
            return "Error: Queue vacía"
        # pop(0) elimina el primer elemento (índice 0)
        return self.queue.pop(0)

    def is_empty(self):
        return len(self.queue) == 0

    def __str__(self):
        return f"Contenido de la Queue: {self.queue}"


class Table:
    """Tabla / Diccionario (Pares Clave-Valor)"""
    def __init__(self):
        self.table = {}

    def insert(self, key, value):
        self.table[key] = value

    def get(self, key):
        return self.table.get(key, "Clave no encontrada")

    def delete(self, key):
        if key in self.table:
            del self.table[key]

    def __str__(self):
        return f"Contenido de la Table: {self.table}"


# 2. PROGRAMA DE PRUEBA (DEMOSTRACIÓN)

def run_demo():
    print("=== DEMOSTRACIÓN DE ESTRUCTURAS ===\n")

    # Demo Stack
    print("--- STACK (LIFO) ---")
    pila = Stack()
    pila.push("Plato 1")
    pila.push("Plato 2")
    pila.push("Plato 3")
    print(f"Estado inicial: {pila}")
    print(f"Haciendo POP: {pila.pop()}") # Debe salir Plato 3
    print(f"Estado final: {pila}\n")

    # Demo Queue
    print("--- QUEUE (FIFO) ---")
    cola = Queue()
    cola.enqueue("Cliente 1")
    cola.enqueue("Cliente 2")
    cola.enqueue("Cliente 3")
    print(f"Estado inicial: {cola}")
    print(f"Atendiendo (DEQUEUE): {cola.dequeue()}") # Debe salir Cliente 1
    print(f"Estado final: {cola}\n")

    # Demo Table
    print("--- TABLE / DICTIONARY ---")
    tabla = Table()
    tabla.insert("user1", "Alice")
    tabla.insert("user2", "Bob")
    print(f"Estado inicial: {tabla}")
    print(f"Buscando 'user1': {tabla.get('user1')}")
    tabla.delete("user1")
    print(f"Después de borrar 'user1': {tabla}")

# 3. TEST CASES (DESCRIPCIÓN)
"""
TEST-CASES REALIZADOS:
1. Stack: Se intentó hacer pop() en una pila vacía. Resultado: Mensaje de error controlado.
2. Queue: Se intentó hacer dequeue() en una cola vacía. Resultado: Mensaje de error controlado.
3. LIFO: Se validó que el último elemento pusheado sea el primero en salir.
4. FIFO: Se validó que el primer elemento pusheado sea el primero en salir.
5. Hash Table : Funcionamiento y manejo de claves inexistentes.
"""

run_demo()