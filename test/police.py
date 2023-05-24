import matplotlib.font_manager as fm

# Récupération de la liste des polices de caractères disponibles
available_fonts = fm.get_fontconfig_fonts()

# Affichage des polices de caractères
for font_path in available_fonts:
    font_name = fm.get_font(font_path).family_name
    print(font_name)
