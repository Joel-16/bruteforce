a = input("Enter passsword :")
b = len(a)
if a != "":
   i=0
   while i<b:
         for count in range (30, 126):
             d = chr(count)            
             if d == a[i]:
                 i += 1
                 print(d, end="")
                 break
              else:
                  print("please input a password")
