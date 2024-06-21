from random import randint

user_choice = int(input("Enter 0 (hayang) or 1 (kulob): "))                 #para mag input sa na pilian sa user kung 0 or 1 ba og para ma convert sa integer ang napili sa user
choices = ["hayang", "kulob"]                                               #para mo pili sa choices nga 0 or 1
c1, c2 = randint(0, 1), randint(0, 1)                                       #randint kani ang mag generate og random integer na pwedi ra niya pilian kay ang 0 og 1 unya ang c1 og c2 ang ge assign nga value

print(f"You: {choices[user_choice]}, C2: {choices[c1]}, C3: {choices[c2]}") #kini ang mag display og text ang print unya ang f kay ang string, ang sulod sa string kay ang list ang nag represent sa list kay ang choices unya ang user_choice kay ang integer na gi pili na 0 or 1 ang c1 og c2 kay ang random integer na hinungdan ni randint

if user_choice == c1 == c2:                                                 #dire sulod sa statement pag ang pilion sa user og c1 pati c2 kay pareho mahimong true ang result                                      
    print("It's a draw!")                                                   #dire na dayun mag gawas ang draw
else:                                                                       #si else ang gamiton pag dili mahitabo ang draw
    print("You win!" if user_choice != c1 and user_choice != c2             #kung si user kay na lahi kang c1 og c2 ang mo result kay you win
          else "C2 win!" if c1 != user_choice and c1 != c2                  #kung ang c1 kay dili pareha kang user ang mo gawas kay c2 win
            else "C3 win!")                                                 #kung wala wala sa unang kondisyon ang pareha ang mo gawas kay c3 win