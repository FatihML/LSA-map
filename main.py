import folium

#create a map

m = folium.Map(location=[51.48682874043062, -3.17997401066769],zoom_start=13)

#create markers
folium.Marker([51.487227028193765, -3.1978635962740625],
                popup='<b>Fatih | Mohammad\nCathedral Road 151\nCF11 9PJ</b>',
                tooltip="Fatih | Mohammad").add_to(m)
folium.Marker([51.48781128722012, -3.197975652594761],
                popup='<b>Aliu | Waleed\nCathedral Road 150\nCF11 9JB</b>',
                tooltip="Aliu | Waleed").add_to(m)
folium.Marker([51.4719338184207, -3.185432601203385],
                popup='<b>Abdullah\n81 Mardy St\nCF11 6QW</b>',
                tooltip="Abdullah").add_to(m)
folium.Marker([51.489534566026315, -3.150678669268602],
                popup='<b>Eduardo\n13 Arthur St\nCF24 1QR</b>',
                tooltip="Eduardo").add_to(m)
#new markers
folium.Marker([51.48801550906192, -3.1711184225839117],
                popup='<b>Hicham\nRichmond Road\nCF24 3AR</b>',
                tooltip="Hicham").add_to(m)
folium.Marker([51.495521400993574, -3.1709854379489717],
                popup='<b>Osama\n92 Arabella St\nCF24 4TB</b>',
                tooltip="Osama").add_to(m) 
folium.Marker([51.499107752509424, -3.175074751162364],
                popup='<b>Musa\nCF24 4GG</b>',
                tooltip="Musa").add_to(m)
folium.Marker([51.4806262833672, -3.1582443302227854],
                popup='<b>Raman\n4 Inchmarnock\nCF24 2AL</b>',
                tooltip="Raman").add_to(m) 

m.save('map.html')  