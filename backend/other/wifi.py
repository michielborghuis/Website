import subprocess


class Wifi:
    def wifi(self):
        data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8').split('\n')
        wifis = [line.split(':')[1][1:-1] for line in data if "All User Profile" in line]

        for wifi in wifis:
            results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', wifi, 'key=clear']).decode('utf-8').split('\n')
            results = [line.split(':')[1][1:-1] for line in results if "Key Content" in line]
            try:
                print(f'Name: {wifi}, Password: {results[0]}')
            except IndexError:
                print(f'name: {wifi}, Password: Not Available')


def main():
    w = Wifi()
    w.wifi()

if __name__ == "__main__":
    main()
