# El dueño de un restaurante de comida Mexicana ha decidido comprar un restaurante de comida Italiana y abrir un nuevo restaurante de comida fusión. La apertura esta a la vuelta de la esquina y aun no han podido actualizar el menu, ayuda a actualizar su menu de platos disponibles
# menu_mexicano: "Tacos","Enchiladas","Guacamole","Tamales"
# menu_italiano: "Pizza","Pasta","Lasagna","Tiramisú"

menu_mexicano = {"Tacos", "Enchiladas", "Guacamole", "Tamales"}
menu_italiano = {"Pizza", "Pasta", "Lasagna", "Tiramisú"}

menu_fusionado = menu_mexicano.union(menu_italiano)

print("Menú fusionado:")
print("\n".join(menu_fusionado))



