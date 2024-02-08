import subprocess

def run_linux_command(command):
    try:
        output = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT)
        return output.decode("utf-8")
    except subprocess.CalledProcessError as e:
        return e.output.decode("utf-8")

def main():
    while True:
        user_input = input("Linux Emulator $ ")
        if user_input.lower() in ['exit', 'quit']:
            break
        output = run_linux_command(user_input)
        print(output)

if __name__ == "__main__":
    main()
      
