import os

if __name__=='__main__':
    print("welcome to robospeaker by chiru")
    while True:
        x=input("enter what u want me to speak:")
        if x=="q":
            os.system("say bye bye friend'")
            break
        command = f"say{x}"
        os.system(command)