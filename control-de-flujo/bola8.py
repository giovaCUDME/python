#giovanni molinet
#31-03-25

import random

respuesta = ['✅ si, definitivamente.',
             '⭐ con toda certeza, que si.',
             '🔒 sin lugar a dudas.',
             '🤔 respuesta confusa, intentalo de nuevo.',
             '🕒 preguntalo nuevamente mas tarde.',
             '😧 mejor no decirle ahora.',
             '❌ mis fuentes dicen que no.',
             '🌧️ el panorama es muy favorable.',
             '🤷‍♂️ muy dudoso.']

pregunta = input('pregunta:')

respuesta = random.choice(respuesta)

print('respuesta:', respuesta)