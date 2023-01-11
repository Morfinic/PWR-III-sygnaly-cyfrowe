import numpy as np
import matplotlib.pyplot as plt

# Stworzenie figury na wyświetlenie wykresów
fig = plt.figure()
# Stworzenie wykresu biegunowego przedstawiającego kręcące śię śmigło
ax1 = fig.add_subplot(121, projection="polar")
# Stworzenie wykresu kartezjańskiego przedstawiające śmigło z użyciem skanera
ax2 = fig.add_subplot(122)

ax2.set_xlim(-1.5, 1.5)
ax2.set_ylim(-1.5, 1.5)

# Liczba śmigieł
n = 5
# Liczba skanowanych lini jednej klatki
line = 4
# Ilość klatek skanowanego obrazu
fr = 256 / line
# Wysokość segmentu (sin przyjmuje wartości od -1 do 1)
seg_height = 2 / fr
# Skanowanie zaczyna się od góry
seg_start = 1

radians = np.linspace(0, 2 * np.pi, 256)
frames = np.linspace(-32, 32, int(256/line))

# Generowanie "obrazu" dla każdej klatki
for frame in frames:
    for rad in radians:
        radius = np.sin(n * rad + (frame * np.pi) / 10)
        # Nanoszenie obrazu na wykres biegunowy
        ax1.plot(rad, radius, "g.")

        # Zamiana współrzędnych biegunowych na kartezjańskie
        x = np.cos(rad) * radius
        y = np.sin(rad) * radius
        # Jeśli y znajduje się w skanowanym segmencie nanieś go na wykres
        if y <= seg_start and y > seg_start - seg_height:
            ax2.plot(x, y, "g.")
    # Określ nowy segment dla następnej klatki
    seg_start = seg_start - seg_height
    plt.pause(0.25)
    ax1.clear()