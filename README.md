# ATM Simulation

This Python script simulates a simple ATM system. Users can check their balance, withdraw money, deposit money, and exit the system. The script validates the user's ATM PIN before allowing access to these operations.

## Features

1. Check Balance
2. Withdraw Money
3. Deposit Money
4. Exit

## How to Use

1. **Insert Card**: Run the script to start the simulation.
2. **Enter ATM PIN**: Input your ATM PIN to access your account.
3. **Choose an Option**:
    - `1`: Check your current balance.
    - `2`: Withdraw money from your account.
    - `3`: Deposit money into your account.
    - `4`: Exit the ATM system.

## Script Details

- The script uses a predefined ATM PIN (`password=132004`) and an initial balance (`balance=45005`).
- The user is prompted to enter their ATM PIN (`pin=int(input("enter your atm pin "))`).
- If the entered PIN is correct, the user is presented with a menu of options.
- Based on the user's choice, the corresponding action is performed.

## Example Usage
Please insert Your CARD enter your atm pin 132004 1 == balance 2 == withdraw balance 3 == deposit balance 4 == exit

Please enter your choice 1 Your current balance is 4500

## Error Handling

- The script includes a try-except block to ensure that the user enters a valid option.

## Note

- This is a simple simulation and does not interact with any real banking systems.


