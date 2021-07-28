# pip3 install colorama

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip3", "install", package])

list =[
    {'name':'family1','address':'mac1'}
]

def search(list,address,color):

    found=False
    user_name=''
    for user in list:
        if address == user['address']:
            found=True
            user_name=user['name']

    if found:
        print(color.GREEN+f'{user_name} is a family member')
    else:
        print(color.RED+f'{address} not a family member')
    
def main():
    
    #imports
    from colorama import Fore, Back, Style
    from datetime import datetime
    import sys,subprocess

    guest_to_search = sys.argv[1]
    print(f'{datetime.now()}')
    search(list,guest_to_search,Fore)

if __name__=='__main__':
    main()
