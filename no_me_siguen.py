from bs4 import BeautifulSoup
import re

def extract_usernames(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        soup = BeautifulSoup(f, "html.parser")
    
    usernames = set()
    for a in soup.find_all("a", href=True):
        href = a["href"].strip().lower()
        # Buscar el nombre dentro del link, sin _u/, sin barras finales
        match = re.search(r"instagram\.com/(?:_u/)?([a-z0-9._]+)/?", href)
        if match:
            username = match.group(1).strip().lower()
            usernames.add(username)
    return usernames

# Archivos HTML
followers_file = "followers_1.html"      # los que me siguen
following_file = "following.html"    # los que sigo

# Extraer nombres
followers = extract_usernames(followers_file)
following = extract_usernames(following_file)

# Comparar los que sigo pero no me siguen
no_me_siguen = sorted(following - followers)

# Mostrar resultados
print(f"Total seguidos (following): {len(following)}")
print(f"Total seguidores (followers): {len(followers)}")
print(f"Personas que sigo pero no me siguen: {len(no_me_siguen)}\n")

for user in no_me_siguen:
    print(user)
