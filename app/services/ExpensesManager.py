# class ExpensesManager:
#     def __init__(self):
#         self._expenses = []

#     def load_expenses_from_json(self, file_path: str):
#         with open(file_path, 'r', encoding='utf-8') as file:
#             import json
#             data = json.load(file)
#             if 'result' in data and 'transactions' in data['result']:
#                 self.process_expenses(data['result']['transactions'])
#             else:
#                 raise ValueError("Invalid JSON structure - missing required fields")

#     def process_expenses(self,expenses):
#         for expense in expenses:
#             extracted_data = self.extract_relevant_fields(expense)
#             self._expenses.append(extracted_data)

#     def extract_relevant_fields(self,expense):
#         extracted_data = {
#         "actualPaymentAmount": expense.get("actualPaymentAmount"),
#         "merchant_name": expense.get("merchant_name"),
#         "originalAmount": expense.get("originalAmount"),
#         "originalCurrency": expense.get("originalCurrency"),
#         "paymentDate": expense.get("paymentDate"),
#         "purchaseDate": expense.get("purchaseDate"),
#         "transactionType": expense.get("dealData", {}).get("transactionType"),
#         "category id": expense.get("category id"),
#         "planName": expense.get("planName"),

#     }
#         return extracted_data


#     def get_all_expenses(self):
#         return self._expenses

#     def get_total_amount(self) -> float:
#         return sum(trx['actualPaymentAmount'] for trx in self._expenses)

#     def clear_all_expenses(self):
#         self._expenses.clear()
