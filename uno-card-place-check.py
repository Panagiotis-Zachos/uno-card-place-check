def check_card(face_up, hand):

    if not len(hand) == len(face_up) == 2:
        print('Invalid input length')
        return

    hand_color, hand_number = hand
    face_up_color, face_up_number = face_up

    if not (face_up_color  in 'rgby' and hand_color in 'rgby'):
        print('Invalid color')
        return None

    if hand_color == face_up_color or hand_number==face_up_number:
        return True
    return False

print('Enter cards as follows, for example, if the face up card is a Green 4, enter g4 etc.')
val = None
while val is None:
    val = check_card(input('Enter face up card: '), input('Enter hand card: '))
    if val == True:
        print('Valid Card!')
    elif val == False:
        print('Invalid Card!')