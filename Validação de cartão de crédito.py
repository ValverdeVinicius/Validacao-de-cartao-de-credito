card_number = list(input("Digite o número do cartão: ").strip())

# Remove o último dígito do cartão
check_digit = card_number.pop()

# Inverter a ordem dos números restantes
card_number.reverse()

processed_digits = []

for index, digit in enumerate(card_number):
	if index % 2 == 0:
		doubled_digit = int(digit) * 2

		# Subtrair 9 de qualquer resultados que sejam superiores a 9		
		if doubled_digit > 9:
			doubled_digit = doubled_digit - 9

		processed_digits.append(doubled_digit)
	else:
		processed_digits.append(int(digit))

total = int(check_digit) + sum(processed_digits)

# Verificar se a soma dos dígitos é divisível por 10
if total % 10 == 0:
	print("Valido!")
else:
	print("Invalido!")
