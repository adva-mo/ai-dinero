from TransactionManager import TransactionManager

my_manager= TransactionManager()
my_manager.load_transactions_from_json('transactions.json')
print(my_manager.get_all_transactions())
print(my_manager.get_total_amount())