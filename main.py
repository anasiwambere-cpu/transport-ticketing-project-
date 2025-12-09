from database import initialize_db
from admin import admin_menu
from customer import customer_menu

def main():
    initialize_db()
    print('=== Online Food Delivery System ===')
    while True:
        print('1. Admin')
        print('2. Customer')
        print('3. Exit')
        choice = input('Choose: ')
        if choice == '1': admin_menu()
        elif choice == '2': customer_menu()
        elif choice == '3': break
        else: print('Invalid option')

if __name__ == '__main__':
    main()
