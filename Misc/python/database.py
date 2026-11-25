"""Tiny address-book database stored in a fixed-size binary file
(Python version of "Learn C the Hard Way" ex17).

Usage: database.py <dbfile> <action> [action params]
    c                 create
    g <id>            get
    s <id> <name> <email>   set
    d <id>            delete
    l                 list
"""
import struct
import sys

MAX_DATA = 512
MAX_ROWS = 100

# Same layout as the C struct Address: int id, int set, char name[], char email[]
ADDRESS_FMT = f"<ii{MAX_DATA}s{MAX_DATA}s"
ADDRESS_SIZE = struct.calcsize(ADDRESS_FMT)


class Address:
    def __init__(self, id_, set_=0, name="", email=""):
        self.id = id_
        self.set = set_
        self.name = name
        self.email = email

    def pack(self):
        return struct.pack(ADDRESS_FMT, self.id, self.set,
                           self.name.encode()[:MAX_DATA],
                           self.email.encode()[:MAX_DATA])

    @classmethod
    def unpack(cls, data):
        id_, set_, name, email = struct.unpack(ADDRESS_FMT, data)
        return cls(id_, set_, name.split(b"\0", 1)[0].decode(),
                   email.split(b"\0", 1)[0].decode())

    def print(self):
        print(f"{self.id} {self.name} {self.email}")


def die(message):
    print(f"ERROR: {message}")
    sys.exit(1)


class Connection:
    def __init__(self, filename, mode):
        self.rows = [Address(i) for i in range(MAX_ROWS)]
        try:
            if mode == "c":
                self.file = open(filename, "wb")
            else:
                self.file = open(filename, "r+b")
                self.load()
        except OSError as e:
            die(f"Failed to open the file: {e.strerror}")

    def load(self):
        data = self.file.read(ADDRESS_SIZE * MAX_ROWS)
        if len(data) != ADDRESS_SIZE * MAX_ROWS:
            die("Failed to load database.")
        self.rows = [Address.unpack(data[i * ADDRESS_SIZE:(i + 1) * ADDRESS_SIZE])
                     for i in range(MAX_ROWS)]

    def close(self):
        if self.file:
            self.file.close()

    def write(self):
        self.file.seek(0)
        self.file.write(b"".join(a.pack() for a in self.rows))
        self.file.flush()

    def create(self):
        self.rows = [Address(i) for i in range(MAX_ROWS)]

    def set(self, id_, name, email):
        addr = self.rows[id_]
        if addr.set:
            die("Already set, delete it first")
        addr.set = 1
        # names longer than MAX_DATA are truncated (the C strncpy bug is avoided)
        addr.name = name[:MAX_DATA - 1]
        addr.email = email[:MAX_DATA - 1]

    def get(self, id_):
        addr = self.rows[id_]
        if addr.set:
            addr.print()
        else:
            die("ID is not set")

    def delete(self, id_):
        self.rows[id_] = Address(id_)

    def list(self):
        for cur in self.rows:
            if cur.set:
                cur.print()


def main(argv):
    if len(argv) < 3:
        die("USAGE: database.py <dbfile> <action> [action params]")

    filename = argv[1]
    action = argv[2][0]
    conn = Connection(filename, action)
    id_ = int(argv[3]) if len(argv) > 3 else 0
    if id_ >= MAX_ROWS:
        die("There's not that many records.")

    if action == "c":
        conn.create()
        conn.write()
    elif action == "g":
        if len(argv) != 4:
            die("Need an id to get")
        conn.get(id_)
    elif action == "s":
        if len(argv) != 6:
            die("Need id, name, email to set")
        conn.set(id_, argv[4], argv[5])
        conn.write()
    elif action == "d":
        if len(argv) != 4:
            die("Need id to delete")
        conn.delete(id_)
        conn.write()
    elif action == "l":
        conn.list()
    else:
        die("Invalid action: c=create, g=get, s=set, d=del, l=list")

    conn.close()


if __name__ == "__main__":
    main(sys.argv)
