import random
import time
import math 
import operator #thực hiện phép toán

# SETUP

delay = 1 # <-- Biến này được sử dụng sau này trong mã để xác định khoảng thời gian chờ giữa mỗi thao tác mới trong bài kiểm tra. 
#Trong trường hợp này, độ trễ được đặt thành 1 giây.


ops = {'+':operator.add,
    '-':operator.sub,
    '*':operator.mul,
    '/':operator.truediv,
}

count_correct = 0 #theo dõi Số lượng câu trả lời đúng 
count_incorrect = 0 #theo dõi Số lượng câu trả lời sai
count_skipped = 0#theo dõi Số lượng câu trả lời bỏ qua 

true = "Correct"
false = "Incorrect"
Help = """
Bài Kiểm tra Toán
Để bỏ qua hoặc nộp bài nhấn enter

Để dừng lại Ctrl+C"""

# nếu bạn nhận được nhiều số sau dấu chấm
# bạn có thể cắt bớt nó cho đến khi nó có 3 số sau dấu chấm
# ví dụ thay vì gõ: 3.5641566 bạn chỉ cần gõ: 3.564
def truncate(num, dig): #truncate nhận 2 đối số là num và dig 
    stepper = 10.0 ** dig
    #Biến stepperđược xác định và đặt thành 10 lũy thừa của dig. Nó được sử dụng để cắt bớt số numđến digvị trí thập phân.
    return math.trunc(stepper *num) / stepper
    #Hàm math.trunc()được sử dụng để cắt bớt số numthành số vị trí thập phân được chỉ định bởi digđối số. 
    #Biến stepperđược sử dụng để nhân numtrước khi bị cắt bớt. 
    #Sau đó, số bị cắt bớt được chia steppercho số bị cắt đến digvị trí thập phân. 
    #Số bị cắt ngắn được trả về dưới dạng đầu ra của hàm này.


def main():

    global count_correct          ##các biến này được định nghĩa bên ngoài hàm chính và đang được sử dụng bên trong hàm chính.
    global count_incorrect      ####Bằng cách sử dụng từ khóa "toàn cầu", các biến được truy cập dưới dạng biến toàn cục thay vì được coi là biến cục bộ mới trong hàm chính.
    global count_skipped          ##Điều này cho phép chức năng chính sửa đổi và truy cập các giá trị của các biến này đã được xác định bên ngoài nó.

    print(Help)

    while 1:
        try:

            num1 = random.randint(1,150) #tạo ra một số nguyên ngẫu nhiên giữa các giá trị của avà b,num1 sẽ là một số nguyên ngẫu nhiên trong khoảng từ 1 đến 150

            op = random.choice(list(ops.keys())) #lựa chọn ngẫu nhiên từ các khóa của opstừ điển. random.choice() - nhân chia cộng trừ 

            if op == "/": num2 = random.randint(2,10) ##nếu op là chia thì num2 nằm trong khoảng từ 2 tới 10
            elif op == "*": num2 = random.randint(2,20) ##nếu op là nhân thì num2 nằm trong khoảng từ 2 tới 20
            else: num2 = random.randint(1,150) ##tương tự num1

            answer = ops.get(op)(num1,num2)

            opp = f"{num1} {op} {num2} ="

            user_try = input(str(opp) + ' ')

            if user_try == '':
                print('Answer: ' + str(answer)+ '\n')      ###Nếu người dugn2 nhập khoảng trắng ,tập lệnh sẽ in câu trả lời đúng và tăng số lượng câu trả lời bị bỏ qua.
                count_skipped += 1
            elif float(user_try) == answer or float(user_try) == truncate(answer,3):
                print(true + '\n')
                count_correct += 1 
            #Nếu đầu vào của người dùng là một số dấu phẩy động bằng với câu trả lời đúng 
            #hoặc bằng với câu trả lời đúng bị cắt bớt đến 3 chữ số thập phân
            #tập lệnh sẽ in thông báo "Đúng" và tăng số lượng câu trả lời đúng.



            else:
                print(false + ', Correct answer: ' + str(answer)+ '\n')
                count_incorrect += 1
                # Nếu đầu vào của người dùng không bằng câu trả lời đúng, tập lệnh sẽ in thông báo "Sai" cùng với câu trả lời đúng và tăng số lượng câu trả lời sai.

            time.sleep(delay)#Tập lệnh ngủ trong khoảng thời gian được đặt trong biến độ trễ trước khi chuyển sang lần lặp tiếp theo.



        except KeyboardInterrupt: #tryKhối được bao quanh toàn bộ tập lệnh và exceptcâu lệnh đang bắt KeyboardInterruptlỗi
                                  #điều này xảy ra khi người dùng nhấn Ctrl+Ctrong khi thực thi tập lệnh.
            total = count_correct+count_incorrect+count_skipped #
            print("""

Correct answers: {}/{}

Incorrect answers: {}/{}

Skipped: {}/{}

""".format(count_correct,total,count_incorrect,total,count_skipped,total))
            ###Một thông báo được in chứa tổng số câu trả lời đúng, sai và bị bỏ qua ở định dạng "Câu trả lời đúng: x/y, Câu trả lời không chính xác: x/y, Đã bỏ qua: x/y" 
            exit(0)##Tập lệnh thoát với mã trạng thái là 0, cho biết thoát thành công.

        except ValueError:
            print("Oh please, type numbers only!!")
            exit(1)

if __name__ == '__main__':
    main()
