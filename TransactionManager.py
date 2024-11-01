class TransactionManager:
    def __init__(self):
        self._transactions = []

    def load_transactions_from_json(self, file_path: str):
        with open(file_path, 'r', encoding='utf-8') as file:
            import json
            data = json.load(file)
            if 'result' in data and 'transactions' in data['result']:
                self.process_transactions(data['result']['transactions'])
            else:
                raise ValueError("Invalid JSON structure - missing required fields")

    def process_transactions(self,transactions):
        for transaction in transactions:
            extracted_data = self.extract_relevant_fields(transaction)
            self._transactions.append(extracted_data)

    def extract_relevant_fields(self,transaction):
        extracted_data = {
        "actualPaymentAmount": transaction.get("actualPaymentAmount"),
        "merchantName": transaction.get("merchantName"),
        "originalAmount": transaction.get("originalAmount"),
        "originalCurrency": transaction.get("originalCurrency"),
        "paymentDate": transaction.get("paymentDate"),
        "purchaseDate": transaction.get("purchaseDate"),
        "transactionType": transaction.get("dealData", {}).get("transactionType"),
        "categoryId": transaction.get("categoryId"),        
        "planName": transaction.get("planName"),
        
    }
        return extracted_data
    
    
    def get_all_transactions(self):
        return self._transactions
    
    def get_total_amount(self) -> float:
        return sum(trx['actualPaymentAmount'] for trx in self._transactions)
        
    def clear_all_transactions(self):
        self._transactions.clear()