#5) დედამ გაგიშვათ აფთიაქში თავის ტკივილის წამლის საყიდლათ, ეს წამალი დღეში უნდა დალიო შენი წონის მიხედვით. თუ 10 დან 20 კილომდე ხარ ნახევარი ტაბლეტი უნდა დალიო დღეში, თუ 30-40 კილომდე ხარ 1 ტაბლეთი ორჯერ დღეში და თუ 45 კილოზე მეტი ხარ სამი ტაბლეტი უნდა დალიო ორჯერ დღეში. თქვენი მისიაა ამ ინფორმაციით გაარკვიოთ მომხარებელს რამდენი წამალი აქვს დასალევი და დღეში რამდენჯერ უნდა დალიოს.


wona = int(input("chaweret tqveni wona")) 

if wona <10:
    print("tqventvis ar sheidzleba migeba") 


elif wona >=10 and wona <= 20:
    print("miiget naxevari tableti dgeshi 1 xel") 


elif wona >= 10 and wona <= 40:
    print("miiget 1 tableti dgeshi 2 jer") 


elif wona >= 45:
    print("daliet 3 tableti dgeshi 2 jer")