def check_chan_le(so_bat_ki):
    if so_bat_ki %2 == 0:
        return True
    else:
        return False

def double_and_check_greater_than_nine(so_bat_ki):
    if so_bat_ki * 2 > 9:
        so_moi = so_bat_ki * 2 - 9
        return so_moi
    else:
        return so_bat_ki * 2

def valid_credit_card_number():
    print("So the tin dung ban vua nhap vao kha dung")

def invalid_credit_card_number():
    print("So the tin dung ban vua nhap vao khong kha dung")

def main():
    main_check = True
    while main_check:
        credit_card_number = reversed(list(input("Nhap so the tin dung ma ban can check vao day")))
        for chu_so in credit_card_number:
            if chu_so.isdigit == True:
                pass
            else:
                invalid_credit_card_number()
                main_check = False

    # day so moi cua the tin dung
        day_so_moi = []

        so_chu_so = len(credit_card_number)
        if 12 <= so_chu_so <= 19:
            pass
        else:
            invalid_credit_card_number()
            break

    #check de them nhung chu so tu thu 1 cho den cuoi
        
        for x in range(0,len(credit_card_number)-1) :
           chan_hay_le = check_chan_le(x)
           if chan_hay_le == True:
               y = double_and_check_greater_than_nine(credit_card_number[x])
               day_so_moi.append(y)
           else:
               day_so_moi.append(credit_card_number[x])

    #tong day so moi
        sum = 0
        for so_moi in day_so_moi:
           sum += so_moi

    #buoc cuoi check tong co chiahet cho 10 hay ko
        if sum%10==0:
            valid_credit_card_number()
            break
        else:
            invalid_credit_card_number()
            break









