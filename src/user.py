from itemlist import ItemList
from userlist import UserList

class User:
    def __init__(self):
        self._fines = float()
        self._identification = int()
        self._item_list = ItemList()
    def __del__(self):
        pass

    def able_to_borrow(self, max_number_loans, max_total_fine):
        # checks if user is able to borrow
        if self.get_fine_total() > max_total_fine or self._item_list.number_of_items() > max_number_loans:
            return False
        else:
            return True

    def checkout_item(self, item_requested, date):
        # checks out item
        if self.able_to_borrow():
            ItemList.checkout_item(item_requested, date)
        else:
            return None

    def get_fine_total(self):
        # returns the total amount of fines for the user
        return self._item_list.get_fines()

    def get_identification(self):
        return self._identification

    def pay_fine(self, amount):
        # subtracts amount from user's total fines
        self._fines = ItemList.get_fines(self._item_list) - amount
        pass

    def return_item(self):
        # updates user's returned item list
        return
