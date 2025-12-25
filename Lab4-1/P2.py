from BankAccount import BankAccount

john = BankAccount("John", "saving", 500)
tim = BankAccount("Tim", "loan", -1000000)
sarah = BankAccount("Sarah", "saving")
sarah_loan = BankAccount("Sarah", "loan", -100_000_000)
john.deposit(3000)
john.print_customer()

tim.print_customer()
tim.pay_loan(-tim.balance/2)
tim.print_customer()

sarah.deposit(50_000_000)
sarah.print_customer()

sarah_loan.print_customer()
