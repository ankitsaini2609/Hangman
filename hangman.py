import random
print("You need to guess the name of country and if you make 6 wrong attempts you lose")
failed = 6
flag = 0

asia = ['bangladesh','bhutan','crunei','cambodia','china','india','indonesia','japan','kazakhstan','northkorea','southkorea','kyrgyzstan','laos','malaysia','maldives','mongolia','myanmar','nepal','philippines','singapore','sriLanka','taiwan','tajikistan','thailand','turkmenistan','uzbekistan','vietnam']
middle_east = ['afghanistan','algeria','azerbaijan','bahrain','egypt','iran','iraq','israel','jordan','kuwait','lebanon','libya','morocco','oman','pakistan','qatar','saudi arabia','somalia','syria','tunisia','turkey','united arab emirates','yemen']
europe = ['albania','andorra','armenia','austria','belarus','belgium','bosnia','herzegovina','bulgaria','croatia','cyprus','czech republic','denmark','estonia','finland','france','georgia','germany','greece','hungary','iceland','ireland','italy','kosovo','latvia','liechtenstein','lithuania','luxembourg','macedonia','malta','moldova','monaco','montenegro','netherlands','norway','poland','portugal','romania','russia','san marino','serbia','slovakia','slovenia','spain','sweden','switzerland','ukraine','united kingdom of great britain','northern ireland','vatican city']
north_america = ['canada', 'greenland', 'mexico']
central_america = ['antigua and barbuda', 'the bahamas', 'barbados', 'belize', 'costa rica', 'cuba', 'dominica', 'dominican republic', 'el salvador', 'grenada', 'guatemala', 'haiti', 'honduras', 'jamaica', 'nicaragua', 'panama', 'saint kitts and nevis saint','lucia saint','vincent and the grenadines','trinidad and tobago']
sub_saharan_africa = ['angola','benin','botswana','burkina faso','burundi','cameroon','cape verde','central african republic','chad','comoros','republic of the congo','democratic republic of the congo','cote d ivoire','djibouti','equatorial guinea','eritrea','ethiopia','gabon','the gambia','ghana','guinea','guinea bissau','kenya','esotho','liberia','madagascar','malawi','mali','mauritania','mauritius','mozambique','namibia','niger','nigeria','rwanda','sao tome and principe','senegal']
south_america = ['argentina', 'bolivia', 'brazil', 'chile', 'colombia', 'ecuador', 'guyana', 'paraguay', 'peru', 'suriname', 'uruguay', 'venezuela']

i = random.randint(0,6) #used to select region
if (i == 0):
    l = len(asia)
    j = random.randint(0,l-1) #integer used to select country
    guess = asia[j]
    lg = len(guess)
    country = 'asia'
elif (i == 1):
    l = len(middle_east)
    j = random.randint(0,l-1)
    guess = middle_east[j]
    lg = len(guess)
    country = 'middle_east'
elif (i == 2):
    l = len(europe)
    j = random.randint(0,l-1)
    guess = europe[j]
    lg = len(guess)
    country = 'europe'    
elif (i == 3):
    l = len(north_america)
    j = random.randint(0,l-1)
    guess = north_america[j]
    lg = len(guess)
    country = 'north_america'
elif (i == 4):
    l = len(central_america)
    j = random.randint(0,l-1)
    guess = central_america[j]
    lg = len(guess)
    country = 'central_america'
elif (i == 5):
    l = len(sub_saharan_africa)
    j = random.randint(0,l-1)
    guess = sub_saharan_africa[j]
    lg = len(guess)
    country = 'sub_saharan_africa'
elif (i == 6):
    l = len(south_america)
    j = random.randint(0,l-1)
    guess = south_america[j] 
    lg = len(guess)
    country = 'south_america'
#guess is actual string that user want to guess.
final = guess
guess = list(guess) #i need to convert it into list because guess is string and string are immuttable so i cannot manipulate guess that's why i am converting it into list.
print()
print("Hint: the country belong to "+country+" region and the length of the string to be guess is "+str(lg))
print()
f = 0 #it used to check when list ans have all the character as in guess then it will break the loop and tell you got the correct string
print("Now Your turn guess characters")
print()
ans =[] #used to store main answer
for g in guess:
    if (g == ' '):
        ans.append(' ')
        f += 1
    else:
        ans.append('-')
for q in ans:
    print(q,end='')        

print()
while(failed > 0):
    c = input()
    count = lg#help to manage failed variable
    if (len(c) > 1 or len(c) == 0):
        print("you have enter string")
        failed -= 1
    else :
        for r in range(lg):# just use for the matching of the character in the string
            if (c.lower() == guess[r]):
                ans[r] = c.lower()
                guess[r] = '`'
                f += 1
                if (f == lg):
                    print("\nYou Won thanx for playing")
                    flag = 1
                    break
        #    elif (guess[r] == ' '):
       #         ans[r] = ' '
            else:
      #          ans[r] = '-'
                count -= 1
        for q in ans:
            print(q,end='')
        print()
        if(count <= 0):
            failed -= 1
        if(flag == 1):
            break

if (flag == 0):
    print("You lose next time come with better guesses")
    print("Correct Answer is "+ final)
