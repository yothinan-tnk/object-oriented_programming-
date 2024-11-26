sum = 0

while True:
    try:
        num = input("ใส่ค่า (หรือพิมพ์ 'หยุด' เพื่อหยุด): ")
        if num == "หยุด":
            break
        num = int(num)
        if num == 0:
            raise ZeroDivisionError
        elif num < 0:
            raise Exception("ห้ามใส่ค่าติดลบ")
        sum += num
        print(f"ผลรวมตอนนี้ {sum}")

    except ValueError:
        print("ใส่เฉพาะตัวเลข")
    except ZeroDivisionError:
        print("ห้ามใส 0")
    except Exception as e:
        print(e)
print(f"ผลรวมทั้งหมด {sum}")
