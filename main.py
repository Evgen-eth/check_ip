import requests

def get_ip_address():
    try:
        # Запрос к внешнему сервису для получения IP-адреса
        response = requests.get('https://api.ipify.org?format=json')
        ip_data = response.json()
        ip_address = ip_data['ip']
        return ip_address
    except Exception as e:
        print("Ошибка при получении IP-адреса:", e)
        return None

def get_system_info():
    try:
        # Получение IP-адреса
        ip_address = get_ip_address()

        # Вывод IP-адреса
        print("IP адрес:", ip_address)
    except Exception as e:
        print("Ошибка при получении информации о системе:", e)

if __name__ == "__main__":
    get_system_info()
