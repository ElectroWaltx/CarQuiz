#Display image, take input, check if input is correct
import random
from PIL import Image
import requests
from io import BytesIO
from tqdm.auto import tqdm
switch = True
for i in range(0,100):
    print("")
def entertostart():
    print("Hello! Welcome to CarQuiz.")
    print("Please press enter to start")
    if input("") == '':
        print("Loading...")
    else: 
        exit(0)

def picdisplay():
    img1 = Image.open(BytesIO(requests.get("https://www.mercedes-benz.com.hk/en/passengercars/mercedes-benz-cars/models/amg-gt/amg-gt-coupe/explore/model/_jcr_content/par/videoimageslider_3e3/slides/videoimageslide_e011/image.MQ6.12.20180503165323.jpeg").content))
    img2 = Image.open(BytesIO(requests.get("https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/p90390718-highres-1592255347.jpg").content))
    img3 = Image.open(BytesIO(requests.get("https://cdn.motor1.com/images/mgl/NR1vY/s1/2020-audi-r8-coupe.jpg").content))
    img4 = Image.open(BytesIO(requests.get("https://upload.wikimedia.org/wikipedia/commons/thumb/c/c6/2011_Ferrari_458_Italia_DCT_S-A_4.5_Front.jpg/1200px-2011_Ferrari_458_Italia_DCT_S-A_4.5_Front.jpg").content))
    img5 = Image.open(BytesIO(requests.get("https://www.forbes.com/wheels/wp-content/uploads/2020/08/2021-porsche-panamera-1200x630-1.png").content))
    img6 = Image.open(BytesIO(requests.get("https://secure-akns.subaru.com/content/media/mp_hero_880/20_BRZ_photos_ext_02.jpg").content))
    img7 = Image.open(BytesIO(requests.get("https://specials-images.forbesimg.com/imageserve/5f02b2e299f5170006fad6fe/960x0.jpg").content))
    img8 = Image.open(BytesIO(requests.get("https://trabalhos.esmad.ipp.pt/tsiw/18-19/nes/wp_group06/wp-content/uploads/2019/01/Lamborghini-Aventador.jpg").content))
    img9 = Image.open(BytesIO(requests.get("https://www.motortrend.com/uploads/sites/5/2017/07/2018-Maserati-GranTurismo-coupe-front-three-quarters.jpg").content))
    img10 = Image.open(BytesIO(requests.get("https://www.bentleymedia.com/_assets/85abbd41-8ada-4e36-b08c-28fb49b04d5d.jpg").content))
    for i in tqdm(range(10000)):
        print(" ", end='\r')
    img_list = [img1, img2, img3, img4, img5, img6, img7, img8, img9, img10]
    global pos 
    pos = random.randint(0,6)
    disp_img = img_list[pos]
    disp_img.show()

def gameplay():
    playerchoice = input("Which car is this?(Enter the manufacturer_name(space)model_name): ")
    if pos == 0 and playerchoice.lower() == "mercedes amg gt":
        print("Correct!")
    elif pos == 1 and playerchoice.lower() == "bmw m5":
        print("Correct!")
    elif pos == 2 and playerchoice.lower() == "audi r8":
        print("Correct!")
    elif pos == 3 and playerchoice.lower() == "ferrari 458":
        print("Correct!")
    elif pos == 4 and playerchoice.lower() == "porsche panamera":
        print("Correct!")
    elif pos == 5 and playerchoice.lower() == "subaru brz":
        print("Correct!")
    elif pos == 6 and playerchoice.lower() == "aston martin db5":
        print("Correct!")
    elif pos == 7 and playerchoice.lower() == "lamborghini aventador":
        print("Correct!")
    elif pos == 8 and playerchoice.lower() == "maserati granturismo":
        print("Correct!")
    elif pos == 9 and playerchoice.lower() == "bentley continental gt":
        print("Correct!")
    else:
        print("Wrong :(")

def play_again():
    switch = True 
    while switch == True:
        playagain_input = input("Do you want to play again?(Press Y for yes and N for no): ").lower()
        if playagain_input == "y":
            for i in range(0,100):
                print("")
            return True
            switch = False
        elif playagain_input == "n":
            return False
            switch = False
        else:
            print("Invalid! Please enter Y or N.")
            switch = True

while True: 
    entertostart()
    picdisplay()
    gameplay()
    if play_again() == False:
        print("Thanks for playing!")
        exit(0)
        

        




    




