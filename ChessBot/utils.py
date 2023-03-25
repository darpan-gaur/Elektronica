import cv2
import joblib
m = ['a','b','c','d','e','f','g','h']

# PATH_TO_MODEL = 'model.pkl'
# model = joblib.load(PATH_TO_MODEL)

def crop_img(path_to_image):
    img = cv2.imread(path_to_image)
    img = cv2.resize(img, (512, 512))
    out = []
    for i in range(8):
        temp = []
        for j in range(8):
            temp.append(img[i*64:(i+1)*64,j*64:(j+1)*64])
        out.append(temp)
    return out

def get_array(path_to_photo):
    # 5 dimensional array of 64x(size of one cropped image)
    imgs = crop_img(path_to_photo)
    arr = [[model.predict(imgs[i][j]) for j in range(8)] for i in range(8)]
    # for i in range(8):
    #     temp = []
    #     for j in range(8):
    #         temp.append(model.predict(imgs[i][j]))
    #     arr.append(temp)
    return arr


def move_from_player(arr, prev):
    changes = []
    ct = 0
    for i in range(8):
        for j in range(8):
            if (arr[i][j] != prev[i][j]):
                # s = f"{chr(j+'a')}{i+1}"
                changes.append([i,j])
                ct += 1
    # print(changes)
    move = ""
    if (ct==2):
        # One of the filled becomes empty and one of the empty becomes filled
        if (prev[changes[0][0]][changes[0][1]] =='a' and arr[changes[1][0]][changes[1][1]] != 'a'):
            move = f"{m[changes[0][1]]}{changes[0][0]+1}{m[changes[1][1]]}{changes[1][0]+1}"
        elif (prev[changes[0][0]][changes[0][1]] !='a' and arr[changes[1][0]][changes[1][1]] == 'a'):
            move = f"{m[changes[1][1]]}{changes[1][0]+1}{m[changes[0][1]]}{changes[0][0]+1}"
        # One of the filled becomes empty and one of the filled becomes filled with another filled
        else:
            if (arr[changes[0][0]][changes[0][1]] == 'a'):
                move = f"{m[changes[0][1]]}{changes[0][0]+1}{m[changes[1][1]]}{changes[1][0]+1}"
            else:
                move = f"{m[changes[1][1]]}{changes[1][0]+1}{m[changes[0][1]]}{changes[0][0]+1}"
    else:
        # Just one move needed
        move = f"{m[changes[0][1]]}{changes[0][0]+1}{m[changes[2][1]]}{changes[2][0]+1}"
        # move.append(f"{m[changes[3][1]]}{changes[3][0]+1}{m[changes[1][1]]}{changes[1][0]+1}")
    return move

def update_array(arr, move):
    temp = str(move)
    # print(temp)
    arr[int(temp[3])-1][ord(temp[2])-ord('a')] = arr[int(temp[1])-1][ord(temp[0])-ord('a')]
    arr[int(temp[1])-1][ord(temp[0])-ord('a')] = 'a'
    return arr