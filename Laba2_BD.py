import Controller
import sys
from psycopg2 import Error

controller=Controller.Controller()

try:
    request = sys.argv[1]
except IndexError:
    controller.view.blank()
else:
    if request=='print'or request=='Print':
        try:
            request2 = sys.argv[2]
        except IndexError:
            controller.view.blank2()
        else:
            controller.print(request2)
    elif request=='delete'or request=='Delete':
        try:
            request2 = sys.argv[2]
        except IndexError:
            controller.view.blank2()
        else:
            try:
                request3 = sys.argv[3]
            except IndexError:
                controller.view.blank3()
            else:
                try:
                    request4 = sys.argv[4]
                except IndexError:
                    controller.view.blank4()
                else:
                    controller.delete(request2, request3, request4)
    elif request=='insert'or request=='Insert':
        try:
            request2 = sys.argv[2]
        except IndexError:
            controller.view.blank2()
        else:
            try:
                request3 = sys.argv[3]
            except IndexError:
                controller.view.blank3()
            else:
                try:
                    request4 = sys.argv[4]
                except IndexError:
                    controller.view.blank4()
                else:
                    try:
                        request5 = sys.argv[5]
                    except IndexError:
                        controller.view.blank5()
                    else:
                        if request2=='Event_category':
                            controller.insert1(request2, request3, request4, request5)
                        else:
                            try:
                                request6 = sys.argv[6]
                            except IndexError:
                                controller.view.blank6()
                            else:
                                try:
                                    request7 = sys.argv[7]
                                except IndexError:
                                    controller.view.blank6()
                                else:
                                    controller.insert2(request2, request3, request4, request5, request6, request7)
    elif request=='update'or request=='Update':
        try:
            request2 = sys.argv[2]
        except IndexError:
            controller.view.blank2()
        else:
            try:
                request3 = sys.argv[3]
            except IndexError:
                controller.view.blank3()
            else:
                try:
                    request4 = sys.argv[4]
                except IndexError:
                    controller.view.blank4()
                else:
                    try:
                        request5 = sys.argv[5]
                    except IndexError:
                        controller.view.blank5()
                    else:
                        if request2=='Event_category':
                            controller.update1(request2, request3, request4, request5)
                        else:
                            try:
                                request6 = sys.argv[6]
                            except IndexError:
                                controller.view.blank6()
                            else:
                                try:
                                    request7 = sys.argv[7]
                                except IndexError:
                                    controller.view.blank6()
                                else:
                                    controller.update2(request2, request3, request4, request5, request6, request7)
    elif request=='generate'or request=='Generate':
        try:
            request2 = sys.argv[2]
        except IndexError:
            controller.view.blank2()
        else:
            try:
                request3 = sys.argv[3]
            except IndexError:
                controller.view.blank3()
            else:
                controller.generator(request2, request3)
    elif request=='search'or request=='Search':
        t1=0
        a1=' '
        str1=' '
        dt11=' '
        dt12=' '
        max1=0
        min1=0
        t2=0
        a2=' '
        str2=' '
        dt21=' '
        dt22=' '
        max2=0
        min2=0
        t3=0
        a3=' '
        str3=' '
        dt31=' '
        dt32=' '
        max3=0
        min3=0
        k1=' '
        k2=' '
        k3=' '
        print("Name first table: Tk or Ev or Ev_cat")
        n_t=input()
        if n_t=='Tk':
            t1='Ticket'
            print("Name attribute: name or price or rest")
            inp=input()
            if inp=='name':
                a1='name'
                print("Input name")
                str1=input()
            elif inp=='price':
                a1='price'
                print("Input price min")
                mi=input()
                print("Input price max")
                ma=input()
                try:
                    max1=int(ma)
                    max2=int(mi)
                except:
                    controller.view.wronginput()

            elif inp=='rest':
                a1='rest'
                print("Input rest min")
                mi=input()
                print("Input rest max")
                ma=input()
                try:
                    max1=int(ma)
                    min1=int(mi)
                except:
                    controller.view.wronginput()

        elif n_t=='Ev':
            t1='Event'
            print("Name attribute: place or date")
            inp=input()
            if inp=='place':
                a1='place'
                print("Input place")
                str1=input()
            elif inp=='date':
                print("Input date: since")
                dt11=input()
                print("Input date: until")
                dt12=input()
        elif n_t=='Ev_cat':
            t1='Event category'
            a1='name'
            print("Input category name")
            str1=input()
        else:
            controller.view.wronginput()

        print("Name second table: Tk or Ev or Ev_cat")
        n_t=input()
        if n_t=='Tk':
            t2='Ticket'
            print("Name attribute: name or price or rest")
            inp=input()
            if inp=='name':
                a2='name'
                print("Input name")
                str2=input()
            elif inp=='price':
                a2='price'
                print("Input price min")
                mi=input()
                print("Input price max")
                ma=input()
                try:
                    max2=int(ma)
                    min2=int(mi)
                except:
                    controller.view.wronginput()

            elif inp=='rest':
                a2='rest'
                print("Input rest min")
                mi=input()
                print("Input rest max")
                ma=input()
                try:
                    max2=int(ma)
                    min2=int(mi)
                except:
                    controller.view.wronginput()

        elif n_t=='Ev':
            t2='Event'
            print("Name attribute: place or date")
            inp=input()
            if inp=='place':
                a2='place'
                print("Input place")
                str2=input()
            elif inp=='date':
                a2='date'
                print("Input date: since")
                dt21=input()
                print("Input date: until")
                dt22=input()
        elif n_t=='Ev_cat':
            t2='Event category'
            a2='name'
            print("Input category name")
            str2=input()
        else:
            controller.view.wronginput()

        print("Name third table: Tk or Ev or Ev_cat")
        n_t=input()
        if n_t=='Tk':
            t3='Ticket'
            print("Name attribute: name or price or rest")
            inp=input()
            if inp=='name':
                a3='name'
                print("Input name")
                str3=input()
            elif inp=='price':
                a3='price'
                print("Input price min")
                mi=input()
                print("Input price max")
                ma=input()
                try:
                    max3=int(ma)
                    min3=int(mi)
                except:
                    controller.view.wronginput()

            elif inp=='rest':
                a3='rest'
                print("Input rest min")
                mi=input()
                print("Input rest max")
                ma=input()
                try:
                    max3=int(ma)
                    min3=int(mi)
                except:
                    controller.view.wronginput()

        elif n_t=='Ev':
            t3='Event'
            print("Name attribute: place or date")
            inp=input()
            if inp=='place':
                a3='place'
                print("Input place")
                str3=input()
            elif inp=='date':
                a3='date'
                print("Input date: since")
                dt31=input()
                print("Input date: until")
                dt32=input()
        elif n_t=='Ev_cat':
            t3='Event category'
            a3='name'
            print("Input category name")
            str3=input()
        else:
            controller.view.wronginput()

        controller.search2(t1,a1,str1,max1,min1, t2,a2,str2,max2,min2, t3,a3,str3,max3,min3,dt11,dt12,dt21,dt22,dt31,dt32)
    else:
        controller.view.wronginput()
