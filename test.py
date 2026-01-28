def calculate_total(items):
    total = 0
    for item in items:
        total += item['price'] * item['quantity']
    return total

def process_data(data):
    result = []
    for entry in data:
        if entry['active']:
            processed = {
                'id': entry['id'],
                'value': entry['value'] * 1.1
            }
            result.append(processed)
    return result

def main():
    items = [
        {'name': 'A', 'price': 100, 'quantity': 2},
        {'name': 'B', 'price': 200, 'quantity': 1}
    ]
    total = calculate_total(items)
    print(f"Total: {total}")

if __name__ == "__main__":
    main()
