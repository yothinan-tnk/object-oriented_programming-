while True:
    try:
        print("โปรแกรมหาพื้นที่สี่เหลี่ยม")
        side = int(input("ใส่ค่าด้าน :"))
        if side == 0:
            raise ZeroDivisionError
        elif side < 0:
            raise Exception("ห้ามใส่ค่าติดลบ")
        bside = side
        area_square = bside * side
        print(f"ค่าพื้นที่สี่เหลี่ยม = {area_square}")
        print("โปรแกรมหาพื้นที่ 3 เหลี่ยม")
        base = int(input("ใส่ค่าฐาน :"))
        height = int(input("ใส่ค่าสูง :"))
        if base == 0 or height == 0:
            raise ZeroDivisionError
        elif base < 0 or height < 0:
            raise Exception("ห้ามใส่ค่าติดลบ")
        area_triangle = 0.5 * base * height
        print(f'ค่าของพื้นที่ 3 เหลี่ยม = {area_triangle}')
        print("โปรแกรมหาพื้นที่วงกลม")
        radius = int(input("ใส่รัศมี :"))
        if radius == 0:
            raise ZeroDivisionError
        elif radius < 0:
            raise Exception("ห้ามใส่ค่าติดลบ")
        area_circle = 3.14 * radius ** 2
        print(f"ค่าพื้นที่วงกลม = {area_circle}")

    except ValueError:
        print("ใส่เฉพาะตัวเลข")
    except ZeroDivisionError:
        print("ห้ามใส่ 0")
    except Exception as e:
        print(e)
