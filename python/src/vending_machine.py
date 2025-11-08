import os
import time
import json


class Item:
    def __init__(self, item_name, item_price):
        self.name = item_name
        self.price = item_price


class ItemSlot:
    def __init__(self, item: Item):
        self.item = item
        self.capacity = 10
        self.amount = 10

    def distribute_item(self):
        self.amount -= 1


class ItemGrid:
    def __init__(self, list_of_item_slots):
        self.items = list_of_item_slots


class VendingMachine:
    inserted_amount = 0

    def __init__(self, initial_state=None):
        self.inserted_amount = 0
        self.item_grid = ItemGrid([])
        if initial_state is not None:
            for item in initial_state:
                print(item)

    def add_item(self, item):
        self.item_grid.items.append(ItemSlot(item))

    def list_contents(self):
        for slot in self.item_grid.items:
            print(f"{slot.item.name} has capacity {slot.amount}.")

    def check_balance(self, item):
        difference = item.price - self.inserted_amount
        if difference >= 0:
            print(f"INSERT {difference} to buy")
            return False
        else:
            return True

    def checkout(self, item):
        self.inserted_amount -= item.price

    def clear_screen(self):
        os.system("clear")

    def run(self):
        self.clear_screen()
        while True:
            command = input()
            if command == "INSERT":
                value = 0
                while not value == "STOP":
                    value = input("VALUE> ")
                    try:
                        self.inserted_amount += int(value)
                    except:
                        pass
            elif command == "DIST":
                self.list_contents()
                coordinates = input("What would you like to drink?> ")
                slot = self.item_grid.items[int(coordinates)]
                item = slot.item
                slot.distribute_item()
                if self.check_balance(item):
                    self.checkout(item)
                    print("Thank you for your order!")
                    time.sleep(2)
                else:
                    print("INSUFFICIENT BALANCE!")
                    time.sleep(1)
            else:
                print("THIS COMMAND IS NOT RECOGNIZED")
                time.sleep(0.5)
            self.clear_screen()


def main():
    machine = VendingMachine(["Hello", "Vending Machine!"])
    cola = Item("coca_cola", 1.50)
    fanta = Item("fanta", 2.00)
    machine.add_item(cola)
    machine.add_item(fanta)
    machine.run()


if __name__ == "__main__":
    main()
