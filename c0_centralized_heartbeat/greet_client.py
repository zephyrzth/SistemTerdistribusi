import Pyro4
import time

def test_no_ns():
    uri = "PYRO:obj_27d7c59497c44c688319f7d8a4a95935@localhost:40549"
    gserver = Pyro4.Proxy(uri)
    print(gserver.get_greet('ronaldo'))

def test_with_ns():
    uri = "PYRONAME:greetserver@localhost:7777"
    gserver = Pyro4.Proxy(uri)
    print(gserver.get_greet('ronaldo'))
    while(True):
        actionType = input("0 = Create File\n1 = Read File\n2 = Update File\n3 = Delete File\n4 = List files\n-1 = Exit the program\nEnter the action type : ")
        if actionType == "0":
            filename = input("Enter filename : ")
            print(gserver.create_file(filename))
        elif actionType == "1":
            filename = input("Enter filename : ")
            print(gserver.read_file(filename))
        elif actionType == "2":
            filename = input("Enter filename (textfile) : ")
            contents = input("Enter text to write : ")
            print(gserver.update_file(contents, filename))
        elif actionType == "3":
            filename = input("Enter filename : ")
            print(gserver.delete_file(filename))
        elif actionType == "4":
            directory = input("Enter the directory to list : ")
            hasil = gserver.list_file(directory)
            for f in hasil:
                print(f)
        elif actionType == "-1":
            break
        else:
            print("Wrong input!")
        print("\n")

def coba_heartbeat():
    uri = "PYRONAME:greetserver@localhost:7777"
    gserver = Pyro4.Proxy(uri)
    print(gserver.get_greet('ronaldo'))
    client_id = gserver.get_device_total()
    print(gserver.add_device(client_id))
    while True:
        time.sleep(5)
        print(gserver.add_heartbeat(client_id))
        gserver.central_heartbeat()


if __name__=='__main__':
    #filename = "D:\\Sistem_Terdistribusi\\sister2019\\c0"
    #contents = "Coba McQueen YaQueen"
    # 0 = Create, 1 = Read, 2 = Update, 3 = Delete, 4 = List all files
    #actionType = 4
    #test_with_ns()
    coba_heartbeat()
