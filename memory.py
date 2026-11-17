
import sqlite3

DB_NAME = "memory.db"


def initialize_memory():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS memories (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id TEXT,
            information TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    conn.commit()
    conn.close()


def save_memory(user_id, information):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO memories (user_id, information) VALUES (?, ?)",
        (user_id, information)
    )

    conn.commit()
    conn.close()


def retrieve_memories(user_id):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute(
        "SELECT id, information FROM memories WHERE user_id = ? ORDER BY id DESC",
        (user_id,)
    )

    results = cursor.fetchall()
    conn.close()

    return results


def delete_all_memories(user_id):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM memories WHERE user_id = ?",
        (user_id,)
    )

    conn.commit()
    conn.close()


def update_memory(memory_id, new_information):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute(
        "UPDATE memories SET information = ? WHERE id = ?",
        (new_information, memory_id)
    )

    conn.commit()
    conn.close()
