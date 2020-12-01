#>>>>>>>>Saudações

print("Bem vindo a Imobiliária\n")

#>>>>>>>> perguntando tudo

var_grade = input("Qual o grade da casa?\n")
var_yr_build = input("Qual o yr_build da casa?\n")
var_bedrooms = input("Quantos bedrooms tem a casa?\n")
var_floors = input("Quantos floors tem a casa?\n")
var_sqrt_above = input("Quantos sqrt_above tem a casa?\n")
var_bathrooms =  input("Quantos bathrooms tem a casa?\n")

#>>>>>>>> transformando em inteiro

grade = int(var_grade)
yr_build = int(var_yr_build)
bedrooms = int(var_bedrooms)
floors = int(var_floors)
sqrt_above = int(var_sqrt_above)
bathrooms = float(var_bathrooms)

#>>>>>>>> clusterizando

#grade

if grade < 5:
    grade_trat = 1
elif grade < 10:
    grade_trat = 2
else: 
    grade_trat = 3


#yr_build

if yr_build < 1980:
    yr_build_trat = 1
elif yr_build < 1991:
    yr_build_trat = 2
elif yr_build < 2001:
    yr_build_trat = 3
elif yr_build < 2011:
	yr_build_trat = 4
else:
	yr_build_trat = 5
    
#bedrooms

bedrooms_trat = bedrooms

#floors

floors_trat = floors

#sqrt_above

if sqrt_above < 1000:
    sqrt_above_trat = 1
elif sqrt_above < 2000:
    sqrt_above_trat = 2
elif sqrt_above > 1999:
    sqrt_above_trat = 3
		
#bathrooms

bathrooms_trat = bathrooms

#respostas da arvore

if grade_trat <= 2.5 and yr_build_trat <=2.5:
    resp = 0 #1
elif grade_trat <= 2.5 and yr_build_trat > 2.5 and floors_trat <= 1.5 and sqrt_above_trat <= 2.5:
    resp = 0 #2
elif grade_trat <= 2.5 and yr_build_trat > 2.5 and floors_trat <= 1.5 and sqrt_above_trat > 2.5 and bathrooms_trat <= 2.5:
    resp = 1 #3
elif grade_trat <= 2.5 and yr_build_trat > 2.5 and floors_trat <= 1.5 and sqrt_above_trat > 2.5 and bathrooms_trat > 2.5:
    resp = 0 #4
elif grade_trat <= 2.5 and yr_build_trat > 2.5 and floors_trat > 1.5:
    resp = 0 #5   
elif grade_trat > 2.5  and bedrooms_trat <= 4.5 and yr_build_trat <= 3.5:
    resp = 0 #6  
elif grade_trat > 2.5  and bedrooms_trat <= 4.5 and yr_build_trat > 3.5 and floors_trat <= 2.5:
    resp = 1 #7 
elif grade_trat > 2.5  and bedrooms_trat <= 4.5 and yr_build_trat > 3.5 and floors_trat > 2.5:
    resp = 0 #8 
elif grade_trat > 2.5  and bedrooms_trat > 4.5:
    resp = 0 #9 

if resp == 0:
    print ("A casa provavelmente tem o preço por área abaixo da média do CEP\n")
elif resp == 1:
    print ("A casa provavelmente tem o preço por área acima da média do CEP\n")
    