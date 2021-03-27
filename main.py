import folium

#create a map

m = folium.Map(location=[51.48682874043062, -3.17997401066769],zoom_start=13)

#create markers
folium.Marker([51.487227028193765, -3.1978635962740625],
                popup='<b>Fatih | Mohammad\nCathedral Road 151\nCF11 9PJ</b>',
                tooltip="Fatih | Mohammad").add_to(m)
folium.Marker([51.48781128722012, -3.197975652594761],
                popup='<b>Aliu\nCathedral Road 150\nCF11 9JB</b>',
                tooltip="Aliu").add_to(m)
folium.Marker([51.4719338184207, -3.185432601203385],
                popup='<b>Abdullah\n81th Mardy St\nCF11 6QW</b>',
                tooltip="Abdullah").add_to(m)
folium.Marker([51.489534566026315, -3.150678669268602],
                popup='<b>Eduardo\n13th Arthur St\nCF24 1QR</b>',
                tooltip="Eduardo").add_to(m)               
m.save('map.html')  